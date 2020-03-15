module PrimePlaceNotation

using Primes

export to_ppn, parse_ppn

function to_ppn(𝑛)
    𝑛 == 1 && return "0" # FTA exception
    𝑥 = ""
    𝐹 = factor(𝑛)
    for 𝑝 in primes(𝑛)
        if haskey(𝐹, 𝑝)
            𝑥 *= "$(𝐹[𝑝])"
        else
            𝑥 *= 𝑝 < maximum(keys(𝐹)) ? "0" : ""
        end
    end
    reverse(𝑥) # 2s place on the right
end

function parse_ppn(𝑥)
    𝑠 = reverse("$𝑥") # start with the 2s place
    𝑠 == "0" && return 1 # FTA exception
    𝑛 = 1
    𝑟 = length(𝑠)
    𝑃 = primes(prime(𝑟)) # array of primes ≤ rth prime
    for 𝑖 in 1:𝑟
        𝑘 = Int(𝑠[𝑖]) - Int('0') # value for exponent
        𝑛 *= 𝑃[𝑖]^𝑘
    end
    𝑛
end

end
