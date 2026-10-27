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

# Governance & Upgrades

BeeZee is run by its community. Changes to the network, from a new setting to a full software upgrade, are made through **proposals** that BZE stakers vote on. The explorer shows every proposal, how the vote is going, and who voted, and it watches network upgrades live.

## The Proposals page

The [Proposals page](https://explorer.getbze.com/proposals) starts with what is **Voting now**, then **All proposals**. Filter by **All**, **Voting**, **Passed** or **Rejected**, or use **Find a proposal**. Each row shows the status, the result, the turnout and when voting ended.

## A proposal's page

* **The summary**: who proposed it and when, **Yes so far** and **Turnout so far** while voting is open (or the **Result** once it ended), and when voting ends.
* **What this proposal does**: the proposal explained in plain words, for example which setting it changes and to what, how much it pays from the community pool and to whom, or which upgrade it schedules and at which block, with a link to the release notes. A text proposal says that it changes nothing on the chain by itself. **Read the full text** opens the proposer's own description.
* **Votes**: the Yes, No, Abstain and Veto shares, and three checks: **Enough people voted**, **Enough Yes votes** and **Not vetoed**. While voting is open, **If it ended now** tells you whether the proposal would pass right now.
* **Who voted**: switch between **Validators** and **Everyone**. Under the validators, the explorer names the active validators that have not voted yet, or did not vote, with their share of the voting power.
* **Timeline**: submitted, deposit, voting start and end.

{% hint style="info" %}
**Want to vote?** The explorer only shows votes. Vote from your own wallet in the [Staking app](../staking/README.md) with the account you stake from: your vote then counts for your stake instead of your validator's, and you can change it until voting ends. The **Vote on Staking** link on the proposal takes you straight there.
{% endhint %}

Checking which validators skip votes is one of the best ways to judge them. Validators that vote on every recent proposal get a mark in the [Hall of Fame](validators-hall-of-fame.md).

## Upgrade watch

When a software upgrade passes, every validator has to install the new version at the scheduled block. The network pauses at that block and restarts once validators holding more than two thirds of the voting power are back on the new version. You can work out when the upgrade block will arrive with **Future block** (see [Blocks & Transactions](blocks-and-transactions.md#future-block)).

While the network is paused, the explorer follows the restart live:

* An orange strip at the top of every page says **The chain is paused for the … upgrade**, for how long, and how much of the voting power is back, with a **See who is missing** link.
* The upgrade's proposal page (and the Validators page) shows a **Chain paused for the upgrade** panel: a bar for **Back on the new version** with a marker at the two-thirds line, progress bars for the restart rounds, and the list of validators **Not back yet** with their voting power. It updates every few seconds.

**Your coins are safe during the pause.** Nothing can be sent or traded until the network restarts, and every app picks up where it left off afterwards.

### After the upgrade

Once the network is running again, the upgrade's proposal page keeps an **After the upgrade** table: every validator of the set, in the order they came back, and how long each took.

This is a record most explorers never keep, and it matters to you as a delegator. A validator that came back in two minutes has someone on call. One that came back an hour late kept missing blocks after the restart, and missing too many gets a validator jailed, its stakers' rewards with it. Validators that came back within ten minutes of the latest upgrade keep their place in the [Hall of Fame](validators-hall-of-fame.md).

{% content-ref url="parameters.md" %}
[parameters.md](parameters.md)
{% endcontent-ref %}
