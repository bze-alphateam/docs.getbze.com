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

# Accounts

Every BZE address has a page on the explorer. Paste yours into the search box, or use the **View on Explorer** link in any BZE app's wallet panel, to see your own account the way the network sees it. Anyone can look up any address, which is what makes the chain transparent: it also means you can check a project's treasury, a trader's open orders or a validator's owner account before you trust them.

## The account page

At the top: the address with a copy button, when the account was first seen, and what kind of account it is. A **Personal account** belongs to whoever holds its wallet. Well-known accounts get a name, and a validator's owner account links to its validator, for example "owner of Honeycomb".

Four tiles sum up the BZE in it:

* **Available**: BZE you can spend or send, with its US dollar value.
* **Staked**: BZE staked, and with how many validators.
* **Rewards to claim**: staking rewards waiting for you, with a link to claim them in the Staking app.
* **Unstaking**: BZE in its unbonding period, and when the next part unlocks.

## The tabs

### Activity

Everything that happened to the account, newest first, explained in words. Narrow it down with **All**, **Sent**, **Received**, **Staking**, **DEX**, **Rewards**, **Governance**, **Tokens**, **Burner**, **Cross-chain** and **Other**.

Activity includes things that are *not* your own transactions: incoming transfers, rewards paid out to you, a reward program's payouts or a raffle prize. It is the full story of your account, not only what you signed.

**Cross-chain transfers** carry a status, so you can tell at a glance where your coins are:

* **Pending**: sent, waiting for the other network to confirm.
* **Delivered** (outgoing) or **Received** (incoming): it arrived.
* **Expired**: it ran out of time before arriving; your coins come back once the refund goes through.
* **Refunded**: the transfer was rejected or timed out, and your coins came back to you.
* **Rejected**: an incoming transfer that BeeZee turned down; it goes back to where it came from.

{% hint style="success" %}
**Example:** you bridged USDC to BeeZee to buy $GUILD, and your balance hasn't moved yet. Open your account's **Cross-chain** activity: **Pending** means it is still on its way, **Received** means it's there and your app just needs a refresh.
{% endhint %}

### Tokens

Every token the account holds, with its origin (native BZE, created on Factory, or brought in from another network) and balance. Sort them **By value** or **By name**.

### Orders

For traders: the account's open orders on the DEX's order-book markets, grouped by asset. For each asset you see how much is locked **In orders**, and the markets holding it, so you know exactly which orders are tying up your coins. Cancel or change them in the [DEX](../dex/order-book-markets.md).

### Staking

The account's stake, validator by validator: how much, what share of the total, and the rewards waiting at each. Ongoing unstaking is listed with its unlock dates.

## Accounts that belong to the chain

Some addresses don't belong to any person: the community pool, the Burner, the DEX's pools and the like. Open one and the explorer says **This account belongs to the chain, not to a person**. It shows what the account **Holds** (at DEX prices), when its coins move, and **Who can sign** for it: nobody, because no private key exists and only the network's rules move its coins. Its **Holdings** and **Movements** tabs show the detail. You can see every such account on [Chain Parameters](parameters.md).

Addresses that hold coins on behalf of a cross-chain connection show as **Cross-chain escrow**.

{% content-ref url="tokens.md" %}
[tokens.md](tokens.md)
{% endcontent-ref %}
