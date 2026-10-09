import time
from enum import Enum, auto

def kbit(a, k, i):
    return (a >> (k - 1 - i)) & 1

class RL(Enum):
    IDLE = auto()
    LOOP = auto()
    BLAKLEY = auto()
    RECEIVE = auto()
    OUT = auto()

class BLAKLEY(Enum):
    IDLE = auto()
    LOOP1 = auto()
    LOOP2 = auto()
    OUT = auto()



class Blakley_method:
    def __init__(self, A, B, n, k):
        self.state = BLAKLEY.IDLE
        self.a = A
        self.b = B
        self.n = n
        self.k = k
        self.counter1 = 0
        self.counter2 = 0
        self.result = 0
        self.done = 0
    

    def compute_next_state(self, RL):
        if (self.state == BLAKLEY.IDLE):
            self.result = 0
            self.done = False
            if (RL.waiting):
                return BLAKLEY.LOOP1
            else:
                print("Blakley IDLE")
                return BLAKLEY.IDLE
            

        elif (self.state == BLAKLEY.LOOP1):
            self.result += 2*self.result + kbit(self.a, self.k, self.counter1)
            print(f'BLAKLEY LOOP1 iteration: {self.counter}')

            self.counter1 += 1
            if self.counter1 >= self.k:
                self.counter1 = 0
                return BLAKLEY.OUT
            return BLAKLEY.LOOP2

        elif (self.state == BLAKLEY.LOOP2):
            self.counter2 += 1
            
            if self.result >= self.n:
                self.result -= self.n

            if self.counter2 >= 2:
                return BLAKLEY.LOOP1
            return BLAKLEY.LOOP2
            
        elif (self.state == BLAKLEY.OUT):
            self.done = True
            print("BLAKLEY OUT")
            return BLAKLEY.IDLE
            

class RL_method:
    def __init__(self, Message, key, n):
        self.state = RL.IDLE
        self.P = Message
        self.C = 1
        self.e = bin(key)[2:]
        self.e = self.e[::-1]
        self.h = len(self.e)
        self.k = 0
        self.counter = 0
        self.result = 0
        self.waiting = 0
        self.done = 0

    def compute_next_state(self, blakley):
        if (self.state == RL.IDLE):
            print("--RL IDLE--")
            print("starting loop")
            return RL.LOOP

        elif (self.state == RL.LOOP):
            print(f'RL LOOP iter: {self.counter}')
            if (self.e[self.counter] == '1'):
                self.k = len(bin(self.C)) - 2
                #TODO: Set flag for blakley with C,P,n,k
            else:
                self.k = len(bin(self.P)) - 2
                #TODO: Set flag for blakley with P,P,n,k

            self.counter += 1
            if self.counter > self.h - 1:
                if self.e[-1] == '1':
                    self.k = len(bin(self.C)) - 2
                    #TODO: Set flag RL.BLAKLEY with C,P,n,k
            return RL.BLAKLEY

        elif (self.state == RL.BLAKLEY):
            #TODO: Start blakley with correct inputs
            self.waiting = True

            print("RL BLAKLEY")

            return RL.RECEIVE

        elif (self.state == RL.RECEIVE):
            if blakley.done:
                self.waiting = False
                #if blakley(P,P,n,k):
                self.P = blakley.result
                #elif blakley(C,P,n,k):
                self.C = blakley.result
                print(f'RL RECEIVED: {self.result}')
                return RL.LOOP
            elif self.done:
                self.result = self.C
            else:
                print("waiting")
                return RL.RECEIVE

        elif (self.state == RL.OUT):
            print("----RL FINISHED----")
            print(f'Ciphered message: {self.result}')
            print("-------------------")
            self.result = 0
            return RL.IDLE

        
def main():
    clock_period = 0.1
    success = 0
    task_RL = RL_method(Message=10)
    task_Blakley = Blakley_method(A = 1, B = 2)

    for i in range(100):
        # 1. Evaluate all FSMs using their current states
        rl_next = task_RL.compute_next_state(blakley=task_Blakley)
        b_next = task_Blakley.compute_next_state(RL=task_RL)
#        # 2. Perform the clocked actions using current states
#        task_RL.update()
#        task_Blakley.update()
        # 3. Commit all state transitions together
        task_RL.state = rl_next
        task_Blakley.state = b_next

        # 4. Wait until the next rising edge
        time.sleep(clock_period)
    print(success)


main()
