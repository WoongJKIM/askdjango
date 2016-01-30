#한번에 url설정 및 함수를 불를 수 있음

from django.conf.urls import url
from django.http import JsonResponse

#JSON 형태로 글을 출력하는 함수
def post_list(request):
    post_list=[
        {'id':1,'title':'title1'},
        {'id':2,'title':'title2'},
    ]
    return JsonResponse(post_list, safe=False)

#URL 설정 내에 위의 함수를 불름
urlpatterns = [
    url('^$', post_list),
]