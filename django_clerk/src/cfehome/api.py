import os
import httpx
import json
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import authenticate_request, AuthenticateRequestOptions

from django.conf import settings
from django.http import JsonResponse

import warnings

# Suppress all warnings from a specific package
warnings.filterwarnings("ignore", module="clerk_backend_api")
warnings.filterwarnings("ignore", module="pydantic")

CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY


def get_clerk_user_id_from_request(request):
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=['http://localhost:3002']
        )
    )
    payload = request_state.payload
    clerk_user_id = payload.get('sub')
    if not request_state.is_signed_in:
        return None
    return clerk_user_id



def hello_world_api_view(request):
    clerk_user_id = get_clerk_user_id_from_request(request)
    if not clerk_user_id:
        return JsonResponse({"detail": "please login"}, status=400)
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    clerk_user = sdk.users.get(user_id=clerk_user_id) # User.objects.get(id=id)
    clerk_user_json = json.loads(clerk_user.model_dump_json())
    return JsonResponse(clerk_user_json)