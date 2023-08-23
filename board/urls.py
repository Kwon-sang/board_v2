from django.urls import path
from django.views.generic import ListView

from .views import question_views, answer_views
from .models import Question


app_name = 'board'

urlpatterns = [
    path('', question_views.question_list, name='index'),

    path('question/', question_views.question_create, name='question_create'),
    path('question/<int:question_id>/', question_views.question_detail, name='question_detail'),
    path('question/<int:question_id>/delete/', question_views.question_delete, name='question_delete'),
    path('question/<int:question_id>/update/', question_views.question_update, name='question_update'),

    path('question/<int:question_id>/answer/', answer_views.answer_create, name='answer_create'),
    path('answer/<int:answer_id>/delete', answer_views.answer_delete, name='answer_delete'),
    path('answer/<int:answer_id>/update', answer_views.answer_update, name='answer_update'),
]