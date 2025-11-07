from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ Save to database
            submitted = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, "hello/contact.html", {"form": form, "submitted": submitted})
