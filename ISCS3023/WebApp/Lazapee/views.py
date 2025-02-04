from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Payslip
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, 'Lazapee/HomeHTML.html')

def create_Employee(request):
    if (request.method == "POST"):
        userName = request.POST.get('un')
        id_nos = request.POST.get('id_no')
        rates= request.POST.get('rate')
        allowances = request.POST.get('allowance')

        if allowances == "":
            allowances = '0'

        if Employee.objects.filter(id_number__contains=id_nos):
            return render(request,'Lazapee/create_EmployeeHTML.html', {"error": "Employee already exists."})
          
        else:
            try:
                Employee.objects.create(name=userName, id_number= id_nos, rate=rates, allowance=allowances)
                Employee_obj = Employee.objects.all()
                return render(request, 'Lazapee/EmployeeHTML.html', {'employee':Employee_obj, "success": "Employee added successfully."})
            except Exception as e:
                return render(request,'Lazapee/create_EmployeeHTML.html', {"error": e})

            
    else:
        return render(request, 'Lazapee/create_EmployeeHTML.html')

def view_Employees(request):
    Employee_obj = Employee.objects.all()
    return render(request, 'Lazapee/EmployeeHTML.html', {'employee':Employee_obj})

def delete_Employee(request, pk):
    Employee.objects.filter(pk=pk).delete()
    return redirect('view_Employees')

def update_Employee(request, pk):
    if(request.method=="POST"): 

        RATE = request.POST.get('rate')
        ALLOWANCE =  request.POST.get('allowance')

        if ALLOWANCE == "":
            allows = get_object_or_404(Employee, pk=pk).getAllowance()
            ALLOWANCE = allows + 0
            
        Employee.objects.filter(pk=pk).update(rate=RATE, allowance=ALLOWANCE)
        return redirect('view_Employees')
    else:
        e = get_object_or_404(Employee, pk=pk)
        return render(request, 'Lazapee/updateEmployeeHTML.html', {'e':e})

def view_Payslips(request):
    employees_obj = Employee.objects.all()
    payslip_obj = Payslip.objects.all().order_by("-pk")

    if (request.method == "POST"):
        id_numb = request.POST.get("person")
        mon = request.POST.get("month")
        yr = request.POST.get("year")
        cyc = request.POST.get("cycle")


        # if missing input, error.
        if id_numb == None or mon == "" or yr == "" or cyc == "":
            message = "Please input all required information."
            return render(request, 'Lazapee/PayslipsHTML.html', {'employees': employees_obj, 'payslips':payslip_obj, 'message': message})

        # if payslip is has been created, error.
        if Payslip.objects.filter(month=mon,year=yr,pay_cycle=cyc):
            message="Payslip already exists."
            return render(request, 'Lazapee/PayslipsHTML.html', {'employees': employees_obj, 'payslips':payslip_obj, 'message': message})
        
        else:
            # all employees
            if id_numb == "All Employees":
                for i in employees_obj:  
                        employee_id = get_object_or_404(Employee, id_number=i.getID())
                        base = (employee_id.rate * 0.5)
                        ot = employee_id.getOvertime()
                        allows = employee_id.getAllowance()
                        philhealth= base * 0.04
                        socsec = base * 0.045
                        pi = 100
                        gross = base*0.5 + ot + allows
                        

                        if cyc == '1':
                            tax = tax_c1(gross, pi)
                            deduct = tax + pi
                            tp = c1(gross, pi) - deduct
                            d_range = "1-15"
                        
                        elif cyc == '2':
                            tax = tax_c2(gross, philhealth, socsec)
                            deduct = tax + philhealth + socsec
                            tp = (c2(gross, philhealth, socsec) - tax)
                            d_range = "16-30" 


                        Payslip.objects.create(id_number=employee_id, month=mon, date_range = d_range, year=yr, pay_cycle=cyc, rate=base, overtime=ot, earnings_allowance=allows, deduction_health=philhealth,pag_ibig=pi, sss=socsec, deduction_tax=tax, total_pay=tp,  gross_pay=gross, total_deduction=deduct)
                        i.resetOvertime()


            # one employee selected
            else:
                employee_id = get_object_or_404(Employee, id=id_numb)
                base = (employee_id.rate*0.5)
                ot = employee_id.getOvertime()
                allows = employee_id.getAllowance()
                philhealth = base * 0.04
                socsec = base * 0.045
                pi = 100
                gross = base*0.5 + ot + allows
                

                if cyc == '1':
                    tax = tax_c1(gross, pi)
                    deduct = tax + pi
                    tp = c1(gross, pi) - deduct
                    d_range = "1-15"
                
                elif cyc == '2':
                    tax = tax_c2(gross, philhealth, socsec)
                    deduct = tax + philhealth + socsec
                    tp = (c2(gross, philhealth, socsec) - tax)
                    d_range = "16-30"  


                Payslip.objects.create(id_number=employee_id, month=mon, date_range = d_range, year=yr, pay_cycle=cyc, rate=base, overtime=ot, earnings_allowance=allows, deduction_health=philhealth,pag_ibig=pi, sss=socsec, deduction_tax=tax, total_pay=tp,  gross_pay=gross, total_deduction=deduct)
                employee_id.resetOvertime()


            return redirect('view_Payslips')  
            

    else:
        return render(request, 'Lazapee/PayslipsHTML.html', {'employees': employees_obj, 'payslips':payslip_obj})
    

def c1(gross, pagibig):
    formula = (gross - pagibig)
    return formula

def tax_c1(gross, pagibig):
    formula = (gross - pagibig) * 0.2
    return formula

def c2(gross, ph, ss):
    formula = (gross - ph - ss)
    return formula

def tax_c2(gross, ph, ss):
    formula = (gross - ph - ss) * 0.2
    return formula



def update_OT(request, pk):
    Employee_obj = Employee.objects.all()
    emp = get_object_or_404(Employee, pk=pk)
    if (request.method == "POST"):
        ot = float(request.POST.get("ot_hrs"))
        ot_hours= ot + emp.ot_hrs
        overtime = emp.getOvertime() + (emp.getRate()/160) * (1.5 * ot)
        Employee.objects.filter(pk=pk).update(overtime_pay=overtime, ot_hrs=ot_hours)
        return redirect('view_Employees')  
            

    else:
        return render(request, 'Lazapee/EmployeeHTML.html', {'employee':Employee_obj})
    
def view_Receipt(request, pk):
    p = Payslip.objects.get(pk=pk)
    e = Employee.objects.get(id_number=p.id_number.getID())

    return render(request, 'Lazapee/Payslips_ReceiptHTML.html', {'p':p, 'e':e})