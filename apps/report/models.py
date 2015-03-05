from django.db import models
from apps.users.models import Staff

# Create your models here.
class Report(models.Model):

    content = models.TextField()
    challenges = models.TextField(default='loremsjhsfb jhsb jsfbjhfdbjhfbhjb ')
    achievements = models.TextField(default='loremsjhsfb jhsb jsfbjhfdbjhfbhjb ')
    plans = models.TextField(default='loremsjhsfb jhsb jsfbjhfdbjhfbhjb ')
    creator = models.ForeignKey(Staff, related_name='reports')

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"



class Review(models.Model):

    text = models.TextField()
    reviewer = models.ForeignKey(Staff, related_name='reviews')
    report = models.ForeignKey(Report, related_name='reviews')


    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"



class Comment(models.Model):

    text = models.TextField()
    author = models.ForeignKey(Staff, related_name='comments')
    review = models.ForeignKey(Review, related_name='comments')

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Tag(models.Model):

    word = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
