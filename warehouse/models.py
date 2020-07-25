from django.db import models

class Category(models.Model):
	category=models.CharField(max_length=50)

	def __str__(self):
		return self.category		

class Item(models.Model):
	approval = models.BooleanField(default=True)
	item_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	start_date = models.DateField()
	exp_date = models.DateField()

	
	def __str__(self):
		return self.name


class Staff(models.Model):
	staff_id = models.CharField(max_length=255)
	staff_name = models.CharField(max_length=255)
	staff_phone = models.CharField(max_length=255)
	staff_join = models.TimeField()
	staff_out = models.TimeField()

	def __str__(self):
		return self.staff_name


class Branch(models.Model):
	place=models.CharField(max_length=50)
	description=models.CharField(max_length=100)
	address = models.CharField(max_length=255, default='yangon, myanmar')
	
	def __str__(self):
		return self.place

	
class Transaction(models.Model):
	trans_id=models.AutoField(primary_key=True)	
	quantity=models.IntegerField()
	time=models.DateTimeField(auto_now=True)
	item=models.ForeignKey(Item,on_delete=models.CASCADE,blank=False,null=False)
	client=models.ForeignKey(Branch,on_delete=models.CASCADE,blank=False,null=False)
	
	def __str__(self):
		return ("%s , %s , %s" % (self.item.name,self.client.place,self.time))
