from django.shortcuts import render, redirect
import sendgrid

from tasks.models import *

s = sendgrid.SendGridClient('app22616172@heroku.com','4suhwxvr')
message = sendgrid.Mail()
message.set_from('DEMONSLAYER <app22616172@heroku.com>')
message.add_to('MINION <jk3405@nyu.edu>')
subj = ''
text_content = ''

msg = ''
logged_in_as = ''
logged_in = False

# Create your views here.
def index(request):
  if request.method == 'POST' and 'task_name' in request.POST:
    n = request.POST['task_name']
    b = request.POST['task_branch']
    p = request.POST['task_pts']
    if n == '':
      changeMsg('error. must enter text in field')
    else:
      changeMsg('success!')
      new_task = Task(name=n,branch=b,point_worth=p)
      new_task.save()
      subj = 'NEW TASK'
      text_content = "You have been assigned a new task: "+n
      message.set_subject(subj)
      message.set_text(text_content)
      s.send(message)
  task_list = Task.objects.order_by('id')
  context = {'user':logged_in_as,'task_list':task_list, 'msg':msg}
  return render(request, 'all.html', context)

def login(request):
  #if login is successful, change login
  global logged_in
  global logged_in_as
  if request.method == 'POST':
    n = request.POST['login_name']
    if n != '': 
      if len(User.objects.filter(name=n)) > 0:
        logged_in_as = User.objects.get(name=n)
        logged_in = True
        changeMsg("login successful")
      else:
        changeMsg("bad login")
  return redirect('index')

def alter(request,task_id):
  if logged_in:
    finished_task = Task.objects.get(id=task_id)
    pts = str(finished_task.point_worth)
    subj = 'Task #'+task_id+' changed!'
    if finished_task.completed:
      finished_task.completed = False
      logged_in_as.point_total -= finished_task.point_worth
      string = "Your task has been marked undone. You have unearned "+pts+" points."
    else:
      finished_task.completed = True
      logged_in_as.point_total += finished_task.point_worth
      string = "Congrats! You've completed a task and earned "+pts+" points!"
    finished_task.save()
    logged_in_as.save()
    changeMsg(string)
  else:
    changeMsg("You may not check off things!")
  return redirect('index')

def changeMsg(string):
  global msg
  msg = string
  return
