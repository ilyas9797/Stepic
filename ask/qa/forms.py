from django import forms
from qa.models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) == 0:
            raise forms.ValidationError('Поле должно быть заполнено\n',
                                        code = 1)
        return title


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
