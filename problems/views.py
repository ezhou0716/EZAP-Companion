from django.shortcuts import render
from firebase_admin import firestore
import random

# Create your views here.
def get_problems():
    db = firestore.client() 
    ref = db.collection('derivatives')

    problems = [doc.to_dict() for doc in ref.stream()]
    
    return problems


def problems(request):
    if request.method == 'POST' and 'new_problem' in request.POST:
        problems = get_problems()
        random_problem = random.choice(problems)
        return render(request, 'problems.html', {'random_problem': random_problem})
    else:
        return render(request, 'problems.html')