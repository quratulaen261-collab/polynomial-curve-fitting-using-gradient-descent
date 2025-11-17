# Polynomial Regression using Gradient Descent

## Project Overview
This project demonstrates **polynomial curve fitting** using **gradient descent**.  
We fit a quadratic curve of the form:


to a small dataset. This is a beginner-friendly project to understand how **gradient descent optimizes multiple parameters** to minimize error.

---

## Dataset
We use a small sample dataset (can be easily modified):

| X  | Y     |
|----|-------|
| 1  | 2.2   |
| 2  | 4.8   |
| 3  | 9.1   |
| 4  | 16.3  |
| 5  | 25.5  |

---

## Features
- Implements **gradient descent from scratch**.
- Fits a **quadratic curve** to the data.
- Plots the **original points** and the **learned curve**.
- Displays **learned parameters** (a, b, c).

---

## How it Works
1. Initialize parameters `a`, `b`, and `c`.
2. Compute predictions `y_pred` using the quadratic equation.
3. Calculate **gradients** using Mean Squared Error (MSE) loss.
4. Update parameters using gradient descent.
5. Repeat for a number of **epochs** until convergence.
6. Plot the results.

---

## Installation
Make sure you have Python installed along with the required libraries:

```bash
pip install numpy matplotlib
