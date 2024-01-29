from django.shortcuts import render
from firebase_admin import db

# Create your views here.
def get_problem():
    ref = db.reference('/derivatives')

    problems = ref.get()

    return problems


def problems(request):
    problem = get_problem()
    
    return render(request, 'problems.html')