import json
from helpers import myclerk
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import BlogPost

@csrf_exempt
@myclerk.api_login_required
def list_or_create_post_api_view(request):
    if request.method not in ["POST", "GET"]:
        return JsonResponse({"detail": "not allowed"}, status=400)
    user = request.user
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        blog_post_obj = BlogPost.objects.create(
            user=user,
            content=data.get('content'),
        )
        return JsonResponse({"content": blog_post_obj.content,
                            "user_id": request.user.clerk_user_id, 
                            "user_id2": blog_post_obj.user.clerk_user_id, 
                            "id": blog_post_obj.id})
    # assume GET method
    qs = BlogPost.objects.filter(user=user).order_by('-created_at')
    data = qs.values("id", "content", "created_at", "user__clerk_user_id")
    response_data = {
        "results": list(data),
        "count": qs.count(),
    }
    return JsonResponse(response_data)