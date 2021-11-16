import random


def encode_secret(secret, share_count, K):
    shares = [random.randint(1, K) for _ in range(share_count - 1)]
    shares.append((secret - sum(shares)) % K)
    return shares

def decode_secret(shares, K):
    return sum(shares) % K

def run():

    K = 1000

    secret = random.randint(1, K)
    share_count = 5

    encoded_secret = encode_secret(secret, share_count, K)
    decoded_secret = decode_secret(encoded_secret, K)

    print(f"Raw secret: {secret}")
    print(f"Encoded secret: {encoded_secret}")
    print(f"Decoded secret: {decoded_secret}")


if __name__ == "__main__":
    run()
