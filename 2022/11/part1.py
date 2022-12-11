import math
from dataclasses import dataclass


@dataclass
class Test:
    divisible: int
    monkey_true_ix: int
    monkey_false_ix: int
    operation: any

    def __post_init__(self):
        _, op, b = self.operation.split()

        if op == "+":
            if b == "old":
                self.operation = lambda item: item + item
            else:
                self.b = int(b)
                self.operation = lambda item: item + self.b
        elif op == "*":
            if b == "old":
                self.operation = lambda item: item * item
            else:
                self.b = int(b)
                self.operation = lambda item: item * self.b

    def get_monkey_true(self):
        return monkeys[self.monkey_true_ix]

    def get_monkey_false(self):
        return monkeys[self.monkey_false_ix]


class Monkey:

    def __init__(self, items: list[int], divisibility: int, test: Test) -> None:
        self.inspections = 0

        self.items = items
        self.divisibility = divisibility
        self.test = test

    def inspect(self):
        self.inspections += len(self.items)
        while self.items:
            item = self.items.pop(0)

            # 1. Operation
            item = self.test.operation(item)

            # 2. Div by 3
            item = math.floor(item / 3)

            # 3. Check divisibility
            true = item % self.divisibility == 0

            # 4. Move to another monkey
            if true:
                self.test.get_monkey_true().items.append(item)
            else:
                self.test.get_monkey_false().items.append(item)


with open("11/input.txt") as f:
    data = f.read().split("\n\n")

monkeys = []
for monkey_string in data:
    # Split by lines
    monkey, items, operation, test, true_ix, false_ix = monkey_string.split("\n")

    # List of ints representing items
    items = [int(item) for item in items.split(": ")[1].split(", ")]

    # X *+ Y
    operation = operation.split("new = ")[1]

    # Divisible by X
    divisibility = int(test.split()[-1])

    # Monkey X if test passed, Monkey Y if not
    true_ix = int(true_ix.split()[-1])
    false_ix = int(false_ix.split()[-1])

    monkeys.append(Monkey(items, divisibility, Test(divisibility, true_ix, false_ix, operation)))

for _ in range(20):
    for monkey in monkeys:
        monkey.inspect()

inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print("Part 1:", math.prod(inspections[:2]))
