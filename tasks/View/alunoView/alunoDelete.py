from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Aluno, Tarefa
from tasks.serializers import AlunoSerializer

class AlunoDelete(APIView):
    def get_object(self, pk):
        try:
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        aluno = self.get_object(pk)
        # Desassocia ou exclui todas as tarefas associadas a esse aluno.
        for tarefa in aluno.tarefa_set.all():
            tarefa.aluno = None
            tarefa.save()
            # Ou se você desejar excluir as tarefas associadas:
            # tarefa.delete()
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
