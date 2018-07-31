from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from dictionaries.forms import AddWordForm
from dictionaries.models import WordDictionary, Word


class DictionaryListView(LoginRequiredMixin, ListView):
    context_object_name = 'dictionary_list'
    template_name = 'dictionaries/dictionary_list.html'

    # queryset = WordDictionary.objects.all()

    def get_queryset(self):
        return self.request.user.worddictionary_set.all()


class DictionaryDetailView(LoginRequiredMixin, DetailView):
    model = WordDictionary
    # context_object_name = 'dictionary'
    template_name = 'dictionaries/dictionary_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DictionaryDetailView, self).get_context_data(**kwargs)
        context['form'] = AddWordForm
        return context


def add_word_form_view(request, dict_id):
    form = AddWordForm(request.POST)
    if form.is_valid():
        word = Word(eng_word=form.cleaned_data.get('eng_word'),
                    ua_word=form.cleaned_data.get('ua_word'),
                    word_dictionary_id=dict_id)
        word.save()
    return redirect('dictionaries:concrete_dict', pk=dict_id)
