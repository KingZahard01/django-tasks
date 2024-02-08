# from django.shortcuts import render
from django.http import HttpResponse  # , JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    return render(request, 'about.html')


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def hello(request, username):
    # inserta el username en el h2
    return HttpResponse("<h2>Hello %s</h2>" % username)


def create_task(request):
    # si me visitan con metodo get
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        project_id = 3
        project_instance = Project.objects.get(pk=project_id)
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project=project_instance
        )
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project, 
        'tasks': tasks,
    })