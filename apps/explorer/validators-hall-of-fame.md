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

# Validators Hall of Fame

Picking a validator is the one real decision in staking, and most explorers leave you with a long list sorted by size. The BZE Explorer does the homework for you. The **Hall of Fame** is a short list of validators that have *shown*, on the chain itself, that they take the job seriously. It is the first tab on the [Validators page](https://explorer.getbze.com/validators), marked with a crown.

## Who gets in

A validator earns its place in the Hall of Fame by meeting every one of these, all at once:

* **It is active** and producing blocks right now, so it pays rewards.
* **It voted on every one of the last four governance proposals**, whatever it voted. A validator that votes is one that pays attention to the network it helps run.
* **It missed almost no blocks**: at most 10 in the recent signing window the network uses to judge validators. That is near-perfect uptime.
* **It came back fast after the last network upgrade**: within 10 minutes of the network pausing for it. Upgrades are when sleepy operators get caught out; quick returns mean someone is watching.

The page states the current rule above the list, with the real numbers, so you always know exactly what a member has proven. There is no application and nobody hand-picks members: a validator is in while it meets the rule, and drops out the moment it doesn't.

{% hint style="success" %}
**Why these four?** Each one is something you, as a delegator, would want to check yourself but can't easily see. Voting shows engagement, signing shows reliability, and a quick return after an upgrade shows there is a real person on call. A validator that misses blocks can be penalised, and part of the stake behind it lost, so reliability protects *your* coins.
{% endhint %}

## Reading the list

Each member's row shows its name in gold, its stake and share of the voting power, and two badges that say what earned it the place, for example **Didn't miss a block in the last 10,000 blocks** and **Voted on all of the last 4 proposals**.

The list is sorted **smallest first** on purpose. All active validators pay the same base reward, so a smaller, reliable validator earns you just as much (only the commission differs). Staking with it also spreads the voting power across more hands, which keeps the network harder to attack. Big validators get bigger on their own; the Hall of Fame gives the small, well-run ones a fair chance.

You can search the list by name with **Find a validator**, the same as the **Active** and **Inactive** tabs.

## The crown, everywhere

Hall of Fame members wear their crown across the explorer: next to their gold name in the Active list and on their own validator page. Hover over the crown (or tap it on a phone) and a small card explains why that validator is in, with its own figures, such as "Missed 4 of the last 10,000 blocks (10 allowed)", and a link to the full Hall of Fame.

## Using it to choose a validator

**Example:** you want to stake the BZE you bought for the book club and don't know any validators. Open the Hall of Fame, pick a member near the top of the list with a commission you are happy with, and open its page to double-check its history. Then follow the **Stake on Staking** link at the top of the page: the [Staking app](../staking/README.md) opens, ready to stake with that validator.

A few tips:

* **Spread it out.** Splitting your stake between two or three members lowers your risk further.
* **Check the commission.** The Hall of Fame says nothing about price. Compare commissions on the validator pages; the **Your reward rate here** tile shows what you would earn after commission.
* **Look again now and then.** Membership is live. If a validator you back drops out, its page tells you why, and you can move your stake without waiting by redelegating (see [Managing Your Stake](../staking/managing-your-stake.md)).

{% hint style="info" %}
The Hall of Fame tab only appears while at least one validator meets the rule. Being outside it doesn't mean a validator is bad, only that it hasn't proven all four things recently: a validator that joined lately, for example, wasn't around to vote on the last four proposals.
{% endhint %}

{% content-ref url="validator-pages.md" %}
[validator-pages.md](validator-pages.md)
{% endcontent-ref %}
