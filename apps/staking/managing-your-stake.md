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

Once your BZE is staked, the [Staking app](https://staking.getbze.com) becomes your home for keeping an eye on it: collecting your rewards, moving your stake around, and unstaking when the time comes. Here is how each part works.

{% hint style="info" %}
**Keep a little BZE in your wallet.** Claiming, undelegating and redelegating each cost a small network fee, paid from your wallet rather than from your stake or rewards. If your wallet cannot cover it, the app tells you before you send anything.
{% endhint %}

## My Validators

**My Validators** lists every validator you have staked with, biggest stake first. Each card shows the validator's commission, how much you have **Delegated** (with its approximate US dollar value), and the **Rewards** waiting for you to claim. Three buttons sit at the bottom of each card:

* **Delegate**: stake more BZE with this validator. The new amount is added to your existing stake.
* **Undelegate**: start unstaking (see [Undelegating](#undelegating) below).
* **Redelegate**: move your stake to another validator (see [Redelegating](#redelegating) below).

This is also the only place where validators that have **stopped earning** show up. The main validator list only shows active validators, but My Validators keeps every validator you still have stake with, so you can always act on it. If one of them is **jailed** (penalised and switched off for misbehaving or being offline) or otherwise inactive, its card is outlined in red, a **Jailed** badge appears when it applies, and a **Not Earning Rewards** box explains what is wrong. Right inside that box, **Redelegate Now** lets you move the stake to a healthy validator in one step.

{% hint style="warning" %}
**Act quickly when you see "Not Earning Rewards".** Stake with a jailed or inactive validator earns nothing until you move it. Redelegating fixes that right away.
{% endhint %}

## Claiming rewards

Your rewards build up automatically from the moment you stake, but they do not land in your wallet on their own: you **claim** them yourself. There is no auto-compound on the network, so nothing moves until you say so.

Select **Claim All** next to the My Validators heading (it shows your total pending rewards). A dialog opens with every validator that has rewards for you, all selected by default. Pick some or all of them, then select **Claim** to collect them in a single transaction.

{% hint style="info" %}
**Want to compound?** Since rewards do not reinvest themselves, compounding is a two-step move: **claim** your rewards, then **delegate** them again on top of your existing stake. Do that regularly and your stake, and your future rewards, keep growing.
{% endhint %}

## Undelegating

When you want your coins back, select **Undelegate** on the validator's card, enter an amount (the **25%**, **50%**, **75%** and **Max** shortcuts are based on what you have delegated), and confirm. This does not return your BZE straight away. It starts the **unbonding period**, a waiting time during which the coins are locked and earn nothing, before they arrive back in your wallet.

{% hint style="warning" %}
**Unstaking is not instant.** The unbonding period is set by the network and can change through governance. The dashboard shows its current length on the **Unbonding Period** card (visible before you connect a wallet). During that time your coins are locked and earn no rewards, and the Staking app cannot cancel an unbonding once it has started. If you only want to switch validators, **redelegating** avoids this wait entirely.
{% endhint %}

Everything you are unstaking appears under **Unbonding Delegations**, soonest first. Each entry shows the amount, the time left (for example **5d left**) and the date it **Completes**. Once the wait is over, it is marked **Ready** and the coins are back in your wallet.

## Redelegating

**Redelegating** moves stake from one validator to another **without** the unbonding wait: your coins keep earning the whole time. It is the go-to fix when a validator you back goes offline or gets jailed. Select **Redelegate** (or **Redelegate Now**), choose the **Destination Validator** from the list, enter an amount, and confirm.

The network puts two limits on redelegating. When you hit one, the transaction is refused and the app shows a **Transaction Failed** message with the network's explanation:

* **Moved stake has to settle first.** After you redelegate to a validator, you cannot redelegate away from that validator again until the unbonding period has passed since that move. You can still undelegate from it at any time.
* **Only a limited number of redelegations can be pending at once** between the same two validators. The limit is set by the network. Wait for an earlier redelegation to finish its unbonding period, or move a bigger amount in one go.

{% hint style="success" %}
**Example:** you redelegate 500 BZE from Validator A to Validator B. A few days later, B is jailed. You cannot redelegate away from B just yet, because your move is still settling. Your options are to wait until the unbonding period has passed since the first move, or to undelegate from B.
{% endhint %}

## A couple of honest notes

{% hint style="info" %}
**This app is for native BZE staking only.** Reward programs for *other* tokens (staking your BZE or project tokens to earn a mix of coins) live in the DEX and Communities apps instead. There is also no governance voting here.
{% endhint %}

{% content-ref url="../communities/staking-programs.md" %}
[staking-programs.md](../communities/staking-programs.md)
{% endcontent-ref %}

{% content-ref url="staking-your-bze.md" %}
[staking-your-bze.md](staking-your-bze.md)
{% endcontent-ref %}
