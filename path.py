from dataclasses import dataclass
import enum
from typing import List, Tuple


@dataclass
class Path:
    from_: str
    to_: str
    path: List[Tuple]
    cost: int
    num_of_days: int

    def result(self, result: enum.Enum):
        print(f"{str.capitalize(result(self.from_).name)} -> {str.capitalize(result(self.to_).name)}", end=' ')
        print(f"Cost: {self.cost}", end=' ')
        print(f"Path: ", end='')
        for i in range(len(self.path)):
            print(f"{str.capitalize(result(self.path[i][0]).name)}{self.path[i][1]}", end=' ')
            if len(self.path) - 1 > i:
                print(f" -> ", end='')
        print(f"Number of days: {self.num_of_days}")
