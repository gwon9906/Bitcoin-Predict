# Bitcoin Price Prediction with Multi-Output CNN-LSTM Model

<p align="center">
  <b>Predict Bitcoin closing prices in USD and KRW with advanced deep learning models</b>
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

## CNN-LSTM Architecture

This model combines the feature extraction power of **Convolutional Neural Networks (CNN)** with the temporal modeling capabilities of **Long Short-Term Memory (LSTM)** layers.


### **Key Components**
- **Input**:
  - Price data (`usd_open`, `krw_open`, etc.).
  - Global trends (`bitcoin`, `coinbase`).
  - Korean trends (`비트코인`, `업비트`).

- **CNN Layers**:
  - Extracts key patterns from price data.
  - Reduces dimensionality using MaxPooling layers.

- **LSTM Layers**:
  - Models sequential dependencies in price and trend data.
  - Separate LSTM layers for Korean and global trends.

- **Fully Connected Layers**:
  - Combines all extracted features.
  - Outputs the predicted `usd_close` and `krw_close`.

- **Outputs**:
  - `usd_close`: Predicted closing price in USD.
  - `krw_close`: Predicted closing price in KRW.

---
