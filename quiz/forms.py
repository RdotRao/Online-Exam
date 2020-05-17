from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.forms import ModelForm
from .models import Quiz , Category , SubCategory
from true_false.models import TF_Question
from multichoice.models import MCQuestion , Answer

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)

class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))

class Createexam(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'

class TFquestionForm(forms.ModelForm):
    class Meta:
        model = TF_Question
        fields = '__all__'
class MCquestionForm(forms.ModelForm):
    class Meta:
        model = MCQuestion 
        fields = '__all__'

class MCanswerForm(forms.ModelForm):
    class Meta:
        model = Answer 
        fields = '__all__'

