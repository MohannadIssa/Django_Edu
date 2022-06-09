from django.db import models
from django.db import models




class Project(models.Model):
    pnumber=models.IntegerField(primary_key=True);
    name = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255,blank=True, null=True)
    tools = models.CharField(max_length=255,blank=True, null=True)
    link = models.CharField(max_length=255,blank=True, null=True)
    notes = models.CharField(max_length=255,blank=True, null=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        
       


class Student(models.Model):
    number = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255,blank=True, null=True)
    lname = models.CharField(max_length=255,blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    notes = models.CharField(max_length=255,blank=True, null=True)
    project = models.ForeignKey('Project',
             on_delete=models.PROTECT,
             blank=True,related_name="students")

    def __str__(self) :
            return self.fname+" "+self.lname
 

    class Meta:
         ordering = ['number']

