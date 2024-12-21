from django.http import HttpResponse

from .models import *
from django.shortcuts import render, redirect
from .forms import AchievementForm
from django.contrib.auth import login,logout,authenticate
from  django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetails.objects.create(user = user, empcode = ec)
            EmployeeExperience.objects.create(user=user)
            EmployeeEduction.objects.create(user=user)

            error = "no"
        except:
            error ="yes"
    return render(request,'registration.html',locals())


def emp_login(request):
    error = ""
    if request.method =="POST":
        u = request.POST['email']
        p = request.POST['pwd']
        user  = authenticate(username= u, password = p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    employee = EmployeeDetails.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['dept']
        des = request.POST['des']
        interest = request.POST['interest']
        skill = request.POST['skill']
        econt = request.POST['contact']
        dt = request.POST['jdate']
        gender = request.POST['gender']
        profile = request.FILES['profile']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        employee.empdept = dept
        employee.designation = des
        employee.interest = interest
        employee.skill = skill
        employee.contact = econt
        employee.gender = gender
        employee.profile = profile

        if dt:
            employee.jioningdate = dt
        try:
            employee.save()
            employee.user.save()
        except:
            error = "yes"
    return render(request, 'profile.html', locals())


def achievement(request):
    if request.method == "POST":
        guest = request.POST.get("guest")
        project = request.POST.get("project")
        upload = request.FILES.getlist("upload")
        for u in upload:
            EmpAchievement(guest_lec=guest, project_name=project, upload=u).save()
            messages.success(request,"Your Paper Added successfully!!!")
        return render(request,'emp_home.html')

    return render(request,'achievement.html',locals())





def Paper_publication(request):
    if request.method == "POST":
        option = request.POST.get("paper")
        upload = request.FILES.getlist("upload")
        for u in upload:
            Emp_Paper(option=option,upload=u).save()
            messages.success(request,"Your Paper Added successfully!!!")
        return render(request,'emp_home.html')

    return render(request,'Paper_publication.html',locals())

def journals(request):
    if request.method == "POST":
        option = request.POST.get("paper")
        upload = request.FILES.getlist("upload")
        for u in upload:
            Emp_Journals(option=option,upload=u).save()
            messages.success(request,"Your Journals Added successfully!!!")
        return render(request,'emp_home.html')
    return render(request, 'journals.html', locals())




def Logout(request):
    logout(request)
    return redirect('index')

def my_exp(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user = user)
    return render(request, 'my_exp.html', locals())


def edit_exp(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user = user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig = request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2desig = request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration


        try:
            experience.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_exp.html', locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    education = EmployeeEduction.objects.get(user = user)
    return render(request,'my_education.html', locals())

def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    education = EmployeeEduction.objects.get(user = user)

    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagegra = request.POST['percentagegra']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc= request.POST['percentagessc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra= schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc




        try:
            education.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_education.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'change_password.html',locals())

def achievement(request):
    return render(request,'achievement.html')


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error="yes"
    return render(request,'admin_login.html',locals())



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'admin_change_password.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetails.objects.all()
    return render(request,'all_employee.html',locals())





