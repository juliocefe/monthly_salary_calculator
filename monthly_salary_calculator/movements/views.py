from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import MovementForm, MovementFilterForm
from .models import Movement


# Create your views here.
class MoventsView(View):

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
    

def movements_report(request):
    context = {
        "form": MovementFilterForm()
    }
    return render(request, "movements/report.html", context)
    