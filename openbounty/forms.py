from django import forms
from openbounty.models import Challenge

class ChallengeForm(forms.ModelForm):
	challenge = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Challenge
		fields = ["bounty","title","challenge","expiration_date"]

