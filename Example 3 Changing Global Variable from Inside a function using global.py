c = 0 # global variable

def add():
    global c 
    c = c + 2 # Increment by 2
    print("Inside add():", c )

add()
print("In main:", c)