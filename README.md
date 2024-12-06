# Bitcoin Price Prediction with Multi-Output CNN-LSTM Model

<p align="center">
  <img src="https://example.com/logo.png" alt="Project Logo" width="200">
</p>

<p align="center">
  <b>Predict Bitcoin closing prices in USD and KRW with deep learning</b>
</p>

---

## Features

<table>
  <tr>
    <th>Feature</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Multi-Input</td>
    <td>Uses price data, global trends, and Korean trends as input features.</td>
  </tr>
  <tr>
    <td>Multi-Output</td>
    <td>Predicts Bitcoin closing prices in both USD and KRW simultaneously.</td>
  </tr>
  <tr>
    <td>Architecture</td>
    <td>Combines CNN and LSTM layers for feature extraction and sequential modeling.</td>
  </tr>
</table>

---

## Model Architecture

<p align="center">
  <img src="https://example.com/model-architecture.png" alt="Model Architecture" width="600">
</p>

- **Input**:
  - Price data (`usd_open`, `krw_open`, etc.).
  - Global trends (`bitcoin`, `coinbase`).
  - Korean trends (`비트코인`, `업비트`).
- **Layers**:
  - Convolutional and MaxPooling layers for price data.
  - LSTM layers for trend data.
- **Outputs**:
  - `usd_close`: Predicted closing price in USD.
  - `krw_close`: Predicted closing price in KRW.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
