#!/usr/bin/env python3

# pip install ecdsa
# pip install pysha3

from ecdsa import SigningKey, SECP256k1
import sha3

def checksum_encode(addr_str): # Takes a hex (string) address as input
    keccak = sha3.keccak_256()
    out = ''
    addr = addr_str.lower().replace('0x', '')
    keccak.update(addr.encode('ascii'))
    hash_addr = keccak.hexdigest()
    for i, c in enumerate(addr):
        if int(hash_addr[i], 16) >= 8:
            out += c.upper()
        else:
            out += c
    return '0x' + out

def gen(suppress=False):
    keccak = sha3.keccak_256()

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    address = keccak.hexdigest()[24:]

    private = priv.to_string().hex()
    public = pub.hex()
    addy = checksum_encode(address)

    if not suppress:
        print("Private key:", private)
        print("Public key: ", public)
        print("Address:    ", addy)

    return [private, public, addy]


# def test(addrstr):
#     assert(addrstr == checksum_encode(addrstr))

# test('0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed')
# test('0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359')
# test('0xdbF03B407c01E7cD3CBea99509d93f8DDDC8C6FB')
# test('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb')
# test('0x7aA3a964CC5B0a76550F549FC30923e5c14EDA84')

if __name__ == '__main__':
    gen()