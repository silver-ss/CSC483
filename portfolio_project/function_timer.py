import time
from functools import wraps

def timer(func):
    """
    wrapper for search function that starts a times, runs the function 
    then ends the times and takes end time - start time to find run_time
    clear wrapper after each iteration. Can collect the last runtime 
    using function.last_run
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # record start time
        start = time.perf_counter()
        # run function
        result = func(*args, **kwargs)
        # stop timer and find runtime
        run_time = time.perf_counter() - start 
        # store run_tim as last run
        wrapper.last_run = run_time
        # pass returned results from function
        return result
    # clear last_run value
    wrapper.last_run = None
    return wrapper