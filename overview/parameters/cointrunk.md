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

# CoinTrunk Parameters

These settings cover CoinTrunk, BeeZee's on-chain news feed: publishing articles and tipping the people who publish them. On the BZE Explorer they're under [CoinTrunk](https://explorer.getbze.com/parameters#cointrunk).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current ones.
{% endhint %}

## Paid articles

**Trusted publishers**, approved by governance, post articles for free. Anyone else can still publish, as a **paid article**.

| Setting                         | What it does                                                                                                     | At the time of writing |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Paid article fee**            | What each paid article costs. Unlike most fees on BeeZee, it's always paid in **BZE**.                           | 25,000 BZE             |
| **Paid articles per month**     | How many paid articles the whole network accepts each month, from everyone together. Once it's reached, paid articles wait for next month. | 5 |

**Where the fee goes.** The community pool.

**Why it exists.** The fee and the monthly limit keep the feed worth reading: they stop it from filling up with adverts and spam while still leaving a door open for anyone with something to say.

## Tipping publishers

**What it does.** When you tip a publisher (CoinTrunk calls it **paying respect**), a share of your tip goes to the community pool and the rest goes straight to the publisher. Tips are paid in one set token.

**At the time of writing:** tips are paid in **BZE**, and **20%** of each tip goes to the community pool.

{% hint style="success" %}
**For example.** You tip a publisher 100 BZE for a great article. The publisher receives 80 BZE, the community pool receives 20 BZE, and the publisher's respect total goes up by 100.
{% endhint %}

{% content-ref url="../cointrunk/README.md" %}
[README.md](../cointrunk/README.md)
{% endcontent-ref %}
