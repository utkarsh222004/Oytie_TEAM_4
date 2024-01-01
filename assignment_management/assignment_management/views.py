from django.http import HttpResponse
from django.shortcuts import render,redirect
from service.models import Teacher
from service.models import Assignment
from service.models import Batch
from service.models import Student
from service.models import Solution
import datetime 
 
def home(request):
    return HttpResponse("Hello World!!")

def login(request):
    return render(request,"login.html")

def loginmap(request):
    if 'teacher_id' in request.session:
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
    if 'student_id' in request.session:
        userdata=Student.objects.filter(id=request.session['student_id'])
        if(userdata):
            for data in userdata:
                student_id=data.id
                student_name=data.username
                student_batch=data.batch
           
            batch=Batch.objects.filter(id=student_batch.id)
            for b in batch:
                batch_name=b.batch_name
                
            main_list=[]
            assignset=Assignment.objects.filter(batch_id=student_batch)
            for a in assignset:
                solution=Solution.objects.filter(stud_id=request.session['student_id'],assign_id=a.id)
                if solution:
                 for s in solution:
                    sol=s.solution
                    comment=s.comment
                    points=s.points
                else:
                    sol='-'
                    comment='-'
                    points='-'
                   
                list=[a.id,a.name,a.deadline,sol,comment,points]
                main_list.append(list)

                   
            data={"student_name":student_name}
            data.update({"student_batch":batch_name})
            
            data['assignment']=main_list
            
            return render(request,"studentpage.html",data)
          

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

    elif request.GET.get('myIdentity')=="student":
        
        userdata=Student.objects.filter(username=request.GET['username'] ,password=request.GET['password'])
        if(userdata):
            for data in userdata:
                student_id=data.id
                student_name=data.username
                student_batch=data.batch
            request.session['student_id']=student_id
            batch=Batch.objects.filter(id=student_batch.id)
            for b in batch:
                batch_name=b.batch_name
                
            main_list=[]
            assignset=Assignment.objects.filter(batch_id=student_batch)
            for a in assignset:
                solution=Solution.objects.filter(stud_id=request.session['student_id'],assign_id=a.id)
                if solution:
                 for s in solution:
                    sol=s.solution
                    comment=s.comment
                    points=s.points
                else:
                    sol='-'
                    comment='-'
                    points='-'
                   
                list=[a.id,a.name,a.deadline,sol,comment,points]
                main_list.append(list)

                   
            data={"student_name":student_name}
            data.update({"student_batch":batch_name})
            
            data['assignment']=main_list
            
            return render(request,"studentpage.html",data)
          
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

def edit_assign(request,id):
    assignset=Assignment.objects.filter(id=id)
    for assign in assignset:
        assign_name=assign.name
        assign_que=assign.questions
        assign_deadline=assign.deadline
    data={"id":id,"name":assign_name,"que":assign_que,"deadline":assign_deadline}
    return render(request,'edit_assign.html',data)

def submit_solution(request):
    sol=request.GET.get('solution')
    assign_id=request.GET.get('assign_id')
    stud_id=request.session['student_id']
    date=datetime.date.today()
    res=Solution(stud_id_id=stud_id,assign_id_id=assign_id,solution=sol,submission_date=date,points='not checked yet',comment='not checked yet')
    res.save()
    url='/studentpage/'
    return redirect(url)

def logout(request):
    if 'teacher_id' in request.session:
        del request.session['teacher_id']
    elif 'student_id' in request.session:
        del request.session['student_id']
    return render(request,'login.html')

