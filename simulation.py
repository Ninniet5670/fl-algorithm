import flwr as fl
from client import FlowerClient

def start_client(cid):
    return FlowerClient(int(cid)) # ERRO antes, necessitava do ID

strategy = fl.server.strategy.FedAvg()

history = fl.simulation.start_simulation(
    client_fn        = start_client,
    num_clients      = 3,
    config           = fl.server.ServerConfig(num_rounds=5),
    strategy         = strategy,
    # client_resources ={"num_cpus": 1, "num_gpus": 0},
)

# print(history)