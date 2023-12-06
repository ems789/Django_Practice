from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-create_date") # 조회 결과를 정렬하는 함수(-create_date)는 작성일시 역순 정렬을 의미
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context) # 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
    # 즉 질문 목록으로 조회한 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 생성한 후 리턴.

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question} # 이게 뭐임?
    return render(request, 'pybo/question_detail.html', context)