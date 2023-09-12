from time import thread_time

def fact(n):
  if n > 0:
    return n*fact(n-1)
  else:
    return 1

def fib_bad(n):
  if n > 1:
    return fib_bad(n-1) + fib_bad(n-2)
  else:
    return 1

def main():
  for i in range(40):
    exe_time = thread_time()
    fib_val = fib_bad(i)
    exe_time = thread_time() - exe_time
    print(f"{i}:\t\t{fib_val}\t\tin{exe_time}")

if __name__ == "__main__":
  main()