
#keyword arguments
def add_fn(a,b=0, c= 0):
    print(f"a: {a}, b: {b}, c: {c}")
    return a+b+c
add_fn(4, c=5)

def add_fn_pos(*a):
  a
  return a
add_fn_pos(4,5,6,7,8)