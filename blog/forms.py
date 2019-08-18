# If the CharField of your form corresponds to a model CharField, make sure both have the same max_length value.

from django import forms

class CommentForm (forms.Form):
  author = forms.CharField(
      max_length=60, # this has to match comment class
      widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder": "Name"
      })
  )
  body = forms.CharField(widget=forms.Textarea(
      attrs={
        "class": "form-control",
        "placeholder": "Comment"
      })
  )