from tests.test_algorithm import TESTS
from algorithms import ALGORITHMS
import matplotlib.pyplot as plt
import time
import argparse
import tracemalloc


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
        for test in self.tests:
            print('__________TEST__________' + test.name)
            for alg in ALGORITHMS:
                print(alg.name())
                for i in range(self.n_times):
                    tracemalloc.start()
                    start_time = int(round(time.time() * 1000))
                    alg.findall(test.substring, test.text)
                    timer = int(round(time.time() * 1000)) - start_time
                    mem = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()
                    self.test_time[test.name][alg.name()].append(timer)
                    self.test_mem[test.name][alg.name()].append(mem)

    def report(self, name: str, samples, scale: str):
        data = self.test_time
        figure, axises = plt.subplots(len(data), figsize=(30, 90))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(samples[test][alg]))
                y_arr = list(map(lambda x: x, samples[test][alg]))

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
        benchmark.report('results_mem.png', benchmark.test_mem, 'memory')
