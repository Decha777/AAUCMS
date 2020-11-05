from django.shortcuts import render, redirect
from .models import Activity, Problem, Task, Decision, Problem, Person, College


def create_activity(request):
    if request.method  == 'POST':
        Activity.objects.create(activity_name=request.POST['activity_name'])
    return redirect('/tasks')


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


from django.views import View





class TaskView(View):
    activities_list = Activity.objects.all()
    context = {'activities_list': activities_list}
    def setDecision(self,decision):
        decision = Decision.objects.create(decision_name=decision)
        return decision;
    def setProblemEnc(self,problem_encountered):
        problem = Problem.objects.create(problem_name = problem_encountered)
        return problem
    def setActivity(self,activity_id):
        activity = Activity.objects.get(pk = activity_id)
        return activity
    def post(self,request):
        if request.method  == 'POST':
            decision = request.POST['decision_name']
            
            problem_encountered = request.POST['problem_name']
            
            username = request.POST['username']

            phone = request.POST['phone']
            person = Person.objects.create(phone=phone,username=username)
            activity_id = request.POST['activity_id']
            
            college = College.objects.create(college_name = 'College')
            task = Task.objects.create(decision = self.setDecision(decision), problem = self.setProblemEnc(problem_encountered),activity= self.setActivity(activity_id),responsible_person=person,college=college)
            task.save()
        return render(request, '../templates/index.html', self.context)
    def get(self,request):
        return render(request, '../templates/index.html', self.context)


# @login_required
def report(request):
    return render(request, '../templates/report.html')






