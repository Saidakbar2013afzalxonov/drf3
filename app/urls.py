from django.urls import path
from .views import PostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostView)

urlpatterns = router.urls