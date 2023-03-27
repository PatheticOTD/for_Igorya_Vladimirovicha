__a,__b,__c = 7,2,8

def triangle_perimetr(a = __a, b = __b, c = __c):
    return a + b + c

def triangle_area(a = __a, b = __b, c = __c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

