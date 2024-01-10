from django.shortcuts import render
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
    return render(request, 'bbs/index.html', context)

def diary(request, diary_name):
    return render(request, "diaryhub/diary.html", {"diary_name": diary_name})