def fact(n):
  if n > 0:
    return n*fact(n-1)
  else:
    return 1

def main():
  for i in range(20):
    print(f"{i}:\t{fact(i)}")

if __name__ == "__main__":
  main()