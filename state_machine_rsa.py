import time
from enum import Enum, auto


class RL(Enum):
    IDLE = auto()
    BLAKLEY = auto()
    RECEIVE = auto()
    OUT = auto()

class BLAKLEY(Enum):
    IDLE = auto()
    LOOP = auto()
    OUT = auto()

#class BLAKLEY2(enumerate):
#    IDLE = 1
#    LOOP = 2
#    OUT = 3


class Blakley_method:
    def __init__(self, A, B):
        self.state = BLAKLEY.IDLE
        self.a = A
        self.b = B
        self.counter = 1
        self.result = 0
        self.done = 0
    

    def compute_next_state(self, RL):
        if (self.state == BLAKLEY.IDLE):
            if (RL.waiting):
                return BLAKLEY.LOOP
            else:
                print("Blakley IDLE")
                return BLAKLEY.IDLE
            

        elif (self.state == BLAKLEY.LOOP):
            print(f'BLAKLEY LOOP {self.counter}')
            if self.counter >= 3:
                return BLAKLEY.OUT
            return BLAKLEY.LOOP

        elif (self.state == BLAKLEY.OUT):
            print("BLAKLEY OUT")
            return BLAKLEY.IDLE

    def update(self):
        if self.state == BLAKLEY.IDLE:
            self.result = 0
            self.done = False
        elif self.state == BLAKLEY.LOOP:
            self.result += self.a + self.b
            self.counter += 1
            if self.counter > 3:
                self.counter = 1
        elif self.state == BLAKLEY.OUT:
            self.done = True

        

class RL_method:
    def __init__(self, Message):
        self.state = RL.IDLE
        self.message_in = Message
        self.counter = 0
        self.result = 0
        self.waiting = 0

    def compute_next_state(self, blakley):
        if (self.state == RL.IDLE):
            print("--RL IDLE--")
            return RL.BLAKLEY

        elif (self.state == RL.BLAKLEY):
            print("RL BLAKLEY")
            return RL.RECEIVE

        elif (self.state == RL.RECEIVE):
            if blakley.done:
                print(f'RL RECEIVED: {blakley.result}')
                return RL.OUT
            else:
                print("waiting")
                return RL.RECEIVE

        elif (self.state == RL.OUT):
            print("----RL FINISHED----")
            return RL.IDLE

    def update(self):
        self.counter += 1
        if self.state == RL.BLAKLEY:
            self.waiting = True
        elif (self.state == RL.OUT):
            self.waiting = False





def main():
    clock_period = 1.0

    task_RL = RL_method(Message=10)
    task_Blakley = Blakley_method(A = 1, B = 2)

    for i in range(100):
        # 1. Evaluate all FSMs using their current states
        rl_next = task_RL.compute_next_state(blakley=task_Blakley)
        b_next = task_Blakley.compute_next_state(RL=task_RL)
        # 2. Perform the clocked actions using current states
        task_RL.update()
        task_Blakley.update()
        # 3. Commit all state transitions together
        task_RL.state = rl_next
        task_Blakley.state = b_next
        # 4. Wait until the next rising edge
        time.sleep(clock_period)


main()
