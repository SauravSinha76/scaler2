class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



def intersection(A,B):
    len_A =0
    len_B =0

    temp_A = A
    temp_B = B

    while temp_A:
        temp_A = temp_A.next
        len_A += 1

    while temp_B:
        temp_B = temp_B.next
        len_B += 1

    temp_A = A
    temp_B = B
    if len_A < len_B:
        diff = len_B - len_A
        while diff > 0:
            temp_B = temp_B.next
            diff -= 1
    else:
        diff = len_A - len_B
        while diff > 0:
            temp_A = temp_A.next
            diff -= 1

    while temp_B and temp_A:
        if temp_B == temp_A:
            return temp_B
        temp_B = temp_B.next
        temp_A = temp_A.next

    return None



