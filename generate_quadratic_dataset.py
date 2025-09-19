#!/usr/bin/env python3
"""
Generate quadratic dataset for neural network training.

This script generates training and test datasets for learning the quadratic function:
f(a, b) = 2a^2 + 3b + 1

The datasets are saved as CSV files that can be used by the neural network notebook.
"""

import numpy as np
import pandas as pd
import os

def quadratic_function(a, b):
    """
    Generate the target quadratic function.
    
    Args:
        a, b: Input features
        
    Returns:
        Target value: 2a^2 + 3b + 1
    """
    return 2 * a**2 + 3 * b + 1

def generate_dataset(n_samples, a_range=(-2, 2), b_range=(-2, 2), random_seed=42):
    """
    Generate a dataset for the quadratic function.
    
    Args:
        n_samples: Number of samples to generate
        a_range: Range for feature 'a' (min, max)
        b_range: Range for feature 'b' (min, max)
        random_seed: Random seed for reproducibility
        
    Returns:
        pandas.DataFrame: Dataset with columns 'a', 'b', 'target'
    """
    np.random.seed(random_seed)
    
    # Generate random inputs
    a = np.random.uniform(a_range[0], a_range[1], n_samples)
    b = np.random.uniform(b_range[0], b_range[1], n_samples)
    
    # Calculate targets
    target = quadratic_function(a, b)
    
    # Create DataFrame
    df = pd.DataFrame({
        'a': a,
        'b': b,
        'target': target
    })
    
    return df

def main():
    """Generate training and test datasets."""
    print("Generating quadratic dataset...")
    print("Function: f(a, b) = 2a^2 + 3b + 1")
    print("Input range: a, b ∈ [-2, 2]")
    
    # Generate training dataset
    print("\nGenerating training dataset...")
    train_df = generate_dataset(n_samples=1000, random_seed=42)
    train_df.to_csv('quadratic_train.csv', index=False)
    print(f"✅ Training dataset saved: {len(train_df)} samples")
    
    # Generate test dataset
    print("\nGenerating test dataset...")
    test_df = generate_dataset(n_samples=200, random_seed=123)
    test_df.to_csv('quadratic_test.csv', index=False)
    print(f"✅ Test dataset saved: {len(test_df)} samples")
    
    # Display sample data
    print("\n=== Sample Training Data ===")
    print(train_df.head(10))
    
    print("\n=== Dataset Statistics ===")
    print("Training data:")
    print(train_df.describe())
    
    print("\nTest data:")
    print(test_df.describe())
    
    # Verify the function
    print("\n=== Function Verification ===")
    test_cases = [(1.0, 1.0), (2.0, -1.0), (0.5, 0.5), (-1.0, 2.0)]
    print("Test cases:")
    for a, b in test_cases:
        result = quadratic_function(a, b)
        print(f"f({a:4.1f}, {b:4.1f}) = {result:8.3f}")
    
    print("\n✅ Dataset generation complete!")

if __name__ == "__main__":
    main()

