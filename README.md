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