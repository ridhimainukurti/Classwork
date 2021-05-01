def bubsort (input_lst):

    n = len(input_lst)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        swapped= False
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if input_lst[j] > input_lst[j+1] :
                input_lst[j], input_lst[j+1] = input_lst[j+1], input_lst[j]
                swapped = True

        if swapped == False:
            break

    return (input_lst)
