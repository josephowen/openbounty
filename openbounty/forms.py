from django import forms
from openbounty.models import Challenge, Comment

class ChallengeForm(forms.ModelForm):
	challenge = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Challenge
		fields = ["bounty","title","challenge","expiration_date"]

class MoneyForm(forms.Form):
    money = forms.DecimalField(decimal_places=2,max_digits=10)
    
class CommentForm(forms.ModelForm):
	#comment = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Comment
		fields = ["title","comment"]

