from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):#한 모델에 포함되어 있는 필드가 아니라 조인 형태로 저장 되는 파일의 경우
    email=forms.EmailField()

    def save(self, commit=True):
        user=super(SignupForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user

class SignupForm2(UserCreationForm):#모델에 포함되어있는 필드의 경우
    class Meta(UserCreationForm.Meta):
        fields=['username','email']

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='3+3=?')

    def clean_answer(self):
        answer=self.cleaned_data.get('answer',None)#현재 폼에서 answer에 해당하는 필드의 값을 불러옴
        if answer!=6:
            raise forms.ValidationError('땡!!')#유효성
        return answer

