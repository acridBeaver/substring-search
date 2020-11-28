from tests.algorithm_test import TESTS
from algorithms import ALGORITHMS
from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
from memory_profiler import memory_usage
import argparse


class Benchmark:

    def __init__(self, n_times):
        self.tests = TESTS
        self.n_times = n_times

        self.test_time = {}
        self.test_mem = {}
        for test in self.tests:
            self.test_time[test.name] = {alg.name(): [] for alg in ALGORITHMS}
            self.test_mem[test.name] = {alg.name(): [] for alg in ALGORITHMS}

    def run(self):
        start_mem = np.mean(memory_usage())
        execute = 'alg.search(test.substring, test.text)'
        for alg in ALGORITHMS:
            for test in self.tests:
                memory_expression = (alg.search, (test.substring, test.text))
                for i in range(self.n_times):
                    self.test_time[test.name][alg.name()].append(
                        timeit(execute, globals=locals(), number=1))
                    self.test_mem[test.name][alg.name()].append(
                        max(memory_usage(memory_expression)) - start_mem)

    def report(self, name: str, samples, scale: str, pow=1e5):
        data = self.test_time
        figure, axises = plt.subplots(len(data), figsize=(15, 40))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(samples[test][alg]))
                y_arr = list(map(lambda x: x * pow, samples[test][alg]))

                axises[i].scatter(x_arr, y_arr, label=alg)
                axises[i].set_title(test)
                axises[i].set_xlabel('runs')
                axises[i].set_ylabel(scale)
                axises[i].legend()
        figure.savefig(name, format='png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simple benchmark for substring searching algorithms')
    parser.add_argument('N', metavar='N_times', type=int,
                        help='an integer of times to run tests')
    parser.add_argument('--report', '-r', action='store_true',
                        help='makes report of tests in report.png')

    args = parser.parse_args()
    benchmark = Benchmark(args.N)
    benchmark.run()

    if args.report:
        benchmark.report('results_time.png', benchmark.test_time, 'time')
        benchmark.report('results_mem.png', benchmark.test_mem, 'memory', pow=1)
