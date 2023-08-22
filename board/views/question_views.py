from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from board.models import Question
from board.forms import QuestionForm


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
    return render(request, 'board/question_create.html', {'form': form})


@login_required
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if request.user != question.author:
            messages.error(request, '현재 게시물에 대한 삭제 권한이 없습니다.')
            return redirect('board:question_detail', question_id=question_id)
        question.delete()
        messages.success(request, '질문을 삭제하였습니다.')
    return redirect('board:index')


@login_required
def question_update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if request.user != question.author:
            messages.error(request, '현재 게시물에 대한 수정 권한이 없습니다.')
            return redirect('board:question_detail', question_id=question_id)
        form = QuestionForm(request.POST, instance=question)
        form.save()
        messages.success(request, '질문을 수정하였습니다.')
        return redirect('board:question_detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'board/question_update.html', {'form': form})
