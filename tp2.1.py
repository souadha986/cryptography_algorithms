
def rc4(key, data):
    key = key.encode("utf-8")
    data = data.encode("utf-8")

    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    output = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        k = S[(S[i] + S[j]) % 256]
        output.append(byte ^ k)

    return bytes(output)


key = "secret"
message = "a553be70ed"

encrypted = rc4(key, message)
print("Encrypted:", encrypted.hex())


