from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Diary

# Create your views here.
def index(request):
    diarys = Diary.objects.all()
    context = {
        'diarys':diarys,
    }
    return render(request, "diaryhub/index.html", context)

def diary(request, id):
    diary = get_object_or_404(Diary, pk=id)
    # return HttpResponse(diary)
    context = {
        "diary_name": str(id),
        'diary':diary,
    }
    return render(request, "diaryhub/diary.html", context)
