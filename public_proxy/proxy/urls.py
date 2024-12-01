from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )


app_name = "proxy"

router = routers.DefaultRouter()


urlpatterns = [
        path('api/', include(router.urls)), # add the router to our urls
        path('proxy/', views.makeProxy, name="makeProxy"), # add the router to our urls
        ]

