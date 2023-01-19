import json

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListCreateView(View):

    def get(self, request):
        response = []
        for cat in Category.objects.all():
            response.append({"ad": cat.id, "name": cat.name})
        return JsonResponse(response, safe=False)

    def post(self, request, **kwargs):
        data = json.loads(request.body)
        new_cat = Category.objects.create(
            name=data["name"]
        )
        return JsonResponse({"id": new_cat.id, "name": new_cat.name}, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({"id": cat.id, "name": cat.name}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdListCreateView(View):

    def get(self, request):
        response = []
        for ad in Ad.objects.all():
            response.append(
                {"ad": ad.id,
                 "name": ad.name,
                 "author": ad.author,
                 "price": ad.price})
        return JsonResponse(response, safe=False)

    def post(self, request, **kwargs):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            address=data["address"],
            description=data["description"],
            is_published=data["is_published"],
        )
        return JsonResponse(
                {"ad": new_ad.id,
                 "name": new_ad.name,
                 "author": new_ad.author,
                 "price": new_ad.price,
                 "address": new_ad.address,
                 "description": new_ad.description,
                 "is_published": new_ad.is_published}, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
                {"ad": ad.id,
                 "name": ad.name,
                 "author": ad.author,
                 "price": ad.price,
                 "address": ad.address,
                 "description": ad.description,
                 "is_published": ad.is_published}, safe=False)
