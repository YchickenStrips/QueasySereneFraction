import csv
from time import perf_counter


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

def fib_new(n):
a=1
b=1
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1





def main():
  with open("func_perf.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(50):

      print(f"Running iteration {i}...")
      
      exe_time_fib = perf_counter()
      fib_val = fib_bad(i)
      exe_time_fib = perf_counter() - exe_time_fib


      exe_time_fact = perf_counter()
      fact_val = fact(i)
      exe_time_fact = perf_counter() - exe_time_fact
      
      csvwriter.writerow([i, fib_val, exe_time_fib, fact_val, exe_time_fact])

    print("Done!")

if __name__ == "__main__":
  main()

