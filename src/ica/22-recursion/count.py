def countdown(n):
    if n==0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n-1)

countdown(5)
countdown(1)
countdown(0)
