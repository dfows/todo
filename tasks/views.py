from django.shortcuts import render, redirect
import sendgrid

from tasks.models import *

s = sendgrid.SendGridClient('app22616172@heroku.com','4suhwxvr')
message = sendgrid.Mail()
message.set_from('DEMONSLAYER <app22616172@heroku.com>')
message.add_to('MINION <jk3405@nyu.edu>')
subj = ''
text_content = ''

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
      subj = 'NEW TASK'
      text_content = "You have been assigned a new task."
      message.set_subject(subj)
      message.set_text(text_content)
      s.send(message)
  task_list = Task.objects.order_by('id')
  context = {'task_list':task_list, 'msg':msg}
  return render(request, 'all.html', context)

def alter(request,task_id):
  finished_task = Task.objects.get(id=task_id)
  pts = str(finished_task.point_worth)
  subj = 'Task #'+task_id+' changed!'
  if finished_task.completed:
    finished_task.completed = False
    text_content = "Your task has been marked undone. You have unearned "+pts+" points."
  else:
    finished_task.completed = True
    text_content = "Congrats! You've completed a task and earned "+pts+" points!"
  finished_task.save()
  message.set_subject(subj)
  message.set_text(text_content)
  s.send(message)
  return redirect('index')

