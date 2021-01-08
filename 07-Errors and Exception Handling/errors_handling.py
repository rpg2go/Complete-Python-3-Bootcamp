
def write_file():
    try:
        f = open('testfile', 'w')
        f.write("Write a test line")    
    except TypeError:
        print("There was a type error!")
    except OSError:
        print("Hey you have an OS Error")
    except:
        print("All other exceptions")    
    finally:     
        print("I always run")
    
    
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number:"))
        except:
            print("Whoops! That is not a number!")
        else:
            print("Yes, thank you")            
            break
        finally:
            print("End of try/except/finally")    
            

write_file()

ask_for_int()
