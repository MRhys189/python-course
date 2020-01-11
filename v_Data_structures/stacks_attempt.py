from collections import deque
client_orders = deque([])
client_orders = ["James Onys", "Rhys Murage", "Titus Mwangi"]
print(client_orders)
client_orders.append(1)
print(client_orders)
client_orders.pop(1)
print(client_orders)
client_orders.append(0, "Rhys Murage")
print(client_orders)
