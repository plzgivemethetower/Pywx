import hashlib
token = "non"
def check_signature(signature, timestamp, nonce):
    L = [timestamp, nonce, token]
    L.sort()
    s = L[0] + L[1] + L[2]
    return hashlib.sha1(s).hexdigest() == signature