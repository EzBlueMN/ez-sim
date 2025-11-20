class Environment:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        for agent in self.agents:
            agent.act(self)

    def summary(self):
        for agent in self.agents:
            print(f"Agent {agent.id}: {agent.wealth} tokens")
