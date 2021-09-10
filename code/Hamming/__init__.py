#!/usr/bin/python3.10
from bitarray import bitarray

def encode_hemming(bits: str | list | bitarray) -> str | list | bitarray:
    bit_type = type(bits)
    if bit_type == list:
        bits = "".join(["1" if i and i != "0" else "0" for i in bits])
    bits = bitarray(bits)
    

def decode_hemming():
    pass

if __name__ == "__main__":
    encode_hemming(
        [
            "1",
            "1",
            False,
            "0",
            "0",
            True,
            "0",
            1,
            "1",
            0,
        ]
    )