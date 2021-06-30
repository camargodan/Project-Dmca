from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Plans, Pages
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


class PageCreateForm(ModelForm):

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
