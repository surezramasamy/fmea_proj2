from django.db import models
from django.utils import timezone

class Part_name(models.Model):
    part_name=models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
       return self.part_name

class Process_or_Function(models.Model):
    Process_or_function_name=models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return str(self.Process_or_function_name)



class Fmea_Record(models.Model):
    date = models.DateField(default=timezone.now())
    Part_Name=models.ManyToManyField(Part_name,blank=True,null=True)
    Process_OR_Function = models.ForeignKey(Process_or_Function,on_delete=models.CASCADE,blank=True,null=True)
    Potential_Failure_Mode = models.CharField(max_length=256)
    Potential_Effects_of_Failure=models.CharField(max_length=256)
    Sev=models.IntegerField()
    Class=models.CharField(max_length=10,blank=True,null=True)
    Potential_causes_or_Mechanisms_of_Failure=models.CharField(max_length=256,)
    Occ=models.IntegerField()
    Current_Process_Control_Prevention=models.CharField(max_length=256,)
    Current_Process_Control_Detection=models.CharField(max_length=256,)
    Det=models.IntegerField()
    RPN=models.IntegerField()
    Recommended_Actions=models.CharField(max_length=256,blank=True,null=True)
    Resp_Target_Date=models.CharField(max_length=256,blank=True,null=True)
    Actions_Taken=models.CharField(max_length=256,blank=True,null=True)
    Sev_Rev=models.IntegerField(blank=True,null=True)
    Occ_Rev=models.IntegerField(blank=True,null=True)
    Det_Rev=models.IntegerField(blank=True,null=True)
    RPN_Rev=models.IntegerField(blank=True,null=True)
    Rev_No=models.IntegerField(blank=True,null=True)
    Rev_Date=models.CharField(max_length=256,blank=True,null=True)
    Rev_History=models.CharField(max_length=256,blank=True,null=True)

    def All_parts(self):
        return "\n".join([p.part_name for p in self.Part_Name.all()])



# Create your models here.
