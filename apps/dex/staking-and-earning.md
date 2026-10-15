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

# Staking & Earning

The DEX isn't only for trading. Its **Staking** tab opens **Staking & Rewards**, one page for every way to put your tokens to work and earn while you hold them. At the top you'll see your **Total Value Staked**, how many **Active Stakes** you have and your **Unclaimed Rewards**, and a search box to find a token's opportunities quickly.

The page has three kinds of earning, from top to bottom.

## BZE Native Staking

The first card is staking BZE itself. Validators are the machines that keep the BeeZee network running. When you stake (delegate) your BZE to one, you help secure the chain and earn a share of the rewards it produces, including the new BZE created by inflation. Your BZE never leaves your control: you're lending your vote of confidence, not handing it over.

The card shows the current **APR**, **Your Stake**, your **Rewards** waiting to be collected, any **Pending Unlock** (BZE on its way back to you, with the date it arrives), and the unlock period. Select the card for its actions:

* **Claim** collects your BZE staking rewards right here in the DEX.
* **Stake** and **Unstake** open the [Staking](../staking/README.md) app, which is built for choosing validators and managing your delegations.

## Staking programs

Next come the **staking programs**: campaigns, each with an end date, where you stake one token and share a daily prize paid in another (or the same) token. Programs for LP tokens are the [Boost Rewards](liquidity-pools.md#boost-rewards) of the liquidity pools, so you'll find them here too.

Each card shows whether the program is **Running**, **Finished** or **Waiting for stakers**, its estimated **APR** (a yearly rate, based on current conditions) and four numbers: **Unlock** (the waiting time after you unstake), **Daily** (how much is shared out each day), **Minimum** (the smallest stake it accepts) and **Total** (how much everyone has staked). Select a card for **Stake**, **Unstake** and **Claim**:

* **Stake** shows your **Estimated Daily Rewards** before you select **Confirm Stake**.
* **Unstake** shows an **Unstaking Notice** with how many days your tokens stay locked before they come back.
* **Claim** collects the rewards you've earned so far.

## Denom rewards

At the bottom, **Denom rewards** lists every token's **holders pool**: stake a token into its own pool and earn the prizes **anyone** funds for it, either a **daily** prize or one-off **airdrops**. The token's team, its fans or its partners can all add to the prizes. Each card is called **Stake TICKER, earn prizes** and is labelled **Paying daily** or **No daily schedule — airdrops only**.

A card shows what the pool **Pays per day**, its **Total staked**, how long the **Unlock** takes (or **Instant**), and its **Minimum** stake. Once you've joined, it also shows **Your stake** with your estimated share per day, and your **Pending prizes**.

* **Stake** joins the pool (the button becomes **Add** once you're in). Adding more pays out your pending prizes first, in the same transaction.
* **Claim** collects your pending prizes. Your stake stays in and keeps earning.
* **Claim all denom rewards** appears at the top of the section whenever you have prizes waiting, with the number of pools in brackets, and collects them all in one transaction.
* **Exit** pays out your pending prizes, then releases your **whole** stake. Exiting is all or nothing; there's no partial exit. If the pool has an unlock period, your tokens show under your pending unlocks and earn nothing until it ends; with **Instant**, they're back in your wallet straight away.

Changed your mind after exiting? You can stake again whenever you like: right away with other tokens you hold, or with the returning ones once their unlock period ends.

{% content-ref url="../communities/holders-pool.md" %}
[holders-pool.md](../communities/holders-pool.md)
{% endcontent-ref %}

{% hint style="info" %}
Rewards are **claimed manually**. They build up over time, and you collect them whenever you like. They don't get added to your stake automatically.
{% endhint %}

{% hint style="warning" %}
Unstaking often isn't instant. BZE staking, staking programs and many holders pools have an **unlock period**, during which your tokens are locked and earning nothing before they return to your wallet. Check the period shown on the card before you commit.
{% endhint %}

{% hint style="success" %}
**For example.** A gaming guild funds a daily **$GUILD** prize in the $GUILD holders pool. Members stake their $GUILD from the Staking page, watch their share tick up, and claim whenever they like. When a partner studio airdrops some extra $GUILD into the pool to celebrate a launch, everyone staking gets a slice, simply for being part of the guild.
{% endhint %}

For step-by-step guides, head to the pages built for each:

{% content-ref url="../staking/staking-your-bze.md" %}
[staking-your-bze.md](../staking/staking-your-bze.md)
{% endcontent-ref %}

{% content-ref url="../staking/managing-your-stake.md" %}
[managing-your-stake.md](../staking/managing-your-stake.md)
{% endcontent-ref %}

{% content-ref url="../communities/staking-programs.md" %}
[staking-programs.md](../communities/staking-programs.md)
{% endcontent-ref %}
