# Reinforcement Learning Multi-Armed Bandit (MAB)

## Project Structure
```
├── src/                       # Core modules and bandit logic
│   ├── bandits.py
│   ├── advertisementBandit.py
│   ├── advertisementBandit_Solvers.py
│   ├── contentPersonalizationBandit.py
│   └── contentPersonalizationBandit_Solvers.py
├── scripts/                   # Run scripts for experiments
│   ├── run_mab_advertisement.py
│   └── run_mab_personalization.py
├── tests/                     # Unit tests (add your tests here)
├── Results/                   # Output plots and results
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore unnecessary files
└── README.md                  # Project overview and instructions
```

## Getting Started

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run experiments**
   ```bash
   python scripts/run_mab_advertisement.py
   python scripts/run_mab_personalization.py
   ```
   Output plots will be saved in the `Results/` folder.

## Features
- Modular codebase for easy extension
- Advertisement and content personalization bandit solvers
- Epsilon-Greedy, UCB1, Bayesian UCB, and Thompson Sampling algorithms
- Ready for deployment and scaling

## Contributing
- Fork the repo, create a feature branch, and submit a pull request
- Add tests in the `tests/` folder

## License
MIT

```bash
git clone https://github.com/Shastri-727/Reinforcement_learning_MAB.git
cd Reinforcement_learning_MAB
pip install -r requirements.txt
```

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
