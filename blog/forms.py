from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating a comment.

    Inherits from forms.ModelForm and defines the fields for the Comment model.

    Attributes:
        model (Comment): The Comment model to use for the form.
        fields (tuple): The fields to include in the form.

    """

    class Meta:
        model = Comment
        fields = ("name", "email", "body")
