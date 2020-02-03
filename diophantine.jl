function theorem2_9(a, b, c)
  d, r, s = gcdx(a, b)
  rem(c, d) == 0 || throw(DomainError((a = a, b = b, c = c), "gcd($a, $b) = $d does not divide $c; so, no solutions to $(a)x + $(b)y = $c"))
  (
      x0 = r * c ÷ d,
      dx = b ÷ d,
      y0 = s * c ÷ d,
      dy = a ÷ d
  )
end

function diophantine(a, b, c)
  try
      solutions = theorem2_9(a, b, c)
      "$(a)x + $(b)y = $c has solutions x = $(solutions.x0) + $(solutions.dx)t, y = $(solutions.y0) − $(solutions.dy)t; t an integer"
  catch e
      e
  end
end

function diophantine(a, b, c, range)
  try
      solutions = theorem2_9(a, b, c)
      for t in range
          x = solutions.x0 + solutions.dx * t
          y = solutions.y0 - solutions.dy * t
          println((t = t, x = x, y = y))
      end
  catch e
      e
  end
end
