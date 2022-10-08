from django.urls import path
from .views import first, second, third

app_name = 'lovely'
urlpatterns = [
    path('first/', first, name='first'), #경로, view 함수, 이를 부르는 이름 순이다.
    path('second/', second, name='second'),
    path('third/', third, name='third'),
]

