# Defining a function
def fun1():
    print("Inside fun1()...")

# Calling the function
fun1()

# Printing the function object (reference, not execution)
print(fun1)

# Assigning function reference to another variable
fun2 = fun1

# Calling the function using new reference
fun2()

# Printing the new reference
print(fun2)

#--------------------------------------------------------------------------------------------------------
def alpha(ref):
    print("Inside alpha()...")
    ref()
def beta():
    print("Inside beta()...")

alpha(beta)


#--------------------------------------------------------------------------------------------------------

# Function that takes another function as a parameter
def alpha(ref):
    print("Inside alpha()...")
    ref()   # Calling the function passed as argument


# Another function
def beta():
    print("Inside beta()...")


# Passing function 'beta' to 'alpha'
alpha(beta)


#--------------------------------------------------------------------------------------------------------
# Function to calculate sum of list
def get_sum(lst):
    print(sum(lst))


# Function to calculate product of list
def get_product(lst):
    p = 1
    for i in lst:
        p = p * i
    print(p)


# Higher-order function: returns a function based on choice
def fun(choice):
    if choice == 'sum':
        return get_sum      # returning function reference
    else:
        return get_product  # returning function reference


# fun returns get_sum
fun1 = fun('sum')
fun1([10, 20, 30, 40])   # Calls get_sum


# fun returns get_product
fun2 = fun('prod')
fun2([1, 2, 3, 4, 5])     # Calls get_product

#--------------------------------------------------------------------------------------------------------

def outer():
    print('outer function()')
    
    def inner():
        print('inner function()')
    return inner   # returning function reference

f = outer()
f()

#--------------------------------------------------------------------------------------------------------
# outer function acts like a decorator
def outer(ref):
    
    # wrapper function adds extra functionality
    def wrapper(lst):
        # Check condition before calling original function
        if 0 in lst:
            print('0 is present')
        else:
            ref(lst)   # Call original function
    
    return wrapper   # return modified function


# Original function
def get_product(lst):
    p = 1
    for i in lst:
        p = p * i
    print("Product:", p)


# Wrapping original function
mod_get_prod = outer(get_product)

# Calling modified function
mod_get_prod([0, 20, 30])
mod_get_prod([1, 2, 3, 4])

#--------------------------------------------------------------------------------------------------------

