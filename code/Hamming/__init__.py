#!/usr/bin/python3.10
from bitarray import bitarray
from math import log, ceil

def is_power(num, exp) -> bool:
    """
    checks if num is able to be represented as x**exp with x as int
    """
    return log(num, exp)-int(log(num, exp)) == 0

def to_hamarray(bits: str | list | bitarray) -> bitarray:
    """
    adds 0 to iterable at positions 2**x
    """
    bits = "".join(
        [
            (
                # ceil(log(i,2)) shifts index for each bit insearted
                "1" if int(bits[i-ceil(log(i,2))-1])
                else "0"
            ) if not is_power(i, 2)
            else "0"
            # size of return value
            for i in range(1, len(bits)+int(log(len(bits),2))+2)
        ])
    return bitarray(bits)

def to_type(bits: bitarray, bit_type: type) -> str | list | bitarray:
    """
    convenience function to convert bitarray into a given type
    """
    if bit_type == str:
        return "".join(str(i) for i in bits)
    if bit_type == list:
        return list(bits)
    return bits

def check_hamming(bits: bitarray) -> int:
    """
    creates hamming check code
    uses algorithm: if 1, xor result with position
    count starts at 1
    """
    pbits = None
    for i in range(len(bits)):
        if bits[i]:
            if pbits is None:
                pbits = i + 1
            else:
                pbits ^= i + 1
    return pbits

def rm_pbits(bits: bitarray) -> bitarray:
    """
    zeros all of the check bits, to allow easy operation
    on the data bits while keeping their position
    """
    return bitarray([
        bits[i-1] if not is_power(i, 2)
        else 0
        for i in range(1, len(bits)+1)
    ])

def get_pbits(bits: bitarray) -> int:
    """
    returns only the check bits
    """
    res = 0
    exp = 0
    tmp = ""
    while len(bits) >= 2**exp:
        tmp += str(bits[int(2**exp)-1])
        exp += 1
    for i in range(len(tmp)):
        res += int(tmp[-i-1]) * 2**i
    return res

def encode_hamming(bits: str | list | bitarray) -> str | list | bitarray:
    """
    takes data bits and applies hamming code
    making them less likely to loose data
    """
    bit_type = type(bits)
    bits = to_hamarray(bits)
    pbits = check_hamming(bits)
    pbits = "{0:b}".format(pbits)
    # fill pbits with zeros
    pbits = "0" * int(log(len(bits),2) - len(pbits) + 1) + pbits
    pbits = bitarray(pbits)
    # inseart pbits into bits that have the form of a hamming code
    for i in range(len(pbits)):
        bits[2**i-1] = pbits[i]
    # return input type for convenience
    return to_type(bits, bit_type)

def decode_hamming(bits: str | list | bitarray) -> str | list | bitarray:
    """
    checks if data is valid. If not, it
    tryes to correct it
    """
    bit_type = type(bits)
    bits = bitarray([int(i) for i in bits])
    # compare data with check bits
    pbits = check_hamming(rm_pbits(bits)) ^ get_pbits(bits)
    # if 0 -> no error
    # else: try to correct
    if pbits:
        if pbits <= len(bits):
            bits[pbits-1] ^= 1
        else:
            return -1
    # if not corrected, return error code
    if check_hamming(rm_pbits(bits)) ^ get_pbits(bits):
        return -1
    # cut out correction bits
    bits = [
        bits[2**i:(2**(i+1))-1]
        for i in range(1, int(log(len(bits),2)+1))
    ]
    bits = bitarray(i for j in bits for i in j)
    return to_type(bits, bit_type)