from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UploadViewset

router = SimpleRouter()
router.register(r'', UploadViewset, basename='upload')
urlpatterns = [
    path('', include(router.urls))
]