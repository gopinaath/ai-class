import random
import pandas as pd

def linear_function(a, b):
    """Linear function: f(a, b) = 3a + 4b"""
    return 3*a + 4*b

def generate_dataset(num_samples=1000, seed=42):
    """Generate dataset for the linear function"""
    random.seed(seed)
    
    # Generate random inputs
    a_values = [random.random() for _ in range(num_samples)]
    b_values = [random.random() for _ in range(num_samples)]
    
    # Calculate target outputs
    targets = [linear_function(a, b) for a, b in zip(a_values, b_values)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'a': a_values,
        'b': b_values,
        'target': targets
    })
    
    return df

if __name__ == "__main__":
    # Generate training dataset
    print("Generating linear function dataset...")
    train_df = generate_dataset(num_samples=1000, seed=42)
    
    # Generate test dataset
    test_df = generate_dataset(num_samples=200, seed=123)
    
    # Save datasets as CSV
    train_df.to_csv('linear_train.csv', index=False)
    test_df.to_csv('linear_test.csv', index=False)
    
    print("Dataset generation complete!")
    print(f"Training samples: {len(train_df)}")
    print(f"Test samples: {len(test_df)}")
    
    # Show a few examples
    print("\nFirst 5 training examples:")
    print(train_df.head())
    
    print(f"\nFiles created:")
    print(f"- linear_train.csv ({len(train_df)} samples)")
    print(f"- linear_test.csv ({len(test_df)} samples)")
