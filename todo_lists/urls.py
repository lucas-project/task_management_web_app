# sub urls for todo_list


from django.urls import path

from . import views

app_name = 'todo_lists'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # page that shows all projects
    path('projects/', views.projects, name='projects'),
    # details of a project
    path('projects/<int:project_id>/', views.project, name='project'),
    # add a new project
    path('new_project/', views.new_project, name='new_project'),

    # for creating new todo tasks by user
    path('new_todo/<int:project_id>/', views.new_todo, name='new_todo'),
    # for creating new todo tasks by user
    path('new_progress/<int:project_id>/', views.new_progress, name='new_progress'),
    # for creating new todo tasks by user
    path('new_done/<int:project_id>/', views.new_done, name='new_done'),
    
    # for editing current todo tasks
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    # for editing current in-progress tasks
    path('edit_progress/<int:progress_id>/', views.edit_progress, name='edit_progress'),
    path('progress/', views.visualisation, name='visualisation'),
    path('delete/<str:todo_id>/', views.delete_todo, name='delete_todo'),
    path('delete_project/<str:project_id>/', views.delete_project, name='delete_project'),
    path('edit_project/<str:project_id>/', views.edit_project, name='edit_project'),

    path('wiki', views.wikiMain, name='wikiMain'),
    path('wiki1', views.wiki1, name='manager_wiki1'),
    path('readwiki1', views.readwiki1, name='manager_readwiki1'),
    path('wiki2', views.wiki2, name='manager_wiki2'),
    path('readwiki2', views.readwiki2, name='manager_readwiki2'),
    path('wiki3', views.wiki3, name='manager_wiki3'),
    path('readwiki3', views.readwiki3, name='manager_readwiki3'),
    path('wiki4', views.wiki4, name='manager_wiki4'),
    path('readwiki4', views.readwiki4, name='manager_readwiki4'),
    path('wiki5', views.wiki5, name='manager_wiki5'),
    path('readwiki5', views.readwiki5, name='manager_readwiki5'),
    path('wiki6', views.wiki6, name='manager_wiki6'),
    path('readwiki6', views.readwiki6, name='manager_readwiki6'),
    path('wiki7', views.wiki7, name='manager_wiki7'),
    path('readwiki7', views.readwiki7, name='manager_readwiki7'),
    path('wiki8', views.wiki8, name='manager_wiki8'),
    path('readwiki8', views.readwiki8, name='manager_readwiki8'),



    path('resourcepage', views.resourcepage, name='resourcepage'),
    path('resource1', views.resource1, name='project_resource1'),
    path('readresource1', views.readresource1, name='project_readresource1'),
    path('resource2', views.resource2, name='project_resource2'),
    path('readresource2', views.readresource2, name='project_readresource2'),
    path('resource3', views.resource3, name='project_resource3'),
    path('readresource3', views.readresource3, name='project_readresource3'),
    path('resource4', views.resource4, name='project_resource4'),
    path('readresource4', views.readresource4, name='project_readresource4'),
    path('upload', views.upload, name='upload'),
    path('checkresource<id>', views.checkresource, name='project_checkresource'),
    path('downloadresource<id>', views.downloadresource, name='project_downloadresource'),
]
