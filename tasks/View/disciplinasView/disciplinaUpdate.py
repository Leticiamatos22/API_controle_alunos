from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Disciplina
from tasks.serializers import DisciplinaSerializer

class DisciplinaUpdate(APIView):
    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
