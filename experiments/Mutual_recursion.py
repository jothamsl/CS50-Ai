# Two functions are called mutually recursive if the first function makes a
# recursive call to the second function and the second function, in turn, calls
# the first one.

# Hofstader Sequence
# A Hofstadter sequence is a member of a family of related integer sequences
# defined by non-linear recurrence relations.

# Hofstader sequence, female function
def hofstaderFemale(n):
    if n < 0:
        return 
    else:
        val = 1 if n == 0 else (n - hofstaderFemale(n - 1))
        return val

# Male function 
def hofstaderMale(n):
    if n < 0:
        return
    else:
        val = 0 if n == 0 else (n - hofstaderMale(n - 1))
        return val

# Driver 
print("F:", end=" ")
for i in range(0, 20):
    print(hofstaderFemale(i), end=" ")

print("\n")
print("M:", end=" ")
for i in range(0, 20):
    print(hofstaderMale(i), end=" ")

