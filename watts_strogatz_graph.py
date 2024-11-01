import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

# Create plots directory if it does not exist
os.makedirs("plots", exist_ok=True)

# Parameters
T, R, P, S = 1.8, 1.5, 0, -0.3         # Payoffs for Prisoner's Dilemma
beta_values = [0.1, 0.5]               # Selection intensities for payoff-based strategy
b, c = 1.8, 0.3                        # Benefit and cost for cooperation
num_nodes = 1000                       # Number of nodes for Watts-Strogatz Network
k_values = [2, 6]                      # Average degree of network for Watts-Strogatz
popularity_factor = 22                 # Average edges per node in Facebook dataset
timesteps = 100                        # Number of turns in each game
num_simulations = 10                   # Number of simulations per condition

# Define the two payoff matrices
M1 = np.array([[R, S], [T, P]])
M2 = np.array([[14.5, -0.5], [15, 0]])

def initialize_strategy(num_nodes):
    """Randomly initialize strategy (1 for cooperate, 0 for defect)"""
    return np.random.choice([0, 1], num_nodes)

def calculate_payoff(strategy, network, matrix):
    """Calculate payoff for each node based on strategy and neighbors"""
    payoff = np.zeros(len(strategy))
    for i in network.nodes:
        for j in network.neighbors(i):
            payoff[i] += strategy[i] * matrix[0][strategy[j]] + (1 - strategy[i]) * matrix[1][strategy[j]]
    return payoff

def fermi_function(payoff_i, payoff_j, beta):
    """Fermi function to model probability of strategy change"""
    return 1 / (1 + np.exp(-beta * (payoff_j - payoff_i)))

def simulate_game(network, matrix, beta, strategy_type="payoff", timesteps=100):
    """Simulate the Prisoner's Dilemma game and record number of cooperators at each turn"""
    strategy = initialize_strategy(len(network))
    cooperator_counts = []
    
    for _ in range(timesteps):
        payoff = calculate_payoff(strategy, network, matrix)
        cooperator_counts.append(np.sum(strategy) / len(strategy))  # Record proportion of cooperators
        
        for i in network.nodes:
            neighbor = np.random.choice(list(network.neighbors(i)))
            
            # Determine beta based on strategy type
            if strategy_type == "popularity":
                beta = network.degree[neighbor] / (len(network) - 1)
            
            if np.random.rand() < fermi_function(payoff[i], payoff[neighbor], beta):
                strategy[i] = strategy[neighbor]  # Update strategy
                
    return cooperator_counts

# Run simulations and plot results for each k value, matrix, and strategy type
for strategy_type in ["payoff", "popularity"]:
    for matrix, matrix_name in [(M1, "M1"), (M2, "M2")]:
        for beta in beta_values:
            for k in k_values:
                # Initialize Watts-Strogatz network
                network = nx.watts_strogatz_graph(num_nodes, k, 0.1)
                
                # Run multiple simulations and plot each
                plt.figure()
                for sim in range(num_simulations):
                    cooperator_counts = simulate_game(network, matrix, beta, strategy_type=strategy_type, timesteps=timesteps)
                    plt.plot(range(timesteps), [count * 100 for count in cooperator_counts], alpha=0.3, label=f'Simulation {sim+1}' if sim == 0 else "")
                
                plt.xlabel('Turn (Timestep)')
                plt.ylabel('Percentage of Cooperators')
                plt.ylim(0, 100)  # Set y-axis to show 0 to 100% scale
                plt.title(f'Cooperation Trends Over Time\n({strategy_type.capitalize()} Strategy, Matrix {matrix_name}, k={k}, Beta={beta})')
                plt.legend(loc='upper right')
                
                # Save plot
                filename = f"plots/{strategy_type}_strategy_{matrix_name}_k{k}_beta{beta}_trends.png"
                plt.savefig(filename)
                plt.close()  # Close figure to free memory

print("Plots saved in the 'plots' directory.")
