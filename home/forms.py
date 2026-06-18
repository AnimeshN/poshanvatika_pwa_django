from django.db.models import fields
from .models import UploadPictureModel, UploadWellPictureModel,BasicPoshanModel,AhmedSchoolForm,UploadSeedModel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _  # or gettext_lazy

class BasicPoshanForm(forms.ModelForm):
    class Meta:
        model = BasicPoshanModel
        fields = '__all__'

class AhmedSchoolForm(forms.ModelForm):
    class Meta:

       model=AhmedSchoolForm
       fields='__all__'



class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = UploadPictureModel
        # fields = ('picture','name','nutri_nm','area','village','district','state','pincode','lat','lng')
        fields = '__all__'
        labels = {
            'picture': _("Picture"),
            'name': _("Name"),
            'nutri_nm': _("Nutrient Name"),
            'area': _("Area"),
            'village': _("Village"),
            'district': _("District"),
            'state': _("State"),
            'pincode': _("Pincode"),
            'lat': _("Latitude"),
            'lng': _("Longitude"),
        }
        help_texts = {
            'picture': _("Upload a picture"),
            'name': _("Enter your name"),
            'nutri_nm': _("Enter the nutrient name"),
            'area': _("Enter the area"),
            'village': _("Enter the village"),
            'district': _("Enter the district"),
            'state': _("Enter the state"),
            'pincode': _("Enter the pincode"),
            'lat': _("Enter the latitude"),
            'lng': _("Enter the longitude"),
        }

class UploadWellPictureForm(forms.ModelForm):
    class Meta:
        model = UploadWellPictureModel
        fields = ('picture','name','well_nm','radius','depth','level','village','district','state','pincode', 'lat', 'lng','date','username', 'water_quality')

class UploadSeedForm(forms.ModelForm):
    class Meta:
        model = UploadSeedModel
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        
# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None      
    
#     class Meta:
#         model=User
#         fields = ('username', 'email', 'password1', 'password2')
#         def save(self, commit=True):
#             user = super(NewUserForm, self).save(commit=False)
#             user.email = self.cleaned_data['email']
#             if commit:
#                 user.save()
#             return user

class AutoCADFileUploadForm(forms.Form):
    file = forms.FileField(label='Select AutoCAD file')



class PoshanVatikaForm(forms.Form):

    owner = forms.CharField(label="Name", max_length=255)

    state = forms.CharField(max_length=255)
    district = forms.CharField(max_length=255)
    tehsil = forms.CharField(max_length=255, required=False)
    village = forms.CharField(max_length=255)

    pincode = forms.CharField(max_length=20, required=False)

    nutri_area = forms.CharField(
        label="Nutri Vatika Area",
        max_length=255,
        required=False
    )

    variety_num = forms.CharField(
        label="No. of Varieties",
        max_length=255,
        required=False
    )

    variety_list = forms.CharField(
        label="Varieties Grown",
        widget=forms.Textarea(attrs={"rows": 3}),
        required=False
    )

    seed_type = forms.CharField(
        max_length=255,
        required=False
    )

    seed_source = forms.CharField(
        max_length=255,
        required=False
    )

    est_yield = forms.CharField(
        label="Estimated Yield",
        max_length=255,
        required=False
    )

    support = forms.CharField(
        max_length=255,
        required=False
    )

    afif_support = forms.CharField(
        max_length=255,
        required=False
    )

    picture = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'browser-default',
                'style': 'width:100%;padding:10px;margin-bottom:15px;'
            })