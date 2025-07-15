# Multi-Armed Bandits for Advertisement and Content Personalization

This repository contains implementations and experiments on multi-armed bandit (MAB) algorithms for two classic web applications:
- **Online Advertisement Placement**
- **Content Personalization**

The project compares the performance of several popular bandit algorithms on simulated environments representative of these applications, allowing you to evaluate strategies such as ε-Greedy, UCB1, Bayesian UCB, and Thompson Sampling.

## Table of Contents

- [Overview](#overview)
- [Bandit Modules](#bandit-modules)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage](#usage)
  - [Advertisement Bandit](#advertisement-bandit)
  - [Content Personalization Bandit](#content-personalization-bandit)
- [Results](#results)
- [File Structure](#file-structure)
- [License](#license)

## Overview

Multi-armed bandit algorithms are crucial for sequential decision-making where exploration–exploitation trade-offs arise. This repository demonstrates how core algorithms perform in scenarios like ad click-through optimization and personalized content recommendation.

## Bandit Modules

- **AdvertisementBandit:** Models online ad placements, with each arm representing a different ad slot, each having an unknown probability of reward (click).
- **ContentPersonalizationBandit:** Models different content categories for personalization, each with an unknown engagement probability.

## Algorithms Implemented

- **ε-Greedy:** Explores randomly with probability ε, otherwise exploits the current best arm.
- **UCB1 (Upper Confidence Bound):** Balances exploration and exploitation using confidence intervals.
- **Bayesian UCB:** Uses Bayesian inference with a Beta prior.
- **Thompson Sampling:** Selects arms according to their probability of being optimal, estimated via posterior sampling.

## Installation

Clone this repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/multi-armed-bandits.git
cd multi-armed-bandits
pip install -r requirements.txt
```

**Requirements** (ensure these are present in `requirements.txt`):
- `numpy`
- `matplotlib`

## Usage

Each experiment simulates a multi-armed bandit problem and compares the cumulative regret, probability estimation, and action distribution for each solver.

### Advertisement Bandit

To run the advertisement placement simulation:

```bash
python run_mab_advertisement.py
```

### Content Personalization Bandit

To run the content personalization simulation:

```bash
python run_mab_personalization.py
```

The scripts will print details about the experiments and save plots comparing algorithm performance.

## Results

After running the experiments, the scripts will generate figures illustrating:

1. **Cumulative Regret:** As a function of time—lower regret means better performance.
2. **Estimated Probabilities:** Compare estimated to true reward probabilities.
3. **Action Frequency:** Distribution of how often each arm (ad/content) was selected.

Plots will be saved in the project directory as:
- `ads_results_K10_N5000.png`
- `personalisation_results_K10_N5000.png`

## File Structure

| File                                  | Description                                              |
|----------------------------------------|----------------------------------------------------------|
| `bandits.py`                          | Abstract and base classes for bandit problems            |
| `advertisementBandit.py`               | Advertisement bandit environment                         |
| `advertisementBandit_Solvers.py`       | Solvers for the advertisement bandit                     |
| `contentPersonalizationBandit.py`      | Content personalization bandit environment               |
| `contentPersonalizationBandit_Solvers.py` | Solvers for the content personalization bandit         |
| `run_mab_advertisement.py`             | Script to run ad bandit experiments and plot results     |
| `run_mab_personalization.py`           | Script to run content bandit experiments and plot results|
