from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Aluno, Disciplina
from tasks.serializers import DisciplinaSerializer

class DisciplinaList(APIView):
    def get_object(self, pk):
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        aluno = self.get_object(pk)
        disciplinas = aluno.disciplinas.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)
