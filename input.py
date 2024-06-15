def game_winner(colors):
    def can_remove(color_string, piece):
        return piece*3 in color_string

    current_player = 'wendy'  # Wendy starts the game
    while True:
        if current_player == 'wendy' and can_remove(colors, 'w'):
            colors = colors.replace('www', 'ww', 1)
            current_player = 'bob'
        elif current_player == 'bob' and can_remove(colors, 'b'):
            colors = colors.replace('bbb', 'bb', 1)
            current_player = 'wendy'
        else:
            # No more moves can be made, return the winner
            return 'wendy' if current_player == 'bob' else 'bob'

# Taking input from the user
user_input = input("Enter the string of colors (e.g., 'wwwbbbbwww'): ")
winner = game_winner(user_input)
print(f"The winner is {winner}")
