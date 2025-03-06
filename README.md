# Reinforcement Learning-Based Multi-Armed Bandit (MAB) Project

## Overview
This project implements reinforcement learning-based Multi-Armed Bandit (MAB) algorithms to optimize decision-making strategies in two real-world scenarios:

1. **Advertisement Optimization Bandit**: Selecting the best ads to display for maximizing click-through rates.
2. **Content Personalization Bandit**: Recommending personalized content to enhance user engagement.

The project explores different MAB algorithms, balancing exploration (trying new strategies) and exploitation (leveraging known successful strategies) to improve performance over time.

## Why This is Relevant
Multi-Armed Bandit algorithms are widely used in online advertising, recommendation systems, A/B testing, and adaptive clinical trials. By optimizing decision-making, businesses can maximize conversions, enhance user satisfaction, and improve revenue generation. This project demonstrates how reinforcement learning techniques can be applied to practical problems involving uncertainty and real-time decision-making.

## Features
- **Implementation of four MAB algorithms:**
  - Epsilon-Greedy
  - Upper Confidence Bound (UCB1)
  - Bayesian UCB
  - Thompson Sampling
- **Two problem scenarios:**
  - Ad placement optimization
  - Content recommendation for user engagement
- **Performance evaluation using cumulative regret analysis**
- **Visualization of results, including:**
  - Cumulative regret plots
  - Estimated probabilities of actions
  - Action distribution over trials

## Project Structure
```
├── advertisementBandit.py                 # Defines the Advertisement MAB environment
├── advertisementBandit_Solvers.py         # Implements solvers for ad optimization
├── contentPersonalizationBandit.py        # Defines the Content Personalization MAB environment
├── contentPersonalizationBandit_Solvers.py# Implements solvers for content recommendation
├── bandits.py                             # Base Bandit class for both scenarios
├── run_mab_advertisement.py               # Runs experiments on ad optimization
├── run_mab_personalization.py             # Runs experiments on content recommendation
├── ads_results_K10_N5000.png              # Results visualization for ad optimization
├── personalisation_results_K10_N5000.png  # Results visualization for content recommendation
```

## Installation
To run this project, install the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage
Run the experiments for each scenario:

```bash
python run_mab_advertisement.py
python run_mab_personalization.py
```

## Results
The project evaluates different MAB algorithms using cumulative regret analysis. The results are visualized to show how each algorithm balances exploration and exploitation.

- **Best-performing algorithm for advertisement optimization:** Thompson Sampling (lowest cumulative regret)
- **Best-performing algorithm for content personalization:** Thompson Sampling (optimal balance between exploration and exploitation)

## Future Improvements
- Implementing Contextual Bandits to consider user attributes for more personalized recommendations.
- Extending the model to work with real-world datasets for ad placements and content recommendations.
- Deploying the models as an interactive web-based demo.

## Contributions
Contributions are welcome! If you have suggestions for improvements, feel free to fork this repository and submit a pull request.
