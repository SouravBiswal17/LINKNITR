from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student, Alumni

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_type = request.POST.get("user_type")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if user_type == "student":
            if Student.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                student = Student.objects.create(username=username, password1=password1, password2=password2)
                student.save()
                messages.success(request, "Student registered successfully.")
                return redirect("login")

        elif user_type == "alumni":
            if Alumni.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                alumni = Alumni.objects.create(username=username, password1=password1, password2=password2)
                alumni.save()
                messages.success(request, "Alumni registered successfully.")
                return redirect("login")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        student = Student.objects.filter(username=username, password1=password).first()
        alumni = Alumni.objects.filter(username=username, password1=password).first()

        if student:
            # Manually handle session for student
            request.session['user_id'] = student.id
            request.session['user_type'] = 'student'
            return redirect("student_home",)
        elif alumni:
            # Manually handle session for alumni
            request.session['user_id'] = alumni.id
            request.session['user_type'] = 'alumni'
            return redirect("alumni_home")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

    return render(request, "login.html")

def student_home(request):
    if request.session.get('user_type') == 'student':
        student = Student.objects.get(id=request.session['user_id'])
        # You can pass alumni data here if needed
        students = Student.objects.all()
        alumni = Alumni.objects.all()
        context = {
            'student': student,
            'students': students,
            'alumni': alumni,
        }
        return render(request, 'internship.html', context)
    return redirect('login')

def alumni_home(request):
    if request.session.get('user_type') == 'alumni':
        alumni = Alumni.objects.get(id=request.session['user_id'])
        # You can pass student data here if needed
        alumnis = Alumni.objects.all()
        students = Student.objects.all()
        context = {
            'alumni': alumni,
            'alumnis': alumnis,
            'students': students,
        }
        return render(request, 'internship.html', context)
    return redirect('login')




def user_logout(request):
    # Clear session data
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect("login")

def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Alumni, Notification

def apply_to_alumni(request, alumni_id):
    if request.method == "POST":
        student_id = request.session.get('user_id') 
        student = Student.objects.get(id=student_id)
        alumni = Alumni.objects.get(id=alumni_id)

        # Create a notification
        Notification.objects.create(
            recipient=alumni,
            sender=student,
            message=f"{student.username} has shown interest in connecting with you."
        )

        # Redirect or render a success message
        messages.success(request, "Your request has been sent to the alumni.")
        return redirect("student_home")

    return redirect("student_home")



from django.shortcuts import render
from .models import Alumni

def alumni_notifications(request):
    alumni_id = request.session.get('user_id')  # Assuming the alumni is logged in and user_id is stored in session
    alumni = Alumni.objects.get(id=alumni_id)
    
    notifications = alumni.notifications.filter(is_read=False).order_by('-created_at')

    return render(request, "alumni_notifications.html", {"notifications": notifications})


def mentor_profile(request):
    return render(request,'mentorprofile.html')


def student_profile(request):
    return render(request,'studentprofile.html')

# username :- Link_NITR
# password :- Link_NITR004