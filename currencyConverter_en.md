# Currency Converter Challenge - CSGames 2023

## Context

Since the trust in banks has been shattered and cooperation between the new inhabitants is necessary, the commitee has decided that every currency must be accepted and converted automatically free of charge. This is to garantee equality and facilitate transactions to have continuity in the economy. 

## General overview

You and your team must create a program that allows rapid and easy conversion of currency. This program will include a GUI to permit users to easily interact and see the conversion of various different currencies. You will need to use an API to get the current value of the various currencies and then convert the currency selected by the user to other currencies.

## Comptetition value

`500 points`

## Tasks

This program must be written in **Python**

### GUI

For the GUI portion of this project, **you must use the tkinter library** : [tkinter](https://docs.python.org/3/library/tkinter.html)

- Create a window for the GUI of the application (30 points)
- Add a logo (10 points)
- Use a custom font (10 points)
- Create a heading (10 points)
- Allow a user to select a source and target currency from a list (40 points)
- Add a function to allow a user to display a greater number of target currencies for easy consulting (30 points)
- Integration of the *Atlantis* theme (20 points)
- General design and presentation (80 points)

### API

You must use the **ExchangeRate API** for conversion of regular currencies : [ExchangeRate API](https://www.exchangerate-api.com/)

- Use the ExchangeRate API to get currency information (20 points)
- Create a function that allows to get currency codes (30 points)
- Create a function that allows currency conversion (30 points)

#### Cryptocurrency

Crypto currencies took a lot of importance after the rich betrayed humanity and the banks shut down. Include a way to convert crypto currencies. You can use whichever API you wish for this but we recommend [CoinAPI](https://www.coinapi.io/). Careful, the free tier is limited to 100 transactions per key.

- Use an API to get the value of various crypto currencies (20 points)
- Allow users to convert between various crypto currencies (20 points)
- Allow users to convert between regular and crypto currencies (60 points)

### General

- Project runs without modifications (20 points)
- Code is clean and commented (20 points)
- Code in accordance to standard practices and following the Python Style guide (20 points)
- Provide a README with clear instructions on how to run and use your program (30 points)
