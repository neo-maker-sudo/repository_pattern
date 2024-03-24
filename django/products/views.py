import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product_business.adapters.repository import ProductRepository
from product_business.service_layer import services


@csrf_exempt
def create_product_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        services.create_product(
            data["product_name"], data["price"], data["total"], ProductRepository()
        )

        return HttpResponse("OK", status=201)


def retrieve_product_view(request, product_id):

    product = services.retrieve_product(product_id, ProductRepository())

    return JsonResponse(
        {"name": product.name, "price": product.price, "total": product.total},
        status=200,
    )
