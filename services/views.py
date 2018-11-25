from django.shortcuts import render


# Create your views here.
def services(request):

    return render(request, "services.html")


def kennels(request):

    return render(request, "kennels.html")


def grooming(request):

    return render(request, "grooming.html")
