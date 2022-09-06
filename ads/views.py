from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView

from ads.models import Ad


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
