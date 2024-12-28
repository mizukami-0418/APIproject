from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User


class HelloWorldAPIViews(APIView):
    def get(self, request):
        # クエリパラメータからusernameを取得（例: /api/hello/?username=John）
        username = request.query_params.get('username', None)
        if username:
            message = f"Hello {username}!"
        else:
            message = "Hello World!" # usernameがない場合のデフォルトメッセージ
        return Response({"message": message})
    
    def post(self, request):
        # エラーハンドリング
        if not request.data:
            return Response(
                {"error": "No data provided."},
                status=status.HTTP_400_BAD_REQUEST
            )
        # POSTリクエストで送信されたデータからusernameを取得
        username = request.data.get('username', None)
        if username:
            user = User.objects.create(username=username)
            user.save()
            
            return Response(
                {"message" : f"Hello {username}!", "id": user.id},
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": "Username is required."},
                status=status.HTTP_400_BAD_REQUEST
            )