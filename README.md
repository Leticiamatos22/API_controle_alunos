# API_controle_alunos

API de Gerenciamento de Alunos, Disciplinas e Tarefas

Esta API Django foi criada para auxiliar os alunos na gestão de suas disciplinas e tarefas de forma eficiente. A API apresenta três modelos principais: Aluno, Disciplina e Tarefa, com relacionamentos bem definidos entre eles. 

Abaixo estão as funcionalidades essenciais disponíveis nesta API:

Modelos de Dados
Modelo Aluno:
Campos: nome, email

Modelo Disciplina:
Campos: nome, descricao

Modelo Tarefa:
Campos: titulo, descricao, data_entrega, concluida
Relacionamento Many-to-Many com Disciplina: Uma tarefa pode estar associada a uma ou mais disciplinas.