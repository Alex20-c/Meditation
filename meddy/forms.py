from django import forms
from .models import Procedure,Profile

class ProcedureForm(forms.ModelForm):
    class Meta:
        model = Procedure
        exclude = ['user','user_procedure_id']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = ('process','steps')

