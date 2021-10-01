from datetime import datetime, timedelta, date
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ModelChoiceField, SelectDateWidget
from .models import Plans, Pages, TubePages, Clients, Nicks, GoogleReports, TubeReports
from crispy_forms.helper import FormHelper
User = get_user_model()


class UserEditForm(forms.ModelForm):
    """ Form for edit user """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'imag_clie')
        labels = {
            'imag_clie': 'Profile image'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'})
        }


class UserStatus(forms.ModelForm):

    class Meta:
        model = User
        fields = ('is_active', 'is_superuser', 'is_worker', 'is_client')


# Class for show the full name in a select form against the username which it is by default
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class UserAssign(forms.ModelForm):
    worker_id = UserModelChoiceField(label='Worker to assign', queryset=User.objects.filter(is_worker=True))
    date_assign = forms.DateField(label='Expire date', initial=datetime.now() + timedelta(days=31))

    class Meta:
        model = Clients
        fields = ('plan_id', 'worker_id', 'date_assign')
        labels = {
            'plan_id': 'Name of the plan'
        }


class PlanCreateForm(ModelForm):

    class Meta:
        model = Plans
        fields = ('plan',)

        widgets = {
            'plan': forms.TextInput(attrs={'placeholder': 'Name of the plan', 'id': 'plan'})
        }


class OfficialPageCreateForm(ModelForm):

    class Meta:
        model = Pages
        fields = ('name_page', )

        widgets = {
            'name_page': forms.TextInput(attrs={'placeholder': 'Name of the plan', 'id': 'name_page'})
        }


class TubePageCreateForm(ModelForm):

    class Meta:
        model = TubePages
        fields = ('name_tube_page', 'contact_tube')
        labels = {
            'name_tube_page': 'Url of the tube page',
            'contact_tube': 'Contact of the tube page'
        }

        widgets = {
            'name_tube_page': forms.TextInput(attrs={'placeholder': 'URL of the tube page', 'id': 'name_tube_page'}),
            'contact_tube': forms.TextInput(attrs={'placeholder': 'Email or url to the DMCA form'})
        }


class NicksCreateForm(ModelForm, forms.Form):
    class Meta:
        model = Nicks
        fields = ('nick', 'prio', 'pages',)
        widgets = {
            'pages': forms.CheckboxSelectMultiple(attrs={'placeholder': 'Select one or multiple pages'}),
        }


class NickEditForm(forms.ModelForm):
    class Meta:
        model = Nicks
        fields = ('nick', 'prio', 'pages',)
        widgets = {
            'pages': forms.CheckboxSelectMultiple(attrs={'placeholder': 'Select one or multiple pages'}),
        }


class AddReport(forms.ModelForm):

    class Meta:
        model = GoogleReports
        fields = ('date_gore', 'id_clai_gore', 'type_clai_gore', 'urls_gore',)

        widgets = {
            'date_gore': forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'value': date.today()}),
            'id_clai_gore': forms.TextInput(attrs={'placeholder': 'ID of the claim', 'class': 'form-control'}),
            'type_clai_gore': forms.Select(attrs={'placeholder': 'Type of claim', 'class': 'form-control'}),
            'urls_gore': forms.Textarea(attrs={'placeholder': 'Fill the input with the links', 'class': 'form-control',
                                               'style': 'height: 100px'}),
        }


class AddTube(forms.ModelForm):

    class Meta:
        model = TubeReports
        fields = ('date_tube', 'tube_urls',)

        widgets = {
            'date_tube': forms.DateInput(attrs={'placeholder': 'Date', 'class': 'form-control', 'value': date.today()}),
            'tube_urls': forms.Textarea(attrs={'placeholder': 'Fill the input with the links', 'class': 'form-control',
                                               'style': 'height: 100px'}),
        }
