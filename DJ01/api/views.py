# In hackademy/api/views.py
from django.contrib.auth.models import User, Group
from django.http import HttpRequest
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.views import Response
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.renderers import JSONRenderer

from django.contrib.auth.decorators import login_required


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def edit_users_view(request: HttpRequest):
    data = UserSerializer(
        User.objects.all(), many=True, context={"request": request}
    ).data

    return Response(data)
