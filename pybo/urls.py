from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # /pybo/2/ 페이지가 요청되면 여기에 등록한 매핑 룰에 의해 /pybo/<int:question_id>/가 적용되어
    # question_id에 2가 저장되고 view.detail 함수가 실행 된다.
]
