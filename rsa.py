def blakely (a, b, n, k):
    R = 0                                   # step 1
    if not (0 <= a <= n-1) or not (0 <= b <= n-1):  #assumes 0 <= a,b <= n-1
        return "error"
    else:
        for i in range(0, k): #step 2
            R = 2*R + kbit(a, k, i) * b     #step 3
            for ii in range(2):             #step 41 and 4.2
                if R >= n:
                    R -= n # replaces R = R % n
        return R                            #step 5

def kbit(a, k, i):
    return (a >> (k - 1 - i)) & 1

#TODO: Binary exponentiation method RL/lR

#------------------------------------------------
#slett før innlevering !!!!!!!!!!!!!!!
#------------------------------------------------

#testing 
# n = p*q

n = 11 * 13                # 143
k = (n - 1).bit_length()   # bits needed for n-1 = 142 -> k = 8

# Exhaustive test: every (a, b) pair in [0, n-1]
mismatches = []
for a in range(n):
    for b in range(n):
        expected = (a * b) % n
        got = blakely(a, b, n, k)
        if got != expected:
            mismatches.append((a, b, expected, got))

print(f"Checked {n*n} pairs, {len(mismatches)} mismatches")

# Edge cases worth spot-checking on your own
for a, b in [(0, 0), (n-1, n-1), (11, 13), (1, n-1)]:
    print(a, b, "->", blakely(a, b, n, k), "expected", (a*b) % n)
