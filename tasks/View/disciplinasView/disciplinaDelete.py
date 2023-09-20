from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Disciplina
from tasks.serializers import DisciplinaSerializer

class DisciplinaDelete(APIView):
    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        disciplina = self.get_object(pk)
        # Desassocia ou exclui todas as tarefas associadas a essa disciplina.
        for tarefa in disciplina.tarefas.all():
            tarefa.disciplinas.remove(disciplina)
            tarefa.save()
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
