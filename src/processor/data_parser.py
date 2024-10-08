import os
from queue import Queue
from typing import List


class DataParser:

    @staticmethod
    def split_line(line: str) -> List[str]:
        return line.strip().split()

    def read_from_file(self, file, queue_: Queue):
        counts = []
        head_tail = os.path.split(file)
        dir_name = head_tail[0].split(os.sep)[-1]
        with open(file, 'r') as f:
            lines = [line.strip() for line in f]
            for i, line in enumerate(lines):
                if line == "$MEAS_TIM:":
                    live_time = int(self.split_line(lines[i + 1])[0])
                if line == "$DATA:":
                    start_index = int(i + 2)
                    break
            for j, line in enumerate(lines[start_index:]):
                if not line.startswith("$"):
                    counts.append(int(line))
                else:
                    break
            counts.append(live_time)
            queue_.put({f"{dir_name}_{head_tail[1]}": counts})
