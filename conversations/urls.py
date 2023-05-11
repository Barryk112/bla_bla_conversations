from . import views
from django.urls import path


urlpatterns = [
    path('', views.ConversationList.as_view(), name='home'),
    path('<slug:slug>/', views.ConversationDetail.as_view(), name='conversation_detail'),
]
