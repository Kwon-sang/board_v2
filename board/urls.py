from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='index'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail')
]