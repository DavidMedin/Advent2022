def main():
    file = open("day11.data")

    monkeys = []
    class Monkey:
        items = None
        op = None
        test = 0
        when_true = 0
        when_false = 0
        inspect_count = 0
        monk_id = 0
        def __init__(self) -> None:
            self.items = []
            self.op = ""

        def do(self,old):
            new = eval(self.op)
            return new

        def fuck(self):
            for item in self.items:
                item = self.do(item)
                self.inspect_count += 1
                if item%self.test == 0:
                    monkeys[self.when_true].items.append(item%9699690)
                else:
                    monkeys[self.when_false].items.append(item%9699690)
            self.items = []

    for line in file.readlines():
        words = line.split()
        if len(words) == 0: continue;
        if words[0] == "Monkey":
            monkeys.append(Monkey())
        elif words[0] == "Starting":
            for i in range(2, len(words)):
                proced = words[i]
                if words[i].isdigit() == False:
                    proced = words[i][:-1]
                monkeys[len(monkeys)-1].items.append(int(proced))
        elif words[0] == "Operation:":
            monkeys[len(monkeys)-1].op = words[3] + words[4] + words[5]
        elif words[0] == "Test:":
            monkeys[len(monkeys)-1].test = int(words[3])
        elif words[1] == "true:":
            monkeys[len(monkeys)-1].when_true = int(words[5])
        elif words[1] == "false:":
            monkeys[len(monkeys)-1].when_false = int(words[5])

    for round in range(10000):
        for monk in monkeys:
            monk.fuck()

    sort = sorted(monkeys, key=lambda monk: monk.inspect_count, reverse=True)
    print(sort[0].inspect_count * sort[1].inspect_count)

main()