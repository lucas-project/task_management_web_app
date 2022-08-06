from django.db import models
import datetime

class Project(models.Model):
    
    name = models.CharField(max_length=20) 
    create_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    project_code = models.CharField(max_length=20)
    details = models.TextField()
    team = models.CharField(max_length=200)

    def __str__(self):
        return self.details


class Todo(models.Model):
    # todo_list's content
    text = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    # resources = models.FileField(upload_to='uploads/%d/%m/%Y/')
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.text[:60] + "..."


class Progress(models.Model):  
    text = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    name = models.ForeignKey(Todo, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True) 
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.text


class Done(models.Model):
    text = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.ForeignKey(Todo, on_delete=models.CASCADE)
    # name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField(default=datetime.datetime.now)
    
    project_code = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return self.text


class Team(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class wiki(models.Model):
    file = models.FileField(upload_to='wikis')

class resource(models.Model):
    resource = models.FileField(upload_to='resources')

from django.contrib import admin
admin.site.register(Todo)
admin.site.register(Progress)
admin.site.register(Done)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(wiki)
admin.site.register(resource)