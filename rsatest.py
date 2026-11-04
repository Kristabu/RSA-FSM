
key_n = 0x99925173ad65686715385ea800cd28120288fc70a9bc98dd4c90d676f8ff768d
key_e = 0x0000000000000000000000000000000000000000000000000000000000010001
key_d = 0x0cea1651ef44be1f1f1476b7539bed10d73e3aac782bd9999a1e5a790932bfe9

M_arr_in = 0x0000000011111111222222223333333344444444555555556666666677777777

# RSA encryption
C = pow(M_arr_in, key_e, key_n)

# RSA decryption
M_dec = pow(C, key_d, key_n)

print(f"Input:      {M_arr_in:064X}")
print(f"Encrypted:  {C:064X}")
print(f"Decrypted:  {M_dec:064X}")

print("\nEncryption/decryption successful:", M_dec == M_arr_in)
