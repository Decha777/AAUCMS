from django.db import models

# Create your models here.

class College(models.Model):
    college_name = models.CharField(max_length=256)

    def __str__(self):
        return self.college_name
    

class Activity(models.Model):
    activity_name = models.CharField(max_length=500)

    def __str__(self):
        return self.activity_name
    


class Person(models.Model):
    username =models.CharField(max_length=256)
    phone = models.IntegerField()

    def __str__(self):
        return self.username
    

                                                    
class Problem(models.Model):
    problem_name = models.TextField()

    def __str__(self):
        return self.problem_name
    
class Decision(models.Model):
    decision_name = models.TextField()

    def __str__(self):
        return self.decision_name
    


class Task(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='college')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='activity')
    responsible_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='problem')
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE, related_name='decision')