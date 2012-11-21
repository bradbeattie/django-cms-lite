from django import forms


class CmsPageForm(forms.Form):
    source = forms.CharField(
        help_text="Be careful. Mistakes as simple as unescaped HTML characters like < and > can easily break things.",
        widget=forms.Textarea(
            attrs={
                "class": "span6",
                "rows": "30",
            },
        )
    )
