#!/usr/bin/python3.10
from bitarray import bitarray
from math import log, ceil

def encode_hemming(bits: str | list | bitarray) -> str | list | bitarray:
    bit_type = type(bits)
    if bit_type == list:
        bits = "".join(
            [
                (
                    "1" if bits[i-ceil(log(i,2))-1] and bits[i-ceil(log(i,2))-1] != "0" 
                    else "0"
                ) if log(i,2)-int(log(i,2)) != 0
                else "0"
                for i in range(1, len(bits)+int(log(len(bits),2))+2)
            ])
    bits = bitarray(bits)
    pbits = None
    for i in range(len(bits)):
        if bits[i]:
            if pbits is None:
                pbits = i + 1
            else:
                pbits ^= i + 1
    pbits = "{0:b}".format(pbits)
    pbits = "0" * int(log(len(bits),2) - len(pbits) + 1) + pbits
    pbits = bitarray(pbits)
    for i in range(len(pbits)):
        bits[2**i-1] = pbits[i]
    return bits

        
    

def decode_hemming():
    pass

if __name__ == "__main__":
    encode_hemming(
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