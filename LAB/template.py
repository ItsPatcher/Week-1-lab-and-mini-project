"""
RECORD CHECK  -  my version
===========================

Name  :  Manuel Paquete
Lane  :  IT      
Date  :  24/9/2026 (DD/MM/YY)

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#The following comments address the various inputs selected, and their respective results. The only input that remained constant was "hostname".
#Each value required for a calculation, and displayed on the instances, is from the same session. Ex. gb_used: 47.3 and gb_total: 133 were used together, and produced
#the first instances of "difference" and "percent".

#When ran with a total of 0, the program returns an error with the message "ZeroDivisionError: float division by zero".

hostname = input("Your host name: ")    
gb_used = float(input("Amount of Gygabytes used: "))     
gb_total = float(input("Total amount of Gygabytes: "))

#gb_used instances: 47.3, 81.21 , 119.2
#gb_total instances: 133, 125, 150

difference = gb_total - gb_used
percent = (gb_used / gb_total) * 100

#difference instances: 85.70, 43.79, 30.80
#percent instances: 35.56%, 64.97%, 79.47%

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print("Used        :", f"{gb_used:>10.2f}")
print("Total       :", f"{gb_total:>10.2f}")
print("Free        :", f"{difference:>10.2f}")
print("Percent     :", f"{percent:>10.2f}","%")
print("=" * 34)