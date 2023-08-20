from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    model = Question
    fields = ['subject', 'contents']


class AnswerForm(forms.ModelForm):
    model = Answer
    fields = ['contents']