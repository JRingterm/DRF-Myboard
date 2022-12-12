from rest_framework import viewsets
#from django_filters.rest_framework import DjangoFilterBackend #view마다 필터 설정할때 사용 (이미 settings.py에서 등록해서 안써도됨)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import Profile
from .models import Post, Comment
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer, CommentCreateSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]
    #filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'likes']

    def get_serializer_class(self):
        if self.action == 'list' or 'retreive': #전체 조회, 1개 조회 이면
            return PostSerializer #게시글을 조회할 때의 데이터를 변환하는 시리얼라이저(세세한 데이터까지 다 변환)
        return PostCreateSerializer #게시글을 작성할 때의 데이터를 변환하는 시리얼라이저(유저가 입력해야하는 데이터만 변환)
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

@api_view(['GET']) #데코레이터
@permission_classes([IsAuthenticated]) #좋아요 권한은 회원가입한 유저라면 누구든 가능.
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all(): #해당 유저가 이미 좋아요를 눌렀다면
        post.likes.remove(request.user) #좋아요에서 제거
    else:
        post.likes.add(request.user) #좋아요에 추가

    return Response({'status': 'ok'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return CommentSerializer
        return CommentCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)

