#probability  basics
def addition_rule(p_A,p_B,p_A_and_B):
    return p_A + p_B - p_A_and_B
    
def multiplication_rule_independent(p_A,p_B):
    return p_A*p_B
    
def expectation(values,probabilities):
    return sum(v*p for v,p in zip(values,probabilities))
    
print("P(A or B):", addition_rule(0.4, 0.3, 0.1))
print("P(A and B, independent):", multiplication_rule_independent(0.4, 0.3))
print("Expectation:", expectation([0, 1, 2], [0.5, 0.3, 0.2]))