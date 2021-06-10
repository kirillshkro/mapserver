from django import forms
from .models import Friend
import datetime


class FriendForm(forms.ModelForm):
	dob = forms.DateField(
		label='Дата рождения',
		widget=forms.SelectDateWidget(years=range(1950, datetime.date.today().year - 5))
	)
	
	def __init__(self, *args, **kwargs):
		super(FriendForm, self).__init__(*args, **kwargs)
		
		for name in self.fields.keys():
			self.fields[name].widget.attrs.update({
				'class': 'form-control'
			})
	
	class Meta:
		model = Friend
		fields = ("__all__")
