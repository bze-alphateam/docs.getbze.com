---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Order-Book Markets

Swapping is quick, but sometimes you want to name your own price and wait for the market to come to you. That's what **order-book markets** are for. Instead of trading against a pool, you post buy and sell orders that match with other traders: the classic way to trade, for people who want more control.

## Finding a market

Open the **Exchange** tab to browse every trading pair on BeeZee. You can search by token, and each row shows the **24h Price** (the current price and its 24-hour change) and the **24h Volume**, so you can see what's active at a glance. A **Verified** badge marks pairs where both tokens have been checked, which helps you tell a well-known token from a look-alike; verified pairs are listed first. Pick a pair to open its market.

## On a market page

The top of the page shows the pair's price with its **24h Volume**, **24h High** and **24h Low**. Below that, a market gives you everything you need to trade at your own price:

* **Order Book**: a live list of the sell orders (red, on top) and buy orders (green, below) waiting to be filled, with the last traded price in between. Click any row to drop that price into both order forms, together with the total amount available up to that row.
* **Price Chart**: the pair's history, with timeframes you can switch between to zoom in or out.
* **Buy and Sell forms**: set your **Price**, **Amount** and **Total**, and place your order.

### Placing an order

Each form has three fields that work together:

* **Price**: what you'll pay (or ask) for one token, in the other token of the pair.
* **Amount**: how many tokens you want to buy or sell.
* **Total**: the price times the amount, in the other token: what you'll spend on a buy, or receive from a sell.

Fill in any two and the app works out the third. To use what you have, click a balance in the **Balance** box: your balance of the first token fills **Amount**, and your balance of the second fills **Total**. When that token is also the one you pay fees with, the app keeps the network fee back for you.

If nobody is selling at your buy price (or buying at your sell price), your order **rests in the book** and waits for someone to trade with it.

If your price reaches orders that are already in the book (a buy priced at or above the cheapest sell orders, or a sell at or below the best buy orders), you trade with them straight away, **at their prices, best first**, so you never pay more than those orders ask. When your order reaches several prices, a note under the form tells you which ones it will match ("Match orders with price from … to …"), and only those orders are filled: if you wanted more than they hold, place another order for the rest. When it reaches just one price, whatever those orders can't cover is placed in the book at that price and waits like any other order.

{% hint style="info" %}
**A few things the app checks before your order goes out:**

* **A minimum order size.** Very small orders can't be placed. If yours is too small, the app tells you the minimum for that price.
* **Your balance and the fees.** A buy needs enough of the second token for the total, a sell enough of the first token, and in both cases enough left over for the network and trading fees.
* **A sensible price.** If the app says your price is too high (or too low), bring it closer to the best order in the book.
{% endhint %}

### Your orders and history

Every order that's still waiting shows up under **Your Orders**. Cancel one with its **×** button, or clear the lot with **Cancel All**, and the tokens it held come back to your wallet.

Two tabs keep track of what has filled:

* **Market History**: the latest trades by everyone on this market.
* **My History**: your own trades, so you can see what filled and when.

## Maker and taker fees

The **Trading Fees** box on every market shows what you'll pay. Which fee applies depends on one thing: whether your order waits in the book or fills on the spot.

* A **maker** order rests in the book and adds liquidity for others to trade against. It pays the lower **Maker Fee**, currently 0.001 BZE, as shown in the app.
* A **taker** order fills immediately by taking an order that's already there. It pays the **Taker Fee**, currently 0.1 BZE, as shown in the app.

In plain terms: if you're patient and let your order sit, you pay less; if you want it done *now* and grab an existing order, you pay a little more. Both fees are set by the network and can change, so the app always reads the current values. Click either one for details, including the network fee your order pays on top and what it costs in your chosen fee token.

{% hint style="success" %}
**For example.** A gaming guild's **$GUILD** token trades against BZE. A member thinks it's a touch overpriced today, so instead of swapping they place a **buy** order a little below the current price and let it rest. A while later another trader sells into it, their order fills, and because their order waited in the book, they paid the small maker fee.
{% endhint %}

## Halted markets

If either token of a pair is marked **Trading halted**, the market still opens, but the buy and sell forms are replaced by a red notice: the network no longer executes orders there. Your orders that were already resting won't fill either, so cancel them under **Your Orders** to get your tokens back. See [Trading halted](assets.md#trading-halted).

{% hint style="info" %}
Wallet, buying BZE, bridging tokens in, and fee settings are shared across the apps. See the [Using the Apps](../../using-the-apps/connecting-a-wallet.md) guides. Want to trade a pair that doesn't exist yet? New markets are created in [Token Factory](../token-factory/markets-and-liquidity.md).
{% endhint %}
