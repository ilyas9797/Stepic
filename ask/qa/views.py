from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

# Create your views here.

from django.http import HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def main_list(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    base_url = '/?page='
    return render(request, 'questions_page.html',
                  {'questions': page.object_list,
                   'base_url': base_url,
                   'page': page})

@require_GET
def popular_list(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    base_url = '/popular/?page='
    return render(request, 'questions_page.html',
                  {'questions': page.object_list,
                   'base_url': base_url,
                   'page': page})

@require_GET
def question(request, **kwargs):
    q = get_object_or_404(Question, id=kwargs['qid'])
    return render(request, 'question_detail.html',
                  {'question': q,
                   'answers': q.answer_set.all()})

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    # Page
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
    
