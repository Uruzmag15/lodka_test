import json
from rest_framework import viewsets
from rest_framework import mixins
from django.http import HttpResponse


from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError as err:
            return HttpResponse('Incorrect json data! Error: "{}"'.format(err))

        def get_or_create_object(object, parent=None):
            obj_name = object.get('name')

            if obj_name:
                category, _ = Category.objects.get_or_create(name=obj_name,
                                                             parent=parent)
                for children in object.get('children', []):
                    get_or_create_object(children, parent=category)

            return

        get_or_create_object(json_data)

        return HttpResponse('Success!')
