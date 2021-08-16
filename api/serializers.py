#定義したモデルをシリアライズするためにこれをモデル名Serializer(ModelSerializer)する
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        #Meta内でmodel=モデル、シリアライズするfieldを選択(全ての場合は'__all__')
        model=Note
        fields='__all__'