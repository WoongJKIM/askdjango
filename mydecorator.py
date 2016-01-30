#데코레이트를 통해 사전에 인자에 대한 검사를 수행해 확인하고 자료를 출력하는 예제 파일

import time

def cache(fn):
    cached={}
    def wrap(x,y):
        key=(x,y)
        if key not in cached:
            cached[key]=fn(x,y)
            print("같은거있음")
        return fn(x,y)
    return wrap

@cache
def add(x,y):
    print("calc!!!")
    time.sleep(1)
    return x+y

print(add(1,2))
print(add(2,3))
print(add(1,2))
print(add(3,2))