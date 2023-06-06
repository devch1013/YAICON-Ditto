from django.contrib import admin
from django.urls import path
from ditto.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('save_canvas/', save, name="save"),
    path('result_all', results, name="result_all"),
    path('result/<str:col>', result_page, name="result"),
    path('queue/<str:col>', queue_check, name="queue"),
    path("test_inference", test_inference)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
