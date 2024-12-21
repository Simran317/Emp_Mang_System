from django import forms

class AchievementForm(forms.Form):
    guest = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    project_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    upload = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))