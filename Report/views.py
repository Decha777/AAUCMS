from django.shortcuts import render, redirect
from .models import Activity, Problem, Task, Decision, Problem, Person, College, ProjectManager
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator

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
    
    task_var = None;
    def setDecision(self,decision_name,activity):
        decision = Decision.objects.filter(decision_name=decision_name)
        if decision.exists():
            return decision.first()
        decision = Decision.objects.create(decision_name=decision_name)
        return decision
    def setProblemEnc(self,problem_encountered,activity):
        problem = Problem.objects.filter(problem_name = problem_encountered)
        if problem.exists():
            return problem.first()
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
        person = Person.objects.filter(phone=phone,username=username)
        if person.exists():
            return person.first()
        person = Person.objects.create(phone=phone,username=username)
        return person
    def taskExists(self,activity):
        task = Task.objects.filter(activity=activity)
        self.task_var = task
        
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
            
            
            if(self.taskExists(activity)):
                task = self.task_var.update(decision = self.setDecision(decision,activity), problem = self.setProblemEnc(problem_encountered,activity),activity= activity,responsible_person=person,college=college)
            else:
                task = Task.objects.create(decision = self.setDecision(decision,activity), problem = self.setProblemEnc(problem_encountered,activity),activity= self.setActivity(activity_id),responsible_person=person,college=college)
                task.save()
            return JsonResponse({'message':'success'})
        # return render(request, '../templates/index.html', self.context)
    
    def get(self,request):
        if( not request.user.is_authenticated):
            return redirect('accounts/login/')
        activities_list = Activity.objects.all()
        paginator = Paginator(activities_list, 4) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'activities_list': page_obj}
        return render(request, '../templates/index.html', context)

def get_decision_name(request):
    if request.method  == 'POST':
        decision_id = request.POST.get('decision',None)
        decision = Decision.objects.get(pk = decision_id)
        return JsonResponse({'decision':model_to_dict(decision)})

def get_usernames(request):
    if request.method  == 'POST':
        username = request.POST.get('username',None)
        # activity_id = request.POST.get('activity_id',None)
        print(username)
        person = Person.objects.filter(username__contains=username)
        return JsonResponse({'persons':list(person.values())})

def get_phones(request):
    if request.method  == 'POST':
        phone = request.POST.get('phone',None)        
        person = Person.objects.filter(phone__contains=phone)
        return JsonResponse({'persons':list(person.values())})

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
    
    
    
    college_id = request.POST.get('college')
    print(college_id)
    if (college_id == 'All'):
        return redirect('/')
    elif college_id == None:
        tasks_list = Task.objects.all()
    else:
        tasks_list = Task.objects.filter(college_id = college_id)
        
    colleges = College.objects.all()

    paginator = Paginator(tasks_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/report.html' ,{'colleges':colleges,'tasks_list': page_obj})

def college_report(request,id):
    colleges = College.objects.all()
    if (id == 0):
        return redirect('/')
    elif id == None:
        return redirect('/')
    else:
        tasks_list = Task.objects.filter(college_id = id)
    college = College.objects.get(pk = id)
    paginator = Paginator(tasks_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/college_report.html', {'colleges':colleges,'tasks_list': page_obj,'college_name':college.college_name})
    
    
def activity_report(request):
    activities_list = Activity.objects.all()
    tasks_all = []
    for activity in activities_list:
        tasks = Task.objects.filter(activity = activity)
        tasks_all.append(tasks)
    print(tasks_all)
    paginator = Paginator(tasks_all, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, '../templates/activity_report.html', {'tasks_all': page_obj})


