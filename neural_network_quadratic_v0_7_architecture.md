# Neural Network Architecture: Quadratic Function Learning

## Network Structure from neural_network_quadratic_v0_7.ipynb

```
Input Layer (2 neurons)     Hidden Layer 1 (20 neurons)    Hidden Layer 2 (20 neurons)    Hidden Layer 3 (10 neurons)    Output Layer (1 neuron)
┌─────────────┐             ┌─────────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────┐        ┌─────────────┐
│     a       │────────────▶│                         │    │                         │    │                     │        │             │
│             │             │  Linear(2 → 20)         │    │  Linear(20 → 20)        │    │  Linear(20 → 10)    │        │  Linear(10 → 1) │
│     b       │────────────▶│  + ReLU Activation      │───▶│  + ReLU Activation      │───▶│  + ReLU Activation  │───────▶│             │
└─────────────┘             └─────────────────────────┘    └─────────────────────────┘    └─────────────────────┘        └─────────────┘
```

## Detailed Architecture

### Layer-by-Layer Breakdown:

1. **Input Layer (2 neurons)**
   - Input: `a` (feature 1)
   - Input: `b` (feature 2)
   - Shape: `[batch_size, 2]`

2. **Hidden Layer 1 (20 neurons)**
   - Operation: `Linear(2 → 20) + ReLU`
   - Weights: `[2, 20]`
   - Bias: `[20]`
   - Activation: ReLU (Rectified Linear Unit)
   - Shape: `[batch_size, 20]`

3. **Hidden Layer 2 (20 neurons)**
   - Operation: `Linear(20 → 20) + ReLU`
   - Weights: `[20, 20]`
   - Bias: `[20]`
   - Activation: ReLU
   - Shape: `[batch_size, 20]`

4. **Hidden Layer 3 (10 neurons)**
   - Operation: `Linear(20 → 10) + ReLU`
   - Weights: `[20, 10]`
   - Bias: `[10]`
   - Activation: ReLU
   - Shape: `[batch_size, 10]`

5. **Output Layer (1 neuron)**
   - Operation: `Linear(10 → 1)`
   - Weights: `[10, 1]`
   - Bias: `[1]`
   - No activation (linear output)
   - Shape: `[batch_size, 1]`

## PyTorch Implementation

```python
model = nn.Sequential(
    nn.Linear(2, 20),    # Input layer: 2 inputs → 20 hidden neurons
    nn.ReLU(),           # Non-linear activation
    nn.Linear(20, 20),   # Hidden layer: 20 → 20
    nn.ReLU(),           # Non-linear activation
    nn.Linear(20, 10),   # Hidden layer: 20 → 10
    nn.ReLU(),           # Non-linear activation
    nn.Linear(10, 1)     # Output layer: 10 → 1 output
)
```

## Training Configuration

- **Loss Function**: MSE (Mean Squared Error)
- **Optimizer**: Adam (learning rate = 0.001)
- **Batch Size**: 32
- **Epochs**: 50
- **Total Parameters**: 2×20 + 20 + 20×20 + 20 + 20×10 + 10 + 10×1 + 1 = **1,031 parameters**

## Data Flow

```
Input: [a, b] (2D vector)
  ↓
Linear(2→20) + ReLU: [20D vector]
  ↓
Linear(20→20) + ReLU: [20D vector]
  ↓
Linear(20→10) + ReLU: [10D vector]
  ↓
Linear(10→1): [1D scalar] → Predicted target value
```

## Target Function

The network learns to approximate: **f(a, b) = 2a² + 3b + 1**

## Performance

- **Test Loss**: 0.044998
- **Training Loss**: 0.046159 (final epoch)
- **Architecture Type**: Feedforward Multi-Layer Perceptron (MLP)
- **Activation**: ReLU (enables non-linear learning of quadratic relationships)
