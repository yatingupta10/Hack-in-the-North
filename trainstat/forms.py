from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('No', 'Name', 'Punctuality', 'Food', 'Crowd', 'Services', 'Cooling', 'SeatAvailability')