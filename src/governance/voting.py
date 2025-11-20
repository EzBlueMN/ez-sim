def majority_vote(agents):
    # Simple vote : les agents avec >50 tokens votent "oui"
    votes = [agent.wealth > 50 for agent in agents]
    result = sum(votes) > len(agents)/2
    return result
