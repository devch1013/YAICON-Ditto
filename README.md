<img src="https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/DITTO.png" width = "900" >


# DITTO: Doodle to Image Translation Web Project

## :confetti_ball: YAICON 1st Prize!! :confetti_ball: 


## Members 
- 박지호: AI, BE 
- 박찬혁: PM, BE Lead 
- 안정우: Data, AI 
- 이수민: FE Lead, AI 
- 장윤호: Data, AI 
- 최정우: AI Lead
  
---
</br>
</br>

- This is [ControlNet](https://github.com/lllyasviel/ControlNet)(Latent Diffusion) Web Application Project
- Our model generates high quality Image from prompt guided Doodle.
- To enhance the Doodle to Image performance, we fine-tuned ControlNet using `SBU Captions` dataset.
- This is the result of our web
<p align = "center">
<img src = "https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/video.gif" width ="450" align = "center">
</p>


## 0. Inference Results
|![0](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result0.png)|![1](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result1.png)|
|:---:|:---:|
|![2](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result2.png)|![3](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result3.png)
|![4](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result4.png)|![5](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result5.png)|


<!-- 
|![0](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result0.png)|![1](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result0.png)|![2](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result0.png)|
|:---:|:---:|:---:|
|![3](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result0.png)|![4](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result1.png)|![5](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/result2.png)| -->


## 1. ControlNet

## Train
***Our goal was to generate high-quality image from even more doodling sketch.***<br/>
We trained pretrained ControlNet.

### Dataset
To train ControlNet on sketch control, caption, sketch and target image are required.  <br/>
We used `SBU Captions` dataset, which is large-scale dataset that contains 860K image-text pairs. <br/>

### Edge Detection
To obtain Doodle of the target image, we have tested several edge detectors. <br/>
We have chose [`PhotoSketch`](https://github.com/mtli/PhotoSketch), which was generating most human-like doodle.

<img src = "https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/edgedetect1.png" width = "800" align = "center">

## 2. Web
|HomePage|SketchPage|ResultPage|
|:---:|:---:|:---:|
|![1](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/front0.png)|![2](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/front2.png)|![3](https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/front3.png)

## How to Run


1. Create conda virtual environment using environment.yaml
```
    conda env create --file environment.yaml
```

2. Move to cloned folder and start django prototype server
```
    python3 manage.py runserver --noreload
```
3. Access to localhost:8000 and enjoy!

<img src="https://github.com/devch1013/YAICON-Ditto/blob/main/imgs/front4.png" >
