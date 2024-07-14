from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Course, Student

# Existing views
def reg(request):
    if request.method == "POST":
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        res = student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled</h1>")
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully</h1>")
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "reg.html", {"students": students, "courses": courses})

def course_search(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        s = Student.objects.all()
        student_list = list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        if len(student_list) == 0:
            return HttpResponse("<h1>No Students enrolled</h1>")
        return render(request, "selected_students.html", {"student_list": student_list})
    else:
        courses = Course.objects.all()
        return render(request, "course_search.html", {"courses": courses})

# New view for 'cts/<int:s>/<int:n>'
def cts_view(request, s, n):
    # This is just a sample response, customize as needed
    return HttpResponse(f"Received s={s} and n={n}")
