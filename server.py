import flwr as fl
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--rounds', type=int, metavar='N', default=10)
args = parser.parse_args()

n_rounds = args.rounds

print(f"Numero de rounds: {n_rounds}")

# fraction_fit=0.1,  # Sample 10% of available clients for training
# fraction_evaluate=0.05,  # Sample 5% of available clients for evaluation
# min_fit_clients=10,  # Never sample less than 10 clients for training
# min_evaluate_clients=5,  # Never sample less than 5 clients for evaluation
strategy = fl.server.strategy.FedAvg()

outputs = fl.server.start_server(
    server_address  = '127.0.0.1:9090',
    config          = fl.server.ServerConfig(num_rounds=n_rounds),
    strategy        = strategy
)

print("Output Federated Learning - Loss/Round: ", outputs.losses_distributed)