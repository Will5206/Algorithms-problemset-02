"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate
import random

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y


def add(a, b):
    """ a + b for BinaryNumbers"""
    return BinaryNumber(a.decimal_val+ b.decimal_val)

 
def sub(a, b):
    return BinaryNumber(a.decimal_val-b.decimal_val)




 
def _is_base_case(x, y):
    return len(x) <=1 and len(y) <=1
 
def _base_multiply(x, y):
    return binary2int(x).decimal_val *binary2int(y).decimal_val


def quadratic(x,y):


    if _is_base_case(x, y):
        return BinaryNumber(_base_multiply(x, y))
    x, y = pad(x, y)
    n = len(x)
    half = n // 2
    xl, xr = split_number(x)
    yl, yr = split_number(y)


    #      x*y =xl*yl*2^n +(xl*yr + xr*yl)*2^(n/2) +xr*yr
    p1 = quadratic(xl.binary_vec, yl.binary_vec)# xl*yl
    p2 = quadratic(xl.binary_vec, yr.binary_vec)# xl*yr
    p3 = quadratic(xr.binary_vec, yl.binary_vec)# xr*yl
    p4 = quadratic(xr.binary_vec, yr.binary_vec) # xr*yr



    return add(add(bit_shift(p1, n), bit_shift(add(p2, p3), half)), p4)







def subquadratic(x, y):

    if _is_base_case(x, y):
        return BinaryNumber(_base_multiply(x, y))

        
    x, y = pad(x, y)
    n = len(x)
    half = n // 2
    xl, xr = split_number(x)
    yl, yr = split_number(y)

    p1 = subquadratic(xl.binary_vec, yl.binary_vec)# xl*yl
    p2 = subquadratic(xr.binary_vec, yr.binary_vec)  # xr*yr
    p3 = subquadratic(add(xl, xr).binary_vec, add(yl, yr).binary_vec)  #(xl+xr)(yl+yr)
    middle = sub(sub(p3, p1), p2)     # = xl*yr + xr*yl



    return add(add(bit_shift(p1, n), bit_shift(middle, half)), p2)

    
def quadratic_multiply(x, y):
    return quadratic(x.binary_vec, y.binary_vec).decimal_val






def subquadratic_multiply(x, y):
    return subquadratic(x.binary_vec, y.binary_vec).decimal_val







## Feel free to add your own tests here.
def test_multiply():
    #assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2
    
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

    for a, b in [(0,0),(0,7),(1,1), (1,255),(3, 5), (7, 9),(13, 1000),(2**31-1, 2**31-1),(123456789,987654321)]:
        assert quadratic_multiply(BinaryNumber(a),BinaryNumber(b)) == a*b
        assert subquadratic_multiply(BinaryNumber(a),BinaryNumber(b)) == a*b




    rng =random.Random(0)
    for i in range(50):
        a =rng.getrandbits(rng.randint(1,300))
        b =rng.getrandbits(rng.randint(1,300))
        assert quadratic_multiply(BinaryNumber(a), BinaryNumber(b)) == a*b
        assert subquadratic_multiply(BinaryNumber(a), BinaryNumber(b)) == a*b



# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
    
