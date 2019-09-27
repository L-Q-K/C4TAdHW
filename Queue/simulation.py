import random
from qom import Queue

class Simulation:
    def __init__(self, pr, min, max, capa):
        self.process_rate = pr
        self.min_req_rate = min
        self.max_req_rate = max
        self.queue = Queue(capa)

    def step(self, req):
        res = []
        lost = 0
        can_process = self.process_rate
        while not self.queue.is_empty():
            if can_process > 0:
                res.append(self.queue.remove())
                can_process -= 1

        for request in req:
            if can_process >0:
                res.append(request)
                can_process -= 1
            else:
                success = self.queue.insert(request)
                if (success == False):
                    lost += 1

        return res, lost

    def run(self, iteration):
        t = 0
        for i in range(iteration):
            req_rate = random.randint(self.min_req_rate, self.max_req_rate)
            temp = ['A'] * req_rate
            res, loss = self.step(temp)
            t += loss

        return t/iteration

for capacity in range(0,10):
    sim = Simulation(5, 4, 7, capacity)
    loss = sim.run(10000)
    print(capacity)
    if loss <= 0.1:
        print('TT')
        break
