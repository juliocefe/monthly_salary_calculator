from django.urls import path

from monthly_salary_calculator.employees.views import (
    EmployeesView,
)

app_name = "employees"
urlpatterns = [
    path("", EmployeesView.as_view(), name=""),
]