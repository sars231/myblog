from django.urls import path,include
from django.conf.urls import url
from blog import views,urls

urlpatterns = [
    path('',views.home),
    path('edit',views.edit)
]