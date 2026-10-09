# <Create a high level model of the algorithm(s) you used for modular multiplication and modular exponentiation.>

def blakely (a, b, n, k):
    print("-")
    print("blakely is running...")
    print("-")
    R = 0                                   # step 1
    if not (0 <= a <= n-1) or not (0 <= b <= n-1):  #assumes 0 <= a,b <= n-1
        return "error"
    else:
        for i in range(0, k): #step 2
            R = (R+R) + kbit(a, k, i) * b     #step 3
            for ii in range(2):             #step 4.1 and 4.2
                if R >= n:
                    R -= n # replaces R = R % n
        return R                            #step 5

def kbit(a, k, i):
    return (a >> (k - 1 - i)) & 1

# RL binary exponentiation i python
def exponentiate(M_in, key, n):
    # Output: C := M^e mod n
    # 1. C := 1 ; P := M
    M_out = 1 
    P = M_in
    
    #Konverter key til binær og gjør key[0] til minst signifikant
    key = bin(key)[2:]
    key = key[::-1] # Flipp så e[0] er minst signifikante bit
    h = len(key)

    print("------------------Exponentiate initialized------------------------")
    print("Values:")
    print(" Message in:    ", P)
    print(" Key:           ", key)
    print(" Lenght of key: ", h)
    print("------------------Starting loop----------------------------------")
    # for funksjonskall
    # 2. for i = 0 to h - 2
    for i in range(0, h-1):
        # 2a. if key_i = 1 then C := C * P (mod n)
        print(f'Loop {i}:')
        if key[i] == '1':
            print(f'Key index {i} was 1')
    	    #C = (C * P) % n
            k = len(bin(M_out)) - 2  # Første to tegn er 0b (designerer binær)
            print(f'k is {k} and message out was {M_out}(binary: {bin(M_out)})')
            M_out = blakely(M_out, P, n, k)
            print(f'New message out {M_out}')
        # 2b. P := P * P (mod n)
        #P = (P *P) % n
        k = len(bin(P)) - 2
        print(f'k is {k} and message in is {P}(binary: {bin(P)})')
        P = blakely(P, P, n, k)
    
    # 3. if e[h-1] = 1 then C := C * P (mod n)
    if key[-1] == '1':
        print(f'key[-1] was 1')
    	#C := (C * P) % n
        k = len(bin(M_out)) - 2 
        print(f'k is {k}, and message out {M_out}(binary: {bin(M_out)})')
        M_out = blakely(M_out, P, n, k)
        print(f'New meassage out {M_out}')
    # 4. return C
    return M_out

n = 119
e = 5   #256 bit
d = 77  #256 bit

M = 117

# Encrypt
cipher = exponentiate(M, e, n)
print("Encrypted:", cipher)

# Decrypt
decrypted = exponentiate(cipher, d, n)
print("Decrypted:", decrypted)

assert decrypted == M, "Round-trip failed!"
print("Success — matches original message.")