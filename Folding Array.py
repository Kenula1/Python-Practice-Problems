def fold_array(array, runs):
    copy_array = array[:]
    for times in range(runs):
        temp_array = []
        pivot = len(copy_array) // 2

        for i in range(pivot):
            temp_array.append(copy_array[i] + copy_array[-(i + 1)])

        if len(copy_array) % 2 != 0:
            temp_array.append(copy_array[pivot])

        copy_array = temp_array[:]
        final_array = temp_array[:]

    return final_array

print(fold_array([1, 2, 3, 4, 5], 1))
