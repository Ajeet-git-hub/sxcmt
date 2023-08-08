from django import forms

class Work_form(forms.Form):
    stu_roll = forms.CharField(max_length = 100, required=True)
    book_id = forms.CharField(max_length = 15, required=True)