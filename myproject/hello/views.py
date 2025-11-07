from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ✅ Try sending email to admin
        try:
            send_mail(
                subject=f"New Contact from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['yourgmail@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Failed to send email to admin: {e}")

        # ✅ Try sending auto-reply to user
        try:
            send_mail(
                subject="Thanks for contacting us!",
                message=f"Hi {name},\n\nThank you for reaching out. We’ll get back to you soon!\n\n– Shannu Team",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Failed to send auto-reply: {e}")

        # ✅ Return success page with musical sound and pulsing tick
        return HttpResponse(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
    <style>
        body {{
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #e0f7fa, #e8f5e9);
            font-family: Arial, sans-serif;
        }}
        .card {{
            background: white;
            padding: 40px 50px;
            border-radius: 15px;
            text-align: center;
            border: 2px solid #4caf50;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            animation: popup 0.6s ease-out;
        }}
        .icon {{
            font-size: 70px;
            color: #4caf50;
        }}
        h2 {{
            color: #2e7d32;
            margin-top: 10px;
            animation: fadeIn 1s ease-out;
        }}
        @keyframes popup {{
            0% {{ transform: scale(0.6); opacity: 0; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to   {{ opacity: 1; }}
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            25% {{ transform: scale(1.2); }}
            50% {{ transform: scale(1); }}
            75% {{ transform: scale(1.15); }}
            100% {{ transform: scale(1); }}
        }}
        .pulse {{
            animation: pulse 0.6s ease-out infinite;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div id="tick" class="icon">✅</div>
        <h2>Your message has been sent successfully!</h2>
    </div>

    <!-- ✅ Reliable loud musical sound -->
    <audio id="successSound" autoplay>
        <source src="https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3" type="audio/mpeg">
    </audio>

    <script>
        const sound = document.getElementById('successSound');
        const tick = document.getElementById('tick');

        // Pulse tick while sound plays
        sound.addEventListener('play', () => {{
            tick.classList.add('pulse');
        }});
        sound.addEventListener('ended', () => {{
            tick.classList.remove('pulse');
        }});

        // Try to play in case autoplay is blocked
        sound.play().catch(err => {{
            console.log("Audio playback blocked:", err);
        }});
    </script>
</body>
</html>
""")

    # GET request loads contact form
    return render(request, "hello/contact.html")
