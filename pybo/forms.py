from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm): # 모델 폼을 상속
    class Meta: # 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다
                # Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }
