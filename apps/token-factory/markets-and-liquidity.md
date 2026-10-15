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

# Getting It Traded

A brand-new token can't be bought until there's somewhere to trade it. The **Get it traded** goals open your token up:

* **Let people buy and sell it**: a **liquidity pool**, for instant swaps.
* **Make trading smoother**: **add liquidity** to a pool, so big trades move the price less.
* **Allow limit orders**: an **order-book market**, where traders name their price.

A pool is all most tokens need. Many projects add a market as well.

## Let people buy and sell it: create a pool

A **liquidity pool** is a shared pot of two tokens that anyone can swap between instantly. Pairing your token with BZE is the usual choice.

1. **Which pair?** Your token and the one it's paired with. Each pair can have only one pool; if it already exists, the app offers **Add liquidity to it** instead. The network stores every pair in alphabetical order, so the app may show your pair the other way round. That's normal.
2. **How much to put in?** The amounts of both tokens. Their ratio sets your token's **starting price**, which the form shows as you type.
3. **Swap fee and where it goes.** The fee charged on every swap: **0.1%**, **0.2%** (the default), **0.3%**, **1%**, or a custom value between 0.1% and 5%. Then choose where the fees go, split between **Providers** (it grows the pool for its liquidity providers), the **Burner** (burned forever) and the community **Treasury**.

{% hint style="warning" %}
**This first deposit stays in the pool for good.** It is the pool's permanent floor: nobody can withdraw it, you included, and you get no LP tokens for it. To add liquidity you can take back later, use **Add liquidity** once the pool exists. The swap fee and where it goes are also fixed when the pool is created.
{% endhint %}

Check **You will pay** (the pool creation fee, read from the network) and select **Create pool**. Swaps can start right away. The success screen shows your pool's **LP token** and offers to **Reward liquidity providers** with a campaign.

## Make trading smoother: add liquidity

Anyone can add to an existing pool, you included, and get **LP tokens** for their share of the pool and the fees it earns. LP tokens can be withdrawn later on the DEX.

1. **Which pool?** The form shows the pool's reserves, its price and your current share.
2. **How much to add?** Deposits follow the pool's ratio: fill in either side and the other is computed for you.
3. **Price protection**: **0.5%**, **1%** (the default) or **3%**. If the price moves more than this before your deposit lands, it is cancelled and nothing is spent.

There is no Token Factory fee, only the network fee. Select **Add liquidity** and the LP tokens arrive in your wallet.

## Allow limit orders: create a market

An **order-book market** lets traders place buy and sell orders on the DEX at the price they choose. Pick the token being traded and the token it's priced in (for example your token, priced in BZE), check the market creation fee, and select **Create market**.

Creating a market is permanent, and every pair can have only one. If it already exists, the app links you to it on the DEX.

## Why pairing with BZE matters

A pool **with BZE** does more than enable swaps. Once your token has a BZE pool behind it, it can be used to **pay network fees**, and newcomers can pick it up in a single swap. To the people using your project, it can feel like BeeZee was built just for them.

{% hint style="success" %}
**For example.** The book club creates a **$PAGE–BZE** pool with the default 0.2% swap fee, sending all the fees to its liquidity providers. With the pool live, new members can grab $PAGE in one click, and they can even pay their fees in $PAGE from then on. Later the club adds a market too, so members can place limit orders.
{% endhint %}

{% content-ref url="../../overview/features/fee-token.md" %}
[fee-token.md](../../overview/features/fee-token.md)
{% endcontent-ref %}

{% content-ref url="growing-your-community.md" %}
[growing-your-community.md](growing-your-community.md)
{% endcontent-ref %}
