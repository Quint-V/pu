from django.contrib.auth.models import Permission, User
from django.db import models
from django import forms


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

# superklasse for sporsmål og svar,
# rent funksjonelt er det fa forskjeller pa dem hvis de kommer
# fra samme superklasse.


class Post(models.Model):
    parent_post = models.ForeignKey('self')
    title = forms.CharField(max_length=200)
    posted_by = models.ForeignKey(User)


class Question(Post):
    question_title = Post.title
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        max_length=10000,
    )
    rating = forms.IntegerField(
        initial=0,
    )
    is_sticky = forms.BooleanField(initial=False)

    def __str__(self):
        return self.question_title


class Comment(Question):
    reply_to = models.ForeignKey(
        Question,
        on_delete='username="deleted user"',
        )
    body = forms.CharField(
        text=forms.Textarea,
        max_length=10000,
        requir=True,
    )
    rating = forms.IntegerField()


class VotedOn(Post):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE())
