class stack:
    def __init__(self):
        self.key = 0
        self.arr = []

    def push(self, num):
        self.arr.append(num)
        self.key += 1

    def pop(self):
        if self.arr:
            self.key -= 1
            del(self.arr[self.key])
            return 1
        else:
            return 0


N = int(input())

for _ in range(N):
    stack_inst = stack()

    ps = input()
    no = False

    for i in range(0, len(ps)):
        if ps[i] == '(':
            stack_inst.push(1)
        else:
            if stack_inst.pop() == 0:
                no = True
                break

    if stack_inst.key == 0 and no != True:
        print("YES")
    else:
        print("NO")
