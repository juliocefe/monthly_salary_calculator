from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
class EmployeesView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            "form": EmployeeForm(),
            "employees": Employee.objects.all()
        }
        return render(request, "employees/index.html", context)
        
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Save the new employee to the database
            form.save()
            messages.success(request, 'Empleado creado con exito!.')
            # Redirect to the employee list page or some other page
        return redirect('employees:')