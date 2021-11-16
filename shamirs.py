import random


def count_shares(ni, s, P, x):
    ret_sum = sum([n * (x ** (len(ni) - i)) for i, n in enumerate(ni)])
    ret_sum += s
    ret_sum %= P
    return ret_sum


def encode_secret(secret, P, n, t):
    coeffs = [random.randint(1, 1000) for _ in range(t - 1)]
    shares = [(i + 1, count_shares(coeffs, secret, P, i + 1)) for i in range(n)]
    return shares


def lagrange_coeff(x, x_i, x_list):
    ret_sum = 1
    for i in range(len(x_list)):
        if x_i == x_list[i]:
            continue
        ret_sum *= (x - x_list[i]) / (x_i - x_list[i])
    return ret_sum


def lagrange_poly(x, x_list, y_list, P):
    ret_sum = 0
    for i in range(len(x_list)):
        temp = y_list[i] * lagrange_coeff(x, x_list[i], x_list)
        if temp < 0:
            ret_sum -= (-temp % P)
        else:
            ret_sum += temp % P
    return ret_sum


def decode_secret(encoded_secret, P):
    xs = [a[0] for a in encoded_secret]
    ys = [b[1] for b in encoded_secret]
    secret = lagrange_poly(0, xs, ys, P)
    return secret % P


def run():    
    
    secret = 601701566
    P = 2 ** 61 - 1

    n = 10
    t = 10

    encoded_secret = encode_secret(secret, P, n, t)
    decoded_secret = decode_secret(encoded_secret, P)

    print(f"P: {P}")
    print(f"Raw secret: {secret}")
    print(f"Encoded secret: {encoded_secret}")
    print(f"Decoded secret: {decoded_secret}")


if __name__ == "__main__":
    run()
