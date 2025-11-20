class Agent:
    def __init__(self, agent_id, wealth=100):
        self.id = agent_id
        self.wealth = wealth

    def act(self, environment):
        # Exemple simple : l'agent donne 1 token à un autre agent aléatoire
        import random
        if self.wealth > 0:
            receiver = random.choice(environment.agents)
            if receiver.id != self.id:
                self.wealth -= 1
                receiver.wealth += 1
