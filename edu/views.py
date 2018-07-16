

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from edu.forms import RegistrationForm
from edu.models import Student
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse


# Create your views here.
def index(request):
    name='khyati'
    args={'name':name}

    return render(request,'edu/index.html',args)

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'edu/reg_form.html',args)

class StudentView(generic.ListView):
    context_object_name='student_list'
    template_name='edu/student_details.html'

    def get_queryset(self):
        return Student.objects.all()

class StudentEntry(CreateView):
    model=Student
    fields=['stu_name','stu_email','stu_phone_no','stu_dob']

class StudentUpdate(UpdateView):
    model=Student
    fields=['stu_name','stu_email','stu_phone_no','stu_dob']

class StudentDelete(DeleteView):
    model=Student
    success_url=reverse_lazy('edu:student_details')
