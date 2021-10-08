#!/usr/bin/python3.10
from bitarray import bitarray
from math import log, ceil

def to_hamarray(bits: str | list | bitarray) -> bitarray:
    bits = "".join(
        [
            (
                "1" if bits[i-ceil(log(i,2))-1] and bits[i-ceil(log(i,2))-1] != "0" 
                else "0"
            ) if log(i,2)-int(log(i,2)) != 0
            else "0"
            for i in range(1, len(bits)+int(log(len(bits),2))+2)
        ])
    return bitarray(bits)

def to_type(bits: bitarray, bit_type: type) -> str | list | bitarray:
    if bit_type == str:
        return "".join(str(i) for i in bits)
    if bit_type == list:
        return [i for i in bits]
    return bits

def check_hamming(bits: bitarray) -> int:
    pbits = None
    for i in range(len(bits)):
        if bits[i]:
            if pbits is None:
                pbits = i + 1
            else:
                pbits ^= i + 1
    return pbits

def encode_hamming(bits: str | list | bitarray) -> str | list | bitarray:
    bit_type = type(bits)
    bits = to_hamarray(bits)
    pbits = check_hamming(bits)
    pbits = "{0:b}".format(pbits)
    pbits = "0" * int(log(len(bits),2) - len(pbits) + 1) + pbits
    pbits = bitarray(pbits)
    for i in range(len(pbits)):
        bits[2**i-1] = pbits[i]
    return to_type(bits, bit_type)

def decode_hamming(bits: str | list | bitarray) -> str | list | bitarray:
    bit_type = type(bits)
    bits = bitarray([int(i) for i in bits])
    pbits = check_hamming(bits)
    if pbits:
        if pbits <= len(bits):
            bits[pbits-1] ^= 1
        else:
            return -1
    if check_hamming(bits):
        return -1
    return to_type(bits, bit_type)

if __name__ == "__main__":
    ham = encode_hamming(
        [
            "0",
            "1",
            False,
            "0",
            1,
            True,
            0,
            0
        ]
    )
    #ham[7] = 1
    #ham[4] = 0
    ham = decode_hamming(ham)
    print(ham)