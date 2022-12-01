from algoritms.LZW import compress, decompress
from algoritms.Burrows_Wheeler import encode, decode
from algoritms.Arithmetic import ArithmeticEncoding
from algoritms import from_decimal_to_binary, from_binary_to_decimal


def full_lzw_compress(message):
    code = encode(message)

    compressed = compress(code)
    print(compressed)
    for i in range(len(compressed) - 1):
        compressed[i] = from_decimal_to_binary(ord(str(compressed[i])), 10)
    return compressed


def full_lzw_decompress(compressed):
    for i in range(len(compressed) - 1):
        compressed[i] = chr(from_binary_to_decimal(compressed[i]))

    decompressed = decompress(compressed)
    return decode(decompressed)



if __name__ == "__main__":
    probability_table = {'a': 0.5, 'b': 0.2, 'c': 0.3}
    AE = ArithmeticEncoding()
    original_msg = "aaaacccbcabcabca"

    encoder, encoded_msg = AE.encode(msg=original_msg,probability_table=probability_table)
    print(f"Message - {original_msg}")
    print(f"Encoded Message: {encoded_msg}")

    # --------------------------------------------------------------------------------------------------------------
    print("-------------------------------------------------------------------------------------------------------")
    # --------------------------------------------------------------------------------------------------------------

    msg = 'ABACABAklsfjglsdkfjglsdf'
    compr = full_lzw_compress(message=msg)
    print(compr)
    print(msg == full_lzw_decompress(full_lzw_compress(message=msg)))

