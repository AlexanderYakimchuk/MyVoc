from django.contrib.auth.models import User
from django.db import models


class WordDictionary(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)


class Word(models.Model):
    eng_word = models.CharField(max_length=200)
    ua_word = models.CharField(max_length=200)
    image_url = models.CharField(max_length=300, blank=True)
    sound_url = models.CharField(max_length=300, blank=True)
    word_dictionary = models.ForeignKey(WordDictionary, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='WordStatus')


class Training(models.Model):
    name = models.CharField(max_length=100)


class WordStatus(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_learned = models.BooleanField(default=False)
