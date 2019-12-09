# -*- coding: UTF-8 -*-
import base64 as b64

def xorAndb64(s, k, e):
    def _rollright(s, n):
        i = -1
        max = len(s) - 1
        while n > 0:
            i = 0 if i == max else i + 1
            s = s + s[i]
            n = n - 1
        return s

    def _expandkey(k, l):
        kl = len(k)
        m = l - kl
        k = _rollright(k, m) if m > 0 else k[:m]
        return k

    def _xor(data, key):
        return bytearray (a ^ b for a, b in zip (*map (bytearray, [data, key])))
    s = s if e else b64.b64decode(s)
    s = _xor(s, _expandkey(k, len(s)))
    s = b64.b64encode(s) if e else s
    return s

