# Cardiovascular Risk Prediction System

A logistic regression model that classifies a user's risk of developing
cardiovascular disease from standard health metrics.

*Built as my A-Level Computer Science NEA (2025–2026). A full write-up,
including methodology and evaluation, is linked below — this README covers
context and setup only.*

---

## Overview

- **Dataset:** ~64,000 patient records
- **Approach:** Data cleaning and feature engineering, followed by logistic
  regression with gradient descent implemented from first principles in
  NumPy — no scikit-learn
- **Result:** ~72.7% classification accuracy on held-out test data

## Why from scratch

The goal of the NEA was to demonstrate understanding of the underlying
mechanics, not to produce the highest possible accuracy — so the model is
implemented without a machine learning library. `NEA_WRITEUP_LINK` covers the
full derivation, design decisions, and evaluation against alternative
approaches.


## Tech

Python, NumPy, Pandas

---

Full write-up: final coursework.pdf
