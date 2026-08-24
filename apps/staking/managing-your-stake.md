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

# Managing Your Stake

Once your BZE is staked, the [Staking app](https://staking.getbze.com) becomes your home for keeping an eye on it — collecting your rewards, moving your stake around, and unstaking when the time comes. Here is how each part works.

## Your validators

The **Your validators** section lists everything you have delegated: which validators you back, how much you have staked with each, and the **pending rewards** waiting for you to claim.

If a validator you back goes inactive or gets jailed — meaning it has stopped doing its job and is earning nothing — the app flags it with a **"Not earning rewards"** warning so you notice quickly. Right beside the warning is a **Redelegate** shortcut, which lets you move that stake to a healthy validator in one step (see [Redelegating](#redelegating) below).

## Claiming rewards

Your rewards build up automatically from the moment you stake — but they do not land in your wallet on their own. You have to **claim** them yourself. There is no auto-compound on the network, so nothing moves until you say so.

Claiming is quick. The app opens a batch dialog where you can **select some or all of your validators** and collect all their rewards in a single transaction.

{% hint style="info" %}
**Want to compound?** Since rewards do not reinvest themselves, compounding is a two-step move: **claim** your rewards, then **stake** them again on top of your existing delegation. Do that regularly and your stake — and your future rewards — keep growing.
{% endhint %}

## Unstaking (undelegating)

When you want your coins back, you **unstake** (also called undelegating). This does not return your BZE straight away — it begins an **unbonding period**, a waiting time during which the coins are locked, earning nothing, before they arrive back in your wallet.

{% hint style="warning" %}
**Unstaking is not instant.** The unbonding period is currently **21 days**. During that time your coins are locked and earn no rewards, and the unbonding cannot be cancelled once started. This is a network setting the community can change through governance, so you can always check the current value on a [block explorer](https://explorer.getbze.com/). If you only need to switch validators, **redelegating** avoids this wait entirely.
{% endhint %}

The app keeps track of any unbonding you have in progress, showing each one with the time left (for example "X days left") or marked **Ready** with the date the coins become available again.

## Redelegating

**Redelegating** moves stake from one validator to another **without** the unbonding wait — your coins keep earning the whole time, with no 21-day lock. It is the go-to fix when a validator you back goes offline or gets jailed: instead of unstaking and waiting, you simply redelegate to a healthy validator and carry on earning. You will find a **Redelegate** action on each of your delegations, and a shortcut right next to any "Not earning rewards" warning.

## A couple of honest notes

{% hint style="info" %}
**This app is for native BZE staking only.** Reward programs for *other* tokens — staking your BZE or project tokens to earn a mix of coins — live in the DEX and Communities apps instead. There is also no governance voting here.
{% endhint %}

{% content-ref url="../communities/staking-programs.md" %}
[staking-programs.md](../communities/staking-programs.md)
{% endcontent-ref %}
