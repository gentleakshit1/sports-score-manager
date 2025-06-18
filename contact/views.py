from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the message
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Redirect to confirmation page
        return redirect('contact_confirmation')

    return render(request, "contact/contact.html")

def contact_confirmation(request):
    return render(request, "contact/contact_confirmation.html")
