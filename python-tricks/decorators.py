import time
def get_time(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        print(f'Execution took: {time.time() - start } seconds')
        return res
    return wrapper


def html_wrapper(tag):
    def html_decorator(func):
        def wrapper(*args):
            print(f'<{tag}>{func(*args)}</{tag}>')
        return wrapper
    return html_decorator


@get_time
def test_func(num1, num2):
    for i in range(num1):
        for ii in range(num2):
            iii = i * ii

@html_wrapper('img')
def yell(string):
    print(string.upper())
    return string.upper()

yell('hello')
