import re

def validate_username(username):
    if not isinstance(username, str):
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    if not re.match("^[A-Za-z0-9_]*$", username):
        return False
    return True

def validate_score(score):
    if not isinstance(score, (int, float)):
        return False
    if score < 0:
        return False
    return True

# Example main processing loop
if __name__ == '__main__':
    while True:
        user_input = input("Enter username: ")
        if validate_username(user_input):
            print(f"Username '{user_input}' is valid.")
        else:
            print("Invalid username. Try again.")

        score_input = input("Enter score: ")
        try:
            score_value = float(score_input)
            if validate_score(score_value):
                print(f"Score '{score_value}' is valid.")
            else:
                print("Invalid score. Must be non-negative.")
        except ValueError:
            print("Score must be a number. Try again.")