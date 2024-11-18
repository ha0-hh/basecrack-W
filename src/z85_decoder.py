# src/z85_decoder.py

Z85_CHARS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', '.', '-', ':', '+', '=', '^', '!', '/',
    '*', '?', '&', '<', '>', '(', ')', '[', ']', '{',
    '}', '@', '%', '$', '#'
]

def z85_decode(encoded_string):
    """Decode a Z85 encoded string to bytes"""
    if len(encoded_string) % 5 != 0:
        raise ValueError("Invalid Z85 string length")

    value = 0
    decoded_bytes = bytearray()

    for i, char in enumerate(encoded_string):
        value = value * 85 + Z85_CHARS.index(char)
        if (i + 1) % 5 == 0:
            decoded_bytes.extend([
                (value >> 24) & 0xFF,
                (value >> 16) & 0xFF,
                (value >> 8) & 0xFF,
                value & 0xFF,
            ])
            value = 0

    return bytes(decoded_bytes)
