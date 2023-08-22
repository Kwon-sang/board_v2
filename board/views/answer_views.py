from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from board.models import Question, Answer
from board.forms import AnswerForm


@login_required
def answer_create(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        answer = Answer(question=question, author=request.user, contents=request.POST['contents'])
        answer.save()
        messages.success(request, '답변을 등록하였습니다.')
    return redirect('board:question_detail', question_id=question_id)


@login_required
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question_id = answer.question_id
    if request.method == 'POST':
        if request.user != answer.author:
            messages.error(request, '현재 게시물에 대한 삭제 권한이 없습니다.')
            return redirect('board:question_detail', question_id=question_id)
        answer.delete()
        messages.success(request, '답변을 삭제하였습니다.')
    return redirect('board:question_detail', question_id=question_id)


@login_required
def answer_update(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question_id = answer.question_id
    if request.method == 'POST':
        if request.user != answer.author:
            messages.error(request, '현재 게시물에 대한 수정 권한이 없습니다.')
            return redirect('board:question_detail', question_id=question_id)
        form = AnswerForm(request.POST, instance=answer)
        form.save()
        messages.success(request, '답변을 수정하였습니다.')
        return redirect('board:question_detail', question_id=question_id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'board/answer_update.html', {'form': form})
