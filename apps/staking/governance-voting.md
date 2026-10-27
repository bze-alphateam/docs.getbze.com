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

# Voting on Proposals

BeeZee is run by its community. Changes to the network, such as a software upgrade, a new setting or a payment from the community pool, are put to a vote as **proposals**, and the people who stake BZE decide. Your staked BZE is your voting power, and the Staking app is where you use it.

## Finding proposals

Open **Governance** in the Staking app's top menu. When proposals are waiting, a small badge next to it shows how many need your vote (or, without a wallet connected, how many are open). The dashboard also flags them: a card next to the staking APR tells you how many proposals are open or need your vote, with **Vote now** and **All proposals** buttons.

The Governance page has two lists:

* **Open for voting**: proposals you can vote on right now. Each card shows how long is left (**Ends in …**), the current tally, the turnout so far and whether the **quorum** (the minimum turnout) has been **reached**, plus your own vote. Select **View proposal** to read it in full.
* **Finished**: past proposals with their result (**Passed**, **Rejected** or **Failed**), when they ended and their final tally. Select **Show older proposals** to go further back.

A short note at the top of the page explains the rules: how long voting lasts, the turnout a proposal needs, the share of **Yes** it needs to pass, and the **No with veto** limit. These values are set by the network and can change through governance, so the app always shows the current ones (on a phone, tap **How voting works**). You can also check them on a block explorer.

## Reading a proposal

A proposal's page starts with its number, its status (for example **Voting** or **Passed**), its type and its title, along with when voting ends. Below that you will find:

* **What it does if it passes**: a plain-language summary of the change, such as which software version it upgrades to or how many coins it sends from the community pool and to whom. **Show technical details** reveals the exact content.
* **Description**: the proposer's own explanation. Select **Show full description** to read all of it.
* **Your vote**: your voting power and your current vote, with buttons to vote.
* **Current tally**: how the votes split so far, and whether the proposal would pass **if voting ended now**, checked against each rule. Once voting is over, it becomes the **Final tally**.
* **Your validators' votes**: how each validator you stake with has voted (shown when your wallet is connected).
* **Timeline**: when the proposal was submitted and when voting started and ends, who proposed it and the deposit behind it.

Select **All proposals** to go back to the list.

## Who can vote

Anyone who **stakes BZE** can vote. Connect your wallet and the Governance page shows **Your voting power**: the BZE you have staked, and with how many validators.

* **Only active stake counts.** BZE staked with a validator that is jailed or otherwise inactive does not count towards your voting power, and the app tells you how much is left out. Moving that stake to an active validator brings it back (see [Managing Your Stake](managing-your-stake.md)).
* **Votes are counted when voting ends.** Your vote counts with the BZE you have staked at that moment. With nothing staked you can still vote, but your vote has **0 voting power** until you stake.

{% content-ref url="staking-your-bze.md" %}
[staking-your-bze.md](staking-your-bze.md)
{% endcontent-ref %}

## Casting your vote

1. Select **Vote** on an open proposal's card, or pick an option straight from **Your vote** on the proposal's page.
2. Under **How do you vote?**, choose one option:
   * **Yes**: you support the proposal.
   * **No**: you are against it.
   * **No with veto**: you are against it, and you think it is spam or harmful. If enough of the votes are vetoes, the proposal fails, and the app warns you that the proposer's deposit can be burned.
   * **Abstain**: you take no side, but your vote still counts towards the turnout.
3. Select **Continue**. The **Confirm your vote** step shows your choice, your voting power, which vote it replaces and the small network fee.
4. Select **Sign and vote** and approve the transaction in your wallet. Nothing is sent until you approve.

When the vote goes through, a **Vote recorded** message confirms it, along with the time until which you can still change it.

{% hint style="info" %}
**If your vote is not sent**, for example because you rejected it in your wallet, the app says so and nothing changes. Select **Try again** whenever you are ready.
{% endhint %}

{% hint style="success" %}
**Example:** the book club behind $PAGE stakes 2,000 BZE. A proposal to fund a new feature from the community pool opens, and the club agrees with it. They open the proposal, read **What it does if it passes**, select **Yes**, then **Continue** and **Sign and vote**. Their vote counts for all 2,000 BZE they have staked.
{% endhint %}

## Changing your vote

You can change your mind as long as voting is open. Select **Change vote**, pick a different option and confirm it the same way. Your new vote replaces the old one, and the last vote you cast is the one that counts.

Once voting has ended, the network clears individual votes, so the app can no longer show how you voted. A block explorer keeps the full record.

## If you don't vote

You don't have to vote on every proposal. Until you do, **your validator's vote counts for the BZE you staked with them**. If you stake with several validators, each one's vote counts for your stake with it, and stake with a validator that has not voted is not counted. The proposal page shows all of this under **Your validators' votes**.

As soon as you vote yourself, your vote replaces your validators' votes for **all** of your staked BZE.

{% hint style="warning" %}
**Your validator might not vote the way you would.** If a proposal matters to you, cast your own vote: it is the only way to make sure your stake says what you think.
{% endhint %}

{% content-ref url="managing-your-stake.md" %}
[managing-your-stake.md](managing-your-stake.md)
{% endcontent-ref %}
