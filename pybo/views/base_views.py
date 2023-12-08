from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

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