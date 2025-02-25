import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇
def speed_calc_decorator(func):
    def wrapper():
        current_time = time.time()
        func()
        passed_time = current_time - time.time()
        print(passed_time)
    
    return wrapper
    
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i