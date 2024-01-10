from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Diary
from .forms import SearchForm

# Create your views here.
def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        diarys = Diary.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        diarys = Diary.objects.all()

    context = {
        'message': 'Hello Django',
        'diarys': diarys,
        'searchForm': searchForm,
    }
    return render(request, 'diaryhub/index.html', context)

def diary(request, id):
    diary = get_object_or_404(Diary, pk=id)
    # return HttpResponse(diary)
    context = {
        "diary_name": str(id),
        'diary':diary,
    }
    return render(request, "diaryhub/diary.html", context)

def create(request):
    diary = Diary(content="hello 日々禄", user_name="tmp")
    diary.save()

    diarys = Diary.objects.all()
    context = {
        'diarys':diarys,
    }
    return render(request, "diaryhub/index.html", context)

def delete(request, id):
    diary = get_object_or_404(Diary, pk=id)
    diary.delete()

    diarys = Diary.objects.all()
    context = {
        'diarys':diarys,
    }
    return render(request, "diaryhub/index.html", context)
