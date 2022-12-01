def compress(uncompressed):
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = chr(dict_size)
            dict_size += 1
            w = c

    if w:
        result.append(dictionary[w])
    return result

def decompress(compressed):
    dict_size = 256
    dictionary = {chr(i): chr(i) for i in range(dict_size)}

    w = result = compressed.pop(0)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == chr(dict_size):
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result += entry

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result
