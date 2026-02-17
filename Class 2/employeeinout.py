class Employee:
    def __init__(self):
     print("employee created")
    def __del__(self):
        print("Destructer called")
def create_obj():
    print('Making object')
    obj = Employee()
    print('Function end')
    return obj
print('Calling create_obj()')
emp = create_obj()
print('Program end')    