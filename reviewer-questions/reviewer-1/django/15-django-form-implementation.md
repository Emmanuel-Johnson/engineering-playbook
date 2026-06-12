```python

# forms


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField()
    email = forms.EmailField()
    

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {"form" : form})
    

<form method='post'>
    {% csrf_token %}
    {{ form.as_p }}
    <button type='submit'></button>
</form>


# model form


from django import models

class ContactDetails(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    

from .models import ContactDetails
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['name', 'age', 'email']
        

from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {"form" : form})
    

<form method='post'>
    {% csrf_token %}
    {{ form.as_p }}
    <button type='submit'>submit</button>
</form>
```