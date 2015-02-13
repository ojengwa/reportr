from django.db import models

# Create your models here.
class ContactModel(models.Model):

    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = "inquiry"
        verbose_name_plural = "inquiries"

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

