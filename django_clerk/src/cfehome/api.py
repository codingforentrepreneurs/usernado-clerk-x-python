from django.http import JsonResponse


def hello_world_api_view(request):

    return JsonResponse({"hello": "world"})