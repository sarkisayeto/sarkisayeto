from . import views
from django.urls import path

urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.update_form, name='update_form'),
    path('history/', views.update_history, name='update_history'),
    path('modifier/<int:id>/', views.modifier_update, name='modifier_update')
] 