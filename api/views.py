#@api_view([''])の形式でviewsの前に置くことでmethod(GET,POST,PUT,DELETEのいずれか)のどの機能を有効にするかを定義
from rest_framework.decorators import api_view
#return Response(data)の形dataは辞書型または辞書型の入ったリスト型でapi形式で返答する
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import NoteSerializer
from.models import Note

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post req'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post req'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):#ここのrequestはこのメソッドがviews形式のメソッドであることを示す。
    notes=Note.objects.all()#ここでNoteクラスのインスタンスを全てnotes変数に代入
    serializer= NoteSerializer(notes,many=True)#ここでNoteSerializerを使いnotesをjson形式に変換
    #シリアライズするインスタンスが複数ある場合はmany=Trueとする。
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):#pkでNotesインスタンスのidを取得できます。
    note=Note.objects.get(id=pk)
    serializer= NoteSerializer(note,many=False)#ここでNoteSerializerを使いnotesをjson形式に変換
    #シリアライズするインスタンスが複数ある場合はmany=Trueとする。
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data=request.data#POSTページで入力されたjson形式のdata

    note=Note.objects.create(
        body=data['body']
    )
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])#更新するview
def updateNote(request,pk):
    data=request.data
    note=Note.objects.get(id=pk)

    serializer=NoteSerializer(note,data=request.data)
    if serializer.is_valid():#更新された値が有効な値かを確認
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])#削除するview
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted!")