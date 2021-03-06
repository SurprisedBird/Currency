from django import forms

from currency import models


class RateForm(forms.ModelForm):
    class Meta:
        model = models.Rate
        fields = ('sale', 'buy', 'source', 'curr_type')


class SourceForm(forms.ModelForm):
    class Meta:
        model = models.Source
        fields = (
            'name',
            'source_url',
        )
