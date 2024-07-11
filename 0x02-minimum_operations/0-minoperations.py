def minOperations(n):
    '''find the minimum numbers of operations needed to result in n H characters.'''
    if not isinstance(n, int):
        return 0
    opertions_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if n % done == 0:
            cp_pa = done
            done += cp_pa
        else:
            done += 1
        opertions_count += 1

    return opertions_count
