from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile

# Create your views here.
class RegisterView(generics.CreateAPIView): #회원등록
    queryset = User.objects.all() #User 모델에 있는 객체를 모두 불러온다
    serializer_class = RegisterSerializer #해당 API에서 사용할 시리얼라이저를 설정한다.

class LoginView(generics.GenericAPIView): #로그인
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data 
        return Response({"token": token.key}, status=status.HTTP_200_OK) #시리얼라이즈를 통해 얻어온 토큰을 그대로 응답해줌

class ProfileView(generics.RetrieveUpdateAPIView): #프로필 가져오기, 수정하기
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer