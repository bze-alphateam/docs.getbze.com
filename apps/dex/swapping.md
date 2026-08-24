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

# Swapping Tokens

Swapping is the simplest way to trade on BeeZee: pick what you have, pick what you want, and the app handles the rest in a single click. It's the home page of the DEX, and for most people it's all they'll ever need.

## Making a swap

1. **Choose your "from" token** — the one you're paying with. The picker is searchable and shows your balances, so you always know what you can spend.
2. **Choose your "to" token** — the one you want to receive.
3. **Enter an amount.** Type how much you want to spend, or use the **Max** button and the **25% / 50% / 75% / 100%** shortcuts to spend part or all of your balance. You can also type the amount you'd like to *receive*, and the app works backwards to fill in the rest.
4. **Confirm.** Your wallet asks you to approve, and the swap settles on the blockchain — no middleman ever holds your funds.

Behind the scenes, your swap trades against **liquidity pools** — shared pots of two tokens that anyone can trade between. The app automatically finds the best path for your trade, and sometimes hops through several pools to get you a better result. When it does, you'll see a **Trade Route** showing the tokens it passed through along the way.

## What you see before you confirm

Swapping is instant, but you're never trading blind. Before you approve, the app shows you:

* **The rate** — how much of the "to" token you'll get for your "from" token.
* **Price impact** — how much your own trade moves the price. Smaller is better; a large number usually means the pool is small relative to your trade.
* **The swap fee** — the trading fee that goes to the pool.
* **A small taker fee** — a flat **0.1 BZE** for trades that fill immediately.

### Max slippage

Prices can move in the moment between quoting your swap and settling it. The **Max slippage** setting is your safety net: if the price moves against you by more than you allow, the swap is cancelled instead of going through at a bad rate. Pick **0.5%**, **1%**, **2%**, or set a custom value. Tighter protection is safer, but in a fast-moving or thinly traded market a very tight setting may cause swaps to fail — loosen it a little if that happens.

{% hint style="success" %}
**For example.** Your book club runs on **$PAGE**. A member wants some to join in, so they open the DEX, choose BZE as the "from" token and $PAGE as the "to" token, tap **50%**, and confirm. The app routes it through the $PAGE–BZE pool and their $PAGE lands in seconds — no need to hunt for a market or set a price.
{% endhint %}

## When a swap can't go through

The app tells you plainly what's happening:

* **Insufficient balance** — you don't have enough of the "from" token for the amount entered. Lower the amount or top up.
* **No route found** — there's no pool (or chain of pools) connecting those two tokens yet. Try a different pair, or someone can create a pool for it in Token Factory.

## Your recent swaps

A **Your Recent Swaps** list keeps a running history of what you've traded, so you can glance back at what went through without leaving the page.

{% hint style="info" %}
Connecting your wallet, buying BZE, and moving tokens in from other chains are shared across all the apps — see the [Using the Apps](../../using-the-apps/connecting-a-wallet.md) guides.
{% endhint %}
