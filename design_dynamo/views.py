from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def graphic(request):
    return render(request, "graphic.html")

def team(request):
    return render(request, "team.html")

def teaser(request):
    return render(request, "teaser.html")

def cgi(request):
    return render(request, "cgi.html")

def submit_query(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        # Add success message
        messages.success(request, 'Data submitted successfully!')

        # Redirect to home page or any other page
        return redirect('home')

    return render(request, 'contact_us.html')
