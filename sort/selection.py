def sort(lt, order='asc'):
    for i in range(len(lt)):
        target = lt[i]
        swap_value = target
        swap_index = None
        for j in range(i + 1, len(lt)):
            current = lt[j]
            if order == 'asc':
                if swap_value > current:
                    swap_value = current
                    swap_index = j
            elif order == 'desc':
                if current > swap_value:
                    swap_value = current
                    swap_index = j
        if swap_index:
            lt[swap_index] = target
            lt[i] = swap_value

    return lt
