from django.shortcuts import render, HttpResponse

html_base = """
   <h1> Mi web Personal</h1>
   <ul>
      <li><a href="/">Portada</a></li>
      <li><a href="/about/">Acerca de...</a></li> 
      <li><a href="/portfolio">Portafolio</a></li>
      <li><a href="/contact/">Contacto</a></li> 
   </ul>    
"""
# Create your views here.
def home(recuest):
    return render (recuest, "core/home.html")
def about(recuest):
    return render (recuest, "core/about.html")
def contact(recuest):
    return render (recuest, "core/contact.html")