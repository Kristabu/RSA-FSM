tests = [
    (0x0000000011111111222222223333333344444444555555556666666677777777,
     0x0000000000000000000000000000000000000000000000000000000000000001,
     0x99925173ad65686715385ea800cd28120288fc70a9bc98dd4c90d676f8ff768d),
]

for i, (a, b, n) in enumerate(tests):
    result = (a * b) % n
    print(f"Test {i+1}:")
    print(f"a      = {a:064X}")
    print(f"b      = {b:064X}")
    print(f"n      = {n:064X}")
    print(f"result = {result:064X}")
    print()