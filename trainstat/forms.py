from django import forms

from .models import Review,Rank

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('No', 'Name', 'Punctuality', 'Food', 'Crowd', 'Services', 'Cooling', 'SeatAvailability')

class RankForm(forms.ModelForm):

    class Meta:
        model = Rank
        fields = ('Source', 'Destination')
