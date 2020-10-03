def findCombinationsUtil(arr, index, num, reducedNum): 

  if (reducedNum < 0):
    return; 

  if (reducedNum == 0):

    for i in range(index): 
      print(arr[i], end = " ") 
    print("") 
    return

  prev = 1 if(index == 0) else arr[index - 1] 

  for k in range(prev, num + 1): 

    arr[index] = k
    findCombinationsUtil(arr, index + 1, num, reducedNum - k)

def findCombinations(n): 
  arr = [0] * n
  findCombinationsUtil(arr, 0, n, n)

findCombinations(6)
