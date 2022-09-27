global_var = [1]
def my_function(global_var):
    global_var.append(2)

my_function(global_var)
print(global_var)
