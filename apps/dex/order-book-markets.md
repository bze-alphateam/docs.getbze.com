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

Swapping is quick, but sometimes you want to name your own price and wait for the market to come to you. That's what **order-book markets** are for. Instead of trading against a pool, you post buy and sell orders that match with other traders — the classic way to trade, for people who want more control.

## Finding a market

Open the **Exchange** tab to browse every trading pair on BeeZee. You can search by token, and each row shows the **current price**, its **24-hour change**, and the **24-hour volume**, so you can see what's active at a glance. A **verified badge** marks pairs whose tokens have been checked, which helps you tell a well-known token from a look-alike. Pick a pair to open its market.

## On a market page

A market gives you everything you need to trade at your own price:

* **The order book** — a live list of the buy orders (bids) and sell orders (asks) waiting to be filled. Click any row to drop that price straight into your order form.
* **The price chart** — the pair's history, with timeframes you can switch between to zoom in or out.
* **Buy / Sell forms** — set the **price** you want and the **amount**, and place your order. If it matches an existing order right away, it fills; if not, it rests in the book and waits.

### Your open orders

Any order that's still waiting shows up under your **open orders**, and you can **cancel** it at any time to get your tokens back. Other tabs let you follow the **market's history** (recent trades by everyone) and **your own trades**, so you can keep track of what filled and when.

## Maker and taker fees

Which fee you pay depends on one thing: whether your order waits in the book or fills on the spot.

* A **maker** order rests in the book and adds liquidity for others to trade against — it pays the lower **maker fee** of **0.001 BZE**.
* A **taker** order fills immediately by taking an order that's already there — it pays the **taker fee** of **0.1 BZE**.

In plain terms: if you're patient and let your order sit, you pay less; if you want it done *now* and grab an existing order, you pay a little more.

{% hint style="success" %}
**For example.** A gaming guild's **$GUILD** token trades against BZE. A member thinks it's a touch overpriced today, so instead of swapping they place a **buy** order a little below the current price and let it rest. A while later another trader sells into it, their order fills, and because their order waited in the book, they paid the small maker fee.
{% endhint %}

{% hint style="info" %}
Wallet, buying BZE, bridging tokens in, and fee settings are shared across the apps — see the [Using the Apps](../../using-the-apps/connecting-a-wallet.md) guides. Want to trade a pair that doesn't exist yet? New markets are created in [Token Factory](../token-factory/markets-and-liquidity.md).
{% endhint %}
