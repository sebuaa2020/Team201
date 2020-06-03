from django.urls import path
from . import views

urlpatterns = [
    path('navigate/', views.navigate, name='navigate'),
    path('fetch_item/', views.fetch_item, name='fetch_item'),
    path('deliver/', views.deliver, name='deliever'),
    path('move_ctrl/', views.move_ctrl, name='move_ctrl'),
    path('hector_mapping/', views.hector_mapping, name='move_ctrl')
]