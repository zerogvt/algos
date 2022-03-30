# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from typing import List

def merge(inp1: List[int], inp2: List[int]):
    print(inp1)
    print(inp2)
    res = []
    # 5. Iterate from front to back both inputs as they will be sorted themselves
    i, j = 0, 0
    while True:
        # 6. each time select the smallest element to append to result.
        #    so the result will be sorted!
        if inp1[i] < inp2[j]:
            res.append(inp1[i])
            i += 1
        else:
            res.append(inp2[j])
            j += 1
        # 7. if any of the inputsis exhausted just append the other one to the res
        if i >= len(inp1):
            res = res + inp2[j:]
            break
        if j >= len(inp2):
            res = res + inp1[i:]
            break
    # 8. and return the sorted merge of the two inputs
    return res

def mergesort(input: List[int]) -> List[int]:
    # 1. Break input in half. Watch out the // for integer div
    lim = len(input)//2
    # 2. base condition - stop recursion at single elements by returning them as is
    if not lim:
        return input
    # 3. break in left and right   
    left = mergesort(input[:lim])
    right = mergesort(input[lim:])
    # 4. return the merge of left and right
    return(merge(left, right))
    

if __name__ == "__main__":
    print(mergesort([100, 200, 500, 700, 1010, 1, 4, 50, 10, 30, 40]))
    print("= = = = = = = = = = = = = = =")
    print(mergesort([3, 2, 1]))
    print("= = = = = = = = = = = = = = =")

