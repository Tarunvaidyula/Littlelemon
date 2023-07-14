from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class Bookingform(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"