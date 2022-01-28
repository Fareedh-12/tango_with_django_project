from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, Creamy, Cookie, Candy, Cupcake!'}

    return render(request, 'rango/index.html/', context=context_dict)


def about(request):
    context_dict = {
        'boldmessage': 'this tutorial has been put together by Fareedh'}

    return render(request, 'rango/about.html/', context=context_dict)
