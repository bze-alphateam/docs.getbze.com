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

A brand-new token can't be bought until there's somewhere to trade it. On the Token Factory home, pick **Create a DEX market**. The **Choose** screen asks **What kind of market do you want to create?** and compares two options:

* **Liquidity pool** (marked **Most common**): swaps happen instantly at the pool's price, your first deposit sets the starting price, and anyone can add liquidity and earn swap fees. Select **Create liquidity pool**.
* **Order-book market**: a trade happens only when a buy and a sell order match, and buyers and sellers each set their own price. No deposit needed. Select **Create order-book market**.

Both work for any pair of tokens, yours or not, and both cost the same creation fee. Pools suit new tokens best, because anyone can swap from the first minute; order books need people placing orders, so they suit tokens with an active community. Most new tokens start with a pool and add an order book once there are regular traders. Creating either one doesn't make you its owner: anyone can trade on it.

## Create a liquidity pool

A **liquidity pool** is a shared pot of two tokens that anyone can swap between instantly. Pairing your token with BZE is the usual choice.

1. **Pair: which pair?** The **Base token** (yours, for example $PAGE) and the **Quote token** it's paired with (for example BZE). Each pair can have only one pool; if it already exists, the app links you to it on the DEX instead. Halted tokens aren't offered.
2. **Starting amounts: how much goes in first?** The amounts of both tokens. Their ratio sets your token's **starting price**, which the step shows as you type.
3. **Fees: what do swappers pay?** The swap fee charged on every swap: **0.1%**, **0.2%** (the default), **0.3%**, **1%**, or your own value between 0.1% and 5%. Then **where the fees go**, set with a slider or by typing percentages, split between **Providers** (it grows the pool for the people who add liquidity), the **Burner** (burned forever) and the community **Treasury**.
4. **Review**: you pay the creation fee and both starting amounts; you get a liquidity pool anyone can swap in.

{% hint style="warning" %}
**The first deposit stays in the pool forever.** It sets the starting price and becomes the pool's permanent floor: nobody can take it out, you included, and you get no withdrawable share for it. The swap fee and where it goes are also fixed when the pool is created. To add liquidity you can take back later, use the DEX once the pool exists.
{% endhint %}

Select **Create pool** and confirm in your wallet. Swaps can start right away. The Done screen recommends **Add liquidity on DEX**, where you can add liquidity you can take out any time, and has a **Copy pool link** button so you can share the pool.

## Adding and removing liquidity

Adding to a pool and taking your liquidity out both happen on the **DEX**, on each pool's page, for any pool. Token Factory links you there from the home page (**Add or remove liquidity**), from the market Choose screen and from each pool on your token's page.

{% content-ref url="../dex/liquidity-pools.md" %}
[liquidity-pools.md](../dex/liquidity-pools.md)
{% endcontent-ref %}

## Create an order-book market

An **order-book market** lets traders place buy and sell orders at the price they choose.

1. **Pair: which pair?** The **Base token** (what is traded, for example $PAGE) and the **Quote token** (what it is priced in, for example BZE). Each pair can have only one market, whichever way round; if it already exists, the app links you to it on the DEX. Halted tokens aren't offered.
2. **Review**: you pay only the creation fee; there is nothing to deposit. You get an empty order book anyone can trade on.

Select **Create market** and confirm. The Done screen recommends **Open the market on DEX**, to place the first orders so traders see a price, and has a **Copy market link** button to share it.

{% hint style="warning" %}
**A market is permanent.** It can't be deleted, and every pair gets only one. A new market is empty: nothing trades until people place orders, so pairs with a pool usually fill faster.
{% endhint %}

## Why pairing with BZE matters

A pool **with BZE** does more than enable swaps. Once your token has a BZE pool behind it, it can be used to **pay network fees**, and newcomers can pick it up in a single swap. To the people using your project, it can feel like BeeZee was built just for them.

{% hint style="success" %}
**For example.** The book club creates a **$PAGE/BZE** pool with the default 0.2% swap fee, sending all the fees to its liquidity providers. With the pool live, new members can grab $PAGE in one click, and they can even pay their fees in $PAGE from then on. Later the club adds an order-book market too, so members can place limit orders.
{% endhint %}

{% content-ref url="../../overview/features/fee-token.md" %}
[fee-token.md](../../overview/features/fee-token.md)
{% endcontent-ref %}

{% content-ref url="growing-your-community.md" %}
[growing-your-community.md](growing-your-community.md)
{% endcontent-ref %}
