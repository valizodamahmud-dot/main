try:
    n = int(input())
    print(n/4)
except ValueError:
    print("input must be a number")  
except ZeroDivisionError:
    print("division by zero is not allowed")  
except:
    print("eror") 
finally:
    print("program finishid")        