from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.core.mail import EmailMessage
from DjangoApp import settings
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    form = ContactFormMessageForm()
    context = {'form':form}
    if request.method == 'POST':
        form  =  ContactFormMessageForm(request.POST)
        if form.is_valid():
            form.save()
            client_name = form.cleaned_data['first_name']
            client_emal = form.cleaned_data['email']
            context = {'client_name':client_name, 'client_emal':client_emal}
            email_template = render_to_string('email_templates/new_message.html', context)

            email = EmailMessage(
                'New message from website',
                email_template,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            email.fail_silently = False
            try:
                email.send()
            except:
                return HttpResponse("Information sent but Imbonizarwo was not notified")
        return redirect('thank-you')
    return render(request, 'home.html', context)

def about(request):
    official_documents = OfficialDocuments.objects.all()
    print(official_documents)
    context = {'official_documents': official_documents}
    return render(request, 'about.html', context)

def contact(request):
    form = ContactFormMessageForm()
    context = {'form':form}
    if request.method == 'POST':
        form  =  ContactFormMessageForm(request.POST)
        if form.is_valid():
            form.save()
            client_name = form.cleaned_data['first_name']
            client_emal = form.cleaned_data['email']
            context = {'client_name':client_name, 'client_emal':client_emal}
            email_template = render_to_string('email_templates/new_message.html', context)

            email = EmailMessage(
                'New message from website',
                email_template,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
            email.fail_silently = False
            try:
                email.send()
            except:
                return HttpResponse("Information sent but Imbonizarwo was not notified")
        return redirect('thank-you')
    return render(request, 'contact.html', context)

def getInvolved(request):
    form = GettingInvolvedLeadForm()
    context = {'form': form}
    if request.method == 'POST':
        form = GettingInvolvedLeadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('thank-you')
    return render(request, 'get-involved.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def base(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base.html', context)


def addBlog(request):
    form = AddBlogFrom()
    context = {'form':form}
    if request.method == 'POST':
        form = AddBlogFrom(request.POST)
        form.save()
        return redirect('blog')
    return render(request, 'add-blog.html', context)

def login(request):
    return render(request, 'login.html')

def volunteeringAplicantsView(request):
    form = VolunteeringAplicantsForm()
    context = {'form': form}
    return render(request, 'v-application-form.html', context)


def applicationComplete(request):
    return render(request, 'application-complete.html')
def thankYou(request):
    return render(request, 'thank-you.html')