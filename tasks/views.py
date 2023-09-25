from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa, Aluno, Disciplina
from .serializers.tarefaSerializer import TarefaSerializer
from .serializers.alunoSerializer import AlunoSerializer
from .serializers.disciplinaSerializer import DisciplinaSerializer


# Views relacionadas a Tarefas
class TaskList(APIView):
    def get(self, request):
        # Lista todas as tarefas
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cria uma nova tarefa
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            # Obtém uma tarefa específica pelo ID
            return Tarefa.objects.get(pk=pk)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # Obtém detalhes de uma tarefa específica pelo ID
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        # Atualiza os detalhes de uma tarefa específica pelo ID
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Exclui uma tarefa específica pelo ID
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views relacionadas a Alunos
class AlunoList(APIView):
    def get(self, request):
        # Lista todos os alunos
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cria um novo aluno
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlunoDetail(APIView):
    def get_object(self, pk):
        try:
            # Obtém um aluno específico pelo ID
            return Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # Obtém detalhes de um aluno específico pelo ID
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        # Atualiza os detalhes de um aluno específico pelo ID
        aluno = self.get_object(pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Exclui um aluno específico pelo ID
        aluno = self.get_object(pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views relacionadas a Disciplinas
class DisciplinaList(APIView):
    def get(self, request):
        # Lista todas as disciplinas
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cria uma nova disciplina
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaDetail(APIView):
    def get_object(self, pk):
        try:
            # Obtém uma disciplina específica pelo ID
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        # Obtém detalhes de uma disciplina específica pelo ID
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        # Atualiza os detalhes de uma disciplina específica pelo ID
        disciplina = self.get_object(pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Exclui uma disciplina específica pelo ID
        disciplina = self.get_object(pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#####

class AlunoTasksView(APIView):
    def get(self, request, pk):
        try:
            # Obtém o aluno pelo ID fornecido
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # Obtém todas as tarefas associadas a esse aluno
        tarefas = Tarefa.objects.filter(aluno=aluno)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
