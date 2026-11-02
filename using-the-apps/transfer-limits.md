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

# Transfer limits

Moving BZE between BeeZee and another chain has a daily limit. It is a safety net: it keeps one bad day on a connected network from becoming a disaster, and for everyday use you will never notice it.

## The daily limit

* **BZE:** each connection to another chain has its own limit of **2% per day of all the BZE that exists**, in each direction. Sending BZE to Osmosis and bringing BZE in from Osmosis are two separate budgets, and so are Osmosis and every other connected chain.
* **Other tokens** (USDC, ATOM and the rest) have **no limit yet**. Governance can add a limit for another token later.
* **USDC.n** (USDC from Noble) still cannot be brought in, as before. You can still send it back out. See [USDC and Retired Tokens](../overview/features/usdc-and-retired-tokens.md).
* Limits **reset at midnight UTC**.

The limit follows the total BZE that exists, so the amount in BZE changes over time. To see what 2% is today, check the current amount of BZE on a block explorer such as [explorer.getbze.com](https://explorer.getbze.com).

Transfers are counted against each other: BZE coming back over a connection frees up room for BZE going out, so moving the same coins back and forth never uses up your day.

## If a transfer goes over the limit

Your tokens are never stuck in between.

* **Sending out of BeeZee:** the transfer fails straight away, before anything leaves your wallet. You only pay the network fee.
* **Sending into BeeZee:** BeeZee refuses the transfer and your tokens are returned to your address on the chain you sent from. The refund is automatic once the relayer delivers the answer, usually within a few minutes.

Then you can try again after midnight UTC, or split the amount into smaller transfers.

## Why there are limits

If another network connected to BeeZee is hacked, or BeeZee itself has a bug, the damage in one day is capped instead of a whole supply leaving at once. That buys time to react.

## Who can change the limits

**Governance** can add, raise, lower or remove any limit with a proposal that BZE stakers vote on.

{% hint style="info" %}
**The guardian.** For emergencies, where waiting for a vote would take too long, an address held by the BeeZee team, the *guardian*, can **lower** a limit or **pause** a token entirely. It can never raise a limit, and a paused token is reopened only by a governance vote.
{% endhint %}

{% hint style="warning" %}
**Limits can change.** What is written here is how things work today. The limits are set by governance and can be raised, lowered or removed later, and a token that has no limit now may get one. Check the current limits on a block explorer, or with the `ratelimit` queries if you use the command line.
{% endhint %}

## Questions

**Will my normal transfers be affected?**
No. 2% of all BZE per connection per day is far above everyday activity, and the other tokens have no limit yet. Only very large BZE transfers can be refused, and they can be split or retried the next day (UTC).

**What happens to my tokens if a transfer is refused?**
Nothing leaves your wallet. A transfer out of BeeZee simply fails. A transfer into BeeZee is returned to you on the chain you sent from once the relayer delivers the answer.

**Who can change the limits?**
Governance can add, raise, lower or remove them. The guardian can only lower them or pause a token in an emergency, never raise them.
