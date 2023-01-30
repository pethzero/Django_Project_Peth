from rest_framework import serializers
from .models import *


class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapper
        fields = ('name', 'aka')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'date', 'body')
