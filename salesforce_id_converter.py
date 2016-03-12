from exceptions import ValueError


def convert_id_15_to_18(sf_id):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    full_chars = chars + '012345'

    if not sf_id or len(sf_id) not in (15, 18):
        raise ValueError('SalesForce id must be string value with length 15 or 18 symbols')

    if 18 == len(sf_id):
        return sf_id

    chunks = [ sf_id[i:i + 5] for i in range(0, 15, 5)]
    suffix = ''
    for chunk in chunks:
        reversed_chunk = chunk[::-1]
        binary_id_str = ''.join(['1' if i in chars else '0' for i in reversed_chunk])
        suffix += full_chars[int(binary_id_str, 2)]
    return sf_id + suffix



