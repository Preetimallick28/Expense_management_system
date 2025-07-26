from django.shortcuts import render

# Create your views here.
def login_(request):
    return render(request,'login.html')

def register_(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        email = request.POST['email']
        email = request.POST['email']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
    return render(request,'register.html')


