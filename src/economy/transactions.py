def transfer(token, sender_id, receiver_id, amount):
    if token.balances.get(sender_id,0) >= amount:
        token.balances[sender_id] -= amount
        token.balances[receiver_id] = token.balances.get(receiver_id,0) + amount
        return True
    return False
