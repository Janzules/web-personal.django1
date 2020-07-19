from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(recuest):
     Projects = Project.objects.all()
     return render (recuest, "portfolio/portfolio.html",{'Projects':Projects})