from django import forms

class ContactForm (forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ))
    email= forms.EmailField(label="Email", required=True,widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ) )
    message=forms.CharField(label="Mensaje",required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':4, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)