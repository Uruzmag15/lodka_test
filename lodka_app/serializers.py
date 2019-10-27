from rest_framework import serializers

from .models import Category


class OneCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    parents = OneCategorySerializer(read_only=True, many=True)
    children = OneCategorySerializer(read_only=True, many=True)
    siblings = OneCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parents', 'children', 'siblings')
