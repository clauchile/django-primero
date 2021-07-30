from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def index(request):
    return HttpResponse("<h1>placeholder para luego mostrar una lista de blogs</h1>")

def root(request):
    return redirect("blogs/")
def create(request):
    return redirect("/")

def new (request):
    return HttpResponse("<h3>placeholder para mostrar un nuevo formulario para crear un nuevo blog</h3>")

def show (request, val):
    return HttpResponse(f'<h2>placeholder para mostrar el blog numero: {val}</h2> <dr> <h3>Método show</h3>')

def edit (request, number):
    return HttpResponse(f'<h2>placeholder para editar el blog numero: {number}</h2> <dr> <h3>Método edit</h3>')

def destroy (request, number):
    return redirect("/blogs/")

def Json (request):
    return JsonResponse({"titulo":"Este es un titulo con Json"})







 #/blogs/< number > - muestra el string "placeholder para mostrar el blog numero: {number}" 
 # con un método llamado "show" (ej. localhost:8000/blogs/15 debería mostrar el mensaje: 
 # 'placeholder para mostrar el blog numero 15')





 #/blogs/< number >/edit - muestra el string "placeholder para editar el blog {number}"
 #  con un método llamado "edit"

 #/blogs/< number >/delete - redirige a la ruta "/blogs" con el método llamado "destroy"

 #(**Bonus**) /blogs/json - regresa una JsonResponse con un titulo y que contenga llaves.