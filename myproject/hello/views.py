from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email to admin
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['yourgmail@gmail.com'],  # replace with your Gmail
        )

        # Send thank-you email to the user
        send_mail(
            subject="Thanks for contacting us!",
            message=f"Hi {name},\n\nThank you for reaching out. We’ll get back to you soon!\n\n– Shannu Team",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        return HttpResponse("<h2>Thank you! Your message has been sent successfully.</h2>")

    return render(request, "hello/contact.html")  # ✅ matches the template path
