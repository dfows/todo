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
