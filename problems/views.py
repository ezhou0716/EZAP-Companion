from django.shortcuts import render
from firebase_admin import firestore
import random

# Create your views here.
def get_problems(unit, tags):
    db = firestore.client() 
    ref = db.collection(unit)

    problems = [doc.to_dict() for doc in ref.stream()]
    
    if tags:
        filtered_problems = []
        for problem in problems:
            if all(tag in problem['tags'] for tag in tags):
                filtered_problems.append(problem)
        return filtered_problems
    return problems


def get_tags(unit):
    db = firestore.client()
    ref = db.collection(unit)
    
    tags = set()
    for doc in ref.stream():
        tags.update(doc.to_dict().get('tags', []))
        
    return tags


def problems(request):
    if request.method == 'POST' and 'new_problem' in request.POST:
        selected_unit = request.POST.get('units')
        selected_tags = request.POST.getlist('tags')

        problems = get_problems(selected_unit, selected_tags)

        random_problem = random.choice(problems) if problems else None

        tags = get_tags(selected_unit)
        
        return render(request, 'problems.html', {'random_problem': random_problem, 'tags': tags, 'selected_unit': selected_unit})
    else:
        return render(request, 'problems.html')
