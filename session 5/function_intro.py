def say_hello(name,age=17): #define function
    variable_something=f'{name}, {age}'
    print(f'hello {name}')
    return variable_something               #use var from inside def
var_sth=say_hello('dd',23)
print(var_sth)
var_sth2=say_hello('ds',231)
print(var_sth2)