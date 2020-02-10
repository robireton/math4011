using Primes

function twinprimes(m)
  results = []
  n = 4
  while length(results) < m
    isprime(n-1) && isprime(n+1) && push!(results, (n-1, n+1))
    n += 2
  end
  results
end
