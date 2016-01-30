from django import forms
from blog.models import Comment

class CommentForm(forms.ModelForm):
    is_agree=forms.BooleanField(label='약관동의', required=True, error_messages={'required':'약관동의 필수!!!',})
    class Meta:
        model =  Comment
        fields = '__all__' #필드의 모든 값을 저장하는 경우
        fields = ['message','image'] #필드를 지정해서 부르고 싶은경우