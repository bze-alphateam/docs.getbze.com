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

# Liquidity Pools

Every instant swap on BeeZee trades against a **liquidity pool** — a shared pot that holds two tokens so people can swap between them. Anyone can help fill those pots, and when you do, you earn a slice of the fees from every trade that passes through.

## How it works

A pool holds two tokens in balance, say $PAGE and BZE. Traders swap one for the other, and each swap pays a small fee that's added back to the pool. When **you add liquidity**, you put in some of both tokens and receive **LP tokens** — think of them as a receipt for your share of the pool. Your LP tokens grow more valuable as fees pile up, and you can hand them back any time to withdraw your share plus your earnings.

This is also what makes BeeZee's fee-token feature tick: once a token has a healthy pool paired with BZE, that token can be used to pay the network's fees — so a community can run entirely on its own token.

## Browsing pools

The **Pools** tab lists every pool. You can **search** for one, and **sort** by:

* **Liquidity** — how much is in the pool (deeper pools mean smaller price impact on trades).
* **Volume** — how much has traded recently.
* **APR** — an estimate of the yearly return from fees, so you can compare pools at a glance.

A **My Pools** view keeps just the pools you're already in. Open any pool to see its **reserves** (how much of each token it holds), the current **price**, its **total liquidity**, and how the trading fee is split — typically between **liquidity providers** (you), the **protocol**, and **buyback & burn**, which uses part of every fee to buy back and permanently remove tokens from supply.

## Adding liquidity

1. Open the pool and choose **Add liquidity**.
2. Enter an amount for **one** side — the app fills in the matching amount of the other token automatically, to keep the pool balanced.
3. Set your **slippage** tolerance (the same safety net as swapping — it protects you if the price shifts while you deposit).
4. Confirm, and you receive **LP tokens** representing your share.

## Removing liquidity

To withdraw, open the pool, choose **Remove liquidity**, and drag the **percentage slider** to pick how much to take out — from a sliver to all of it. Confirm, and your share of both tokens (including the fees you've earned) comes back to your wallet, and the matching LP tokens are returned.

{% hint style="info" %}
**A word on impermanent loss.** When the two tokens' prices drift apart, the value of your deposit can end up a little lower than if you'd simply held the two tokens on their own. The fees you earn are there to make up for it, but it's an honest trade-off worth knowing before you add liquidity — deep, steady pairs tend to feel it least.
{% endhint %}

## Boost Rewards

Some pools let you go a step further. With **Boost Rewards**, you can **lock your LP tokens** into a reward program to earn **extra token rewards** on top of your normal share of trading fees. Before you commit, the app shows your **estimated daily rewards** and the **unlock period**, so you know exactly what you're signing up for.

{% hint style="warning" %}
**Locking has a lock-up.** While your LP tokens are locked, you can't remove that liquidity, and when you decide to unlock there's a **waiting time** before you get them back. Only lock what you're comfortable leaving in place for the full period.
{% endhint %}

{% hint style="success" %}
**For example.** The book club seeds a **$PAGE–BZE** pool so members can swap in and out easily. A few keen members add liquidity, earn a cut of every trade, and then lock their LP tokens with Boost Rewards to pick up extra $PAGE on top — and because the pool exists, members can now pay their fees in $PAGE too.
{% endhint %}

{% hint style="info" %}
Starting a brand-new pool or market for a token that doesn't have one yet happens in **Token Factory**.
{% endhint %}

{% content-ref url="../token-factory/markets-and-liquidity.md" %}
[markets-and-liquidity.md](../token-factory/markets-and-liquidity.md)
{% endcontent-ref %}
