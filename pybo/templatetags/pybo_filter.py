import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter # 템플릿에서 해당 함수를 필터로 사용할 수 있게 해줌
def sub(value, arg):
    return value - arg

# 입력 문자열을 HTML로 변환하는 필터 함수
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))