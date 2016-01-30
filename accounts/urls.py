from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views
from accounts.forms import LoginForm

urlpatterns=[
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^login/$',login,name='login',kwargs={'authentication_form':LoginForm,}),
    url(r'^logout/$',logout,name='logout'),
    url(r'^profile/$',views.profile,name='profile'),
]