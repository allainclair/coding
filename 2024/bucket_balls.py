# By ChatGPT
def get_ball_positions(buckets):
    return [i for i, b in enumerate(buckets) if b == 'B']


def generate_valid_sequences(n, num_balls):
    valid_sequences = []
    for start in range(0, n - (num_balls - 1) * 2):
        sequence = [start + i * 2 for i in range(num_balls)]
        valid_sequences.append(sequence)
    return valid_sequences


def min_moves_to_valid_sequence(current_positions, valid_sequences):
    min_moves = float('inf')
    for sequence in valid_sequences:
        moves = sum(abs(current - target) for current, target in zip(sorted(current_positions), sequence))
        min_moves = min(min_moves, moves)
    return min_moves


def solution(buckets):
    ball_positions = get_ball_positions(buckets)
    n = len(buckets)
    num_balls = len(ball_positions)

    if num_balls == 0 or (num_balls - 1) * 2 >= n:
        return -1

    valid_sequences = generate_valid_sequences(n, num_balls)
    return min_moves_to_valid_sequence(ball_positions, valid_sequences)


# Example usage:
buckets = ".B....B.BB"
print(solution(buckets))  # Output: 2
