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

# Overview

The BZE Explorer at [explorer.getbze.com](https://explorer.getbze.com/) is BeeZee's own block explorer. Most explorers show you raw data and leave you to decode it. This one is built for people: every transaction says what happened in a sentence, every account shows where its coins are, and the validator pages answer the question delegators actually have: *who can I trust with my stake?*

You don't need a wallet to use it. Paste an address, a transaction or a block number, or just browse. When something you see is worth doing yourself, like staking with a validator or voting on a proposal, the explorer links you straight to the BZE app where you can do it.

{% hint style="info" %}
**Testing on testnet?** The testnet has its own explorer at [testnet-explorer.getbze.com](https://testnet-explorer.getbze.com/). It works exactly the same way, and its links take you to the testnet versions of the BZE apps.
{% endhint %}

## What makes it different

* **A Hall of Fame for validators.** A curated list of the validators that vote on governance, almost never miss a block and came back quickly after the last network upgrade. It is the fastest way to find a validator worth backing. See [Validators Hall of Fame](validators-hall-of-fame.md).
* **Live validator health.** A green or red dot tells you whether each validator is signing blocks right now, and how much stake has flowed in or out of it in the last 24 hours and 7 days. See [Validator Pages](validator-pages.md).
* **Plain-language transactions.** Instead of message codes, you read "Swap 100 BZE → PAGE" or "Join the PAGE raffle · 2 tickets" and see **where the funds went**, step by step. See [Blocks & Transactions](blocks-and-transactions.md).
* **Token pages for creators and holders.** Supply, holders, price, recent transfers, and whether anybody can still mint more. See [Tokens](tokens.md).
* **Upgrade watch.** During a network upgrade, the explorer shows live how much of the network is back and which validators are still missing. See [Governance & Upgrades](governance-and-upgrades.md).
* **The chain's rules, in the open.** Every network setting, read live, with the proposal that last changed it. See [Chain Parameters](parameters.md).

## Finding your way around

The menu at the top takes you to **Blocks**, **Transactions**, **Validators**, **Tokens**, **Proposals** and **Parameters**. The **BZE apps** menu next to it jumps to the DEX, Staking, Burner, Factory and Communities apps.

The home page gives you the pulse of the network: a summary strip with the BZE price, the latest block height, the average block time, transactions in the last 24 hours, how much BZE is staked, the staking reward rate and the number of validators. Below it you see the **Latest blocks** and **Latest transactions** as they arrive, refreshing on their own every few seconds.

## Search

The search box at the top understands what you paste:

* a **block number** opens that block,
* a **transaction hash** opens that transaction,
* a **BZE address** opens that account,
* a **validator address** opens that validator,
* anything else (two characters or more) searches validator names and well-known accounts, so typing part of a validator's name is usually enough.

## The status light

At the bottom of every page, a small light tells you whether the explorer is up to date:

* **Green**: the explorer keeps up with the chain. What you see is current.
* **Red**: the explorer is a little behind. The newest blocks and transactions may be missing for a moment; they fill in on their own.

The light is checked once a minute, and you can hover it to see when it was last checked. If the explorer falls behind, a grey strip under the header says so too, so you never mistake a slow explorer for a stopped network. A paused network looks different: during an upgrade, an orange strip says so and links to the live upgrade watch.

{% hint style="info" %}
**Looking for something very old?** The explorer keeps BeeZee's history from a starting block onward. If you open a block or transaction from before that, the page says so and offers to look it up on Ping.pub, the community explorer.
{% endhint %}

## Pages in this section

{% content-ref url="validators-hall-of-fame.md" %}
[validators-hall-of-fame.md](validators-hall-of-fame.md)
{% endcontent-ref %}

{% content-ref url="validator-pages.md" %}
[validator-pages.md](validator-pages.md)
{% endcontent-ref %}

{% content-ref url="blocks-and-transactions.md" %}
[blocks-and-transactions.md](blocks-and-transactions.md)
{% endcontent-ref %}

{% content-ref url="accounts.md" %}
[accounts.md](accounts.md)
{% endcontent-ref %}

{% content-ref url="tokens.md" %}
[tokens.md](tokens.md)
{% endcontent-ref %}

{% content-ref url="governance-and-upgrades.md" %}
[governance-and-upgrades.md](governance-and-upgrades.md)
{% endcontent-ref %}

{% content-ref url="parameters.md" %}
[parameters.md](parameters.md)
{% endcontent-ref %}
