from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import ActivitySerializer, AddLinkSerializer, SignUpSerializer
from authapp import serializers


# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer = SignUpSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
        "user": 'user has been created'
    })


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        "details": {
            'username': user.username,
            'token': token
        }
    })


@api_view(['POST'])
def add_link(request):
    serializer = AddLinkSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    link = serializer.save()

    return Response({
        'detail': "Link has been saved"
    })


@api_view(['POST', 'GET'])
def activities(request):
    if request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        return Response({
            'sender': str(activity.sender),
            'receiver': str(activity.receiver),
            'sender link': str(activity.sender_link),
            'receiver link': str(activity.receiver_link),
            'status': str(activity.status), 
        })
    elif request.method == 'GET':
        #FOR NOW
        pass