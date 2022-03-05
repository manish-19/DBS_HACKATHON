from django.shortcuts import render
from django.contrib import messages

from users.models import book_appointment
# Create your views here.
def home(request):
    return render(request, 'users/wm.html')

def book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        date = request.POST.get('date')
        time = request.POST.get('time')

    details = book_appointment(name=name,email=email,phno=phno,date=date,time=time)
    details.save()
    print(details)
    messages.success(request, "Appointment Booked")
    return render(request,'users/wm.html')

def hni(request):
    alldetails=book_appointment.objects.all()
    records={'alldetails':alldetails}
    print(alldetails)
    return render(request,'users/hni.html',records)   