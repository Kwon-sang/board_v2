from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer
from .forms import QuestionForm


question_list = ListView.as_view(model=Question, ordering=['-created_at'])


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'board/question_detail.html', {'question': question})


@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, '질문이 등록되었습니다.')
            return redirect('board:index')
    else:
        form = QuestionForm()
    return render(request, 'board/question_form.html', {'form': form})


@login_required
def answer_create(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        answer = Answer(question=question, author=request.user, contents=request.POST['contents'])
        answer.save()
        messages.success(request, '답변을 등록하였습니다.')
    return redirect('board:question_detail', question_id=question_id)


