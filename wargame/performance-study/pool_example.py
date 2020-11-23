"""pool_example

Shows a trivial example on how to use various methods of the class Pool.
"""
import multiprocessing

def get_result(num):
    """Trivial function used in multiprocessing example"""
    process_name = multiprocessing.current_process().name
    print("Current process: {0} - Input number: {1}".format(process_name, num))
    return 10 * num

if __name__ == '__main__':
    numbers = [2, 4, 6, 8, 10]

    # Create two worker processes.
    pool = multiprocessing.Pool(3)

    # Use Pool.apply method to run the task using pools of processes
    #mylsit = [pool.apply(get_result, args=(num,) for num in numbers]

    # Use Pool.map method to run the task using the pool of processes
    #mylist = pool.map(func=get_result, iterable=numbers)

    # Use Pool.apply_async method to run the task
    results = [pool.apply_async(get_result, args=(num,))
               for num in numbers]

    # The elements of results list are instances of Pool.ApplyResult
    # Use the object's get() method to get the final values.
    mylist = [p.get() for p in results]

    # Stop the worker processes
    pool.close()

    # Join the processes
    pool.join()
    print("Output: {0}".format(mylist))
