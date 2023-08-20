from django.urls import path
from django.views.generic import TemplateView


app_name = 'board'

urlpatterns = [
    path('', TemplateView.as_view(template_name='board/question_list.html'), name='index')
]