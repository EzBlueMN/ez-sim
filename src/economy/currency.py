class Token:
    def __init__(self):
        self.balances = {}

    def mint(self, agent_id, amount):
        self.balances[agent_id] = self.balances.get(agent_id, 0) + amount
