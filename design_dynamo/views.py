from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.contrib import messages

cred = credentials.Certificate(r"C:\Users\dhruv\PycharmProjects\DesignDynamo\designdynamo\design_dynamo/cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
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

        # Add data to Firestore
        doc_ref = db.collection('queries').add({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'query': query
        })

        # Add success message
        messages.success(request, 'Data inserted successfully!')

        # Redirect to home page or any other page
        return redirect('home')

    return render(request, 'contact_us.html')