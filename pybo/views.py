from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by("-create_date") # 조회 결과를 정렬하는 함수(-create_date)는 작성일시 역순 정렬을 의미
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context) # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    # 즉 질문 목록으로 조회한 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 생성한 후 리턴.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question} # 이게 뭐임?
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    # URL 요청을 POST, GET 요청 방식에 따라 다르게 처리
    if request.method == 'POST': # 폼을 채우고 '저장하기' 버튼을 눌렀을 때
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장을 하여 question 객체를 리턴 받음
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
            form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)