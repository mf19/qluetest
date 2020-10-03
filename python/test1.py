def getPrimes(i):
  result = []

  print("Prime numbers lower than", i, "are:")

  for num in range(0, i):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            result.append(num)
  print(result)

getPrimes(5)