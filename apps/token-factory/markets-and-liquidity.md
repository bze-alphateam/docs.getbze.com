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

# Markets & Liquidity

A brand-new token can't be traded until there's somewhere to trade it. Token Factory gives you two ways to open your token up to the world: an **order-book market** for hands-on trading, and a **liquidity pool** for instant swaps. Many projects set up both.

## Create a market

A **market** pairs your token with another so the two can be traded against each other — most often **your token vs BZE**. It's an order book: people place buy and sell orders at the prices they choose, and matching orders trade.

Just pick the two tokens for the pair and confirm. The app checks that the same pair doesn't already exist and won't let you create a duplicate — one market per pair keeps trading tidy and liquidity in one place.

## Create a liquidity pool

A **liquidity pool** is a shared pot of two tokens that anyone can swap between instantly, with no order to place and no counterparty to wait for. Seeding one for your token is what makes those effortless one-click swaps possible.

When you create a pool you set:

* **The two tokens** and how much of each to seed it with. The starting amounts set the opening price.
* **The swap fee** — the trading fee paid on every swap through the pool. Choose **0.1%**, **0.2%**, **0.3%**, **1%**, or set a **custom** value. Lower fees attract more trades; higher fees earn more per trade.
* **The fee split** — how that fee is divided up. You decide the shares that go to the pool's **liquidity providers** (the people who supply tokens to the pool), to the **burner** (permanently removing tokens from circulation), and to your own **treasury**.

{% hint style="warning" %}
**The first liquidity is locked forever.** When a pool is created, the very first batch of **LP tokens** — the receipts that represent a share of the pool — is permanently burned rather than given to anyone. This is deliberate: it leaves a small, permanent floor of liquidity that can never be pulled out, so the pool can't be fully drained and simply vanish. It's a one-time, irreversible cost of opening a pool, and it protects everyone who trades or provides liquidity afterwards.
{% endhint %}

## Add liquidity

Once a pool exists, anyone can **add liquidity** to it — including you, topping up your own. You deposit both tokens and receive **LP tokens** in return, representing your share of the pool and the fees it earns.

* **Ratio-locked inputs.** You add the two tokens in the pool's current proportion, so when you type an amount for one side the app fills in the matching amount for the other. This keeps the pool balanced.
* **Slippage setting.** A pool's ratio can shift in the moment while your deposit settles. A slippage setting protects you: if it moves more than you allow, the deposit is cancelled instead of going through on worse terms.

## Why pairing with BZE matters

Giving your token a pool **with BZE** does more than enable swaps. It's also the key that unlocks one of BeeZee's signature ideas: once your token has a BZE pool behind it, your token can be used to **pay network fees**, and newcomers can pick it up in a single swap. To people using your app, it can feel like BeeZee was built just for your project.

{% hint style="success" %}
**For example.** The book club creates a **$PAGE–BZE** market so members can place orders, then seeds a **$PAGE–BZE** pool with a 0.3% swap fee for instant swaps. With that pool live, new members can grab $PAGE in one click — and they can even pay their fees in $PAGE from then on.
{% endhint %}

{% content-ref url="../../overview/features/fee-token.md" %}
[fee-token.md](../../overview/features/fee-token.md)
{% endcontent-ref %}
