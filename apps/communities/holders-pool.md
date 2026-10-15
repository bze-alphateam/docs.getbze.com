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

# Holders Pool

A **holders pool** is the simplest way to put a community token to work: you stake the token itself and share the prizes the pool pays out every day. There is one per token, it has no end date, and it can pay **several prize tokens at once**: the project's own token, BZE, or a gift from another community.

You'll find it at the top of the **Stake** section on the token's page in the Communities app.

{% content-ref url="token-pages.md" %}
[token-pages.md](token-pages.md)
{% endcontent-ref %}

## Reading the pool

The **Holders pool** card tells you what you'd be joining:

* **Est. APR**: an estimated yearly return across all the prizes, worked out from what the pool pays and what everything is worth right now. It only shows when every prize token and the staked token have a price, so it's never a guess built on missing numbers.
* **The prize table**: one row per prize token, with how much is **Paid daily** and how long it is **Funded for**. Every day, each prize is split between everyone staking, in proportion to their stake. Days with nobody staking are skipped, so a prize can last longer than its days on the calendar.
* **Total staked**: how much everyone has staked together.
* **Unlock time**: how long you wait to get your tokens back after you unstake, or **Instant** when there's no wait. The network sets it when the pool is created, and it stays the same for that token.
* **Minimum stake**: the smallest stake the pool accepts.

If the table says **The pool pays nothing right now**, the pool exists but no prize is running at the moment. Anyone can add one (see below).

{% hint style="info" %}
**APR is an estimate, not a promise.** It moves with prices, with how much is staked and with the prizes that start and finish. Use it to compare, not as a guaranteed return.
{% endhint %}

## Taking part

Connect your wallet and the right-hand side of the card becomes **Your position**.

### Stake

Select **Stake TICKER** (or **Stake more** once you're in), enter an **Amount** or tap **Max**, and confirm. The form shows your balance and the **Network fee**, and stops you if your stake would be under the minimum. If you already have rewards waiting, staking more pays them out first, in the same transaction.

Once you're staked, **Your position** shows how much you stake and your **share of the pool**, plus what's **Ready to claim** in each prize token.

### Claim

**Claim all** collects everything you've earned, in every prize token, in one go. Your stake stays in and keeps earning. You can also claim from the page's wallet, which gathers rewards from the holders pool and the token's programs under **Rewards ready**.

### Unstake

**Unstake** always takes out **your whole stake**: there's no partial unstake. Any rewards you haven't claimed are paid out first. Then your tokens wait for the pool's **Unlock time** and come back to your wallet; while they wait they show as **Unlocking** with a countdown, and they don't earn anything. When the unlock time is **Instant**, they come back in the same transaction.

{% hint style="warning" %}
**Unstaking is all or nothing, and not always instant.** Your whole stake leaves the pool and stops earning the moment you unstake. If you only want some of it back, unstake everything and stake the rest again once it has returned.
{% endhint %}

## Growing the pool

Two buttons link to Token Factory, where the rewards behind a holders pool are set up:

* **Add rewards to the pool** opens a form to add a daily prize: pick the prize token, how much a day and for how many days. It's open to everyone, not only the creator: a fan, a partner project or another community can all reward this token's holders.
* **Start a holders pool** appears instead of the pool when a token doesn't have one yet (**No holders pool yet**). A holders pool is usually started by the token's team, but anyone can start one. Starting it gives no special rights, and once it exists anyone can fund it.

{% hint style="danger" %}
**Prizes are paid upfront.** Whoever adds a daily prize locks the whole amount (the daily prize times the number of days) when they sign, and it can't be taken back. Read the details in Token Factory before you fund one.
{% endhint %}

{% content-ref url="../token-factory/growing-your-community.md" %}
[growing-your-community.md](../token-factory/growing-your-community.md)
{% endcontent-ref %}

{% hint style="success" %}
**For example.** You hold some **$PAGE** and open the book club's page. Its holders pool pays a little $PAGE and a little BZE every day, and a gaming guild has added 30 days of **$GUILD** as a thank-you. You stake your $PAGE, and each day your share of all three prizes adds up under **Ready to claim**. A week later you **Claim all** and keep your stake earning.
{% endhint %}
