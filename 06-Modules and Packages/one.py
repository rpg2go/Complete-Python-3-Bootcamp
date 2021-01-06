#one.py
def func():
    print("Execute function in one.py")

def function():
    pass

def function2():
    pass

print ("TOP LEVEL IN ONE.PY")


#if __name__ == '__main__':
#    print ("one.py is being run directly")
#else:
#    print ("one.py has been imported")
      
if __name__ == '__main__':
    func()
    
    function()
    function2()