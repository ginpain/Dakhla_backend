"""
from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('chat/', chatbot_view, name='chatbot_view'),
]
"""
# In your urls.py
from django.urls import path
from .views import ChatbotView

urlpatterns = [
    path('chat/', ChatbotView.as_view(), name='chatbot_view'),
]
