import copy
import random

class Hat:
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            self.__dict__[k] = kwargs[k]   

            # this creates a dictionary out of the arguments: e.g. {'blue': 4, 'red', 5} if the arguments where (blue=4, red=5)
        

    def get_contents(self):
        contents = []
        for k,v in self.__dict__.items(): # self.__dict__.items() gives you an iterable list of tuples in (k,v) form
            for _ in range(v):
                contents.append(k)
        return contents


    def draw(self, num):
        # create list to hold drawn balls
        balls_drawn = []
        for _ in range(num):
            balls_drawn.append(random.choice(self.get_contents()))
        if len(balls_drawn) > len(self.get_contents()):
            return self.get_contents()
        else:
            return balls_drawn

def experiment(hat, expected_balls, num_balls_to_draw, num_experiments):
    n = 0 # times expected balls equals drawn balls
    for _ in range(num_experiments):
        balls_drawn_list = hat.draw(num_balls_to_draw)
        counter = 0
        for k,v in expected_balls.items():
            counter += 1
            if balls_drawn_list.count(k) < v:
                break
            else:
                if counter == len(expected_balls.items()):
                    n += 1
    return n/num_experiments





hat = Hat(red=2, blue=4, green=6)
print(experiment(hat, {'blue': 2, 'red': 1}, 4, 6000))
# 0.155833333333