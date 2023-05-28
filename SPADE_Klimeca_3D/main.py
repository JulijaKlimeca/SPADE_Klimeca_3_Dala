import time
import random

import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


# parliecibas
class Car:
    def __init__(self):
        self.location = (0, 0)
        self.chargelevel = 1.0

    def move_to(self, x, y):
        self.location = (x, y)
        self.chargelevel -= 0.05

    def get_chargestate(self):
        return self.chargelevel

    def set_chargestate(self, charge):
        self.chargelevel = charge


# velmes un nodomi
class SensorActuator:
    def __init__(self):
        self.car = Car()

    def get_car(self):
        return self.car

    #parvietoties uz nejausu vietu
    def move_to_random_location(self):
        new_x = random.randint(0, 9)
        new_y = random.randint(0, 9)
        self.car.move_to(new_x, new_y)


class CarAgent(Agent):
    class CarBehaviour(CyclicBehaviour):
        async def run(self):
            # parliecibas uztversana
            car = self.agent.sensor_actuator.get_car()

            # velmju  veidosana balstoties uz parliecibas

            if car.get_chargestate() > 0:
                # nodoms lai parvietoties
                self.agent.sensor_actuator.move_to_random_location()
                print(f"Agent moved to location: {car.location}")
                print("Battery level: {:.2%}".format(car.get_chargestate()))
                print("-                                                            -")
            else:
                print("Battery is empty, stopping the agent.")
                self.kill()

            await asyncio.sleep(1)

    async def setup(self):
        print(f"Agent {self.jid} started")
        self.sensor_actuator = SensorActuator()

        car_behaviour = self.CarBehaviour()
        self.add_behaviour(car_behaviour)


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


if __name__ == "__main__":

    agent1 = CarAgent("julija1@anonym.im", "julijaklim120202")
    ''' agent2 = CarAgent("agent2@anonym.im", "agent2")
    agent3 = CarAgent("agent3@anonym.im", "agent3")
    agent4 = CarAgent("agent4@anonym.im", "agent4")
    agent5 = CarAgent("agent5@anonym.im", "agent5")
    agent6 = CarAgent("agent6@xmpp.xxx", "agent6")
    agent7 = CarAgent("agent7@xmpp.xxx", "agent7")
    agent8 = CarAgent("agent8@xmpp.xxx", "agent8")
    agent9 = CarAgent("agent9@xmpp.xxx", "agent9")
    agent10 = CarAgent("agent10@xmpp.xxx", "agent10")'''

    print(color.BOLD + 'To STOP the Car agents press ctrl+C' + color.END)
    print("-                                                                                 -")

    future1 = agent1.start()
    future1.result()
    '''
    future2 = agent2.start()
    future2.result()

    future3 = agent3.start()
    future3.result()

    future4 = agent4.start()
    future4.result()

    future5 = agent5.start()
    future5.result()

    future6 = agent6.start()
    future6.result()

    future7 = agent7.start()
    future7.result()

    future8 = agent8.start()
    future8.result()

    future9 = agent9.start()
    future9.result()

    future10 = agent10.start()
    future10.result()
'''

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("  The agent/s are stopped!")

    agent1.stop()
    '''  agent2.stop()
    agent3.stop()
    agent4.stop()
    agent5.stop()
    agent6.stop()
    agent7.stop()
    agent8.stop()
    agent9.stop()
    agent10.stop()'''
