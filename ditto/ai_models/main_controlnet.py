import cv2
import einops
import numpy as np
import torch
import random

from ditto.ai_models.share import *
import ditto.ai_models.config
from pytorch_lightning import seed_everything
from ditto.ai_models.annotator.util import resize_image, HWC3
from ditto.ai_models.cldm.model import create_model, load_state_dict
from ditto.ai_models.cldm.ddim_hacked import DDIMSampler


class MainControlNet:
    def __init__(self) -> None:
        ## 모델 load
        self.load_model()

        # 최초 dummy data로 inference 한번 실행
        self.init_dummy_inference()

        print("model ready")

    def load_model(self):
        
        base_model_name = "cldm_v15"
        control_name = 'controlnet_final.pth'

        self.model = create_model(f'ditto/ai_models/models/{base_model_name}.yaml').cpu()
        self.model.load_state_dict(load_state_dict(f'ditto/ai_models/models/{control_name}', location='cuda'), strict=False)
        self.model = self.model.cuda()
        
        # For Inference
        self.ddim_sampler = DDIMSampler(self.model)

    # from gradio_scribble2image.py
    def process(
        self,
        input_image,
        prompt,
        num_samples,
        image_resolution,
        ddim_steps,
        guess_mode,
        strength,
        scale,
        seed=-1,
        eta=0.0,
        a_prompt="best quality, extremely detailed",
        n_prompt="longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality",
    ):
        """
        이미지 numpy uint8 type으로 들어가야함
        """
        with torch.no_grad():
            img = resize_image(HWC3(input_image), image_resolution)
            H, W, C = img.shape

            detected_map = np.zeros_like(img, dtype=np.uint8)
            detected_map[np.min(img, axis=2) < 127] = 255

            control = torch.from_numpy(detected_map.copy()).float().cuda() / 255.0
            control = torch.stack([control for _ in range(num_samples)], dim=0)
            control = einops.rearrange(control, "b h w c -> b c h w").clone()

            if seed == -1:
                seed = random.randint(0, 65535)
            seed_everything(seed)

            if config.save_memory:
                self.model.low_vram_shift(is_diffusing=False)

            cond = {
                "c_concat": [control],
                "c_crossattn": [
                    self.model.get_learned_conditioning([prompt + ", " + a_prompt] * num_samples)
                ],
            }
            un_cond = {
                "c_concat": None if guess_mode else [control],
                "c_crossattn": [self.model.get_learned_conditioning([n_prompt] * num_samples)],
            }
            shape = (4, H // 8, W // 8)

            if config.save_memory:
                self.model.low_vram_shift(is_diffusing=True)

            self.model.control_scales = (
                [strength * (0.825 ** float(12 - i)) for i in range(13)]
                if guess_mode
                else ([strength] * 13)
            )  # Magic number. IDK why. Perhaps because 0.825**12<0.01 but 0.826**12>0.01
            samples, intermediates = self.ddim_sampler.sample(
                ddim_steps,
                num_samples,
                shape,
                cond,
                verbose=False,
                eta=eta,
                unconditional_guidance_scale=scale,
                unconditional_conditioning=un_cond,
            )

            if config.save_memory:
                self.model.low_vram_shift(is_diffusing=False)

            x_samples = self.model.decode_first_stage(samples)
            x_samples = (
                (einops.rearrange(x_samples, "b c h w -> b h w c") * 127.5 + 127.5)
                .cpu()
                .numpy()
                .clip(0, 255)
                .astype(np.uint8)
            )

            results = [x_samples[i] for i in range(num_samples)]
        return [255 - detected_map] + results

    def init_dummy_inference(self):
        dummy_image = np.zeros([256, 256, 3], dtype=np.uint8)
        self.inference(image=dummy_image, prompt="")

    def inference(self, image, prompt):
        # generated_img  = np.zeros([256,256,3], dtype=np.uint8)
        generated_img = self.process(
            input_image=image,
            prompt=prompt,
            num_samples=1,
            image_resolution=512,
            ddim_steps=20,
            guess_mode=False,
            strength=0.95,
            scale=9.0,
            seed=-1,
        )
        return generated_img
