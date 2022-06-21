# Generated by Django 4.0.5 on 2022-06-21 09:50

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(null=True, upload_to='')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('client_message', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GettingInvolvedLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('Financially', 'Financially'), ('Ideas', 'Ideas'), ('Volunteerting', 'Volunteerting')], default='Financially', max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('expectations', models.TextField(max_length=500)),
                ('cv', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Legal Personality', 'Legal Personality'), ('Ministerial Collaboration', 'Ministerial Collaboration'), ('Signed MOUs', 'Signed MOUs')], default='Legal Personality', max_length=255)),
                ('document_file', models.FileField(upload_to='official_documents')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteeringAplicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
            ],
        ),
    ]