from django.urls import path,include
from blog import views,urls

urlpatterns = [
    path('',views.cover),
    path('edit',views.edit)
]