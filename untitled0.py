# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:28:19 2024

@author: tomke
"""

def estimate_pi(num_terms):
    result = 0
    sign = 1

    for i in range(1, num_terms * 2, 2):
        result += sign * (1 / i)
        sign *= -1

    estimated_pi = 4 * result
    return estimated_pi

# Example: Estimate pi using 1000 terms
num_terms = 1000
pi_estimate = estimate_pi(num_terms)

print(f"Estimated value of pi using {num_terms} terms: {pi_estimate}")
