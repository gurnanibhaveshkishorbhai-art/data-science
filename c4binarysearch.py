word = ["Apple","Ball","Cat","Dog","Elephant","Fish"]

key = "Elephant"

low = 0
high = len(word)-1

while low <= high:
    mid = (low + high)//2

    if word[mid] == key:
        print("Found")
        break
    elif key < word[mid]:
        high = mid-1
    else:
        low = mid+1