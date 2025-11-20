class Rules:
    def __init__(self):
        self.rules_list = []

    def apply(self, environment):
        for rule in self.rules_list:
            rule(environment)

# Exemple de règle : redistribution simple
def redistribute(environment):
    total = sum(agent.wealth for agent in environment.agents)
    average = total // len(environment.agents)
    for agent in environment.agents:
        agent.wealth = average
