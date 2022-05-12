import re
from datetime import datetime
import sys
import os


class Counter:

    def __init__(self, path) -> None:
        self.search_pattern = 'NOK'
        self.timepattern = '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
        self.count = 0
        self.path = path
        self.lines = []
        self.result = ''
        self.open()
        self.work()

    def open(self):
        with open(self.path) as f:
            for line in f.readlines():
                self.lines.append(' '.join(line.split()))
        self.lines.sort()

    def same_time(self, line):
        try:
            self.current_time = datetime.strptime(re.search(
                self.timepattern, line).group(), '%Y-%m-%d %H:%M:%S')
            if self.current_time.minute != self.prev_time.minute:
                self.result += f'Found {self.count} NOKs at {self.prev_time.replace(second=0, microsecond=0)}\n'
                self.count = 0
        except:
            self.prev_time = self.current_time

    def work(self):
        for i in range(len(self.lines)):
            try:
                self.same_time(self.lines[i])
                if re.search(self.search_pattern, self.lines[i]):
                    self.count += 1
                self.prev_time = self.current_time
                if i+1 == len(self.lines):
                    print(self.result)
                    print(f'Found {self.count} NOKs at {self.prev_time.replace(second=0, microsecond=0)}\n')
            except NameError as e:
                print(f'NameError Exception : {e}')
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(f'Exception: {e}')
                print(exc_type, fname, exc_tb.tb_lineno)


Counter('test_file.txt')
