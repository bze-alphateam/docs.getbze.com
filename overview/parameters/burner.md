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

# Burner Parameters

The burner has a single network setting: how often it burns. On the BZE Explorer it's under [Burner](https://explorer.getbze.com/parameters#burner).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current one.
{% endhint %}

## Burn schedule

**What it does.** Tokens sent to the burner, by you or by fees routed there, wait in the burner until the next **scheduled burn**. This setting is the number of weeks between burns.

**Who it affects.** Anyone burning tokens, and anyone following BZE's supply. It changes **when** tokens are destroyed, never **whether**: once tokens reach the burner they can't be taken back.

**At the time of writing:** **every 4 weeks**.

**Where it comes from.** The order-book trading fees go to the burner (see [DEX Parameters](dex.md)), as does any share of a pool's swap fees its creator sent to burning. Together with what people burn by hand, that's what each scheduled burn destroys.

{% content-ref url="../../apps/burner/burning-tokens.md" %}
[burning-tokens.md](../../apps/burner/burning-tokens.md)
{% endcontent-ref %}

## Burning raffles

Raffles have **no feature fee** and no extra gas of their own. Starting one costs the starting pot you put in, and taking part costs the contribution price its creator chose, plus the normal network fee each time. The raffle's rules (its length, the price per contribution, the chance per contribution and the prize share) are picked by whoever starts it, not by the network.

When a raffle ends, whatever is left in its pot is burned right away, without waiting for the scheduled burn.

{% content-ref url="../../apps/burner/burning-raffles.md" %}
[burning-raffles.md](../../apps/burner/burning-raffles.md)
{% endcontent-ref %}
