with open('input9.txt', 'r') as file :
    lines=file.readlines()
N=int(lines[0].strip())
array=list(map(int,lines[1].split()))
print(N, array)

def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        swaps = merge_sort(left_half)
        swaps += merge_sort(right_half)

        i = j = k = 0
        merge_swaps = 0 

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                merge_swaps += len(left_half) - i 
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return swaps + merge_swaps

    return 0  

swaps = merge_sort(array)
print("Numero di swap:", swaps)

'''with open('output9.txt', 'w') as file:
    file.write(str(swaps))'''


