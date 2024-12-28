from django.urls import path
from .views import HelloWorldAPIViews


urlpatterns = [
    path('hello/', HelloWorldAPIViews.as_view(), name='hello-world'),
]
