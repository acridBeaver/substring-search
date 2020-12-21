from algorithms.algorithm import Algorithm


class Zfunc(Algorithm):
    @staticmethod
    def search(substring, text):
        zf = Zfunc.z_func(substring + '#' + text)
        length = len(substring)
        for i in range(length + 1, len(zf)):
            if zf[i] == length:
                yield i - (length + 1)

    @staticmethod
    def z_func(string):
        length = len(string)
        zf = [0] * length
        left = right = 0
        for i in range(1, length):
            if i <= right:
                zf[i] = min(right - i + 1, zf[i - left])
            while i + zf[i] < length and string[zf[i]] == string[i + zf[i]]:
                zf[i] += 1
                if i + zf[i] - 1 > right:
                    left = i
                    right = i + zf[i] - 1
        return zf
