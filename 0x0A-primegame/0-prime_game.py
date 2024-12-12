#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

def isWinner(x, nums):
    """Determine who wins the most rounds of the game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Get all primes up to n
        primes = sieve_of_eratosthenes(n)
        primes_set = set(primes)  # Using a set for faster lookups

        # Simulate the game
        turn = 0  # Maria starts first
        while primes_set:
            prime = min(primes_set)  # Pick the smallest prime available
            primes_set -= set(range(prime, n + 1, prime))  # Remove prime and its multiples
            
            # Check whose turn it is
            turn = 1 - turn
        
        # Determine winner based on who couldn't make a move
        if turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Return the winner based on who has the most wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

