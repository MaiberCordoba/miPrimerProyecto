from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status
from apps.posts.models import Post 

class PostApiView(APIView):
    def get(self,request):
        posts = [
            post.title for post in Post.bjects.all()
        ]
        return Response(status=status.HTTP_200_OK,data=posts)