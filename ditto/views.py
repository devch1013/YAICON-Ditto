from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ditto.models import CanvasImg, InferenceQueue
import base64
import io
from PIL import Image, ImageFile
import numpy as np
import cv2
from .utils import *
import uuid
import time
import threading
from .apps import DittoConfig
ImageFile.LOAD_TRUNCATED_IMAGES = True

queue_config = False

th = threading.Lock()

def home(request):
    return render(request, 'home.html')

def save(request):
    if request.method == "POST":
        imagefield_img = request.POST['canvas_data']
        prompt = request.POST["prompt"]
        data = CanvasImg()
        # generate code per inference
        col = uuid.uuid4()
        data.col = col
        data.prompt = prompt
        data.save()
        # inference
        
        decoded_img = base64.b64decode(imagefield_img.split(',')[1])
        pil_img = Image.open(io.BytesIO(decoded_img)).convert("RGB")
        # time.sleep(2)
        # if queue_config:
        #     pil_img.save(f"data/{col}_sketch.jpg")
        #     queue = InferenceQueue(canvas=data)
        #     queue.save()
        #     return JsonResponse({"col":col})
        # else:
        np_img = np.array(pil_img)
        inference(col, np_img, prompt)
        
    
        
         ## inference
        
        return HttpResponseRedirect(f"/result/{col}")
    return render(request, 'home.html')

def result_page(request, col):
    data = CanvasImg.objects.get(col=col)
    context = {"uuid": data.col, "prompt":data.prompt}
    return render(request, "result.html", context)


def test_inference(request):
    if request.method == "POST":
        col = request.POST["col"]
        prompt = request.POST["prompt"]
        new_data = CanvasImg()
        try:
            image = Image.open(f'data/{col}_sketch.jpg')
        except:
            image = Image.open(f'data/{col}.jpg')
            print(image)
        np_img = np.asarray(image)
        new_col = uuid.uuid4()
        inference(new_col, np_img, prompt)
        new_data.col = new_col
        new_data.prompt = prompt
        new_data.save()
        return HttpResponseRedirect(f"/result/{new_col}")
    
    
    return render(request, 'test_inference.html')



def inference(col, np_img, prompt):
    with th:
        result_image = DittoConfig.model.inference(np_img, prompt)  
    # result_image = [np_img, np_img]
    sketch_input = Image.fromarray(result_image[0])
    result_image = Image.fromarray(result_image[1])
    
    sketch_input.save(f"data/{col}_sketch.jpg")
    result_image.save(f"data/{col}.jpg")
    
    
@csrf_exempt
def queue_check(request, col):
    if request.method == "POST":
        try:
            queue = InferenceQueue.objects.get(canvas__col=col)
            remain = len(InferenceQueue.objects.filter(time__lte = queue.time))
            return JsonResponse({"queue":remain})
            
        except:
            return HttpResponseRedirect(f"/result/{col}")
        
        
        
def results(request):
    obj = CanvasImg.objects.all()
    context = {"obj": obj}
    return render(request, 'result_all.html', context)