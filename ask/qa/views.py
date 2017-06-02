from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from qa.models import Question
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404, HttpResponseRedirect
from qa.forms import AskForm, AnswerForm, SignUpForm, SignInForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

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

def question(request, **kwargs):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        q = get_object_or_404(Question, id=kwargs['qid'])
        if answer_form.is_valid():
            answer = answer_form.save()
            answer.author = request.user
            answer.save()
            return HttpResponseRedirect(q.get_url())
    else:
        q = get_object_or_404(Question, id=kwargs['qid'])
        answer_form = AnswerForm()
    return render(request, 'question_detail.html',
                  {'question': q,
                   'answers': q.answer_set.all(),
                   'form': answer_form})

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
    
def ask(request):
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            question = ask_form.save()
            question.author = request.user
            question.save()
            question_url = question.get_url()
            return HttpResponseRedirect(question_url)
    else:
        ask_form = AskForm()
    return render(request, 'create_question.html', {'form': ask_form})

def signup(request):
    err = ''
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = User.objects.create_user(signup_form.cleaned_data['username'], signup_form.cleaned_data['email'], signup_form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('qa:main-list'))
        else: err = 'Неверный логин/пароль'
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'err': err, 'form': signup_form})

def signin(request):
    err = ''
    if request.method == 'POST':
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            err += '11'
            username = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('qa:main-list'))
                else: err += 'Аккаунт заблокирован'
            else: err += 'Неверный логин/пароль'
    else:
        signin_form = SignInForm()
    return render(request, 'signin.html', {'err': err, 'form': signin_form})

@require_POST
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('qa:main-list'))

