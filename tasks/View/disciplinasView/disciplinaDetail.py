from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Disciplina
from tasks.serializers import DisciplinaSerializer

class DisciplinaDetail(APIView):
    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)
