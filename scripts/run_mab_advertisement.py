import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from src.advertisementBandit import AdvertisementBandit
from src.advertisementBandit_Solvers import Solver, EpsilonGreedy, UCB1, BayesianUCB, ThompsonSampling

def plot_results(solvers, solver_names, figname):
    assert len(solvers) == len(solver_names)
    assert all(map(lambda s: isinstance(s, Solver), solvers))
    assert all(map(lambda s: len(s.regrets) > 0, solvers))
    b = solvers[0].bandit
    fig = plt.figure(figsize=(14, 4))
    fig.subplots_adjust(bottom=0.3, wspace=0.3)
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    for i, s in enumerate(solvers):
        ax1.plot(range(len(s.regrets)), s.regrets, label=solver_names[i])
    ax1.set_xlabel('Time step')
    ax1.set_ylabel('Cumulative regret')
    ax1.legend(loc=9, bbox_to_anchor=(1.82, -0.25), ncol=5)
    ax1.grid('k', ls='--', alpha=0.3)
    sorted_indices = sorted(range(b.n), key=lambda x: b.probas[x])
    ax2.plot(range(b.n), [b.probas[x] for x in sorted_indices], 'k--', markersize=12)
    for s in solvers:
        ax2.plot(range(b.n), [s.estimated_probas[x] for x in sorted_indices], 'x', markeredgewidth=2)
    ax2.set_xlabel('Actions sorted by true probabilities ' + r'$\theta$')
    ax2.set_ylabel('Estimated probabilities')
    ax2.grid('k', ls='--', alpha=0.3)
    for s in solvers:
        ax3.plot(range(b.n), np.array(s.counts) / float(len(solvers[0].regrets)), ls='-', lw=2)
    ax3.set_xlabel('Actions')
    ax3.set_ylabel('Fraction of # trials')
    ax3.grid('k', ls='--', alpha=0.3)
    plt.savefig(figname)

def experiment(K, N):
    b = AdvertisementBandit(K)
    print("Randomly generated Bernoulli bandit has reward probabilities:\n")
    for element in b.probas: print(f"{element:.4f}")
    print("The best machine has index: {} and probability: {:.6f}".format(
        max(range(K), key=lambda i: b.probas[i]), max(b.probas)))
    test_solvers = [
        EpsilonGreedy(b, eps=0.01),
        UCB1(b),
        BayesianUCB(b, c=3, init_a=1, init_b=1),
        ThompsonSampling(b, init_a=1, init_b=1)
    ]
    names = [
        r'$\epsilon$' + '-Greedy',
        'UCB1',
        'Bayesian UCB',
        'Thompson Sampling'
    ]
    for solver in test_solvers:
        print('Running ' + solver.Name)
        solver.run(N)
    plot_results(test_solvers, names, "../Results/ads_results_K{}_N{}.png".format(K, N))

if __name__ == '__main__':
    experiment(K=10, N=5000)
