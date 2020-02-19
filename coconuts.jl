function f(x)
  C₀ = x
  if C₀ % 5 == 1
    C₁ = 4 * (C₀ - 1) ÷ 5
    if C₁ % 5 == 1
      C₂ = 4 * (C₁ - 1) ÷ 5
      if C₂ % 5 == 1
        C₃ = 4 * (C₂ - 1) ÷ 5
        if C₃ % 5 == 1
          C₄ = 4 * (C₃ - 1) ÷ 5
          if C₄ % 5 == 1
            C₅ = 4 * (C₄ - 1) ÷ 5
            if C₅ % 5 == 0
              println((C₀, C₁, C₂, C₃, C₄, C₅))
              return true
            else
              return false
            end
          else
            return false
          end
        else
          return false
        end
      else
        return false
      end
    else
      return false
    end
  else
    return false
  end
end

function f₁(x)
  q, r = divrem(x, 5)
  if r == 1
    println((q = q, c = 4q))
    return 4q
  end
  return 0
end

let solutions = [], n = 1
  while length(solutions) < 1
    f(n) && push!(solutions, n)
    n += 1
  end
  println(solutions)
end
