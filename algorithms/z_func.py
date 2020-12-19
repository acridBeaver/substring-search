from algorithms.algorithm import Algorithm

class Zfunc(Algorithm):
    @staticmethod
    def search(substring, text):
        zf = Zfunc.z_func(substring + '#' + text)
        m = len(substring)
        for i in range(m + 1, len(zf)):
            if zf[i] == m:
                yield i - (m + 1)

    @staticmethod
    def z_func(string):
        n = len(string)
        zf = [0] * n
        left = right = 0
        for i in range (1, n):
            if i <= right:
                zf[i] = min(right - i + 1, zf[i - left])
            while i + zf[i] < n and string[zf[i]] == string[i + zf[i]]:
                zf[i] += 1
                if i + zf[i] - 1 > right:
                    left = i
                    right = i+zf[i]-1
        return zf
