from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['skills'].form = forms.SelectMultiple()
        self.fields['skills'].widget.attrs['class'] = 'ui multiple search selection dropdown'
        self.fields['picture'].widget.attrs['enctype'] = 'multipart/form-data'

    class Meta:
        model = Profile
        fields = ('picture', 'skills', )

        def clean(self):
            picture = self.cleaned_data.get('picture', False)
            if picture:
                if picture.__size > 4 * 1024 * 1024:
                    raise forms.ValidationError("Image file too large ( > 4mb )")
                return picture
