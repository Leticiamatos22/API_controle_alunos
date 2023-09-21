from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nome
     # Classe que representa um aluno.

    # Atributos:
    # - nome: O nome do aluno (campo de texto com no máximo 100 caracteres).
    # - email: O endereço de e-mail único do aluno (campo de e-mail).

   
   


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    #  Classe que representa uma disciplina.

    # Atributos:
    # - nome: O nome da disciplina (campo de texto com no máximo 100 caracteres).
    # - descricao: Uma descrição da disciplina (campo de texto).

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.titulo
    
    # lasse que representa uma tarefa atribuída a um aluno em uma ou mais disciplinas.

    # Atributos:
    # - titulo: O título da tarefa (campo de texto com no máximo 100 caracteres).
    # - descricao: Uma descrição mais detalhada da tarefa (campo de texto).
    # - data_entrega: A data de entrega da tarefa (campo de data).
    # - concluida: Um campo booleano que indica se a tarefa foi concluída ou não (padrão é False).
    # - aluno: Uma chave estrangeira que relaciona a tarefa a um aluno específico.
    # - disciplinas: Uma relação many-to-many que permite associar a tarefa a uma ou mais disciplinas.
