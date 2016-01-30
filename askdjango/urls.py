#프로젝트 urls 설정 최상위 url 설정(settings.ROOT_URLCONF="project.urls")<-urls 파일이름이 바꼈을 경우 경로 설정을 해줘야 함
"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
#from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    #url(r'^$',"blog1.views.index"),
    url(r'^weblog/',include('blog.urls')),# blog/ 뒤에 경로를 blog.urls 안에 설정된 경로에 해당하는 것을 부르겠다. #blog/$를 쓰면 뒤와 불러오는 파일은 같고, 주소창에 경로를 칠경우 현재 blog/ 경로는 포함되지 않게
    url(r'^$',lambda request: redirect('blog.views.index'))
    #url(r'^$',views.index),
    #url(r'^blog1/posts/posts/$','blog.views.post_list'),
    #url(r'^blog1/posts/(?p<pk>\d+)/$','blog.views.post_detail'),
    #url(r'^blog1/',include('blog.urls')),
]
"""
기존의 방식, 1.1부터 지원하지 않음
urlpatterns = [
    url(r'^$',"blog.views.index"),
]
경로를 모두다 부르는 것을 비추천
"""
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)