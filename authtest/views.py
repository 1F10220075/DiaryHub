from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required # 関数やクラス前につけることでログインを必須にできる
def private_page(request):
    return render(request, 'authtest/private.html', {})

def public_page(request):
    return render(request, 'authtest/public.html', {})