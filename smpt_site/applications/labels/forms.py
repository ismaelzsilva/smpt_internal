from django import forms

class CreateLabelsForm(forms.Form):
    fabrication_order = forms.IntegerField()
    reference = forms.CharField(max_length=50)
    article = forms.CharField(max_length=50)
    designation = forms.CharField(max_length=50)
    quantity = forms.IntegerField()
