from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from calendar import HTMLCalendar


# Create your views here.

def index(request):
    return render(request,'index.html')

def pythonlogics(request):
    return render(request, 'pythonlogics.html')



@require_http_methods(["POST"])
def ht_cm_view(request):

    height_in_feet = int(request.POST.get("height_in_feet"))
    height_in_inches = int(request.POST.get("height_in_inches"))
    

    height_in_inches += int(height_in_feet * 12)

    result_in_cms = round(height_in_inches * 2.54, 1)


    return render(request, "partials/ht_cm.html", {"result_in_cms": result_in_cms})




@require_http_methods(["POST"])
def BMI_view(request):

    height = float(request.POST.get("height"))
    weight = float(request.POST.get("weight"))

    result = (weight / (height/100)**2)

    if result <= 18.5:
        messages.success(request,"Under Weight")

    elif result <= 24.9:
        messages.success(request,"Healthy")

    elif result <= 29.9:
        messages.success(request,"Over Weight")

    else:
        messages.success(request,"Obesity")

    

    return render(request, "partials/bmi.html", {"result": result})


@require_http_methods(["POST"])
def calendar_view(request):

    year = int(request.POST['year'])
    month = int(request.POST['month'])

    result = HTMLCalendar().formatmonth(year, month)


    return render(request, "partials/calendar.html", {"result": result})


@require_http_methods(["POST"])
def simpleinterest_view(request):

    p = int(request.POST['amount'])
    t = int(request.POST['year'])
    r = int(request.POST['rate-of-interest'])

    result = (p*t*r)/100

    total = result+p

    year = t

    return render(request, "partials/simpleinterest.html", {"result": result,'total':total,'year':year})
