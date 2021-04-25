colors = ["blue", "red", "green", "purple", "orange"]

def quicksort(list, start, end):
    if start >= end:
        return 
    start += 1
    quicksort(list, start, end)

quicksort(colors, 0, len(colors) - 1)
print(colors)