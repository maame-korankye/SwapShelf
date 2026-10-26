from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # is_staff is a privilege flag (grants the department desk and the
        # Django admin), so it must never be editable from the public profile
        # form. Only first/last name and email are user-editable here.
        fields = ["first_name", "last_name", "email"]
