f(x) = (x % 17 == 3) && (x % 16 == 10) && (x % 15 == 0)
let solutions = [], n = 0
  while length(solutions) < 1
    f(n) && push!(solutions, n)
    n += 1
  end
  solutions
end
