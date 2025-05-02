import json
from helpers import myclerk
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import BlogPost

@csrf_exempt
@myclerk.api_login_required
def create_post_api_view(request):
    if not request.method == "POST":
        return JsonResponse({"detail": "not allowed"}, status=400)
    user = request.user
    data = json.loads(request.body.decode('utf-8'))
    blog_post_obj = BlogPost.objects.create(
        user=user,
        content=data.get('content'),
    )
    return JsonResponse({"content": blog_post_obj.content,
                         "user_id": request.user.clerk_user_id, 
                         "user_id2": blog_post_obj.user.clerk_user_id, 
                         "id": blog_post_obj.id})