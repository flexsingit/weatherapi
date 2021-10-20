
from django.conf.urls import url
from django.contrib import admin
from .views import GuestViewset,weatherapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guest', GuestViewset, basename='user')
urlpatterns = router.urls+[url('getweather',weatherapi,name="weatherapi")]