from rest_framework import serializers
from . models import Memorando, Official, Requeriment

class MemorandoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Memorando
        fields = ["uuid","others","number","receiver","title","destiny","confirm","description","user","created_at"]

class OfficialSerializer(serializers.ModelSerializer):

    class Meta:

        model = Official
        fields = ["uuid","others","number","receiver","title","destiny","confirm","description","user","created_at"]


class RequerimentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requeriment
        fields = ["uuid","others","number","receiver","title","destiny","confirm","description","user","created_at"]