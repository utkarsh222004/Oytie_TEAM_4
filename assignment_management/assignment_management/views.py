from django.http import HttpResponse
from django.shortcuts import render
from service.models import Teacher
from service.models import Assignment
from service.models import Batch
 
def home(request):
    return HttpResponse("Hello World!!")

def login(request):
    return render(request,"login.html")

def teacherpage(request):
    if request.session['teacher_id']:
            userdata=Teacher.objects.filter(id=request.session['teacher_id'])
            for data in userdata:
                teacher_name=data.name
            main_list=[]
            assignset=Assignment.objects.filter(teacher_id=request.session['teacher_id'])
            for a in assignset:
                batch=Batch.objects.filter(id=a.batch.id)
                for b in batch:
                    batch_name=b.batch_name
                list=[a.id,a.name,a.deadline,batch_name]
                main_list.append(list)

                   
            data={"teacher_name":teacher_name}
            data['assignment']=main_list
            print(data)
            return render(request,"teacherpage.html",data)

    if request.GET.get('myIdentity')=="teacher":
        userdata=Teacher.objects.filter(username=request.GET['username'] ,password=request.GET['password'])
        if(userdata):
            for data in userdata:
                teacher_id=data.id
                teacher_name=data.username
            request.session['teacher_id']=teacher_id
            main_list=[]
            assignset=Assignment.objects.filter(teacher_id=request.session['teacher_id'])
            for a in assignset:
                batch=Batch.objects.filter(id=a.batch.id)
                for b in batch:
                    batch_name=b.batch_name
                list=[a.id,a.name,a.deadline,batch_name]
                main_list.append(list)

                   
            data={"teacher_name":teacher_name}
            data['assignment']=main_list
            print(data)
            return render(request,"teacherpage.html",data)
        
def logout(request):
    del request.session['teacher_id']
    return render(request,'login.html')