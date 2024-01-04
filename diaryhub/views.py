from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "diaryhub/index.html")

def diary(request, diary_name):
    return render(request, "diaryhub/diary.html", {"diary_name": diary_name})