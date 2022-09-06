from django.http import HttpResponse
from django.shortcuts import render


def response_200(request):
    return HttpResponse('{"status": "OK"}', status=200)

