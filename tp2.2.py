
import struct

DELTA = 0x9E3779B9
ROUNDS = 32
MASK = 0xFFFFFFFF


def xtea_encrypt(message, key):
    if len(message) != 8:
        raise ValueError("Message must be 64 bits (8 bytes).")

    if len(key) != 16:
        raise ValueError("Key must be 128 bits (16 bytes).")

    v0, v1 = struct.unpack(">2I", message)
    k = list(struct.unpack(">4I", key))

    total = 0

    for _ in range(ROUNDS):
        mix = (((v1 << 4) ^ (v1 >> 5)) + v1) & MASK
        v0 = (v0 + (mix ^ ((total + k[total & 3]) & MASK))) & MASK

        total = (total + DELTA) & MASK

        mix = (((v0 << 4) ^ (v0 >> 5)) + v0) & MASK
        v1 = (v1 + (mix ^ ((total + k[(total >> 11) & 3]) & MASK))) & MASK

    return struct.pack(">2I", v0, v1)


def xtea_decrypt(ciphertext, key):
    if len(ciphertext) != 8:
        raise ValueError("Ciphertext must be 64 bits (8 bytes).")

    if len(key) != 16:
        raise ValueError("Key must be 128 bits (16 bytes).")

    v0, v1 = struct.unpack(">2I", ciphertext)
    k = list(struct.unpack(">4I", key))

    total = (DELTA * ROUNDS) & MASK

    for _ in range(ROUNDS):
        mix = (((v0 << 4) ^ (v0 >> 5)) + v0) & MASK
        v1 = (v1 - (mix ^ ((total + k[(total >> 11) & 3]) & MASK))) & MASK

        total = (total - DELTA) & MASK

        mix = (((v1 << 4) ^ (v1 >> 5)) + v1) & MASK
        v0 = (v0 - (mix ^ ((total + k[total & 3]) & MASK))) & MASK

    return struct.pack(">2I", v0, v1)


message = b"ABCDEFGH"
key = bytes.fromhex("00000001000000020000000300000004")

ciphertext = xtea_encrypt(message, key)
print("Encrypted:", ciphertext.hex())

decrypted = xtea_decrypt(ciphertext, key)
print("Decrypted:", decrypted)

