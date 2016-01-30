from django.shortcuts import redirect, render
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm2
from django.contrib.auth.decorators import login_required #로그인이후 페이지
# Create your views here.

def signup(request):
    if request.method=='POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/weblog/')
    else:
        form=SignupForm2()
    return render(request, 'accounts/signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')