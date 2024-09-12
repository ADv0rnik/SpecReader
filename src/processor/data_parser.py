import os
from queue import Queue
from typing import List


class DataParser:

    @staticmethod
    def __split_line(line: str) -> List[str]:
        return line.strip().split()

    def read_from_file(self, file, queue_: Queue):
        counts = []
        head_tail = os.path.split(file)
        with open(file, 'r') as f:
            lines = [line.strip() for line in f]
            for i, line in enumerate(lines):
                if line == "$MEAS_TIM:":
                    live_time = int(self.__split_line(lines[i + 1])[0])
                if line == "$DATA:":
                    start_index = int(i + 2)
                    break
            for j, line in enumerate(lines[start_index:]):
                if not line.startswith("$"):
                    counts.append(int(line))
                else:
                    break
            counts.append(live_time)
            queue_.put({head_tail[1]: counts})
