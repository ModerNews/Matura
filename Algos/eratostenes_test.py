import unittest
from eratostenes import eratosthenes_sieve, check_prime


class SieveTest(unittest.TestCase):
    def setUp(self):
        self.cases = eratosthenes_sieve(10000)

    def test_sieve(self):
        print(self.cases)
        for i in range(len(self.cases)):
            self.assertEqual(self.cases[i], check_prime(i), i)


if __name__ == '__main__':
    unittest.main()
