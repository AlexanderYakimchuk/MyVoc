from django.forms import ModelForm

from dictionaries.models import Word


class AddWordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['eng_word', 'ua_word']
        labels = {'eng_word': 'слово',
                  'ua_word': 'переклад'}
