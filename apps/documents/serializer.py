from rest_framework import serializers
from . models import Memorando, Official, Requeriment

class MemorandoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Memorando
        fields = ["uuid","others","number","receiver","title","destiny","confirm","description","user","created_at"]


