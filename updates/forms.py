from django import forms

from .models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        # V models we want to include
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean(self, *args, **kwargs):
        #validates Data
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise forms.ValidationError('content or image is required')
        return super().clean(*args, **kwargs)

