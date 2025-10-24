#Scope //enclosing
def outer_function():
    msg = 'Hello there!'
    ref = ''
    

    def inner_func():
       nonlocal ref
       ref = 'How are you?'
       print(msg)
       
    inner_func()

outer_function()  




       