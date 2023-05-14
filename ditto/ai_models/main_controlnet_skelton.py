import numpy as np

class MainControlNet:
    def __init__(self) -> None:
        ## 모델 load
        self.model = self.load_model()
        
        # 최초 dummy data로 inference 한번 실행
        self.init_dummy_inference()
        
        print("model ready")
    
    def load_model(self):
        pass
    
    def init_dummy_inference(self):
        dummy_image = np.zeros([256,256,3])
        self.inference(image = dummy_image, prompt = "")

    def inference(self, image, prompt):
        generated_img  = np.zeros([256,256,3], dtype=np.uint8)
        return generated_img
        