from django import forms
from .models import Author
from .models import Quote

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    tags = forms.CharField(required=False)

    class Meta:
        model = Quote
        fields =  fields = ['author', 'quote', 'tags']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def save(self, commit=True):
        quote = super().save(commit=False)
        tag_names = self.cleaned_data.get('tags', '').split(',')
        quote.tags = [name.strip() for name in tag_names if name.strip()]
        if commit:
            quote.save()
        return quote