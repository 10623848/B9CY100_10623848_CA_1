#Git hub link : https://github.com/10623848/B9CY100_10623848_CA_1.git
# Since it was a small project, I used 

class Employee :
    
    #Constructor of the class
    def __init__(self, name, weeklyhours, rate, overtimeRate, weeklytaxcredit) :
    
        self.name = name
        self.weeklyhours = weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit
        
     
    def computeWeeklyPay (self,hours) :
        overtimeHours = 0
        weeklyToPayHours = 0
        
        # Overtime calculation
        if hours > self.weeklyhours :
            overtimeHours = hours - self.weeklyhours
            weeklyToPayHours = self.weeklyhours
        else : weeklyToPayHours = hours
        
        #Calculating rates based on working hours
        weeklyPay = weeklyToPayHours * self.rate
        overTimePay = self.overtimeRate * overtimeHours
        
        return weeklyPay + overTimePay
    
    
    def computeTax(self,grossPay) :
    
        afterTax = 0.4 * grossPay
        netPayAfterTax = afterTax - self.weeklytaxcredit
        
        if netPayAfterTax > 0 :
            return netPayAfterTax
        else : return 0
        
        
    
#Implementing Employe class and calculating taxes
emp = Employee('Saqlain', 35, 11, 15, 445)
grossSalary = emp.computeWeeklyPay(39)
netSalary = emp.computeTax(grossSalary)
print(emp.name, 'Gross Pay : ', grossSalary, '\n\t', 'Net Pay : ', netSalary)