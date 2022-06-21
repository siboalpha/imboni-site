from turtle import title
from unicodedata import category
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255,)
    featured_image = models.ImageField(null=True)
    content = RichTextUploadingField(null=True)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

    def excerpt(self):
        return self.content[0:100]+"..."

    def blog_title(self):
        return self.title[0:50]+"..."

class ContactFormMessage(models.Model):
    date_sent = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    client_message = models.TextField(max_length=40)

    def __str__(self):
        return self.first_name


class GettingInvolvedLead(models.Model):
    Financially = 'Financially'
    Ideas = 'Ideas'
    Volunteering = 'Volunteerting'

    GETTING_INVOLVED_CHOICES = [
        ( Financially,'Financially'),
        (Ideas,'Ideas'),
        (Volunteering, 'Volunteerting'),
    ]
    application_date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=40)
    category = models.CharField(max_length=255, choices=GETTING_INVOLVED_CHOICES, default=Financially)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    expectations = models.TextField(max_length=500)
    cv = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.first_name
    
    
class OfficialDocuments(models.Model):
    legal_personality = 'Legal Personality'
    ministerial_collaboration = 'Ministerial Collaboration'
    signed_MOUs = 'Signed MOUs'

    DOCUMENT_CHOICES = [
        (legal_personality,'Legal Personality'),
        (ministerial_collaboration, 'Ministerial Collaboration'),
        (signed_MOUs, 'Signed MOUs')
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=DOCUMENT_CHOICES, default=legal_personality)
    document_file = models.FileField(upload_to='official_documents')

    def __str(self):
        return self.title

class VolunteeringAplicants(models.Model):
    first_name = models.CharField(max_length=255)