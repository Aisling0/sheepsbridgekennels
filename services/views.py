from django.shortcuts import render


# Create your views here.
def kennels(request):

    return render(request, "kennels.html")


def grooming(request):

    return render(request, "grooming.html")
