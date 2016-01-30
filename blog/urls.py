from django.conf.urls import url,include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$',views.index),#기존에 프로젝트 단에서 설정할 수 있는 경로를 앱마다 따로 url 파일을 생성해 경로를 설정할 수 있음
    url(r'^posts/$','blog.views.post_list'),
    url(r'^posts/(?P<pk>\d+)/$','blog.views.post_detail'),
    url(r'^posts/(?P<post_pk>\d+)/comments/new$','blog.views.comment_new'),
    url(r'^api/v1/', include('blog.api.v1')), #template 파일이 아닌 것을 뷰할 수 있음


]