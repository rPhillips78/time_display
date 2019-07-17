from django.shortcuts import render
from time import strftime
import pytz
from datetime import datetime


# Create your views here.
def index(request):
    chi = pytz.timezone('US/Central')
    chicago_date = datetime.now(chi)

    context = {
        'date': chicago_date.strftime('%a %b %d %Y'),
        'time': chicago_date.strftime('%I:%M %p %Z') 
    }
    return render(request, 'displayTime/index.html', context)


