from django import forms

from .models import Project, Todo, Progress, Done


# user can type in project now
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['team', 'name', 'due_date', 'project_code', 'details']
        widgets = {
                    'start_date': forms.SelectDateWidget(),
                    'due_date': forms.SelectDateWidget(),
        }


# user can type in to do tasks now
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['project', 'text', 'name', 'start_date', 'due_date', 
                  'project_code', 'details']
        # labels = {'project': '', 'create_date': ''}
        widgets = {
                    # 'project': forms.Textarea(attrs={'col': 100}), 
                    'start_date': forms.SelectDateWidget(),
                    'due_date': forms.SelectDateWidget(),
                    # 'resources': forms.FileInput()
                }

# class TodoForm(forms.ModelForm):
    
#     text = forms.CharField()
#     # project = forms.ForeignKey()
#     name = forms.CharField()
#     create_date = forms.DateTimeField()
#     start_date = forms.DateTimeField()
#     due_date = forms.DateTimeField()
    
#     project_code = forms.CharField()
#     details = forms.TextInput()
#     class Meta:
#          model = Todo
#          fields = ['project', 'create_date']


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['project', 'text', 'name', 'start_date', 'due_date', 
                  'project_code', 'details']
        # labels = {'project': ''}
        # widgets = {'project': forms.Textarea(attrs={'col': 100})}


class DoneForm(forms.ModelForm):
    class Meta:
        model = Done
        fields = ['project', 'text', 'name', 'start_date', 'due_date', 
                  'project_code', 'details']
        # labels = {'project': ''}
        # widgets = {'project': forms.Textarea(attrs={'col': 100})}


class ResourceForm(forms.Form):
    resource = forms.FileField(label='resource', required=True, error_messages={'required':'Please select a file'})
