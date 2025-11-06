# for i in range(1, 5):
#     print(i, end=" ")
#     print()
#     for j in range(1, 4):
#         print(j, end=" ")
#     print()

# a = 8
# b = 12

# while b != 0:
#     a, b = b, a % b

# print(f"FPB dari 8 dan 12 adalah {a}")


# n = 100 # Batas angka
# a, b  = 0, 1

# print("Bilangan Fibonacci hingga", n)
# while a <= n:
#    print(a, end=" ")
#    a, b = b, a + b

# n = 3

# for i in range(1, n+1):
   
#     for j in range(n-i):
#       print(" ", end=" ")

#     for k in range(1, i + 1):
#          print(k, end=" ")
#     print()

n = 3

for i in range(1, n+1):

    for k in range(1, i + 1):
        print(k, end=" ")
   
    for j in range(n-i):
      print(" ", end=" ")

    print()