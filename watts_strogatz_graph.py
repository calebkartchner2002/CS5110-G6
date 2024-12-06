import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

# Create plots directory if it does not exist
os.makedirs("plots", exist_ok=True)

# Parameters
R1, S1, T1, P1 = 1.5, -0.3, 1.8, 0     # Payoffs for Prisoner's Dilemma M1
R2, S2, T2, P2 = 14.5, -0.5, 15, 0     # Payoffs for Prisoner's Dilemma M2

beta_values = [0.1, 0.5]               # Selection intensities for payoff-based strategy
num_nodes = 1000                       # Number of nodes for Watts-Strogatz Network
k_values = [2, 6]                      # Average degree of network for Watts-Strogatz
popularity_factor = 22                 # Average edges per node in Facebook dataset
timesteps = 100                        # Number of turns in each game
num_simulations = 10                   # Number of simulations per condition

# Define the two payoff matrices
M1 = np.array([[R1, S1], [T1, P1]])
M2 = np.array([[R2, S2], [T2, P2]])

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

def plot_cooperation_trends(cooperator_counts_list, strategy_type, matrix_name, k, beta, timesteps, num_simulations):
    """Plot cooperation trends over time and save to a file"""
    plt.figure()
    for sim, cooperator_counts in enumerate(cooperator_counts_list):
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

def calculate_cooperation_decay_stats(cooperator_counts_list, strategy_type, matrix_name, beta, k, num_simulations):
    """Calculate and display stats on the decay of cooperation over time with context."""
    decay_rates = []
    mean_cooperation_levels = []
    
    for cooperator_counts in cooperator_counts_list:
        initial_cooperation = cooperator_counts[0]
        final_cooperation = cooperator_counts[-1]
        decay_rate = (initial_cooperation - final_cooperation) / len(cooperator_counts)
        decay_rates.append(decay_rate)
        
        # Calculate mean percentage of cooperators for this simulation
        mean_cooperation_levels.append(np.mean(cooperator_counts) * 100)  # Convert to percentage
    
    avg_decay_rate = np.mean(decay_rates)
    mean_cooperation = np.mean(mean_cooperation_levels)
    variance_cooperation = np.var(mean_cooperation_levels)
    
    # Print enhanced stats with context
    print(f"Stats for Strategy: {strategy_type.capitalize()}, Matrix: {matrix_name}, Beta: {beta}, k: {k}")
    print(f"  Number of Simulations: {num_simulations}")
    print(f"  Average decay rate of cooperation: {avg_decay_rate:.4f}")
    print(f"  Mean percentage of cooperators: {mean_cooperation:.2f}%")
    print(f"  Variance in percentage of cooperators: {variance_cooperation:.4f}")

# Run simulations and process results for each k value, matrix, and strategy type
for strategy_type in ["payoff", "popularity"]:
    for matrix, matrix_name in [(M1, "M1"), (M2, "M2")]:
        for beta in beta_values:
            for k in k_values:

                # Choose a network to run with
                # network = nx.barabasi_albert_graph(num_nodes, k)
                network = nx.watts_strogatz_graph(num_nodes, k, 0.1)
                
                cooperator_counts_list = [
                    simulate_game(network, matrix, beta, strategy_type=strategy_type, timesteps=timesteps)
                    for _ in range(num_simulations)
                ]
                
                # plot_cooperation_trends(cooperator_counts_list, strategy_type, matrix_name, k, beta, timesteps, num_simulations)
                
                calculate_cooperation_decay_stats(
                    cooperator_counts_list,
                    strategy_type=strategy_type,
                    matrix_name=matrix_name,
                    beta=beta,
                    k=k,
                    num_simulations=num_simulations
                )
