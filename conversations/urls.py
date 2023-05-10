from . import views
from django.urls import path


urlpatterns = [
    path('', views.ConversationList.as_view(), name='home')
]