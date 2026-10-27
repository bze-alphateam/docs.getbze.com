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

# Tokens

The [Tokens page](https://explorer.getbze.com/tokens) lists every token on BeeZee: BZE itself, the tokens people created on [Factory](../token-factory/README.md), tokens brought in from other networks, and DEX pool shares. Prices come from the BZE DEX.

## The Tokens page

Tiles at the top count the **Tokens on BZE**, how many are **On the DEX**, how many were **Created this month** and how many are **Cross-chain**. Below, filter the list by origin (**All**, **Native**, **Created on Factory**, **Cross-chain**) or type a name into **Find a token**. Each row shows the token, where it comes from, and its price with the 24-hour change. A token paused by governance shows **Halted on the DEX** instead.

## A token's page

Open any token for its full picture.

* **Created … by**: when the token was created and the account that created it.
* **Total supply**, **Holders**, **Price** and **Moved in 24h**: the basics at a glance.
* **The supply box**: a plain answer to the question every buyer should ask, *can more of this token be created?*
  * **The supply of PAGE can change**: the token still has an admin, who can create more or destroy some at any time.
  * **Nobody can create more PAGE**: the admin renounced, so the supply can only go down as holders burn theirs.
  * **The supply is fixed on BZE**: a cross-chain token, minted on its home network; nobody on BeeZee can create more.
  * **The supply grows with inflation**: BZE itself, paid out to stakers every block.
  * **Pool shares follow the pool**: DEX pool shares are created when someone adds liquidity and destroyed when it is taken out.
* **How it got here**: for a Factory token, the history of its admin (handed over, or **Renounced**); for a cross-chain token, the network it came from and the route it took.
* **About**: the description and the number of decimals.
* **Top holders**: who holds the most, with **Show all holders** for the full list.
* **Recent activity**: the latest transfers, mints and burns of the token.

{% hint style="warning" %}
**Same name, different token.** A cross-chain token that reached BeeZee through a third network is not interchangeable with the same coin sent straight from home, even if it carries the same name. Its page warns you about this in an amber box. Check it before you buy or send, so you know which version you are getting.
{% endhint %}

## For token creators

Your token's page is the public proof of everything you promised your community, and a link you can share anywhere.

* **Show you've renounced.** If you renounced your admin rights in [Managing Your Token](../token-factory/managing-your-token.md), the supply box says **Nobody can create more** for everyone to see. It is the strongest trust signal a new token can have.
* **Show your distribution.** **Top holders** lets your community see that the supply isn't sitting in one wallet.
* **Show it's alive.** **Holders**, **Moved in 24h** and **Recent activity** grow as your community uses the token.

{% hint style="success" %}
**Example:** the book club launches $PAGE, adds a BZE pool on the DEX and renounces the admin. Its explorer page now shows a price, a growing holder count and **Nobody can create more PAGE**. That one link answers most of the questions new members will ask.
{% endhint %}

## For traders

Before you buy a token you don't know, open its page and check three things: whether the supply can still change (and who holds the admin), whether a few wallets hold most of it, and whether people actually trade it. Then follow the price to the [DEX](../dex/README.md). To see a trader's open orders, open their account's **Orders** tab (see [Accounts](accounts.md)).

{% content-ref url="governance-and-upgrades.md" %}
[governance-and-upgrades.md](governance-and-upgrades.md)
{% endcontent-ref %}
