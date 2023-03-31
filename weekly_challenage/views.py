from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

challenages = {
    'Monday':'You need go for Gym',
    'Tuseday':'Don\'t eat non-veg be a vegitarian and do fasting',
    'Wednesday':'Walk 5000 steps so you can burn calories',
    'Thursday':'Need take steam bath which will helpful to glow our skin',
    'Friday':'Do yoga which will make your mind clean and fresh ',
    'Saturday':'Go for Swimming for refreshment and good for body',
    'Sunday':'Take rest that\'s also usefull  ',
    
}

def index(request,day_name):
    try:
        my_challenages = challenages[day_name]
        context={
            'my_challenages' : my_challenages,
            'day_name' : day_name
        }
    except KeyError:
        return HttpResponse('<h1>Entered Day not found</h1>')

    return render(request,'weekly_challenage\index.html',context)


def home(request):
    week_names = list(challenages.keys())
    context = {
        'week_names' : week_names
    }
    return render(request, 'weekly_challenage\home.html',context)