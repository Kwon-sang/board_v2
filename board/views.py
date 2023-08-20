from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from .forms import QuestionForm


class QuestionListView(ListView):
    model = Question
    ordering = ['-created_at']


class QuestionDetailView(DetailView):
    model = Question
