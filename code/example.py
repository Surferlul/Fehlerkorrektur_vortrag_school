from Hamming8 import encode_hamming, decode_hamming

while True:
    action = input("ecnode - e, decode - d, quit - q: ")
    match action:
        case "e":
            inp = input("bits: ")
            print(encode_hamming(inp))
        case "d":
            inp = input("bits: ")
            print(decode_hamming(inp))
        case "q":
            exit()
        case _:
            print("invalid input!")