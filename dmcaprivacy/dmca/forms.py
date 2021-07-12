from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, ModelChoiceField
from .models import Plans, Pages, TubePages, Clients
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

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


# Class for show the full name in a select form against the username which it is by default
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class UserAssign(forms.ModelForm):
    worker_id = UserModelChoiceField(queryset=User.objects.filter(is_worker=True))

    class Meta:
        model = Clients
        fields = ('plan_id', 'worker_id')


class PlanCreateForm(ModelForm):

    class Meta:
        model = Plans
        fields = ('plan',)

        widgets = {
            'plan': forms.TextInput(attrs={'placeholder': 'Name of the plan', 'id': 'plan'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class OfficialPageCreateForm(ModelForm):

    class Meta:
        model = Pages
        fields = ('name_page', )

        widgets = {
            'name_page': forms.TextInput(attrs={'placeholder': 'Name of the plan', 'id': 'name_page'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


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

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
