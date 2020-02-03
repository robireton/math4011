function play_game(a, b, verbose = false)
    moves = [a, b] # Keep track of numbers generated
    player = 1 # Player one goes first
    done = false
    while !done
        # Generate the set of all possible moves
        possible_moves = Set()
        for i in moves
            for j in moves
                i == j || push!(possible_moves, abs(i - j)) # differences (other than zero) are moves
            end
        end
        setdiff!(possible_moves, moves) # numbers that have already been generated are not possible moves

        if (length(possible_moves) > 0)
            push!(moves, rand(possible_moves)) # play one of the possible moves
            player = -1 * player # players alternate turns
        else
            done = true
        end
    end
    !verbose || println(moves, " (", length(moves) - 2, " moves)")

    player == 1 ? 2 : 1 # The current player couldn’t move, so the other player wins
end

function compute_game(a, b)
    # compute number of multiples of gcd(a, b) up to larger of a and b
    # if that number is even, player two won, otherwise, player one
    (max(a, b) ÷ gcd(a, b)) % 2 == 0 ? 2 : 1
end

function test_games(a, b)
    games = 0
    agreements = 0

    for a in a:b
        for b in 1:(a - 1)
            games = games + 1
            play = play_game(a, b, true)
            compute = compute_game(a, b)
            if play == compute
                agreements = agreements + 1
            else
                print("\n\n", play, " not equal to ", compute, "\n\n")
            end
        end
    end
    games, agreements
end

test_games(2, 100)
