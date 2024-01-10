from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Diary, Category
from .forms import SearchForm, DiaryForm

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

def new(request):
    diaryForm = DiaryForm()

    context = {
        'diaryForm': diaryForm
    }

    return render(request, "diaryhub/new.html", context)

def create(request):
    if request.method == "POST":
        diaryForm = DiaryForm(request.POST)
        if diaryForm.is_valid():
            diary = diaryForm.save()

    context = {
        'diary_name':diary.id,
        'diary':diary,
    }
    return render(request, "diaryhub/diary.html", context)

def edit(request, id):

    diary = get_object_or_404(Diary, pk=id)
    diaryForm = DiaryForm(instance=diary)
    context = {
        "diary_name": str(id),
        'diary':diary,
        'diaryForm': diaryForm,
    }
    return render(request, "diaryhub/edit.html", context)

def update(request, id):
    if request.method == "POST":
        diary = get_object_or_404(Diary, pk=id)
        diaryForm = DiaryForm(request.POST, instance=diary)
        if diaryForm.is_valid():
            diaryForm.save()

    context = {
        "diary_name": str(id),
        'diary':diary,
    }
    return render(request, "diaryhub/diary.html", context)

def delete(request, id):
    diary = get_object_or_404(Diary, pk=id)
    diary.delete()

    diarys = Diary.objects.all()
    context = {
        'diarys':diarys,
    }
    return render(request, "diaryhub/index.html", context)
