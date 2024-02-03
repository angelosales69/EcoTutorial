from django.shortcuts import render, redirect
from .forms import TutorialForm
from .models import *


def home_page(request):
    return render(request, "pages/home.html", )


def about_page(request):
    return render(request, "pages/about.html", )


def tutorial_page(request):
    tutorial = Tutorial.objects.all()

    context = {
        'tutorial': tutorial,
    }
    return render(request, "pages/tutorial.html", context)


def contact_page(request):
    return render(request, "pages/contact.html", )


def admindashboard_page(request):
    tutorial = Tutorial.objects.all()

    context = {
        'tutorial': tutorial,

    }
    return render(request, "pages/admindashboard.html", context)


def tutorialform_page(request):
    form = TutorialForm()
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboardagri')

    context = {
        'form': form
    }
    return render(request, "pages/tutorialform.html", context)


def updatetutorial(request, pk):
    tutorial = Tutorial.objects.get(id=pk)
    form = TutorialForm(instance=tutorial)

    if request.method == 'POST':
        form = TutorialForm(request.POST, instance=tutorial)
        if form.is_valid():
            form.save()
            return redirect('dashboardagri')

    context = {
        'form': form
    }
    return render(request, 'pages/tutorialform.html', context)


def deletetutorial(request, pk):
    tutorial = Tutorial.objects.get(id=pk)
    if request.method == 'POST':
        tutorial.delete()
        return redirect('dashboardagri')

    context = {
        'tutorial': tutorial
    }
    return render(request, 'pages/deletetutorial.html', context)
