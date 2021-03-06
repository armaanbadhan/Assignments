import sys
 
def run_program(m):
    print('1 ' + str(m))
    sys.stdout.flush()
    r = int(input())
    if r == 0:
        return False
    elif r == 1:
        return True
    exit()
 
 
# ------------------- Do not touch anything above this line -------------------------------------
 
# complete the function below, use run_program(x) to determine if Chef's program can consume x bytes
# The result will be True if it can and False otherwise
# If you call the function run_program more than 31 times, you will get a wrong answer verdict

l = [0]

def binn(lo, hi):
    if lo>hi:
        return l[0]
    mid = (lo+hi)//2
    if run_program(mid):
        l[0] = mid
        return binn(mid+1, hi)
    else:
        return binn(lo, mid-1)


def find_memory_limit():
    lo, hi = 1, 999999999
    return binn(lo, hi)
 

# ------------------- Do not touch anything below this line -------------------------------------
print("2 " + str(find_memory_limit()))
    