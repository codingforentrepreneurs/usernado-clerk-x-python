import json
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

from django.conf import settings
from django.contrib.auth import get_user_model

import warnings

# Suppress all warnings from a specific package
warnings.filterwarnings("ignore", module="clerk_backend_api")
warnings.filterwarnings("ignore", module="pydantic")

CLERK_SECRET_KEY = settings.CLERK_SECRET_KEY
CLERK_AUTH_PARTIES = settings.CLERK_AUTH_PARTIES

User = get_user_model()


def get_clerk_user_id_from_request(request):
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=CLERK_AUTH_PARTIES
        )
    )
    if not request_state.is_signed_in:
        return None
    payload = request_state.payload
    clerk_user_id = payload.get('sub')
    return clerk_user_id


def update_or_create_clerk_user(clerk_user_id):
    if not clerk_user_id:
        return None, None
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    clerk_user = sdk.users.get(user_id=clerk_user_id) # User.objects.get(id=id)
    if not clerk_user:
        return None, None
    primary_email_address_id = clerk_user.primary_email_address_id
    primary_email = next((email for email in clerk_user.email_addresses if email.id == primary_email_address_id), None)   
    django_user_data = {
        "username": clerk_user.username,
        "first_name": clerk_user.first_name,
        "last_name": clerk_user.last_name,
        "email": primary_email,
    }
    user_obj, created = User.objects.update_or_create(
        clerk_user_id=clerk_user_id,
        defaults=django_user_data
    )
    return user_obj, created
    # clerk_user_json = json.loads(clerk_user.model_dump_json())
    