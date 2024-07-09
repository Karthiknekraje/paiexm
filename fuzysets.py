A={1,3,4,5,7,8,9}
B={2,4,6,8,9}

print("union of a n b:",A | B)
print("intersection of a n b:",A & B)
print("diference of an b:",A - B)
print("symmetrical difference of an b:",A ^ B)

C={3,5,7}
print(C.issubset(A))
def compliment_set(D,U):
    return D-U

if __name__ == "__main__":
    D={1,2,3,4,5,6,7,8,9,10}
    U={2,4,6,8,10}
    compliment=compliment_set(D,U)
    print("Compliment of D in U:",compliment)