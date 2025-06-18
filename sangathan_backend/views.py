# I have created this
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        query = request.POST.get("query")
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
    return render(request, "contact.html")

def developer_view(request):
    return render(request, "developer.html")
