from django.shortcuts import render
from .models import Diary

# Create your views here.
def index(request):
    diarys = Diary.objects.all()
    context = {
        'diarys':diarys,
    }
    return render(request, "diaryhub/index.html", context)

def diary(request, diary_name):
    return render(request, "diaryhub/diary.html", {"diary_name": diary_name})