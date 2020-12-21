from algorithms.algorithm import Algorithm

ANY_LETTER = '*'


class BoyerMooreSearch(Algorithm):

    @staticmethod
    def search(substring, text):
        stop_table = {substring[i]: i for i in range(len(substring))}
        shift_table = BoyerMooreSearch.create_shift_table(substring)

        # Ищем в тексте шаблон
        i = 0
        j = 0
        while i < len(text) - len(substring) + 1:
            sub_text = text[i: i + len(substring)]
            if sub_text == substring:
                yield i
                i += 1
                continue
            for j in range(len(substring) - 1, -1, -1):
                if sub_text[j] != substring[j]:
                    break

            step_stop = 0
            if substring[j] in stop_table:
                step_stop = j - stop_table[substring[j]]
            else:
                stop_table = j + 1

            step_shift = shift_table[len(substring) - j - 1]
            if max(step_stop, step_shift) > 1:
                i += max(step_stop, step_shift) - 1
            i += 1

    @classmethod
    def create_shift_table(cls, substring):
        sub = ANY_LETTER * len(substring) + substring
        shift_arr = [len(substring)] * len(substring)
        shift_arr[0] = 1
        j = 0
        for i in range(len(substring)):
            for j in range(len(substring)):
                left_edge = len(substring) - i
                window = len(sub) - j
                if BoyerMooreSearch.same(substring[left_edge:], sub[window - i: window]) \
                        and substring[left_edge - 1] != sub[window - i - 1]:
                    break
            shift_arr[i] = min(len(substring), j)

        return shift_arr

    @classmethod
    def same(cls, x: str, y: str):
        for p in range(len(x)):
            if x[p] != ANY_LETTER and y[p] != ANY_LETTER and x[p] != y[p]:
                return False
        return True
