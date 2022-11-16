from Agent1 import Agent1
from Agent2 import Agent2
from Agent3 import Agent3
from Agent4 import Agent4
from Agent5 import Agent5
from Agent6 import Agent6
from Agent7 import Agent7
from Agent7faulty import Agent7Faulty
from Agent7faultyfix import Agent7FaultyFix
from Agent8 import Agent8
from Agent8faulty import Agent8Faulty
from Agent8faultyfix import Agent8FaultyFix
from game import run_game
import os
import logging
import numpy as np

class DataCollection():
    dir = "./data/"
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def run_all(self):
        num_agents = 12
        iterations=100
        win = np.zeros(num_agents)
        loss2 = np.zeros(num_agents)
        agent_caught = np.zeros(num_agents)
        for x in range(iterations):
            agents = [Agent1(), Agent2(), Agent3(), Agent4(), Agent5(), Agent6(), Agent7(), Agent7FaultyFix(), Agent8(),  Agent8FaultyFix()]
            victories=[]
            correct_prey_guess={agent:0 for agent in agents}
            correct_predator_guess={agent:0 for agent in agents}
            print(f'iteration {x+1}')
            for agent in agents:
                v, timesteps = run_game(agent)
                victories.append(v)
                prey_guess_rate=agent.correct_prey_guess/timesteps
                predator_guess_rate=agent.correct_predator_guess/timesteps
                correct_prey_guess[agent]+=prey_guess_rate
                correct_predator_guess[agent]+=predator_guess_rate

            for i,victory in enumerate(victories):
                if False not in victory:
                    win[i] += 1
                elif victory[1] == False:
                    loss2[i] += 1
                elif victory[0] == False:
                    agent_caught[i] += 1
        win_string=""
        timeout_string=""
        agent_death=""
        prey_guess=""
        predator_guess=""
        for w, l2, death, agent in zip(win, loss2, agent_caught, agents):
            win_string += f', {w}'
            timeout_string += f', {l2}'
            agent_death += f', {death}'
            prey_guess += f', {correct_prey_guess[agent]}'
            predator_guess += f', {correct_predator_guess[agent]}'
        log_string = win_string[2:]+', , '+timeout_string[2:]+', , '+agent_death[2:]+', , '+prey_guess[2:]+', , '+predator_guess[2:]
        self.logger.info(log_string)

    def init_logger(self):
        log_path = self.dir + 'collecteddata200.csv'
        ch = logging.FileHandler(log_path)
        ch.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(ch)
        return ch

    def collection(self):
        print('Data Collection: ')
        for i in range(1, 31):
            print()
            print(f'-------------------- run {i} --------------------')
            handler = self.init_logger()
            self.run_all()
            self.logger.removeHandler(handler)
        print("-------------------- DONE --------------------")
    
if __name__ == '__main__':
    data_collect = DataCollection()
    data_collect.collection()