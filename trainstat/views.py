from django.shortcuts import render


def index(request):
    return render(request, 'trainstat/index.html', {})

def contact(request):
    return render(request, 'trainstat/contact.html', {})

def about(request):
    return render(request, 'trainstat/about.html', {})

def rate(request):
    return render(request, 'trainstat/rate.html', {})

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
