from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
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

def answer_create(request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
create_date=timezone.now())
    # 답변 등록시 텍스트창에 입력한 내용은 request 객체를 통해 읽을 수 있다 (request.POST.get('content'))

    # 답변을 생성하기 위해 question.answer_set.create를 사용
    # Question과 Answer 모델은 서로 ForeignKey로 연결되어 있기 때문에 이처럼 사용할 수 있다.

    return redirect('detail', question_id=question.id)
    # 답변 생성 후 질문 페이지를 다시 보여주기 위해 redirect 함수를 사용.