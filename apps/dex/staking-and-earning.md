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

The DEX isn't only for trading. Its **Staking** tab opens **Staking & Rewards**, one page for every way to put your tokens to work and earn while you hold them: BZE staking, **simple rewards** and **compounded rewards**, all in one list.

## Your positions

Once you're staking somewhere, have tokens unlocking or have rewards waiting, **Your positions** appears at the top. Its header sums things up: what you have **Staked** (in dollars, and across how many rewards), what's **Unclaimed**, and how many unlocks are in progress. Below it, one row per reward you're in shows its **APR** (with roughly what you earn per day), **Your stake** (with your share of the pool), what's **To claim**, anything **Unlocking**, and how far it has run (**Elapsed / Duration**).

* **Manage** opens that reward's actions: stake more, unstake or exit, and claim.
* **View** opens the reward's own page (see [A reward's page](#a-rewards-page) below).
* **Claim**, the big button in the header, opens **Claim rewards**: a list of every reward you can collect from, all ticked to start with. Untick any you'd rather leave, check the total under **You receive**, and claim them all in **one transaction**.

## Explore rewards

**Explore rewards** lists every reward on BeeZee: BZE staking first, then verified rewards from the highest APR down, then the rest. To narrow it down:

* **Search by token** finds the rewards that stake or pay a token (BZE staking hides while you search).
* The **All**, **Simple**, **Compounded** and **LP** buttons pick a kind; **LP** shows the rewards for liquidity pool shares, the [Boost Rewards](liquidity-pools.md#boost-rewards) of the pools.
* **Verified only** (on to start with) hides rewards whose tokens haven't been verified (see [The Verified Badge](../../overview/features/verified-badge.md)), and **Show finished** brings back simple rewards that have ended.

Each row is tagged **Native**, **Simple** or **Compounded**, carries a **Verified** tag where its tokens have been checked, and says under its name how long the **Unlock** takes (or **instant**), the minimum stake if there is one, and whether it's running. The columns show what you **Earn**, the estimated **APR** (a yearly rate, based on current conditions), what it pays out **Daily**, its **Total staked**, and how many of its days have been paid out (**Ongoing** for rewards with no end date). Rewards you're already in are highlighted and marked **staked**.

Select **Stake** on a row to join it (**Add** if you're already in), or **View** for its full page.

{% hint style="info" %}
A link can open the page with a search already filled in. Token Factory, for example, links here to show the rewards for your token.
{% endhint %}

## A reward's page

**View** opens a page for one simple or compounded reward, with a link button so you can share it. You'll find:

* **What it is**: its name, kind, whether it's running, a **Verified** tag where it applies, and a one-line summary of what you stake and what you earn.
* **Reward**: **Total staked**, what it's **Paid per day**, its **APR**, how long the **Unlock** takes, the **Minimum** stake, and how long it **Runs**.
* **Prize** (or **Prizes**, for a compounded reward paying several tokens): everything it pays out each day, with dollar values where there's a price.

Beside them, the **Stake** box lets you try an amount before you commit. Type one (or use **Max**) and an **Estimated income** box shows what it would earn, in dollars per day, per 30 days and per year (or until the reward ends), along with each token and **Your share after** you join. It's today's daily prizes times your share of the pool, so it goes down as more people stake. Select **Stake** (or **Add stake**) to continue to the confirmation.

Once you're in, the page also shows **Your stake** (with your share and daily income) with an **Unstake** or **Exit** button, what's **Pending** with **Claim**, and anything **Unlocking**.

## BZE staking

The first row is always **BZE Native Staking**: staking BZE itself. Validators are the machines that keep the BeeZee network running. When you stake (delegate) your BZE to one, you help secure the chain and earn a share of the rewards it produces, including the new BZE created by inflation. Your BZE never leaves your control: you're lending your vote of confidence, not handing it over.

Its **Stake** button opens the [Staking](../staking/README.md) app, which is built for choosing validators and managing your delegations. Once you're staking, **Manage** on your position shows your stake, your rewards waiting to be collected and any **Pending Unlock** (BZE on its way back to you, with the date it arrives), and **Claim** collects your BZE staking rewards right here in the DEX. Very small amounts of BZE rewards can't be claimed until they grow a little, so a claim never costs more in fees than it pays.

## Simple rewards

**Simple rewards** are campaigns, each with an end date, where you stake one token and share a daily amount paid in another (or the same) token. Each one is named after the token you stake and its number, like **PAGE #14**. Simple rewards for LP tokens are the [Boost Rewards](liquidity-pools.md#boost-rewards) of the liquidity pools, so you'll find them here too.

A simple reward is **Running**, **Waiting for stakers** or **Finished**. Its actions are **Stake**, **Unstake** and **Claim**:

* **Stake** shows your **Estimated Daily Rewards** before you select **Confirm Stake**.
* **Unstake** shows an **Unstaking Notice** with how many days your tokens stay locked before they come back.
* **Claim** collects the rewards you've earned so far.

## Compounded rewards

A **compounded reward** lets you stake a token and share the prizes **anyone** adds to it, in several tokens, either as a **daily** prize or as one-off **airdrops**. There's one per token, it's named after that token, and it has no end date. The token's team, its fans or its partners can all add to the prizes. It shows as **Paying daily**, or **Airdrops only** when no daily prize is scheduled.

* **Stake** joins it (the button becomes **Add** once you're in). Adding more pays out your pending prizes first, in the same transaction.
* **Claim** collects your pending prizes. Your stake stays in and keeps earning.
* **Exit** pays out your pending prizes, then releases your **whole** stake. Exiting is all or nothing; there's no partial exit. If it has an unlock period, your tokens show under your unlocks and earn nothing until it ends; with an instant unlock, they're back in your wallet straight away.

Changed your mind after exiting? You can stake again whenever you like: right away with other tokens you hold, or with the returning ones once their unlock period ends.

{% hint style="info" %}
**Same rewards, other names in Communities.** On a token's page in the Communities app, its compounded reward is the **Holders pool** and its simple rewards are the **Fixed-term programs**. Staking in either place is the same stake.
{% endhint %}

{% content-ref url="../communities/holders-pool.md" %}
[holders-pool.md](../communities/holders-pool.md)
{% endcontent-ref %}

{% hint style="info" %}
Rewards are **claimed manually**. They build up over time, and you collect them whenever you like. They don't get added to your stake automatically.
{% endhint %}

{% hint style="warning" %}
Unstaking often isn't instant. BZE staking, simple rewards and many compounded rewards have an **unlock period**, during which your tokens are locked and earning nothing before they return to your wallet. Check the **Unlock** shown for the reward before you commit.
{% endhint %}

{% hint style="success" %}
**For example.** A gaming guild funds a daily **$GUILD** prize in the $GUILD compounded reward. Members stake their $GUILD from the Staking page, watch their share tick up, and claim whenever they like. When a partner studio airdrops some extra $GUILD to its stakers to celebrate a launch, everyone staking gets a slice, simply for being part of the guild.
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
