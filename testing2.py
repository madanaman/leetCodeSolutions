import concurrent.futures

def foo(bar):
    print('hello {}'.format(bar))
    return 'foo'

def bar(foo):
    print('hello {}'.format(foo))
    return 'bar'

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo, 'world of foo!')
    future1 = executor.submit(bar, 'world of bar!')
    a = future.result()
    b = future.result()

print(min(a,b))

