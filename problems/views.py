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
        # selected_unit = request.POST.get('units')

        db = firestore.client() 
        ref = db.collection('derivatives')

        problems = [doc.to_dict() for doc in ref.stream()]

        random_problem = random.choice(problems) if problems else None

        tags = set()
        for problem in problems:
            tags.update(problem['tags'])
        
        return render(request, 'problems.html', {'random_problem': random_problem, 'tags': tags})
    else:
        return render(request, 'problems.html')
