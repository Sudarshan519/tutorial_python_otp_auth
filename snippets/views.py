
from django.contrib.auth.models import Group
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import AttendanceSerializer, CompanySerializer, EmployeeSerializer, EmployerSerializer, InvitationSerializer, SnippetSerializer, UserSerializer


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @api_view(['GET', 'POST'])
# def snippet_list(request,format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk,format=None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



#  USING APIVIEW
# from django.http import Http404
# class SnippetList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)



# class SnippetDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly]
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# USING MIXINS
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


#### GENERICE CLASS BASED VIEWS
 
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from rest_framework import generics

from rest_framework import permissions

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    


from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

#USER VIEEW SET
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

  



# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users', request=request, format=format),
        'snippets': reverse('snippets', request=request, format=format)
    })

# from rest_framework import renderers

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)





from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Employee, Employer, phoneModel,Invitation
import base64
import json
from rest_framework.decorators import api_view, permission_classes
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"

class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    # @permission_classes([IsAuthenticated])
    @staticmethod
    def get(request, phone):

        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
       
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone
            )
            
            user=User.objects.create(username=phone,password='')
            print("user created")
            if   request.data['isEmployer'] is True:
                print(request.data['isEmployer'])
                user=User.objects.get(username='auth.AuthUrls')
                employer=Employer.objects.create(phone=phoneModel(Mobile=phone),)
                my_group = Group.objects.get(name='Employer') 
                user.groups.add(my_group)
                print(employer)
            else:
                my_group = Group.objects.get(name='Employee') 
                user.groups.add(my_group)
                employee=Employee.objects.create(phone=phoneModel(Mobile=phone))
                print(employee)
               
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            user =User.objects.get(username=phone)
            # print(user)
            # from rest_framework.authtoken.models import Token
            from rest_framework_simplejwt.tokens import RefreshToken
            refresh = RefreshToken.for_user(user)
            # token = Token.objects.create(user)
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),})
            return Response("You are authorised", status=200) 
        return Response("OTP is wrong/expired", status=400)
# Time after which OTP will expire
# EXPIRY_TIME = 50 # seconds

# class getPhoneNumberRegistered_TimeBased(APIView):
#     # Get to Create a call for OTP
#     @staticmethod
#     def get(request, phone):
        
#         # res= createEmployee(phone)
#         # print(res)
#         try:
#             Mobile = phoneModel.objects.get(Mobile=phone)
            
#               # if Mobile already exists the take this else create New One
#         except ObjectDoesNotExist:
#             phoneModel.objects.create(
#                 Mobile=phone,
#             )
#             Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
#         Mobile.save()  # Save the data
#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
#         OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model for OTP is created
#         print(OTP.now())
#         # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
#         return Response({"OTP": OTP.now()}, status=200)  # Just for demonstration

#     # This Method verifies the OTP
#     @staticmethod
#     def post(request, phone):
#         # res= createEmployee(phone) 
#         try:
#             Mobile = phoneModel.objects.get(Mobile=phone)
#         except ObjectDoesNotExist:
#             return Response("User does not exist", status=404)  # False Call
#         print(request.data['isEmployer'])
        
#         keygen = generateKey()
#         key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
#         OTP = pyotp.TOTP(key,interval = EXPIRY_TIME)  # TOTP Model 
#         if OTP.verify(request.data["otp"]):  # Verifying the OTP
#             Mobile.isVerified = True
#             Mobile.save()
 
#             return Response("You are authorised", status=200)
#         return Response("OTP is wrong/expired", status=400)

# @authentication_classes([SessionAuthentication, BasicAuthentication])
class CreateEmployee(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,) 
    @staticmethod
    def get(self):
        phone=phoneModel.objects.get(Mobile=int(self.user.username))
        try:
            result=Employee.objects.create(user=self.user,phone=phone)
        
        
            print(result)
        except:
            result=Employee.objects.get(user=self.user)
        print(self.user)
        return Response(str(result), 200)
# from django.core import serializers
from rest_framework import serializers
class Employee(viewsets.ModelViewSet):
    # permission_classes=(IsAuthenticated)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                           ]
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer



class Employer(viewsets.ModelViewSet):
    # permission_classes=(IsAuthenticated)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializer

from .models import Attendance
from django.db import connection

from rest_framework.exceptions import APIException
# custom exception
# class ValidationError401(APIException):
#     status_code = status.



class AttendanceV(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,]
    queryset=Attendance.objects.all().order_by('login_time')
    serializer_class = AttendanceSerializer
    def perform_create(self, serializer):
        # print(self.request.user)
        try:
            date=datetime.now()
            dateF=(date.strftime('%Y-%m-%d'))#T%H:%M:%S.%f%z
            # print(str(datetime.now()))
            attendance=Attendance.objects.get(date= (dateF ),user=self.request.user)
            # print(attendance)
            dict=model_to_dict(attendance)
            if self.request.method=="POST":
                
                raise serializers.ValidationError({"duplicate_login":"User already logged in.","data":dict},status.HTTP_409_CONFLICT)
            else:
                serializer.save(user=self.request.user)        
        except ObjectDoesNotExist:
            # print(self.request.body)
            serializer.save(user=self.request.user) 
        
        
       
        
    # def get_queryset(self, request):
    #     max_ids_subquery = Attendance.objects.values('date', ').annotate(max_id=Max('id')).values('max_id')

    #     queryset = Attendance.objects.filter(id__in=max_ids_subquery)

    #     return queryset
    
class InvitationList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     serializer.save(user_detail=self.request.user) 
    # @staticmethod
    # def get(request):
    #     invitations=Invitation.objects.all()
    #     print(invitations)
    #     invitation_serializer= InvitationSerializer(invitations,many=True)
    #     data=invitation_serializer.data
    #     # print(data)
    #     # data = serializers.serialize('json',Invitation.objects.all())
    #     return JsonResponse( data,safe=False)
    # @staticmethod
    # def post(request):
    #     print(request.body)
    #     return JsonResponse(request.data,safe=False)


# def createEmployee( phone):
#     # username=request.data['username']
#     e=Employee.objects.get(phoneModel(phoneModel))
#     print(e)
#     employee= Employee(phoneModel(phone))
#     print(phone)
#     employee.save()
#     print(employee)


class CompanyV(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,IsOwnerOrReadOnly)
    queryset = Company.objects.order_by('created_at').all()
    serializer_class=CompanySerializer
    def perform_create(self, serializer):
        try:
            employer=Employer.objects.get(user=self.request.user)
            serializer.save(employer=employer)
        except Employer.DoesNotExist:
            raise serializers.ValidationError({"employer error":"Employer details does not exists."})