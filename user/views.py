from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializers import RegistrationSerializer, LoginSerializer


# Create your views here.
class UserRegistration(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "User Registration Successfully", "status": 201, "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            user = User.objects.all()
            serializer = RegistrationSerializer(user, many=True)
            return Response({"message": "Retrieve Data  Successfully", "status": 201, "data": serializer.data},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        try:
            post = User.objects.get(id=user_id)
            serializer = RegistrationSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Updated Successfully", "status": 200, "data": serializer.data},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)

    def delete(self, request, user_id):
        try:
            books = User.objects.get(id=user_id)
            books.delete()
            return Response({"message": " deleted Successfully", "status": 200, "data": {}},
                            status=200)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)


class Login(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            login(request, serializer.context.get('user'))
            return Response({"message": "Login Successful", "status": 201, "data": {}}, status=201)
        except Exception as e:
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"Message": "Logout Successfully"})
        return Response({"Message": "User already logout"})
