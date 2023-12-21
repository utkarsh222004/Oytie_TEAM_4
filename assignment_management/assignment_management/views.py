from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import Teacher
from service.models import Assignment
from service.models import Batch
from service.models import Student
from service.models import Solution
 
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

    elif request.GET.get('myIdentity')=="teacher":
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
    else:
        return render(request,"login.html")
        
 
def assignment_creation(request):
    data={"teacher_id":request.session['teacher_id']}
    batchdata=[]
    batch=Batch.objects.all()
    print(batch)
    for x in batch:
        batchdata.append(x.batch_name)

    data['batch']=batchdata
    print(data)
    return render(request,'assignment_creation.html',data)
       

def add_assignment(request):
    name=request.GET.get("name")
    batchdata=Batch.objects.filter(batch_name=request.GET.get("batch"))
    for x in batchdata:
        batch_id=x.id
    teacherdata=Teacher.objects.filter(id=request.session['teacher_id'])
    for x in teacherdata:
        teacher_id=x.id
    deadline=request.GET.get("deadline")
    questions=request.GET.get("questions")
    
    res=Assignment(name=name,batch_id=batch_id,teacher_id_id=teacher_id,questions=questions,deadline=deadline)
    res.save()
    url='/teacherpage/'
    return redirect(url)
       
    

def assignment_response(request,id):
    return render(request,'login.html')

def logout(request):
    del request.session['teacher_id']
    return render(request,'login.html')

