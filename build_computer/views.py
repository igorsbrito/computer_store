from builtins import Exception

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, status

from .models import Computer
from .serializer import ComputerSerializer
from .computer_rules import computer_components_exists, components_amount, components_compatibility


class ComputerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    # if sort variable is in the url can be selected ascendent or descendent sort
    def list(self, request):
        query_params = request.query_params

        if 'sort' in query_params:
            if query_params['sort'] == 'asc':
                ordered_queryset = self.queryset.order_by('created_date')

            elif query_params['sort'] == 'desc':
                ordered_queryset = self.queryset.order_by('-created_date')

            else:
                ordered_queryset = self.queryset

        else:
            ordered_queryset = self.queryset

        queryset_serialized = self.serializer_class(ordered_queryset, many=True)

        return Response(queryset_serialized.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def build_computer(self, request):
        data = request.data
        user = request.user

        if not computer_components_exists(data):
            return Response(
                {'mesage': 'The computer must have at list 3 components, one Mother Board, one CPU and one Memory Ram'},
                status=status.HTTP_400_BAD_REQUEST)

        status_component, components = components_amount(data)
        if status_component == 'fail':
            return Response({'mesage': 'Select only components that exists in the store list'},
                            status=status.HTTP_400_BAD_REQUEST)

        status_compatibility, msg = components_compatibility(components)
        if not status_compatibility:
            return Response({'mesage': msg}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Computer.objects.create_computer(components, user)

        except Exception as error:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)
