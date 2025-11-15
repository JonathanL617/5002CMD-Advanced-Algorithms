import threading
import time

def calculate_factorial(num):
    #set the factorial variable to 1
    result = 1

    #then loop and multiply the result until the num
    for i in range(1, num + 1):
        result *= i

    return result

class FactorialThread(threading.Thread):
    def __init__(self, number, thread_id):
        super().__init__()
        self.number = number
        self.thread_id = thread_id
        self.result = None
        self.start_time = None
        self.end_time = None

    def run(self):
        self.start_time = time.perf_counter_ns()
        self.result = calculate_factorial(self.number)
        self.end_time = time.perf_counter_ns()

def run_multithread(rounds=10):
    numbers = [50, 100, 200]
    times = []

    print('-' * 92)
    print(f'| {"Multithreaded Process".center(88)} |')
    print('-' * 92)
    print(f'| Round | Thread 1 Time (ns) | Thread 2 Time (ns)| Thread 3 Time (ns)| Total Time (ns)/(ms)|')
    print('-' * 92)

    for round_num in range(1, rounds + 1):
        threads = []

        #create threads for each factorial calculation

        for i, num in enumerate(numbers):
            thread = FactorialThread(num, i + 1)
            threads.append(thread)

        start_time = time.perf_counter_ns()
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.perf_counter_ns()

        total_time = end_time - start_time
        times.append(total_time)

        t1 = threads[0].end_time - threads[0].start_time
        t2 = threads[1].end_time - threads[1].start_time
        t3 = threads[2].end_time - threads[2].start_time

        print(f'| {round_num:<5} | {t1:<18,} | {t2:<17,} | {t3:<17,} | {total_time:,} ({total_time // 100000:.2f} ms)   |')


    average_time = sum(times) / len(times)
    print('-' * 92)
    print(f'Average Time for Multithreaded Factorial: {average_time:.2f} nanoseconds ({average_time // 1000000:.2f} ms)')
    print('-' * 92)
    return times, average_time


def run_sequential(rounds=10):
    numbers = [50, 100, 200]
    times = []

    print('-' * 39)
    print(f'| {"Non-multithreaded Process".center(34)}  |')
    print('-' * 39)
    print(f'| Round | Total Time (ns) | Time (ms) |')
    print('-' * 39)

    for round_num in range(1, rounds + 1):
        start_time = time.perf_counter_ns()

        results = []
        for num in numbers:
            result = calculate_factorial(num)
            results.append(result)

        end_time = time.perf_counter_ns()
        total_time = end_time - start_time
        times.append(total_time)

        print(f'| {round_num :<5} | {total_time:<15,} | {total_time // 100000:<8.2f}  |')

    average_time = sum(times) / len(times)
    print('-' * 39)
    print(f'Average Time: {average_time:,.2f}ns ({average_time // 1000000:.2f} ms)')
    print('-' * 39)

    return times, average_time

def compare_result(mt_time, mt_avg, seq_time, seq_avg):
    print('-' * 70)
    print(f'Average Time for Multithreaded: {mt_avg:,.2f} ns ({mt_avg / 1000000:.2f} ms)')
    print(f'Average Time for Sequential: {seq_avg:,.2f} ns ({seq_avg / 1000000:.2f} ms)')

    if seq_avg > mt_avg:
        difference = seq_avg / mt_avg
        print(f'Multithreading is faster by: {difference:.2f}x')

    else:
        difference = mt_avg / seq_avg
        print(f'Sequential is faster by: {difference:.2f}')


def main():

    mt_time, mt_avg = run_multithread(rounds=10)
    seq_time, seq_avg = run_sequential(rounds=10)

    compare_result(mt_time, mt_avg, seq_time, seq_avg)


if __name__ == "__main__":
    main()