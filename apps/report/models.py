from django.db import models
from apps.users.models import Staff

# Create your models here.
class Report(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
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

