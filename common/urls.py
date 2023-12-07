from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), 
    # loginView는 template_name을 지정해주지 않으면 
    # registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]