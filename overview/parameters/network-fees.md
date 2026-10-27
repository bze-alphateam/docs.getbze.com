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

# Network Fees

These settings shape the fee every transaction pays, and decide which tokens can pay it. On the BZE Explorer they're under [Fees](https://explorer.getbze.com/parameters#fees).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current ones.
{% endhint %}

## Minimum gas price

**What it does.** Sets the lowest price per unit of gas the network accepts. Your network fee is the gas your transaction uses times the gas price, so this is the floor under every fee on BeeZee. Validators may ask for more, never less.

**Who it affects.** Everyone who sends a transaction.

**At the time of writing:** 0.01 ubze per unit of gas, where 1 BZE is 1,000,000 ubze. A typical transaction using 200,000 gas pays about **0.002 BZE**.

**If you pay in another token.** When your preferred fee token isn't BZE, the network converts this minimum into your token at the current price in its BZE pool, so you pay the same value either way. Fees paid in another token are swapped to BZE behind the scenes and then shared out like any other network fee.

## Minimum BZE liquidity for fee tokens

**What it does.** Decides which tokens can pay network fees. A token qualifies only when its pool with BZE holds at least this much BZE. The same minimum also decides whether the network can swap your token into BZE to cover a feature fee, and whether bridged tokens sent to the burner can be swapped to BZE and burned.

**Who it affects.** Anyone who pays fees in a token other than BZE, and every project that wants its token to work as a fee token.

**At the time of writing:** **100,000 BZE** in the token's BZE pool.

**Why it matters.** Swapping fees through a shallow pool would move its price with every transaction. Asking for deep liquidity keeps fee swaps fair and the token's price steady. If a pool drops below the minimum, the apps switch anyone using that token back to paying in BZE, so their transactions keep working. This setting technically belongs to the DEX, but it's listed here because it's what makes a fee token work.

{% content-ref url="../features/fee-token.md" %}
[fee-token.md](../features/fee-token.md)
{% endcontent-ref %}

{% hint style="success" %}
**For example.** The book club wants members to pay fees in **$PAGE**. Their $PAGE/BZE pool holds 60,000 BZE, so $PAGE doesn't qualify yet. Members add liquidity until the BZE side passes 100,000, and from then on anyone can pick $PAGE as their preferred fee token.
{% endhint %}

## Blocked incoming transfers

**What it does.** Lists specific tokens arriving through specific cross-chain connections that the network refuses. A transfer on that list bounces: it isn't received on BeeZee, and the sending chain refunds the tokens to the sender, so nothing gets lost. Sending tokens **out** of BeeZee is never affected.

**Who it affects.** Only people bridging a token on the list into BeeZee through that one connection. Governance uses it to stop a retired version of a token from arriving, for example after a token has moved to a new bridge route.

**At the time of writing:** one entry: USDC arriving from Noble (the older **USDC.n**), since BeeZee has moved to a different USDC.

## Internal settings

One more setting here is purely technical: a cap on how much fee-conversion work the network does per block, which keeps blocks fast. It doesn't change what you pay.
