from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) == 0:
            raise forms.ValidationError('Поле должно быть заполнено\n',
                                        code = 1)
        return title
    def clean(self):
        return self.cleaned_data


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

