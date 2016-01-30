from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from blog.forms import CommentForm
from django.shortcuts import redirect
# Create your views here.



#기존에 shortcut만 사용한
def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    return render(request,'blog/post_list.html',{'post_list':Post.objects.all()})

def post_detail(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def comment_new(request, post_pk):
    post=Post.objects.get(pk=post_pk)

    if request.method=='POST':
        form=CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post#<--화면 단에 변수를 보여주고 싶지 않은 경우 서버 단에서만 값을 이동시키고 싶을 경우
            comment.save()
            return redirect('blog.views.post_detail',post_pk)
    else:
        form=CommentForm()

    return render(request,'blog/comment_form.html',{'form':form,})

"""
TemplateView를 소환
index = TemplateView.as_view(template_name="blog/index.html")
"""
'''
#TemplateView를 클래스로 소환해서 정의하고 함수로 불름
class MyTemplateView(object):
    @staticmethod#밑에 함수를 실행하기 위해 사전에 필요한 조건또는 함수를 불름
    def as_view(template_name):
        def view(request):
            return render(request, template_name)
        return view

index = MyTemplateView.as_view(template_name="blog/index.html")
'''