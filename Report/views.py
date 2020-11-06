from django.shortcuts import render, redirect
from .models import Activity, Problem, Task, Decision, Problem, Person, College, ProjectManager
from django.http import JsonResponse
from django.forms.models import model_to_dict

def create_activity(request):
    if request.method  == 'POST':
        activity = Activity.objects.create(activity_name=request.POST['activity_name'])
        return JsonResponse({'activity':model_to_dict(activity)})


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views import View

class TaskView(View):
    activities_list = Activity.objects.all()
    print(activities_list)
    context = {'activities_list': list(activities_list.values())}
    task_var = None;
    def setDecision(self,decision,activity):
        # decision = Decision.objects.filter(decision_name=decision)
        # if decision.exists():
        #     return decision.values()
        # else:
        decision = Decision.objects.create(decision_name=decision)
        return decision;
    def setProblemEnc(self,problem_encountered,activity):
        # problem = Problem.objects.filter(problem_name = problem_encountered)
        # if problem.exists():
        #     return problem.values()
        # else:
        problem = Problem.objects.create(problem_name = problem_encountered)
        return problem
    def setActivity(self,activity_id):
        activity = Activity.objects.get(pk = activity_id)
        return activity
    def getCollege(self,user):
        pm = ProjectManager.objects.get(project_manager=user)
        college = College.objects.get(project_manager=pm)
        return college
    def getPerson(self,phone,username,activity):
        person = Person.objects.filter(phone=phone,username=username,activity=activity)
        if person.exists():
            return person
        else:
            person = Person.objects.create(phone=phone,username=username,activity=activity)
            return person
    def taskExists(self,activity):
        task = Task.objects.filter(activity=activity)
        self.task_var = task
        print(self.task_var)
        if task.exists():
            return True
        else: return False
    def post(self,request):
        print(request.POST)
        if request.method  == 'POST':
            decision = request.POST['decision_name']
            
            problem_encountered = request.POST['problem_name']
            activity_id = request.POST['activity_id']
            college = self.getCollege(request.user)
            activity = self.setActivity(activity_id)
            username = request.POST['username']

            phone = request.POST['phone']
            if(phone == ''):
                phone = None;   
            
            person = self.getPerson(phone,username,activity)
            
            
            # if(self.taskExists(activity)):
            #     task = self.task_var.update(decision = self.setDecision(decision,activity), problem = self.setProblemEnc(problem_encountered,activity),activity= activity,responsible_person=person,college=college)
            #     task.save()
            # else:
            task = Task.objects.create(decision = self.setDecision(decision,activity), problem = self.setProblemEnc(problem_encountered,activity),activity= self.setActivity(activity_id),responsible_person=person,college=college)
            task.save()
            return JsonResponse({'task':model_to_dict(task)})
        # return render(request, '../templates/index.html', self.context)
    
    def get(self,request):
        return render(request, '../templates/index.html', self.context)

def get_decision_name(request):
    if request.method  == 'POST':
        decision_id = request.POST.get('decision',None)
        decision = Decision.objects.get(pk = decision_id)
        return JsonResponse({'decision':model_to_dict(decision)})

def get_problem_name(request):
    if request.method  == 'POST':
        problem_id = request.POST.get('problem',None)
        problem = Problem.objects.get(pk = problem_id)
        return JsonResponse({'problem':model_to_dict(problem)})

def get_responsible_person(request):
    if request.method  == 'POST':
        person_id = request.POST.get('person',None)
        person = Person.objects.get(pk = person_id)
        return JsonResponse({'person':model_to_dict(person)})

def get_activities_task(request):
    if request.method  == 'POST':
        print(request.user)
        pm = ProjectManager.objects.get(project_manager=request.user)
        college = College.objects.get(project_manager=pm)
        tasks = Task.objects.filter(college= college)
        return JsonResponse({'tasks':list(tasks.values())})
    

# @login_required
def report(request):
    return render(request, '../templates/report.html')






