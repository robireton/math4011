function theorem2_9(𝑎, 𝑏, 𝑐)
  𝑑, 𝑟, 𝑠 = gcdx(𝑎, 𝑏)
  rem(𝑐, 𝑑) == 0 || DomainError((𝑎 = 𝑎, 𝑏 = 𝑏, 𝑐 = 𝑐), "gcd($𝑎, $𝑏) = $𝑑 does not divide $𝑐; so, no solutions to $(𝑎)𝑥 + $(𝑏)𝑦 = $𝑐")
  (
      𝑥₀ = 𝑟 * 𝑐 ÷ 𝑑,
      𝛿ˣ = 𝑏 ÷ 𝑑,
      𝑦₀ = 𝑠 * 𝑐 ÷ 𝑑,
      𝛿ʸ = 𝑎 ÷ 𝑑
  )
end

function diophantine(𝑎, 𝑏, 𝑐)
  try
      solutions = theorem2_9(𝑎, 𝑏, 𝑐)
      "$(𝑎)𝑥 $(𝑏 < 0 ? '−' : '+') $(abs(𝑏))𝑦 = $𝑐 has solutions 𝑥 = $(solutions.𝑥₀) $(solutions.𝛿ˣ < 0 ? '−' : '+') $(abs(solutions.𝛿ˣ))𝑡, 𝑦 = $(solutions.𝑦₀) $(solutions.𝛿ʸ < 0 ? '+' : '−') $(abs(solutions.𝛿ʸ))𝑡; 𝑡 ∈ ℤ"
  catch e
      e
  end
end

function diophantine(𝑎, 𝑏, 𝑐, range)
  𝑥₀, 𝛿ˣ, 𝑦₀, 𝛿ʸ = theorem2_9(𝑎, 𝑏, 𝑐)
  [(
    𝑡 = 𝑡,
    𝑥 = 𝑥₀ + 𝛿ˣ * 𝑡,
    𝑦 = 𝑦₀ - 𝛿ʸ * 𝑡
  ) for 𝑡 in range]
end
