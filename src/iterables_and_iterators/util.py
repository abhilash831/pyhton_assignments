from itertools import combinations

def calculate_probability(letters, k):
    all_combinations = list(combinations(letters, k))
    total = len(all_combinations)
    
    with_a = sum(1 for combo in all_combinations if 'a' in combo)
    
    probability = with_a / total
    return f"{probability:.4f}"