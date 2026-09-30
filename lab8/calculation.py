def addnumbers(a,b):
    return a+b

def subtractingnumbers(a=0,b=0):
    return a-b

def multiplyingnumbers(a=1,b=1):
    return a*b

def dividingnumbers(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: not a numerical value."
    except:
        print("ERROR!")
        
