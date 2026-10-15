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

# Staking Programs

Besides its holders pool, a token can have **staking programs**: campaigns with an end date, where you stake one token for a set number of days and share a daily prize. On a token's page they're called **Fixed-term programs**, and they come in two places:

* **Stake your TICKER**: programs where you stake the page's own token. They sit under the holders pool, in **Fixed-term programs**.
* **Ways to earn TICKER**: programs where you stake a *different* token, often an LP token from a liquidity pool, and are paid in the page's token. They show up in the **Earn** section.

The token you stake in a program is locked on its own, separate from the holders pool, with the program's own unlock time.

{% content-ref url="holders-pool.md" %}
[holders-pool.md](holders-pool.md)
{% endcontent-ref %}

## Reading a program card

Each program is a card, so you can size it up before joining:

* **Pays in**: the prize token, with the program's **APR** when it can be worked out.
* **Paid daily**: how much is shared between everyone staking, each day.
* **Ends in**: how many days the program still pays, or **Finished**.
* **Unlock time**: how long your tokens wait after you unstake, or **Instant** when there's no wait. This lock is set by whoever started the program, and it's right on the card so you know it before you join.
* **Total staked**: how much everyone has committed so far.
* **Minimum**: the smallest stake the program accepts.

Programs that stake an **LP token** name both tokens of the pool, like **GUILD/BZE LP**, so you know which liquidity you'd need to provide first.

Running programs are listed first. Once a program has finished, it only stays on the page for people who still have tokens in it, so they can claim and unstake.

{% hint style="info" %}
**APR is an estimate, not a promise.** It's worked out from the daily prize and how much is staked right now, using prices when the prize and the staked token are different. As people join and leave, the real figure moves. When a price is missing, the card leaves the APR out rather than guess.
{% endhint %}

## Taking part

Connect your wallet and the program cards under **Fixed-term programs** gain their buttons.

* **Stake** (or **Stake more**): enter an **Amount** or tap **Max**, check the **Network fee**, and confirm. Your total stake must reach the program's minimum. If you already have rewards waiting, staking more pays them out first, in the same transaction.
* **Claim**: appears when you have something to collect, and sends the prize you've earned to your wallet. Your stake stays in and keeps earning.
* **Unstake**: takes out **your whole stake**. There's no partial unstake: any unclaimed prize is paid out first, then your tokens wait for the program's **Unlock time** and come back to your wallet. When the unlock time is **Instant**, they come back in the same transaction.

Once you're in, the card shows where you stand: **You stake**, what's **Ready to claim**, and anything **Unlocking**, with a countdown to when it returns.

Joining a program from **Ways to earn TICKER** works the same way, with a **Stake** button on its card. To claim from it or unstake later, use the staking page of the DEX, which lists every program on BeeZee, or the page of the token you staked if it's a community token.

{% hint style="warning" %}
**Unstaking takes everything out, and may not be instant.** Your whole stake leaves the program and stops earning the moment you unstake. Check the unlock time before you confirm.
{% endhint %}

{% hint style="success" %}
**For example.** The gaming guild runs a 30-day campaign: stake the **GUILD/BZE LP** token, earn a daily **$GUILD** prize. On the $GUILD page, it shows up under **Ways to earn GUILD**. You add liquidity to the $GUILD–BZE pool in the **Trade** section, and stake the LP tokens you got right from the program's card. From then on, you claim your $GUILD now and then on the DEX's staking page.
{% endhint %}

{% content-ref url="../dex/staking-and-earning.md" %}
[staking-and-earning.md](../dex/staking-and-earning.md)
{% endcontent-ref %}

Running a program of your own? Token Factory walks you through it:

{% content-ref url="../token-factory/growing-your-community.md" %}
[growing-your-community.md](../token-factory/growing-your-community.md)
{% endcontent-ref %}

{% content-ref url="../../overview/features/earning-rewards.md" %}
[earning-rewards.md](../../overview/features/earning-rewards.md)
{% endcontent-ref %}
