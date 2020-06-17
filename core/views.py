from django.shortcuts import render, HttpResponse


def hello(request, x1, x2):
    soma=x1+x2
    return HttpResponse('A soma é: {}'.format(soma))

