import torch
from torch import nn
import random

def mystery(a, b):
  # Quadratic function: ax² + bx + c where a=2, b=3, c=1
  return torch.tensor(2*a*a + 3*b + 1)

print(mystery(1,1))

model = nn.Sequential(
    nn.Linear(2, 20),
    nn.ReLU(),
    nn.Linear(20, 20),
    nn.ReLU(),
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)
print(model)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for i in range(100000):
  a = random.uniform(-2, 2)  # Wider range for quadratic function
  b = random.uniform(-2, 2)
  desiredOutput = mystery(a,b)

  output = model(torch.tensor([a,b], dtype=torch.float32))
  loss = criterion(output.squeeze(), desiredOutput)

  if(i % 5000) == 0:
    print(f"Loss: {loss.item()}")

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

# Test the trained model with various inputs
test_cases = [(1.0, 1.0), (2.0, -1.0), (0.5, 0.5), (-1.0, 2.0)]

print("\nTesting the trained neural network:")
print("Input (a, b) | Neural Network Output | Expected Output | Error")
print("-" * 60)

for a, b in test_cases:
    output = model(torch.tensor([a, b], dtype=torch.float32))
    expected = mystery(a, b)
    error = abs(output.item() - expected.item())
    print(f"({a:4.1f}, {b:4.1f})    | {output.item():15.6f} | {expected.item():13.6f} | {error:.6f}")

print(f"\nFinal test - Input (1.0, 1.0):")
print(f"Neural Network Output: {model(torch.tensor([1.0, 1.0], dtype=torch.float32)).item()}")
print(f"Expected Output: {mystery(1.0, 1.0).item()}")