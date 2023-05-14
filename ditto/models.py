from django.db import models

# Create your models here.
class CanvasImg(models.Model):
    col = models.CharField(max_length=200, null=True, blank=True)
    prompt = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    
    
class InferenceQueue(models.Model):
    canvas = models.ForeignKey("CanvasImg", related_name="queue", on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    processing = models.BooleanField(default=False)