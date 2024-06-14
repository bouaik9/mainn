import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from .models import UploadedFile, Person


l = [
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "skills": "Python, Django, JavaScript",
    "experience": "Software Engineer with 5 years of experience in web development",
    "education": "Bachelor's Degree in Computer Science"
  },
  {
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "phone": "+1987654321",
    "skills": "Java, Spring Boot, SQL",
    "experience": "Full-stack Developer with 3 years of experience in enterprise application development",
    "education": "Master's Degree in Software Engineering"
  },
  {
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "phone": "+1122334455",
    "skills": "C++, Python, Flask",
    "experience": "Backend Developer with 4 years of experience in building scalable systems",
    "education": "Bachelor's Degree in Computer Engineering"
  },
  {
    "name": "Bob Wilson",
    "email": "bob.wilson@example.com",
    "phone": "+1555666777",
    "skills": "JavaScript, React, Node.js",
    "experience": "Frontend Developer with 2 years of experience in building interactive user interfaces",
    "education": "Bachelor's Degree in Information Technology"
  },
  {
    "name": "Emily Brown",
    "email": "emily.brown@example.com",
    "phone": "+1888777666",
    "skills": "HTML, CSS, Bootstrap",
    "experience": "UI/UX Designer with 3 years of experience in designing user-centric interfaces",
    "education": "Bachelor's Degree in Graphic Design"
  },
  {
    "name": "Michael Lee",
    "email": "michael.lee@example.com",
    "phone": "+1222333444",
    "skills": "Python, Django, RESTful APIs",
    "experience": "Backend Developer with 6 years of experience in building scalable web applications",
    "education": "Bachelor's Degree in Computer Science"
  },
  {
    "name": "Sophia Garcia",
    "email": "sophia.garcia@example.com",
    "phone": "+1999888777",
    "skills": "Java, Spring, Hibernate",
    "experience": "Software Engineer with 4 years of experience in enterprise application development",
    "education": "Bachelor's Degree in Computer Engineering"
  },
  {
    "name": "Matthew Martinez",
    "email": "matthew.martinez@example.com",
    "phone": "+1333444555",
    "skills": "JavaScript, Angular, TypeScript",
    "experience": "Frontend Developer with 5 years of experience in building responsive web applications",
    "education": "Bachelor's Degree in Web Development"
  },
  {
    "name": "Olivia Taylor",
    "email": "olivia.taylor@example.com",
    "phone": "+1777666555",
    "skills": "Python, Django, Flask",
    "experience": "Full-stack Developer with 4 years of experience in web development",
    "education": "Bachelor's Degree in Computer Science"
  },
  {
    "name": "William Anderson",
    "email": "william.anderson@example.com",
    "phone": "+1888555666",
    "skills": "React, Redux, Node.js",
    "experience": "Frontend Developer with 3 years of experience in building modern web applications",
    "education": "Bachelor's Degree in Computer Engineering"
  }
]


def add(v):
    for item in v:
        p = Person()
        p.name = item['name']
        p.email = item['email']
        p.phone = item['phone']
        p.skills = item['skills']

        p.experience = item['experience']
        p.education = item['education']
        p.save()


def get_skills(request):
    all = Person.objects.all()
    skills = []
    for item in all:
        if item: 
          sk = item.skills.replace(",", " ").split()
          skills.extend(sk)
    
    serialized_data = ({
            'skills': skills,
       
        })


    json_data = json.dumps(serialized_data)

    return JsonResponse(json_data, safe=False)



@csrf_exempt
def upload_file(request):
    if not request.user.is_authenticated:return redirect("login")

    if not request.user.is_admin:
        return render(request, 'not-admin.html')
    if request.method == 'POST':
        files = request.FILES.getlist('files[]')
        if files:
            upload_dir = 'uploads/'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Loop through each file and write it to the server
            for file in files:
                new = UploadedFile(file=file)
                new.save()
            return render(request, 'uploaded-success.html')
        else:
            return HttpResponse('No files uploaded.', status=400)
    return render(request, 'upload.html')





def all_resume(request):
    # Create and save Person objects using the data
    #add(l)
    if request.user.is_authenticated:
        dataa = Person.objects.all()

        if request.user.is_admin:
            
            request.session['is_admin']=1
            request.session['authenticated']=True


            return render(request, 'view.html', {"data":dataa})
        else:
            request.session['is_admin']=0
            request.session['authenticated']=True

            return render(request, 'view.html', {"data":dataa})
    return redirect("login")




def get_one_resume(request, id):
    if request.user.is_authenticated:
      person = Person.objects.filter(id=id).get()
      return render(request, 'result.html', context={"person":person, "id": person.id, "user_is_admin":request.user.is_admin})
    return redirect('login')



def update_api(request, id, variable):

    if request.method=="POST":
        person = Person.objects.get(id=id)
        data = json.loads(request.body.decode('utf-8'))
        new_value = data.get('field')
        setattr(person, variable, new_value)

        person.save()
        return HttpResponse("ok")   
    return HttpResponse("only POST")


def remove_person(request, id):
    person = Person.objects.get(id=id)
    if person:
        person.delete()
    return HttpResponse("deleted")



def chart(request):
    if not request.user.is_authenticated:
        return redirect("login")
    s = UploadedFile.objects.last()
    number = Person.objects.count()

    return render(request, 'chart.html', context={"number":number, "last_upload":s.uploaded_at})