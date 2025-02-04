from django.db import models

# Create your models here.
class Employee (models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=10)
    rate = models.FloatField(max_length=300)
    overtime_pay = models.FloatField(default='0', null=True)
    allowance = models.FloatField(default='0', null=True)
    objects = models.Manager()
    ot_hrs = models.FloatField(default='0', null=True)

    
    def getName(self):
        return self.name
    
    def getID (self):
        return self.id_number
    
    def getRate(self):
        return self.rate
    
    def getOvertime(self):
        return self.overtime_pay
    
    def resetOvertime(self):
        self.overtime_pay = 0
        self.ot_hrs = 0
        self.save()

    def getAllowance(self):
        return self.allowance
    
    def __str__ (self):
        return f"{self.pk}:{self.id_number}, rate: {self.rate}"




class Payslip (models.Model):    
    id_number = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)
    date_range = models.CharField(max_length=2)
    year = models.CharField(max_length=4, blank=False)
    pay_cycle = models.IntegerField(default='0')
    rate = models.FloatField(default='0')
    earnings_allowance = models.FloatField(default='0')
    deduction_tax = models.FloatField(default='0')
    deduction_health = models.FloatField(default='0')
    pag_ibig = models.FloatField(default='0')
    sss = models.FloatField(default='0')
    overtime = models.FloatField(default='0')
    total_pay = models.FloatField(default='0')
    gross_pay = models.FloatField(default='0')
    total_deduction = models.FloatField(default='0')

    def getIDNumber(self):
        return str(self.id_number.id_number)
    
    def getMonth(self):
        return self.month
    
    def getDate_range(self):
        return self.date_range
    
    def getYear(self):
        return self.year
    
    def getPay_cycle(self):
        return self.pay_cycle
    
    def getRate(self):
        return self.rate
    
    def getCycleRate(self):
        return (self.getRate()/2)
    
    def getEarnings_allowance(self):
        return self.earnings_allowance
    
    def getDeductions_tax(self):
        return self.deduction_tax
    
    def getDeductions_health(self):
        return self.deduction_health
    
    def getPag_ibig(self):
        return self.pag_ibig
    
    def getSSS(self):
        return self.sss
    
    def getOvertime(self):
        return self.overtime
    
    def getTotal_pay(self):
        return self.total_pay 
    
    def getGross(self):
        return self.gross_pay
    
    def getTotalDeduction(self):
        return self.total_deduction

    
    def __str__ (self):
        return f"pk: {self.pk}, Employee: {self.id_number.getID()}, Period: {self.month} {self.date_range}, {self.year}, Cycle: {self.pay_cycle}, Total Pay: {self.total_pay}"
