from django.db import models

# Create your models here.
class Task(models.Model):
  # tasks
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length="25")
  branch = models.CharField(max_length="25")
  assigned_date = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(default=False)
  point_worth = models.IntegerField(blank=False)
  def __unicode__(self):
    return self.name.__str__()

class User(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length="25")
  point_total = models.IntegerField(default=0)
  level = models.IntegerField(default=0)
  def __unicode__(self):
    return self.name.__str__()+" "+self.point_total.__str__()+" level: "+self.level.__str__()
