from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.question_list, name='index'),
    path('question/', views.question_create, name='question_create'),
    path('question/<int:question_id>', views.question_detail, name='question_detail'),

    path('question/<int:question_id>/answer/', views.answer_create, name='answer_create'),
    path('question/<int:question_id>/answer/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]