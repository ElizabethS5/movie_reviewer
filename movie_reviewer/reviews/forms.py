from django import forms
from movie_reviewer.reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [  
            'headline', 
            'text', 
            'recommend']


