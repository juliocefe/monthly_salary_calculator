# python
from dataclasses import dataclass, field
from decimal import Decimal
# django
from django.db.models import F, Sum
# models
from .models import Movement
from monthly_salary_calculator.employees.models import Employee



SALARY_PER_HOUR = Decimal("30.00")  # in pesos
WORK_HOURS_PER_DAY = 8
WORK_DAYS_PER_WEEK = 6
WORKED_WEEKS = 4
GROCERY_BOUHES_PERCENT = Decimal("0.04")
# BONUSES
DELIVERY_BONUS = Decimal("5.00")
# discounts
ISR = Decimal("0.09")
EXTRA_ISR = Decimal("0.03")


def calculate_employee_hours() -> int:
    return (
        WORK_HOURS_PER_DAY 
        * WORK_DAYS_PER_WEEK 
        * WORKED_WEEKS
    )

@dataclass
class EmplyeePayrollAndBenefitsCalculation:

    name: str
    role: Employee.Role
    employee_id: int 
    total_deliveries: int
    hours: int = field(default_factory=calculate_employee_hours)

    BONUS_PER_HOUR = {
        Employee.Role.DRIVER: Decimal("10.00"),
        Employee.Role.LOADER: Decimal("5.00"),
        Employee.Role.ASSITANT: Decimal("0.00"),
    }
    
    @property
    def base_salary(self) -> Decimal:
        return Decimal(self.hours) * SALARY_PER_HOUR
    
    @property    
    def deliveries_bonuses(self) -> Decimal:
        return Decimal(self.total_deliveries) * DELIVERY_BONUS
    
    @property
    def bonuses_by_role(self) -> Decimal:
        return Decimal(self.hours) * self.BONUS_PER_HOUR[self.role]
    
    @property    
    def isr(self) -> Decimal:
        isr_percent = ISR
        if self.gross_salary > Decimal("10__000.00"):
            isr_percent = ISR + EXTRA_ISR
        return isr_percent * self.gross_salary

    @property
    def grocery_bouhes(self) -> Decimal:
        return self.net_salary * GROCERY_BOUHES_PERCENT
    
    @property
    def bonuses(self):
        return (
            self.bonuses_by_role
            + self.deliveries_bonuses
        )

    @property
    def gross_salary(self):
        return self.base_salary + self.bonuses

    @property
    def net_salary(self):
        return self.gross_salary - self.isr

    def __repr__(self) -> str:
        return (f"""({self.name} {self.base_salary=} {self.deliveries_bonuses=} \
            {self.bonuses_by_role=} {self.grocery_bouhes=} {self.isr=} {self.net_salary=})""")


@dataclass
class ReportSelector:

    year: int
    month: int

    @property
    def data(self):
        queryset = self.get_queryset()
        annotate_values = self.get_annotate_values(queryset)
        hours_total = 0
        base_salary = Decimal("0.00")
        deliveries_total = Decimal("0.00")
        bonuses_total = Decimal("0.00")
        withholdings_total = Decimal("0.00")
        grocery_bouhes = Decimal("0.00")
        for employee in annotate_values:
            payroll = EmplyeePayrollAndBenefitsCalculation(**employee)
            hours_total += payroll.hours
            base_salary += payroll.base_salary
            deliveries_total += payroll.deliveries_bonuses
            bonuses_total += payroll.bonuses
            withholdings_total += payroll.isr
            grocery_bouhes += payroll.grocery_bouhes

        return {
            "hours_total": round(hours_total, 2),
            "deliveries_total": round(deliveries_total, 2),
            "bonuses_total": round(bonuses_total, 2),
            "withholdings_total": round(withholdings_total, 2),
            "grocery_bouhes": round(grocery_bouhes, 2),
            "total": round(base_salary, 2)
        }


    def get_queryset(self):
        queryset =  Movement.objects.filter(
            created_at__year=self.year, 
            created_at__month=self.month
        )
        return queryset
    
    def get_annotate_values(self, queryset: Movement):
        results = queryset.values(
            "employee_id",
            name=F("employee__name"), 
            role=F("employee__role")
        ).annotate(
            total_deliveries=Sum('deliveries')
        ).values(
            "employee_id",
            "name",
            "total_deliveries",
            "role"
        ).order_by("employee_id")
        return results