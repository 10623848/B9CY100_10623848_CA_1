class Employee :

    #name = ''
    #weeklyhours = 0
    #rate = 0
    #overtimeRate = 0
    #weeklytaxcredit = 0
    
    def __init__(self, name, weeklyhours, rate, overtimeRate, weeklytaxcredit) :
    
        self.name = name
        self.weeklyhours = weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit
        
    def computeWeeklyPay (self,hours) :
        overtimeHours = 0
        weeklyToPayHours = 0
        
        if hours > self.weeklyhours :
            overtimeHours = hours - self.weeklyhours
            weeklyToPayHours = self.weeklyhours
        else : weeklyToPayHours = hours
        
        weeklyPay = weeklyToPayHours * self.rate
        overTimePay = self.overtimeRate * overtimeHours
        
        return weeklyPay + overTimePay
    
    
    def computeTax(self,grossPay) :
    
        return abs(0.4*grossPay - self.weeklytaxcredit)
        
        
    

emp = Employee('Saqlain', 35, 11, 15, 70)
grossSalary = emp.computeWeeklyPay(39)
netSalary = emp.computeTax(grossSalary)
print(emp.name, 'Gross Pay : ', grossSalary, '\n\t', 'Net Pay : ', netSalary)