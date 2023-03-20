from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MovementForm, MovementFilterForm
from .models import Movement
from .selectors import ReportSelector


# Create your views here.
class MoventsView(LoginRequiredMixin, View):

    def get(self, request):
        form = MovementForm()
        context = {
            "form": form,
            "movements": Movement.objects.all()
        }
        return render(request, "movements/index.html", context)
        
    def post(self, request):
        form = MovementForm(request.POST)
        if form.is_valid():
            # Save the new employee to the database
            form.save()
            messages.success(request, 'Movimiento creado con exito!.')
            # Redirect to the employee list page or some other page
        return redirect('movements:')
    

class MovementReport(LoginRequiredMixin, View):
    template = "movements/report.html"
    def get(self, request):
        context = {
            "form": MovementFilterForm()
        }
        return render(request, self.template, context)
        
    def post(self, request):
        form = MovementFilterForm(request.POST)
        if form.is_valid():
            data = ReportSelector(**form.cleaned_data).data
        context = {"form": form, "data": data}
        return render(request, self.template, context)