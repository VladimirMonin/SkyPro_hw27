import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.views.generic.detail import BaseDetailView

from ads.models import Ad, Categories


def response_200(request):
    return HttpResponse('{"status": "OK"}', status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(
            {
                'id': ad.pk,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
            , safe=False, json_dumps_params={'ensure_ascii': False})


class CatDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse(
            {
                'id': cat.pk,
                'name': cat.name
            }
            , safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()
        response = [
            {
                'id': ad.pk,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            } for ad in ads]

        return JsonResponse(response, safe=False,
                            json_dumps_params={'ensure_ascii': False})

    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ad()

        ad.name = ad_data['name']
        ad.author = ad_data['author']
        ad.price = ad_data['price']
        ad.description = ad_data['description']
        ad.address = ad_data['address']
        ad.is_published = ad_data['is_published']

        ad.save()

        return JsonResponse(
            {
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            }
            , safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        cats = Categories.objects.all()
        response = [
            {
                'id': cat.pk,
                'name': cat.name

            } for cat in cats]

        return JsonResponse(response, safe=False,
                            json_dumps_params={'ensure_ascii': False})
