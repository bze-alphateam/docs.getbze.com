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

# Staking Your BZE

Staking is the simplest way to put your BZE to work. You delegate some of your coins to a **validator** (one of the computers that keep the network running) and in return you earn a share of the rewards, including the new coins the network creates through inflation. You help keep BeeZee secure, and your coins stay yours the whole time: you only choose who to back, you never hand them over.

Everything happens on one dashboard at [staking.getbze.com](https://staking.getbze.com). Before you can stake, connect a wallet with **Connect Wallet to Stake**.

{% content-ref url="../../using-the-apps/connecting-a-wallet.md" %}
[connecting-a-wallet.md](../../using-the-apps/connecting-a-wallet.md)
{% endcontent-ref %}

## What the dashboard shows you

At the top of the page, a row of cards shows what staking looks like right now:

* **Staking APR**: roughly what you can expect to earn over a year, with how much BZE is handed out to stakers each day.
* **Network Staked**: how much BZE everyone has staked in total, with its approximate value in US dollars.
* **Unbonding Period** and **Daily Distribution** (before you connect a wallet): how long your coins take to come back to you after you unstake, and how much BZE goes to stakers each day.
* **Your Stake** and **Pending Rewards** (once your wallet is connected): how much BZE you have staked and the rewards waiting for you to claim, each with its approximate US dollar value.

The figures come from the live network. If something looks out of date, for example just after a transaction, select **Refresh** to reload them. For the wider tokenomics picture, head to the [BeeZee website](https://getbze.com).

## Choosing a validator

Below the cards is **All Validators**, the list of validators you can delegate to. It shows only **active** validators (the ones currently producing blocks and earning rewards), largest first. Search it by name or address with **Search validators...**. Each entry tells you what you need to know at a glance:

* **Rank and VP (voting power)**: how much is staked with that validator. This is a rough sign of how established and trusted it is.
* **Commission**: the cut the validator keeps from the rewards before passing the rest to you. Lower is more generous to you, but a healthy validator needs some commission to keep its machines running.

As a rule of thumb, pick a validator with a **reasonable commission** that you trust to stay online. Spreading your stake across more than one validator is also a perfectly good idea.

Want a shortlist? The BZE Explorer's [Validators Hall of Fame](../explorer/validators-hall-of-fame.md) lists the validators that vote on proposals, almost never miss a block and came back quickly after the last upgrade, and each [validator page](../explorer/validator-pages.md) shows its uptime, history and stake movements.

{% hint style="warning" %}
**Choose reliable validators.** A validator that goes offline for too long, or breaks the network's rules, can be penalised: it gets **jailed** (it stops earning rewards) and a small part of the BZE staked with it can be lost, **including yours**. Backing well-run validators, and spreading your stake, keeps that risk small. If a validator you back is ever jailed, the app warns you so you can move your stake (see [Managing Your Stake](managing-your-stake.md)).
{% endhint %}

## Delegating your BZE

Once you have picked a validator, staking takes a few seconds:

1. Select **Stake** next to the validator.
2. Enter an amount. The **25%**, **50%**, **75%** and **Max** shortcuts fill it in for you. **Available** shows your BZE balance.
3. Select **Delegate**, confirm the transaction in your wallet, and you are done. Rewards start adding up automatically.

You can stake with the same validator again at any time: the new amount is simply added to what you already have staked with it.

{% hint style="info" %}
**The network fee is taken care of.** Every transaction costs a tiny fee in BZE, so the shortcuts (Max included) already leave enough for it in your wallet. If you type an amount that would leave too little behind, the app warns you and offers a one-click **Delegate … BZE instead** button with the largest amount you can stake.
{% endhint %}

{% hint style="success" %}
**Example:** you hold 1,000 BZE and select **Max**. The app fills in a little less than 1,000, keeping back just enough for the fee, so the transaction goes through and you still have BZE to claim rewards or unstake later.
{% endhint %}

That is all there is to it. Once your BZE is staked, you can watch your rewards grow, claim them, move your stake, or unstake at any time.

{% content-ref url="managing-your-stake.md" %}
[managing-your-stake.md](managing-your-stake.md)
{% endcontent-ref %}

{% content-ref url="../../overview/features/stake-bze.md" %}
[stake-bze.md](../../overview/features/stake-bze.md)
{% endcontent-ref %}
