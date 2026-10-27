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

# Rewards Parameters

These settings cover the rewards anyone can run for a token: **simple rewards** (stake a token for a set time, share a fixed prize) and **compounded rewards** (one ongoing reward per token, paying daily prizes in one or more tokens; the Communities app calls it the **holders pool**). On the BZE Explorer they're under [Rewards](https://explorer.getbze.com/parameters#rewards).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current ones. Token Factory always shows the current fees on its review step.
{% endhint %}

## Fees for starting and funding rewards

Every fee below is a flat amount paid **on top of** the prizes you fund, and it goes to the **community pool**. You can pay it in your preferred fee token instead of BZE. The fees keep rewards meaningful: each one is work the network carries out every day for as long as it runs.

| Action                                                                      | Fee at the time of writing |
| --------------------------------------------------------------------------- | -------------------------- |
| **Create a simple reward**                                                  | 25,000 BZE                 |
| **Start a compounded reward** for a token that doesn't have one yet          | 25,000 BZE                 |
| **Add a daily prize** to a compounded reward                                | 25,000 BZE                 |
| **New prize fee**: the first time a token becomes a prize in a compounded reward | 25,000 BZE            |
| **Create a trading reward**, a trading competition on one market             | 50,000 BZE                 |

A few things to know:

* **Extending is free.** Adding days to a simple reward, or extending a running daily prize at the same daily amount, has no feature fee, only the network fee.
* **The new prize fee is paid once per prize token.** Once a token is a prize in a compounded reward, adding more of it later, by you or anyone, doesn't pay it again. If your daily prize uses a new prize token, you pay both the daily prize fee and the new prize fee in the same step.
* **Trading rewards** need a governance vote to start, and aren't offered in the apps yet.

## Compounded reward settings

| Setting                                  | What it does                                                                                                                       | At the time of writing |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Prize tokens per compounded reward**   | The most different tokens one compounded reward can pay. Each new prize token takes a slot for good.                              | 50                     |
| **Unlock time**                          | How long stakers wait to get their tokens back after unstaking. It's fixed when a compounded reward starts and stays the same for that token. | 7 days       |
| **Minimum stake**                        | The smallest stake a new compounded reward accepts. Also fixed when it starts.                                                    | none               |

Unlock time and minimum stake apply to compounded rewards started **after** a change. A token's existing compounded reward keeps the values it started with, so a governance change never moves the goalposts for people already staking.

## Extra gas for unstaking

**What it does.** Adds a fixed amount of extra gas when you unstake from a simple or a compounded reward. There's one setting for each.

**Why.** Unstaking leaves the network work to do later: it has to track your tokens through the unlock time and release them when it ends. The extra gas pays for that work up front, and stops anyone from flooding the unlock queue.

**At the time of writing:** **1,000,000 gas** for each, which adds about **0.01 BZE** to your network fee at the minimum gas price. It's part of the network fee, so it goes to validators and stakers.

{% hint style="success" %}
**For example.** The gaming guild starts a compounded reward for **$GUILD** and pays the 25,000 BZE fee in $GUILD, without touching BZE. Later a partner project adds 30 days of its own token as a daily prize. Since that token is new to the reward, they pay the daily prize fee and the new prize fee together. A month on, the guild extends its own $GUILD prize for another 60 days, and that costs only the network fee.
{% endhint %}

{% content-ref url="../../apps/token-factory/growing-your-community.md" %}
[growing-your-community.md](../../apps/token-factory/growing-your-community.md)
{% endcontent-ref %}
