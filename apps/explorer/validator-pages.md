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

# Validator Pages

Validators are the computers that keep BeeZee running, and the people behind them are who you trust when you stake. The BZE Explorer shows more about them than a typical explorer: whether they are signing blocks *right now*, which way their stake is moving, and a plain history of everything that ever happened to them.

## The Validators page

The [Validators page](https://explorer.getbze.com/validators) opens with four tiles about staking as a whole:

* **Staked BZE**: how much BZE is staked, and what share of all BZE that is.
* **Reward rate**: the approximate yearly reward, before a validator's commission.
* **Unstaking takes**: how long your coins stay locked after you unstake (no rewards meanwhile).
* **Top 5 validators hold**: the share of all stake held by the five biggest validators. A healthier network keeps this low.

Below them are three tabs: the [Hall of Fame](validators-hall-of-fame.md), **Active** (the validators producing blocks and paying rewards, biggest first) and **Inactive** (outside the active seats or jailed, so they pay no rewards). Use **Find a validator** to filter any tab by name.

Each row shows the validator's rank, name, stake, commission, **uptime** and how its stake changed recently.

### Online or offline, at a glance

Next to every active validator's uptime sits a small dot:

* **Green**: the validator is signing blocks right now.
* **Red**: it has missed the last 10 blocks in a row or more. Something is wrong on its side.

Hover the dot (or tap it) for the detail, for example "Signed the latest block" or "Missed the last 40 blocks in a row, about 4 minutes", with the last block it signed.

Uptime is the share of the network's recent signing window that the validator signed. It turns red below 99.5%: a validator that keeps slipping can be **jailed**, which stops its rewards and costs the people staked with it a small part of their stake.

{% hint style="warning" %}
**A red dot is your early warning.** Most apps only tell you once a validator is already jailed. The explorer shows you while it is still happening, so you can move your stake before any penalty. Redelegating is instant and keeps your rewards running (see [Managing Your Stake](../staking/managing-your-stake.md)).
{% endhint %}

### Stake changes

The change column shows each validator's **net stake change over the last 24 hours and 7 days**, for example `24h ▲ +122.0K` in green or `7d ▼ −1.64M` in orange. A window with no change is simply left out.

Stake flowing in usually means delegators trust a validator; a steady stream leaving can be a sign others have noticed a problem, a commission hike, or just a big holder rebalancing. It is one more clue, not a verdict: open the validator's page to see who moved what.

## A validator's page

Open any validator to see its full profile. At the top: its name (in gold, with a crown, for [Hall of Fame](validators-hall-of-fame.md) members), its standing, such as **Active · rank 7 of 40**, **Jailed** or **Inactive**, an **Online** or **Offline** tag, how long it has been validating and how many accounts stake with it. Active validators also get a **Stake on Staking** link that opens the Staking app ready to stake with them.

If an active validator is offline, a red **Offline: not signing blocks** note explains how long it has been missing blocks and, if it stays offline, roughly how long before it gets jailed and what that would cost the people staked with it.

### The tiles

* **Staked with them**: its total stake, its share of all staked BZE, and its 24h and 7d change.
* **Commission**: the share of your rewards the validator keeps.
* **Your reward rate here**: the yearly rate you would actually earn with this validator, after its commission.
* **Uptime**: how many of the recent blocks it signed or missed.

### About

The validator's addresses (its validator address and the **Owner account** where its self-stake and commission land), its **Self-stake** (the validator's own money at risk, a good sign of commitment), and its website, description and contact. Open **More details** at the bottom of the page for the **Commission limits**: the highest commission it can ever charge and how much it may raise it per day. Those limits are a promise set when the validator was created, so a low maximum protects you from sudden hikes.

### Recent stake movements

A list of the last 7 days of stake moving in and out: **Delegated**, **Undelegated**, **Moved to** or **Moved from** another validator (named, with a link), **Cancelled unbonding** and the **Initial self-stake**. Each line shows when, the account, the amount and a link to the transaction.

This is where the stake change becomes a story. A single whale moving to a rival tells you something different from fifty small delegators quietly leaving.

### Recent blocks proposed

The latest blocks this validator proposed, and how often it proposes on average, for example "1 in every 8 blocks". Bigger validators propose more often.

### History

Everything that ever happened to the validator, newest first, in plain words: **Created with 5% commission**, **Commission changed from 5% to 10%**, **Renamed to …**, **Joined the active set**, **Jailed: stopped producing blocks**, **Penalised for missing too many blocks**, **Unjailed** and so on. A validator with no jail or penalty gets a reassuring **Never jailed, never penalised since** its start date.

### Last governance votes

How the validator voted on recent proposals (**Yes**, **No**, **Abstain**, **No with veto** or a **Split vote**), each linked to the proposal. If you care how your network is run, back validators that vote the way you would.

{% hint style="success" %}
**A quick checklist before you stake:** green dot, high uptime, a commission you are happy with and a sensible maximum, a clean history, real self-stake, and recent votes. Or start from the [Hall of Fame](validators-hall-of-fame.md), which checks the most important ones for you.
{% endhint %}

{% content-ref url="../staking/staking-your-bze.md" %}
[staking-your-bze.md](../staking/staking-your-bze.md)
{% endcontent-ref %}
