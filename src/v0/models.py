from django.db import models

# Create your models here.
class WorkerList(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
			return self.name

class Worker(models.Model):
	name = models.CharField(max_length=32)
	surname = models.CharField(max_length=32)
	pay = models.IntegerField()
	status = models.CharField(max_length=32, default='Active')
	workerlist = models.ForeignKey(WorkerList)

	def __str__(self):
			return self.name+' '+self.surname

class Costs(models.Model):
	name = models.CharField(max_length=32)
	money = models.IntegerField(default=0)

	def __str__(self):
			return self.name

class CostsTicket(models.Model):
	name = models.CharField(max_length=32)
	money = models.IntegerField()
	costs =	models.ForeignKey(Costs)	

	def __str__(self):
			return self.name

class Funds(models.Model):
	name = models.CharField(max_length=32)
	money = models.IntegerField(default=0)
	
	def __str__(self):
    		return  self.name

class FundsTicket(models.Model):
	name = models.CharField(max_length=32)
	money = models.IntegerField()
	funds = models.ForeignKey(Funds)

	def __str__(self):
    		return self.money

