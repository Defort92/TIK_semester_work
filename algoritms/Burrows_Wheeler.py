def encode(msg):
    msg = msg + "$"
    table = [msg[i:] + msg[:i] for i in range(len(msg))]
    table = sorted(table)

    last_column = [row[-1:] for row in table]
    bwt = ''.join(last_column)
    return bwt


def decode(bwt):
    table = [""] * len(bwt)
    for i in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]
        table = sorted(table)

    inverse_bwt = [row for row in table if row.endswith("$")][0]
    inverse_bwt = inverse_bwt.rstrip("$")
    return inverse_bwt
