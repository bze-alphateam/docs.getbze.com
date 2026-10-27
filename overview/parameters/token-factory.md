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

# Token Factory Parameters

Creating a token has one network setting of its own. On the BZE Explorer it's under [Factory](https://explorer.getbze.com/parameters#factory).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current ones. Token Factory always reads the current fee and shows it on the review step.
{% endhint %}

## Token creation fee

**What it does.** A flat fee for creating a new token, paid once when you create it.

**Who it affects.** Anyone creating a token. Holding, sending, minting more of, or managing an existing token doesn't pay it.

**At the time of writing:** **25,000 BZE**, or the same value in your preferred fee token.

**Where it goes.** The community pool.

**Why it exists.** A token is a permanent entry on the network. The fee keeps BeeZee free of spam and copycat tokens, so the ones you find have someone behind them, and it funds the community that keeps the network growing.

## What else you might pay

Creating a token is usually the first step of a launch, and the next steps carry fees of their own:

* **Opening a pool or a market** for your token costs the market and pool creation fee. See [DEX Parameters](dex.md).
* **Starting a reward** for your token's holders or liquidity providers costs a reward creation fee. See [Rewards Parameters](rewards.md).
* **Running a burning raffle** has no feature fee; you only fund its starting pot. See [Burner Parameters](burner.md).

{% content-ref url="../../apps/token-factory/creating-a-token.md" %}
[creating-a-token.md](../../apps/token-factory/creating-a-token.md)
{% endcontent-ref %}
