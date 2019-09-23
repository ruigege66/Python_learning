l = [x*x for x in range(5)]#放在中括号中就是列表生成器
g = (x*x for x in range(5))#放在小括号中就是生成器

print(type(l))
print(type(g))#type函数就是返回的是括号内的变量类型

def odd():
    print("Step 1")
    yield 1#在函数odd中，yield负责返回，不用return是因为
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1

if __name__ == "__main__":
    m= odd()
    one=next(m)#odd()是调用生成器
    print(one)
    two = next(m)
    print(two)
    three = next(m)
    print(three)

    m2 = fib(10)
    # print(m2)
    for i in range(6):
        rst = next(m2)
        print(rst)
