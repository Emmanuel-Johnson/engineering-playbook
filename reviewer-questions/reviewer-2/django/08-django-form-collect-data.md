A Django Form is used to collect input data from users like name, email, password, etc.

Example:

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

Use in view:

# views.py

```python
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)   # collected data
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

Template:

```python
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

Interview answer:
“Django Form is used to collect, validate, and process user input data safely.”