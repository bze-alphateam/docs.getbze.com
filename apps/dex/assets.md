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

# Assets Directory

The **Assets** page is BeeZee's token directory: a searchable list of every coin and token on the network. It's the best place to look something up before you trade it.

## Browsing tokens

Search for any token by name or ticker, or scroll the full list. BZE comes first, then verified tokens, then everything else. At the top, four counters give you a feel for the whole network:

* **Total Assets**: every coin and token on BeeZee.
* **Native**: coins that belong to BeeZee itself, starting with BZE.
* **Factory**: tokens created on BeeZee with [Token Factory](../token-factory/README.md), by projects, communities and individuals.
* **IBC**: tokens that come from another blockchain and were moved in through a bridge between chains.

Each token in the list shows its **price**, its **24-hour change**, a tag with its type (**NATIVE**, **FACTORY** or **IBC**), a **Verified** badge where the token has been checked, and a red **Trading halted** badge if trading in it has stopped. Use the arrow on a row to expand its details right in the list, or the link button to copy a link straight to that token.

## Looking at a single token

A token's details give you the full picture:

* **Supply** and **24h Volume**: how much exists (for a bridged token, how much of it is here on BeeZee) and how much traded in the last day.
* **Factory Details**, for Token Factory tokens: the **Creator**, the **Admin** who controls the token today (or **Nobody**), and the supply notice explained below.
* **IBC Details**, for bridged tokens: the **Source Chain** it came from and the technical details of the route it took to BeeZee.
* **Trading Pairs** and **Liquidity Pools**: the order-book markets and pools where the token trades, with their 24-hour volume, so you can jump straight in.

### Who controls the supply

For Token Factory tokens, the supply notice is the single most useful signal on the page, because it tells you whether anyone can still create more of the token:

* **Centralized Supply Control**: the token has an admin who can still mint new tokens, so the supply can grow. That's normal for a young project, but it means you're trusting whoever holds that control.
* **Decentralized Supply**: control has been given up for good. No new tokens can ever be minted, so the supply can never increase.

Token Factory shows the same thing as a badge: **Mintable** matches Centralized Supply Control, and **Fixed supply** matches Decentralized Supply. See [Managing Your Token](../token-factory/managing-your-token.md) for how a creator locks the supply.

{% hint style="warning" %}
A **Verified** badge is a helpful signal, not a guarantee of value. An unverified token isn't necessarily bad, but it's worth a closer look. Check the creator, whether the supply is fixed, the trading volume and where it's paired before you commit, and never trade more than you're comfortable with.
{% endhint %}

{% hint style="success" %}
**For example.** Someone spots a token called **$PAGE** and wants to make sure it's the book club's real one before buying. They open it in Assets, see the **Verified** badge, recognise the creator, notice **Decentralized Supply** (so nobody can quietly print more), and confirm it trades in the $PAGE–BZE pool they expected. Then they swap with confidence.
{% endhint %}

## Trading halted

Very occasionally, BeeZee ends support for a token, and the network stops executing orders and swaps with it. Such a token gets a red **Trading halted** badge on the **Exchange**, **Pools** and **Assets** pages, and its page explains that it's no longer tradeable on BeeZee. From then on:

* **Order forms are locked** on its markets, and orders already in the book won't fill.
* **Swaps skip it**: it disappears from the swap pickers, and routes never go through its pools.
* **New liquidity can't be added** to its pools.

Your funds are never stuck. You can still **cancel your open orders**, **remove your liquidity**, and **transfer or withdraw** the token.

{% hint style="info" %}
If you hold a halted token in an order or a pool, there's no rush and no penalty, but nothing more will happen there. Cancel the orders and remove the liquidity whenever suits you to bring the tokens back to your wallet.
{% endhint %}
