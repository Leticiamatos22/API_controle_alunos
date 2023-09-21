from django.urls import path
from tasks.views import TaskList, TaskDetail,AlunoList, AlunoDetail, DisciplinaList, DisciplinaDetail 

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('aluno/', AlunoList.as_view(), name='task-list'),
    path('aluno/<int:pk>/', AlunoDetail.as_view(), name='task-detail'),
    path('disciplina/', DisciplinaList.as_view(), name='task-list'),
    path('disciplina/<int:pk>/', DisciplinaDetail.as_view(), name='task-detail'),
]
