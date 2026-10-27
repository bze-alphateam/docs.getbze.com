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
**Keep a little BZE in your wallet.** Claiming, unstaking and moving stake each cost a small network fee, paid from your wallet rather than from your stake or rewards. If your wallet cannot cover it, the app tells you before you send anything.
{% endhint %}

## My Validators

**My Validators** lists every validator you have staked with, biggest stake first. Each card shows the validator's commission, how much you have **Staked** (with its approximate US dollar value), and the **Rewards** waiting for you to claim. Three buttons sit at the bottom of each card:

* **Stake**: stake more BZE with this validator. The new amount is added to your existing stake.
* **Unstake**: start getting your coins back (see [Unstaking](#unstaking) below).
* **Move**: move your stake to another validator (see [Moving your stake](#moving-your-stake) below).

This is also the only place where validators that have **stopped earning** show up. The main validator list only shows active validators, but My Validators keeps every validator you still have stake with, so you can always act on it. If one of them is **jailed** (penalised and switched off for misbehaving or being offline) or otherwise inactive, its card is outlined in red, a **Jailed** badge appears when it applies, and a **Not Earning Rewards** box explains what is wrong. Right inside that box, **Move stake** lets you move it to a healthy validator in one step.

To catch trouble even earlier, the [BZE Explorer](../explorer/validator-pages.md) shows a red **Offline** dot as soon as a validator stops signing blocks, before it gets jailed.

{% hint style="warning" %}
**Act quickly when you see "Not Earning Rewards".** Stake with a jailed or inactive validator earns nothing until you move it. Moving it fixes that right away.
{% endhint %}

## Claiming rewards

Your rewards build up automatically from the moment you stake, but they do not land in your wallet on their own: you **claim** them yourself. There is no auto-compound on the network, so nothing moves until you say so.

Select **Claim All** next to the My Validators heading (it shows your total pending rewards). The **Claim Staking Rewards** window opens with every validator that has rewards for you, all selected by default. Pick some or all of them (**Select All** and **Deselect All** help), then select **Claim** to collect them in a single transaction.

{% hint style="info" %}
**Want to compound?** Since rewards do not reinvest themselves, compounding is a two-step move: **claim** your rewards, then **stake** them again on top of your existing stake. Do that regularly and your stake, and your future rewards, keep growing.
{% endhint %}

## Unstaking

When you want your coins back, select **Unstake** on the validator's card. In the **Unstake from …** window, enter an amount (the **25%**, **50%**, **75%** and **Max** shortcuts are based on what you have **Staked** with that validator), then select **Unstake** and confirm. This does not return your BZE straight away. It starts the **unbonding period**, a waiting time during which the coins are locked and earn nothing, before they arrive back in your wallet.

{% hint style="warning" %}
**Unstaking is not instant.** The unbonding period is set by the network and can change through governance. The **Unstake** window tells you its current length before you confirm, and once you have a stake the **Your Stake** card on the dashboard shows it too. During that time your coins are locked and earn no rewards, and the Staking app cannot cancel an unbonding once it has started. If you only want to switch validators, **moving your stake** avoids this wait entirely.
{% endhint %}

Everything you are unstaking appears under **Unbonding Delegations**, soonest first. Each entry shows the amount, the time left (for example **5d left**) and the date it **Completes**. Once the wait is over, it is marked **Ready** and the coins are back in your wallet.

## Moving your stake

**Moving** your stake (also called **redelegating**) shifts it from one validator to another **without** the unbonding wait: your coins keep earning the whole time. It is the go-to fix when a validator you back goes offline or gets jailed. Select **Move** (or **Move stake**), pick the **Destination Validator** from the list (you can search it by name), enter an amount, then select **Move** and confirm.

The network puts two limits on moving stake. When you hit one, the transaction is refused and the app shows a **Transaction Failed** message with the network's explanation:

* **Moved stake has to settle first.** After you move stake to a validator, you cannot move it away from that validator again until the unbonding period has passed since that move. You can still unstake from it at any time.
* **Only a limited number of moves can be pending at once** between the same two validators. The limit is set by the network. Wait for an earlier move to finish its unbonding period, or move a bigger amount in one go.

{% hint style="success" %}
**Example:** you move 500 BZE from Validator A to Validator B. A few days later, B is jailed. You cannot move it away from B just yet, because your move is still settling. Your options are to wait until the unbonding period has passed since the first move, or to unstake from B.
{% endhint %}

## A couple of honest notes

{% hint style="info" %}
**This app is for native BZE staking only.** Reward programs for *other* tokens (staking your BZE or project tokens to earn a mix of coins) live in the DEX and Communities apps instead.
{% endhint %}

{% hint style="info" %}
**Your stake is also your vote.** The BZE you have staked gives you a say on network proposals, right here in the app's **Governance** section.
{% endhint %}

{% content-ref url="governance-voting.md" %}
[governance-voting.md](governance-voting.md)
{% endcontent-ref %}

{% content-ref url="../communities/staking-programs.md" %}
[staking-programs.md](../communities/staking-programs.md)
{% endcontent-ref %}

{% content-ref url="staking-your-bze.md" %}
[staking-your-bze.md](staking-your-bze.md)
{% endcontent-ref %}
