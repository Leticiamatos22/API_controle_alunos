from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tarefa, Aluno, Disciplina
from .serializers.tarefaSerializer import TarefaSerializer
from .serializers.alunoSerializer import AlunoSerializer
from .serializers.disciplinaSerializer import DisciplinaSerializer
from rest_framework import generics

# Views relacionadas a Tarefas
class TaskList(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# Views relacionadas a Alunos

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


# Views relacionadas a Disciplinas

class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


