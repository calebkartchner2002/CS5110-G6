# CS5110-G6

## Popularity-Based Approach to Promote Cooperation in The Prisoner’s Dilemma Game

### **Information on the Research Paper**

#### Introduction:
*   The **Prisoner's Dilemma** is a classic problem in game theory, widely used to study how cooperative behavior emerges and evolves in different settings. It has been applied across various disciplines, including economics, biology, and social sciences. 
*   We are building on existing research that investigates how **popularity-based strategies** can influence cooperation, particularly in networked environments like social networks. The previous study compared synthetic and real-world networks to explore how popularity impacts **cooperative behavior**.

#### Background:
*   Previous studies in this field have primarily focused on how network structures and payoff mechanisms influence cooperation. For example, a **payoff-based strategy** involves players making decisions based on their neighbors’ payoffs.
*   What sets this research apart is its consideration of **popularity**, using 'degree centrality' to measure how the number of connections—or popularity—of a player impacts their decision to cooperate or defect.
*   **Degree centrality** is simply a measure of how many connections a player has in a network. In other words, it gauges how 'popular' a player is based on the number of direct connections they have with others.

#### Proposed Model
*   **Payoff-Based Strategy:** Players adjust their decisions based solely on the payoffs of their neighbors, favoring strategies that yield higher individual rewards.
*   **Popularity-Based Strategy:** Players are more likely to imitate neighbors with higher degree centrality, emphasizing social influence and the appeal of popularity in decision-making.

#### Experimental Setup and Results
*   **Networks Used:** Simulations were conducted on a Watts-Strogatz synthetic network and a real-world Facebook dataset.
*   **Simulations:** Multiple runs were performed, varying the selection intensity parameter (𝛽) to examine its effect on strategy adoption.
*   **Fermi Function:** A probabilistic model used to describe decision-making in strategy switching. It calculates the probability of a player adopting a neighbor’s strategy based on payoff differences. If a neighbor has a higher payoff, the likelihood of switching to the neighbor’s strategy increases:
    *   The function incorporates a parameter (𝛽) that controls sensitivity to payoff differences. A higher 𝛽 makes players more responsive to payoff disparities, increasing the likelihood of imitating successful strategies. Conversely, a lower 𝛽 reduces sensitivity, resulting in more random and less payoff-driven strategy adoption.
*   **Key Results:** Cooperation emerges and stabilizes more effectively in real-world networks when popularity (degree centrality) is considered, with network connectedness significantly influencing outcomes.

### **Modifications to the Simulation**

*   Varying the Rewiring Probability in the Watts-Strogatz Graph:
    *   **Experiment with different rewiring probabilities** (the third parameter in nx.watts_strogatz_graph(num_nodes, k, rewiring_probability)). By changing this probability, you can investigate how the similarity of agent connections (local clustering and network structure) affects cooperation. Lower rewiring probabilities (e.g., 0.1) result in a more regular, lattice-like structure with less randomness in connections, while higher probabilities introduce more randomness, creating a more randomized network. This could help explore how the degree of network randomness influences the emergence of cooperation in the population.

*   Modifying Popularity's Influence on Strategy Switching:
    *    **Alter the relationship between popularity and strategy switching**, such that agents who are more popular (i.e., have a higher degree) are less sensitive to payoff differences and more likely to adopt the strategy of their popular neighbors regardless of payoff. You can do this by adjusting the decision-making rule, where agents with a higher degree may focus less on the payoff differences and more on the social influence from their popular neighbors. For instance, you could implement a rule where popular agents have a fixed tendency to switch strategies based on the popularity of their neighbors, even if it doesn't necessarily lead to a higher payoff. This would explore the impact of social influence and popularity in the absence of payoff-based considerations.

*   Printing Numerical Results of Cooperation Trends:
    *   **Log and print the numerical results** of cooperation at the end of each simulation, rather than relying solely on graphical output. After each simulation, you can calculate and print the average proportion of cooperators over all timesteps or at specific intervals. This will allow for a more quantitative analysis of how cooperation evolves over time and how it compares across different experimental conditions (e.g., varying rewiring probabilities or popularity effects). For example, you could print the average cooperation rate for each condition (strategy type, matrix, 𝛽, and network structure) at the end of each simulation or timestep, and then aggregate the results across multiple simulations for a summary output. This approach would give a clearer numerical comparison of different strategies and network configurations.

### **Cooperation Statistics**

*   Average Decay Rate of Cooperation (avg_decay_rate):
    *   **What it means:** This is the average decrease in the proportion of cooperators per timestep across all simulations. It provides a single summary number to indicate how fast cooperation generally declines over time in the game.
    *   **Interpretation:** A higher positive value indicates that cooperation is decreasing quickly. A lower value (close to zero) means cooperation remains relatively stable over time.

*   Mean Percentage of Cooperators and Variance:
    *   **What it means:** The mean percentage of cooperators is the average proportion of nodes cooperating over all timesteps and all simulations. It provides a summary measure of how cooperative the population remains, on average. The variance quantifies the variability in cooperation levels across simulations, reflecting how consistent or unpredictable cooperation levels are.
    *   **Interpretation:** A high mean indicates a tendency for the population to sustain cooperation, while a low mean suggests cooperation is rare or frequently collapses. A low variance indicates that cooperation levels are similar across simulations, suggesting stability under the given parameters. A high variance implies significant differences in cooperation trends, potentially due to network topology, strategy variability, or randomness in the simulation.