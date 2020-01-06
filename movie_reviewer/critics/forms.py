from django import forms
# from django.contrib.auth.models import User
from movie_reviewer.critics.models import Critic


class NewCriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['username', 'email', 'password',
                  'displayname', 'professional']
