import math


f = lambda x: x**2 - 3*x + x * math.log(x, math.e)
f_diff = lambda x: math.log(x, math.e) + 2*x - 2
f_diff2 = lambda x: (2*x + 1) / x
a, b = 1, 2
epsilon = 0.05

def half_division(a, b):
    x1 = (a + b - epsilon) / 2
    x2 = (a + b + epsilon) / 2
    y1, y2 = f(x1), f(x2)
    if y1 > y2:
        a = x1
    else: b = x2
    if b - a > 2 * epsilon:
        return half_division(a, b)
    xm = ( a + b ) / 2
    ym = f(xm)
    return xm, ym
    
    
def golden_ratio(a, b):
    while (b - a) >= epsilon: 
        x1 = a + 0.382 * (b - a)
        x2 = a + 0.618 * (b - a)
        y1, y2 = f(x1), f(x2)
        if y1 < y2:
            b = x2
        else:
            a = x1
    x = (a + b) / 2
    y = f(x)
    return x, y
    
    
def chords(a, b):
    while True:
        x = a - (f_diff(a) * (a - b)) / (f_diff(a) - f_diff(b))
        y = f_diff(x)
        
        if abs(y) <= epsilon:
            return x, f(x)
        elif y > 0: b = x
        else: a = x

    
def newtone(a, b, X = None):
    x = (a + b) / 2 if X == None else X 
    diff_x = f_diff(x)
    if abs(diff_x > epsilon):
        return(newtone(a, b, X=x - diff_x/f_diff2(x)))
    else:
        return x, f(x)
    
def main():
    print(half_division(a, b))
    print(golden_ratio(a, b))
    print(chords(a, b))
    print(newtone(a, b))
    
if __name__ == '__main__':
    main()