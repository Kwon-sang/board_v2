from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'contents']
        labels = {'subject': '제목', 'contents': '내용'}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['contents']
        labels = {'contents': '내용'}