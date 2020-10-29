from django.shortcuts import render, redirect
from .models import Activity, Problem, Task, Decision, Problem, Person, College


def create_activity(request):
    if request.method  == 'POST':
        Activity.objects.create(activity_name=request.POST['activity_name'])
    return redirect('/tasks')

# Create your views here.
def list_activities(request):
    activities_list = Activity.objects.all()
    context = {'activities_list': activities_list}
    if request.method  == 'POST':
        decision = request.POST['decision_name']
        decision = Decision.objects.create(decision_name=decision)
        problem_encountered = request.POST['problem_name']
        problem = Problem.objects.create(problem_name = problem_encountered)
        username = request.POST['username']

        phone = request.POST['phone']
        person = Person.objects.create(phone=phone,username=username)
        activity_id = request.POST['activity_id']
        activity = Activity.objects.get(pk = activity_id)
        college = College.objects.create(college_name = 'College')
        task = Task.objects.create(decision = decision, problem = problem,activity=activity,responsible_person=person,college=college)
        task.save()
    return render(request, '../templates/index.html', context)
