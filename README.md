# Stock Analysis App



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
  - [Historical Data Visualization](#historical-data-visualization)
  - [Stock Comparison](#stock-comparison)
  - [Stock Price Prediction](#stock-price-prediction)
  - [KISS Investment Strategy](#kiss-investment-strategy)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)



## Introduction

Stock Analysis App is a comprehensive tool designed for users seeking to make informed decisions in the dynamic world of finance. 
It combines data visualization, comparative analysis, and predictive modeling to provide users with valuable insights for making informed investment decisions.

This app offers a range of features including historical data visualization, stock comparison tools, and price prediction using machine learning. 
It also incorporates a unique "Keep It Simple Strategy" (KISS) feature, allowing users to compare various investment avenues such as gold, real estate, bonds, stock indices, and cryptocurrencies. 
Whether you're a seasoned investor or just starting out, this app provides the tools you need to analyze and understand market trends.



## Features

#### Historical Data Visualization

- Interactive price charts for individual stocks
- Financial bar graphs displaying key metrics
- Easy-to-understand visualizations of historical stock performance

#### Stock Comparison

- Select and compare any two stocks side by side
- Evaluate stocks based on:
  - Price charts
  - Financial metrics
  - Historical returns

#### Stock Price Prediction

- Utilizes LSTM (Long Short-Term Memory) model from Keras for predictive analysis
- Incorporates MinMaxScaler from sklearn for optimization
- Provides stock price predictions based on historical data

#### KISS Investment Strategy

- Utilized upto 10 years of historical data for each investment type
- Cleaned data to handle missing or inconsistent values
- Visualized returns in percentage for easy comparison
- Based on the "Keep It Simple Strategy" principle, this feature compares popular investment avenues like: Gold, Real Estate, Bonds, Stock Indices, BitCoin. 



## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/stock-analysis-app.git

# Navigate to the project directory
cd stock-analysis-app

# Before moving forward make sure you have Python and Pip installed and running
# Install required dependencies
pip install -r requirements.txt
```



## Usage

The Stock Analysis App can be accessed in two ways:

1. **Online Link**
   
   For quick access without any setup, you can use this [Stock Analysis App](https://stockanalysis-ys.streamlit.app/)

2. **Local Installation**

   To run the app on your local machine:

   a. Ensure you have completed the installation steps in the [Installation](#installation) section.
   
   b. Navigate to the project directory in your terminal.
   
   c. Run the following command:

   ```bash
   streamlit run app.py
   ```

   d. Streamlit will start the app and provide output similar to:

   ```
   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501
   Network URL: http://192.168.1.1:8501
   ```

   e. Open the provided Local URL in your web browser to use the app.



## Technologies Used

- Libraries: Pandas, Tensorflow, Scikit Learn, Matplotlib
- APIs: Yfinance, FredAPI, EODAPI
- Streamlit
- GitHub



## Screenshots

Here are some screenshots showcasing the key features of the Stock Analysis App:

### Historical Data Visualization
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sad1.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sad2.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sad3.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sad4.png)
*Caption: Interactive price chart and financial bar graph for individual stocks.*

### Stock Comparison
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadc1.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadc2.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadc3.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadc4.png)
*Caption: Side-by-side comparison of two stocks, showing price trends and key metrics.*

### Stock Price Prediction
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadp1.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadp2.png)
![img](https://github.com/yasarsultan/stockAnalysisApp/blob/main/imgs/sadp3.png)
*Caption: LSTM model predictions for stock prices.*

---

For more information or to report issues, please open an issue on the GitHub repository.
