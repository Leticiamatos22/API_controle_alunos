from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Aluno
from tasks.serializers import AlunoSerializer

class AlunoDetail(APIView):
    def get_object(self, pk):
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)
