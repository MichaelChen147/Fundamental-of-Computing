#  This computes the primes less than n by a process known as the Sieve of Eratosthenes.
n = 10
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]

print len(results)
