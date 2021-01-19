from django.db.models import query
from rest_framework import mixins, status
from rest_framework import permissions
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User, Group

from .serializers import *
from .permissions import *


class GroupViewSet(viewsets.ModelViewSet):
    queryset = (Group.objects.prefetch_related('permissions'))
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related(
        'groups',
    )
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsSuperuserOrOwner,
    )

    def get_object(self):
        """
        Returns the user object the view is displaying.
        """
        if self.request.user.is_superuser:
            return super().get_object()
        # May raise a permission denied
        self.check_object_permissions(self.request, self.request.user)

        return self.request.user


class AccountViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     APIView):
    serializer_class = UserSerializer
    permission_classes = (
        IsOwner,
    )

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.serializer_class

        kwargs.setdefault('context', self.get_serializer_context())
        serializer_instance = serializer_class(*args, **kwargs)
        if self.request.method != 'POST':
            serializer_instance.fields.pop('password')
        return serializer_instance

    """
    Concrete view for creating a model instance.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    """
    Concrete view for deleting a model instance.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    """
    Concrete view for updating a model instance.
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_object(self):
        """
        Returns the user object the view is displaying.
        """
        # May raise a permission denied
        self.check_object_permissions(self.request, self.request.user)

        return self.request.user


me_account = AccountViewSet.as_view()