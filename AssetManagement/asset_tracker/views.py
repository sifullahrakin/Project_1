from django.shortcuts import render, redirect
from .models import Company, Employee, Device
from django.utils import timezone

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'add_company.html', {'companies': companies})

def company_detail(request, company_id):
    company = Company.objects.get(pk=company_id)
    employees = Employee.objects.filter(company=company)
    return render(request, 'company_detail.html', {'company': company, 'employees': employees})

def add_company(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = Company.objects.create(name=name)
        return redirect('company_list')
    return render(request, 'add_company.html')

# Define similar views for Employee and Device
def employee_list(request, company_id):
    company = Company.objects.get(pk=company_id)
    employees = Employee.objects.filter(company=company)
    return render(request, 'employee_list.html', {'company': company, 'employees': employees})

def add_employee(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        name = request.POST['name']
        employee = Employee.objects.create(company=company, name=name)
        return redirect('employee_list', company_id=company.id)
    return render(request, 'add_employee.html', {'company': company})

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})

def add_device(request):
    if request.method == 'POST':
        name = request.POST['name']
        condition = request.POST['condition']
        device = Device.objects.create(name=name, condition=condition)
        return redirect('device_list')
    return render(request, 'add_device.html')

def device_detail(request, device_id):
    device = Device.objects.get(pk=device_id)
    return render(request, 'device_detail.html', {'device': device})


def checkout_device(request, device_id):
    device = Device.objects.get(pk=device_id)
    if request.method == 'POST':
        employee_id = request.POST['employee']
        employee = Employee.objects.get(pk=employee_id)

        device.checked_out = timezone.now()
        device.employee = employee
        device.save()

        # Create a log entry for checkout
        device.log_set.create(action='Checked Out', timestamp=timezone.now(),
                              description=f"Device checked out to {employee.name}")

        return redirect('device_detail', device_id=device.id)

    employees = Employee.objects.filter(company=device.employee.company)
    return render(request, 'checkout_device.html', {'device': device, 'employees': employees})


def return_device(request, device_id):
    device = Device.objects.get(pk=device_id)
    if request.method == 'POST':
        device.checked_in = timezone.now()
        device.save()

        # Create a log entry for return
        device.log_set.create(action='Returned', timestamp=timezone.now(), description="Device returned")

        return redirect('device_detail', device_id=device.id)
    return render(request, 'return_device.html', {'device': device})