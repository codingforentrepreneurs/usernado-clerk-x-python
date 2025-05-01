import os

from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

CLERK_SECRET_KEY = os.environ.get("CLERK_SECRET_KEY")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_clerk_user_id_from_request(request):
    sdk = Clerk(bearer_auth=CLERK_SECRET_KEY)
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=['http://localhost:3002']
        )
    )
    if not request_state.is_signed_in:
        return None
    payload = request_state.payload
    clerk_user_id = payload.get('sub')
    return clerk_user_id

# GET -> /
@app.get("/")
def read_root(request:Request):
    clerk_user_id = get_clerk_user_id_from_request(request)
    return {"hello": "world", "clerk_user_id": clerk_user_id}