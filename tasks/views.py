from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa, Aluno, Disciplina
from .serializers.tarefaSerializer import TarefaSerializer
from .serializers.alunoSerializer import AlunoSerializer
from .serializers.disciplinaSerializer import DisciplinaSerializer
from rest_framework import generics

class TaskList(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

#################### CLASS ALUNO ##########################
class AlunoList(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def put(self, request, pk):
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aluno = self.get_object(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
###################### CLASS DISCIPLINA ######################

class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

###################### CLASS Aluno ######################

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer