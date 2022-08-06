from django.shortcuts import render, redirect, get_object_or_404
import matplotlib.pyplot as plt
import numpy as np
from django.contrib import messages

# Create your views here.

# for forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Todo, Progress, Done
from .forms import ProjectForm, TodoForm, ProgressForm, DoneForm
from .models import Team, wiki, resource
from .forms import ResourceForm


def index(request):
    # Todo list homepage
    return render(request, 'todo_lists/index.html')


def projects(request):
    # show all projects

    projects = Project.objects.order_by('project_code')
    context = {'projects': projects}
    return render(request, 'todo_lists/projects.html', context)


def project(request, project_id):
    # show everything under projects
    project = Project.objects.get(id=project_id)
    todos = project.todo_set.order_by('-project_code')
    progresses = project.progress_set.order_by('-project_code')
    dones = project.done_set.order_by('-project_code')
    context = {'project': project, 'todos': todos, 'progresses': progresses, 'dones': dones}
    return render(request, 'todo_lists/project.html', context)


def new_project(request):
    # add new project
    
    if request.method != 'POST':
        # if not submit then create a new form for user
        form = ProjectForm()
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            
            form.save()
            return HttpResponseRedirect(reverse('todo_lists:projects'))
# team', 'name', 'due_date', 'project_code', 'details
    context = {'form': form}
    return render(request, 'todo_lists/new_project.html', context)


def new_todo(request, project_id):
    # add a to do task for a project
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = TodoForm()
    else:
        form = TodoForm(data=request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.project = project
            new_todo.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form}
    return render(request, 'todo_lists/new_todo.html', context)


def new_progress(request, project_id):
    # add a in-progress for a project
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = ProgressForm()
    else:
        form = ProgressForm(data=request.POST)
        if form.is_valid():
            new_progress = form.save(commit=False)
            new_progress.project = project
            new_progress.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form}
    return render(request, 'todo_lists/new_progress.html', context)


def new_done(request, project_id):
    # add done tasks for a project
    project = Project.objects.get(id=project_id)

    if request.method != 'POST':
        form = DoneForm()
    else:
        form = DoneForm(data=request.POST)
        if form.is_valid():
            new_done = form.save(commit=False)
            new_done.project = project
            new_done.save()
            return HttpResponseRedirect(reverse('todo_lists:project', args=[project_id]))
                                        
    context = {'project': project, 'form': form}
    return render(request, 'todo_lists/new_done.html', context)


def edit_todo(request, todo_id):
    # edit current todo task

        todo = Todo.objects.get(id=todo_id)
    
        project = todo.project

        if request.method != 'POST':
            # first time filled with current content
            form = TodoForm(instance=todo)
        else:
            form = TodoForm(instance=todo, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('todo_lists:project',
                                                    args=[project.id]))

        context = {'todo': todo, 'project': project, 'form': form}
        return render(request, 'todo_lists/edit_todo.html', context)


def edit_project(request, project_id):
    # edit current project

        project = Project.objects.get(id=project_id)
    

        if request.method != 'POST':
            # first time filled with current content
            form = ProjectForm(instance=project)
        else:
            form = ProjectForm(instance=project, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('todo_lists:projects'))

        context = {'project': project, 'form': form}
        return render(request, 'todo_lists/edit_project.html', context)


     
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo.delete()
        return redirect('/')

    context = {'todo': todo}
    return render(request, 'todo_lists/delete.html', context)


def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('/')

    context = {'project': project}
    return render(request, 'todo_lists/delete_project.html', context)


def edit_progress(request, progress_id):
    # edit current in-progress task
    progress = Progress.objects.get(id=progress_id)
    project = progress.project

    if request.method != 'POST':
        # first time filled with current content
        form = ProgressForm(instance=progress)
    else:
        form = ProgressForm(instance=progress, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_lists:project',
                                                args=[project.id]))

    context = {'progress': progress, 'project': project, 'form': form}
    return render(request, 'todo_lists/edit_progress.html', context)


# def visualisation(request):

#     todo = Todo.objects.all()
#     todo_count = todo.count()
#     progress = Progress.objects.all()
#     progress_count = progress.count()
#     done = Done.objects.all()
#     done_count = done.count()

#     if request.method != 'POST':
#             # first time filled with current content
#             form = TodoForm(instance=todo)
#     else:
#             form = TodoForm(instance=todo, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('todo_lists:project',
#                                                     args=[project.id]))
#     context = {
#         'form': form,
        
#         'todo_count': todo_count,
#         'progress_count': progress_count,
#         'done_count': done_count,
#     }
#     return render(request, 'todo_lists/progress.html', context)

# def edit_progect(request, project_id):
    # project = Project.objects.get(id=project_id)
    

    # if request.method != 'POST':
    #     # first time filled with current content
    #     form = ProgressForm(instance=progress)
    # else:
    #     form = ProgressForm(instance=progress, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(reverse('todo_lists:project',
    #                                             args=[project.id]))

    # context = {'progress': progress, 'project': project, 'form': form}
    # return render(request, 'todo_lists/edit_progress.html', context)

# def visualisation(request):
#     # Matplotlib通过 pie()方法绘制饼状图
#     x = [1, 2, 3]
#     # 饼状图中每个部分离中心点的距离，其中0.2表示图中远离中心的A部分
#     explode = (0.2, 0, 0)
#     plt.pie(x,
#             labels=['todo','in-progress','done'],
#             explode=explode,
#             autopct='percent:%4.1f%%'  # 每个部分的比例标签。其中：%是一种控制符；4表示输出宽度为4；.1表示输出的时候只输出小数点后1位（其余不显示）；f表示浮点数。
#             )
#     # x,y轴刻度等长
#     plt.axis('equal')  # 防止饼状图被压缩成椭圆
#     plt.show()
#     return render(plt.show)
def visualisation(request):
    todo = Todo.objects.all()
    todo_count = todo.count()
    progress = Progress.objects.all()
    progress_count = progress.count()
    done = Done.objects.all()
    done_count = done.count()

    # if request.method == 'POST':
    #     form = ProjectForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    #         return HttpResponseRedirect(reverse('todo_lists:projects'))
    # else:
    #     form = ProjectForm()
    #     output = {
    #         todo.all().count(),
    #         progress.all().count(),
    #         done.all().count()

    #     }
    context = {'todo_count': todo_count, 'progress_count': progress_count, 'done_count': done_count}

    return render(request, 'todo_lists/progress.html', context)

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-wiki-page-xxxxxxxxxxxxxxxxxx
def wikiMain(request):
    return render(request, 'todo_lists/wiki.html')

def wiki1(request):
    mod = wiki.objects
    ob = mod.get(id=1)
    wiki1 = ob.file
    response = HttpResponse(wiki1)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki1)
    return response

def readwiki1(request):
    mod = wiki.objects
    ob = mod.get(id=1)
    wiki1 = ob.file
    response = HttpResponse(wiki1)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki1)
    return response

def wiki2(request):
    mod = wiki.objects
    ob = mod.get(id=2)
    wiki2 = ob.file
    response = HttpResponse(wiki2)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki2)
    return response

def readwiki2(request):
    mod = wiki.objects
    ob = mod.get(id=2)
    wiki2 = ob.file
    response = HttpResponse(wiki2)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki2)
    return response

def wiki3(request):
    mod = wiki.objects
    ob = mod.get(id=3)
    wiki3 = ob.file
    response = HttpResponse(wiki3)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki3)
    return response

def readwiki3(request):
    mod = wiki.objects
    ob = mod.get(id=3)
    wiki3 = ob.file
    response = HttpResponse(wiki3)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki3)
    return response

def wiki4(request):
    mod = wiki.objects
    ob = mod.get(id=4)
    wiki4 = ob.file
    response = HttpResponse(wiki4)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki4)
    return response

def readwiki4(request):
    mod = wiki.objects
    ob = mod.get(id=4)
    wiki4 = ob.file
    response = HttpResponse(wiki4)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki4)
    return response

def wiki5(request):
    mod = wiki.objects
    ob = mod.get(id=5)
    wiki5 = ob.file
    response = HttpResponse(wiki5)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki5)
    return response

def readwiki5(request):
    mod = wiki.objects
    ob = mod.get(id=5)
    wiki5 = ob.file
    response = HttpResponse(wiki5)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki5)
    return response

def wiki6(request):
    mod = wiki.objects
    ob = mod.get(id=6)
    wiki6 = ob.file
    response = HttpResponse(wiki6)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki6)
    return response

def readwiki6(request):
    mod = wiki.objects
    ob = mod.get(id=6)
    wiki6 = ob.file
    response = HttpResponse(wiki6)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki6)
    return response

def wiki7(request):
    mod = wiki.objects
    ob = mod.get(id=7)
    wiki7 = ob.file
    response = HttpResponse(wiki7)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki7)
    return response

def readwiki7(request):
    mod = wiki.objects
    ob = mod.get(id=7)
    wiki7 = ob.file
    response = HttpResponse(wiki7)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki7)
    return response

def wiki8(request):
    mod = wiki.objects
    ob = mod.get(id=8)
    wiki8 = ob.file
    response = HttpResponse(wiki8)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(wiki8)
    return response

def readwiki8(request):
    mod = wiki.objects
    ob = mod.get(id=8)
    wiki8 = ob.file
    response = HttpResponse(wiki8)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(wiki8)
    return response

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-resources-xxxxxxxxxxxxxxxxxx
def resourcepage(request):
    resource_list = resource.objects.all()
    return render(request, "todo_lists/resource.html", {'resource_list':resource_list} )

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upload(request):
    if request.method == "POST":
        filename = request.FILES.get("myfiles")
        if filename is None:
            messages.error(request, "Please select a file")
            return HttpResponseRedirect(reverse('todo_lists:resourcepage'))
        else:
            newfile = resource.objects.create()
            newfile.resource = filename
            newfile.save()
            return HttpResponseRedirect(reverse('todo_lists:resourcepage'))
    return render(request, "todo_lists/resource.html", locals())

def checkresource(request,id):
    mod = resource.objects
    ob = mod.get(id = id)
    resourceid = ob.resource
    response = HttpResponse(resourceid)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(resourceid)
    return response

def downloadresource(request,id):
    mod = resource.objects
    ob = mod.get(id = id)
    resourceid = ob.resource
    response = HttpResponse(resourceid)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resourceid)
    return response

def resource1(request):
    mod = resource.objects
    ob = mod.get(id=1)
    resource1 = ob.resource
    response = HttpResponse(resource1)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource1)
    return response

def readresource1(request):
    mod = resource.objects
    ob = mod.get(id=1)
    readresource1 = ob.resource
    response = HttpResponse(readresource1)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource1)
    return response

def resource2(request):
    mod = resource.objects
    ob = mod.get(id=2)
    resource2 = ob.resource
    response = HttpResponse(resource2)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource2)
    return response

def readresource2(request):
    mod = resource.objects
    ob = mod.get(id=2)
    readresource2 = ob.resource
    response = HttpResponse(readresource2)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource2)
    return response

def resource3(request):
    mod = resource.objects
    ob = mod.get(id=3)
    resource3 = ob.resource
    response = HttpResponse(resource3)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource3)
    return response

def readresource3(request):
    mod = resource.objects
    ob = mod.get(id=3)
    readresource3 = ob.resource
    response = HttpResponse(readresource3)
    response['Content-Type'] = 'txt'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource3)
    return response

def resource4(request):
    mod = resource.objects
    ob = mod.get(id=4)
    resource4 = ob.resource
    response = HttpResponse(resource4)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(resource4)
    return response

def readresource4(request):
    mod = resource.objects
    ob = mod.get(id=4)
    readresource4 = ob.resource
    response = HttpResponse(readresource4)
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(readresource4)
    return response