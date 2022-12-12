from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission): #GET=누구나, PUT/PATCH=해당유저
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #GET처럼 데이터에 영향을 주지 않는 메소드라면
            return True
        return obj.user == request.user #요청으로 들어온 유저와 객체의 유저를 비교, 같으면 통과(1)