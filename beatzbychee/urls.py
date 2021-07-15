from django.urls import path
from . import views


app_name = 'beatzbychee'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_message_topic/', views.new_message_topic, name='new_message_topic'),
    path('my_music/', views.my_music, name='my_music'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('accessibility', views.accessibility, name='accessibility')
]

