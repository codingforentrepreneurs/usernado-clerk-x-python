from helpers import myclerk
from django.conf import settings
from django.http import JsonResponse

CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY



def hello_world_api_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Login Required"}, status=400)
    # print(request.user)
    user = request.user
    return JsonResponse({"first_name": user.first_name, "id": user.id})