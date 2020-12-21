from django.shortcuts import render
import datetime

# Create your views here.
def index(request):

    now = datetime.datetime.now()
    # if now.day == 1 and now.month == 1:

    return render(request, "newyear/index.html", {
        "newyear": now.day == 1 and now.month == 1
    })
