from django.shortcuts import render
from .models import Rank
from .forms import RankForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'trainstat/index.html', {})

def contact(request):
    return render(request, 'trainstat/contact.html', {})

def about(request):
    return render(request, 'trainstat/about.html', {})

def rank(request):
    if request.method == "POST":
        form = RankForm(request.POST)#doubt
        if form.is_valid():
            passbook = form.save(commit=False)
            passbook.save()
            # return redirect('result', train=passbook.pk)
            train = get_object_or_404(Rank, pk=passbook.pk)
            import sqlite3
            conn = sqlite3.connect('/home/abhijeet/Documents/versionControl/Hack-in-the-North/trainstat/delay.db')
            print conn
            c = conn.cursor()

            # train=[row for row in c.execute("SELECT DISTINCT * FROM delay WHERE Source="+train.Source+" and Destination="+train.Destination+" ORDER BY delay") ]
            # print row
            return render(request,'trainstat/result.html',{'train':train})
    else:
        form = RankForm()
    return render(request, 'trainstat/rank.html', {'form': form})

def rate(request):
    return render(request, 'trainstat/rate.html', {})
<<<<<<< HEAD

def post_new(request):
    if request.method == "POST":
        saved_no = request.POST.get("No", "")
        saved_punctuality = request.POST.get("Punctuality", "")
        saved_crowd = request.POST.get("Crowd", "")
        saved_services = request.POST.get("Services", "")
        saved_cooling = request.POST.get("Cooling", "")
        saved_seatavailability = request.POST.get("SeatAvailability", "")
        Punctuality = models.FloatField()
        feedback = Feedback()
        feedback.save()
    return HttpResponseRedirect(reverse("view", args=(Review.id,)))

# Create your views here.
=======
>>>>>>> 68341b327cca6029ed5cf81fa07c3283a5fd29b2
