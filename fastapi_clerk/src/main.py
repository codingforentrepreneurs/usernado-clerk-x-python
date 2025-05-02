import os

from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

CLERK_FRONTEND_HOST = os.environ.get("CLERK_FRONTEND_HOST")
CLERK_FRONTEND_HOST2 = os.environ.get("CLERK_FRONTEND_HOST2")
CLERK_SECRET_KEY = os.environ.get("CLERK_SECRET_KEY")


authorized_parties=[CLERK_FRONTEND_HOST]
if CLERK_FRONTEND_HOST2:
    authorized_parties.append(CLERK_FRONTEND_HOST2)

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
            authorized_parties=[CLERK_FRONTEND_HOST]
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


class PostCreateSchema(BaseModel):
    content: str

# HTTP POST -> /api/posts/
@app.post("/api/posts/")
def create_post(request:Request, payload: PostCreateSchema):
    clerk_user_id = get_clerk_user_id_from_request(request)
    print(payload.model_dump())
    print(payload.content)
    return {"content": payload.content}