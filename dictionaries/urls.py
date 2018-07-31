from django.urls import path
from django.views.decorators.http import require_POST

from . import views

app_name = 'dictionaries'
urlpatterns = [
    path('dicts/', views.DictionaryListView.as_view(), name='dicts'),
    path('dicts/<int:pk>', views.DictionaryDetailView.as_view(), name='concrete_dict'),
    path('add_word/<int:dict_id>', require_POST(views.add_word_form_view), name='add_word'),

]
