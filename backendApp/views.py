from django.contrib.auth.models import User, Group
from backendApp.models import Client
from rest_framework.response import Response
from rest_framework import status
from backendApp.serializers import ClientSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.request import Request

# class ClientList(APIView):
#     """
#     A class based view for creating and fetching student records
#     """
#     def get(self, format=None):
#         """
#         Get all the student records
#         :param format: Format of the student records to return to
#         :return: Returns a list of student records
#         """
#         clients = Client.objects.all()
#         serializer = ClientSerializer(clients, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         """
#         Create a student record
#         :param format: Format of the student records to return to
#         :param request: Request object for creating student
#         :return: Returns a student record
#         """
#         serializer = ClientSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)

# class ClientDetail(APIView):
#     """
#     Retrieve, update or delete a Client instance.
#     """
#     # not working
#     def get_queryset(self):
#         """
#         This view should return a list of all the users for
#         the user as determined by the username portion of the URL.
#         """
#         username = self.kwargs['username']
#         return Client.objects.filter(username)

#     def get_object(self, pk):
#         try:
#             return Client.objects.get(pk=pk)
#         except Client.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Client = self.get_object(pk)
#         serializer = ClientSerializer(Client)
#         return Response(serializer.data)

#     # not working
#     def put(self, request, pk, format=None):
#         Client = self.get_object(pk)
#         serializer = ClientSerializer(instance=Client, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         Client = self.get_object(pk)
#         Client.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    """
    A class based view for creating and fetching student records
    """
    def get(self, format=None):
        """
        Get all the student records
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """
        Create a student record
        :param format: Format of the student records to return to
        :param request: Request object for creating student
        :return: Returns a student record
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Retrieve, update or delete a Client instance.
    """
    # not working
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the users for
    #     the user as determined by the username portion of the URL.
    #     """
    #     username = self.kwargs['username']
    #     return Client.objects.filter(username)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        User = self.get_object(pk)
        serializer = UserSerializer(User)
        return Response(serializer.data)

    # not working
    def put(self, request, pk, format=None):
        User = self.get_object(pk)
        serializer = UserSerializer(instance=User, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        User = self.get_object(pk)
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)