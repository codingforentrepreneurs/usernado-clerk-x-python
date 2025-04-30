import os
import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import authenticate_request, AuthenticateRequestOptions

from django.conf import settings
from django.http import JsonResponse

CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY


def hello_world_api_view(request):
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=['http://localhost:3002']
        )
    )
    payload = request_state.payload
    clerk_user_id = payload.get('sub')
    print(clerk_user_id, request_state.is_signed_in)
    return JsonResponse({"hello": "world"})