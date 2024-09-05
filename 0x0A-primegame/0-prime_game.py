#!/usr/bin/python3
"""Module that defines the prime game logic.
"""


def isWinner(x, nums):
    """
        Determines the overall winner after playing `x` rounds of a prime-number-based game.
            """
                if x < 1 or not nums:
                        return None
                            marias_wins, bens_wins = 0, 0
                                # Create a boolean list to mark prime numbers up to the largest value in nums
                                    n = max(nums)
                                        primes = [True for _ in range(1, n + 1, 1)]
                                            primes[0] = False
                                                for i, is_prime in enumerate(primes, 1):
                                                        if i == 1 or not is_prime:
                                                                    continue
                                                                            for j in range(i + i, n + 1, i):
                                                                                        primes[j - 1] = False
                                                                                            # Evaluate each round and count the number of primes for each `n` in nums
                                                                                                for _, n in zip(range(x), nums):
                                                                                                        primes_count = len(list(filter(lambda x: x, primes[0: n])))
                                                                                                                bens_wins += primes_count % 2 == 0
                                                                                                                        marias_wins += primes_count % 2 == 1
                                                                                                                            if marias_wins == bens_wins:
                                                                                                                                    return None
                                                                                                                                        return 'Maria' if marias_wins > bens_wins else 'Ben'count % 2 == 1
                                                                                                                            if marias_wins == bens_wins:
                                                                                                                                    return None
count % 2 == 1
                                                                                                                            if marias_wins == bens_wins:
                                                                                                                                    return None
                                                                                                                                        returnreturnreturnupreturn 'Maria' if marias_wins > bens_wins else 'Ben''Ben''Ben''Ben'