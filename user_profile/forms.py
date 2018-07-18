from django import forms
from django.core.exceptions import ValidationError
from django.db import OperationalError

from .models import Profile, Skill, Project


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('picture', 'skills', )

        try:
            widgets = {  # The first object in the tuple is the external representation, the second the internal
                'skills': forms.SelectMultiple(choices=[(str(obj), obj) for obj in Skill.objects.all()],
                                               attrs={'class': 'ui multiple search selection dropdown'}),
            }
        except OperationalError:
            pass

        def clean(self):
            picture = self.cleaned_data.get('picture', False)
            if picture:
                if picture.__size > 4 * 1024 * 1024:
                    raise ValidationError( "Image file too large ( > 4mb )")
                return picture
            else:
                raise ValidationError("Couldn't read uploaded image")


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'application_end', )

        widgets = {
            'application_end': forms.DateInput(attrs={'medium': 'date'})
        }
