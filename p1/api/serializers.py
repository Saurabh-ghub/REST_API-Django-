from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField()
    roll = serializers.IntegerField()
    marks = serializers.IntegerField()