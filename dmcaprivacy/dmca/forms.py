from django import forms
from django.contrib.auth import get_user_model
from .models import Plans
from bootstrap_modal_forms.forms import BSModalModelForm
User = get_user_model()


class BootstrapModelForm(forms.ModelForm):
    """ class to be inherited to add form class  """

    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


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


class PlanCreateForm(BSModalModelForm):
    class Meta:
        model = Plans
        fields = ('plan',)

        widgets = {
            'plan': forms.TextInput(attrs={'placeholder': 'Name of the plan'})
        }
