
# importing  module calc.py
import calc

print(calc.add(10, 2))



# importing sqrt() and factorial from the
# module math
#import math
from math import sqrt, factorial

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.

def factorial_kc(x):
    
    result =1.0
    while x>0:
        result = result*x
        x= x-1
    return result
        
print(factorial_kc(6))        
        

print(sqrt(16))
print(factorial(6))


