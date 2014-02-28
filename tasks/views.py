from django.shortcuts import render, redirect
import sendgrid

from tasks.models import *

# Create your views here.
def index(request):
  msg = ''
  if request.method == 'POST':
    n = request.POST['task_name']
    b = request.POST['task_branch']
    p = request.POST['task_pts']
    if n == '':
      msg = 'error. must enter text in field'
    else:
      msg = 'success!'
      new_task = Task(name=n,branch=b,point_worth=p)
      new_task.save()
  task_list = Task.objects.order_by('id')
  context = {'task_list':task_list, 'msg':msg}
  return render(request, 'all.html', context)

def alter(request,task_id):
  finished_task = Task.objects.get(id=task_id)
  pts = finished_task.point_worth
  s = sendgrid.Sendgrid('app22616172@heroku.com','4suhwxvr',secure=True)
  subj = 'Task #'+task_id+' changed!'
  text_content = ''
  if finished_task.completed:
    finished_task.completed = False
    text_content = "Your task has been marked undone. You have unearned "+pts+" points."
  else:
    finished_task.completed = True
    text_content = "Congrats! You've completed a task and earned "+pts+" points!"
  finished_task.save()
  message = sendgrid.Message(('app22616172@heroku.com','DEMONSLAYER'),subj,text_content)
  message.add_to('jk3405@nyu.edu','GRATEFUL MINION')
  s.web.send(message)
  return redirect('index')

