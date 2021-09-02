from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import medicalrecords


# Create your views here.

def projectclinic(request):
    return render(request, 'projectclinic.html')


def pd(request):
    if request.method == 'POST':
        name = request.POST['name']
        if 'gender' in request.POST:
            gender = request.POST['gender']
        else:
            gender=False
        if 'martial' in request.POST:
            martial = request.POST['martial']
        else:
            martial=False
        number = request.POST['number']
        dateofbirth = request.POST['dateofbirth']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        if 'disease' in request.POST:
            disease = request.POST['disease']
        else:
            disease=False
        if 'medicine' in request.POST:
            medicine = request.POST['medicine']
        else:
            medicine=False
        if 'allergies' in request.POST:
            allergies = request.POST['allergies']
        else:
            allergies=False
        if 'tobacco' in request.POST:
            tobacco = request.POST['tobacco']
        else:
            tobacco=False
        if 'drugs' in request.POST:
            drugs = request.POST['drugs']
        else:
            drugs=False
        if 'alchohol' in request.POST:
            alchohol = request.POST['alchohol']
        else:
            alchohol=False
        if 'generalhealth' in request.POST:
            generalhealth = request.POST['generalhealth']
        else:
            generalhealth=False

        medical=medicalrecords.objects.create(name=name,gender=gender,martial=martial,number=number,dateofbirth=dateofbirth,address=address,city=city,state=state,pincode=pincode,
        disease=disease,medicine=medicine,allergies=allergies,tobacco=tobacco,drugs=drugs,alchohol=alchohol,generalhealth=generalhealth)
        medical.save()
        return redirect('login')
    else:
        return render(request, 'patientdetails.html')
def patientinfo(request):
    med=medicalrecords.objects.all()
    return render(request, 'patientrecords.html',{'me':med})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('patientinfo')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'DoctorLogin.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('pd')
        else:
             messages.info(request,'Password Not Matching')
             return redirect('register')
        return redirect('/')
    else:
        return render(request,'AdminlogIn.html')