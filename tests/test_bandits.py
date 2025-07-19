import unittest
from src.bandits import BernoulliBandit

class TestBernoulliBandit(unittest.TestCase):
    def test_reward_generation(self):
        bandit = BernoulliBandit(3, probas=[0.0, 1.0, 0.5])
        rewards = [bandit.generate_reward(i) for i in range(3)]
        self.assertIn(rewards[0], [0])
        self.assertIn(rewards[1], [1])
        self.assertIn(rewards[2], [0, 1])

if __name__ == "__main__":
    unittest.main()
