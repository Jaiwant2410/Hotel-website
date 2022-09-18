from django.shortcuts import render
from django.http import HttpResponse
from hotel.models import Person
from hotel.models import Contact





# Create your views here.

def Home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        place = request.POST.get("place")
        gest = request.POST.get("gest")
        arrival = request.POST.get("arrival_date")
        leaving = request.POST.get("leaving_date")
        ins = Person(place=place, gest=gest, arrival=arrival, leaving=leaving)
        ins.save()

    return HttpResponse("done")

def contactus(request):
    if request.method == "POST":
        name_1 = request.POST.get("name1")
        email_1 = request.POST.get("email")
        phoneno_1 = request.POST.get("phoneno")
        subject_1 = request.POST.get("subject")
        text_1 = request.POST.get("text")
        print(email_1, phoneno_1, name_1, subject_1, text_1)
    ins1 = Contact(name_1=name_1, number=phoneno_1, email=email_1, subject=subject_1, textarea=text_1)
    ins1.save()

    return HttpResponse("done")







