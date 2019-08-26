import random
from collections import namedtuple, deque 
class ReplayBuffer():
    def __init__(self, maxlen=1208*4*10, batch_size=1208*4):
        self.memory = deque()
        self.batch_size = batch_size
        self.experience = namedtuple("Experience",field_names=["state", "action", "reward", "next_state", "done"])
        
    def add(self, state, action, reward, next_state, done):
        e = self.experience(state, action, reward, next_state, done)
        self.memory.append(e)
        
    def sample(self):
        random.shuffle(self.memory)
        random.shuffle(self.memory)
        random.shuffle(self.memory)
        return [self.memory.popleft() for x in range(self.batch_size)]
    
    def __len__(self):
        return len(self.memory)
