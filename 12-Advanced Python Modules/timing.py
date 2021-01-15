import time
import timeit

def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str, range(n)))


def measure_func_one(num):
    # get current time
    start_time = time.time()

    # run the code & get end time
    result = func_one(num)
    end_time = time.time()

    # measure elapsed time & print it
    elapsed_time = end_time - start_time
    #print(result)
    print(elapsed_time)

def measure_func_two(num):
    # get current time
    start_time = time.time()

    # run the code & get end time
    result = func_two(num)
    end_time = time.time()

    # measure elapsed time & print it
    elapsed_time = end_time - start_time
    # print(result)
    print(elapsed_time)


def timeit_func_one(num):

    setup = '''
    def func_one(n):
        return [str(num) for num in range(n)]
    '''

    stmt = '''
        func_one(100)
        '''

    timeit.timeit(stmt, setup, number=100000)


def timeit_func_two(num):

    setup2 = '''
    def func_two(n):
        return list(map(str,range(n)))
    '''
    stmt2 = '''
    func_two(100)
    '''

    timeit.timeit(stmt2, setup2, number=1000000)

if __name__ == "__main__":
    print("Start script running")
    num = 10000000

    # measure_func_one(num)
    #
    # measure_func_two(num)

    num = 1000

    timeit_func_one(num)
    timeit_func_two(num)