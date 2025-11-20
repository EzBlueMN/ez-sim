from src.simulation.agents import Agent
from src.simulation.environment import Environment
from src.governance.rules import Rules, redistribute
from src.governance.voting import majority_vote

# Créer l'environnement et agents
env = Environment()
for i in range(10):
    env.add_agent(Agent(i))

print("=== Initial State ===")
env.summary()

# Simuler quelques étapes
for step in range(5):
    env.step()
    print(f"=== After step {step+1} ===")
    env.summary()

# Appliquer une règle de redistribution
rules = Rules()
rules.rules_list.append(redistribute)
rules.apply(env)

print("=== After Redistribution ===")
env.summary()

# Faire un vote simple
vote_result = majority_vote(env.agents)
print(f"Vote passed: {vote_result}")
