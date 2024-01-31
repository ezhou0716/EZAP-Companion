from django.shortcuts import render
from firebase_admin import firestore

# Create your views here.
def get_problems():
    db = firestore.client() 
    ref = db.collection('derivatives')

    problems = ref.get()
    
    return problems


def problems(request):
    problems = get_problems()
    
    return render(request, 'problems.html')