from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view): #전체적인 권한
        if request.method == 'GET': #글 조회는 누구나 할수있음.
            return True
        return request.user.is_authenticated #조회가 아닌 다른행위는 로그인 여부를 확인함.

    def has_object_permission(self, request, view, obj):#특정 object에 접근하는 순간 권한 확인
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user #obj의 저서가 현재 로그인된 user와 같으면 True 반환