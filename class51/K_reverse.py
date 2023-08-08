def solve(A,B):

    curr = A
    start = A
    pev_start = A
    j = True
    while curr:
        pev =None
        curr = start
        i = 1
        while curr and i <= B:
            temp = curr.next
            curr.next = pev
            pev = curr
            curr = temp
            i += 1

        if j:
            A = pev
            j = False
        else:
            pev_start.next = pev
            pev_start = start
        start = curr
    return A


