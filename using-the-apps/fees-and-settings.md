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

# Fees & Settings

The **Settings** toggle sits at the top of every BeeZee app, next to the Wallet button. Open it to fine-tune how the app looks and how you pay your fees.

## Appearance

Switch between **dark** and **light** mode, whichever is easier on your eyes. Your choice sticks the next time you visit.

## Preferred fee token

Every action on BeeZee costs a small network fee. By default that's paid in BZE — but you don't have to stop there. You can choose to pay your fees in **another token instead**. Pick it from the **Preferred Fee Token** list here, and the app takes care of the rest quietly in the background.

The list only offers tokens that can actually pay fees right now. A token qualifies when:

* it has a liquidity pool paired with BZE,
* that pool holds at least a **minimum amount of BZE**, set by the network, and
* trading in it hasn't been paused.

If the token you picked stops qualifying later — say its pool drops below the minimum — the app quietly switches you back to paying in BZE, so your transactions keep working.

This is one of BeeZee's signature ideas: with a pool behind it, almost any token can pay the fees, so an app can feel like it was built entirely around that one token.

{% hint style="success" %}
**For example.** A member of that book club sets their preferred fee token to **$PAGE**. From then on, every send, swap, and stake they make is paid in $PAGE — they take part in everything without ever needing to hold BZE, and BeeZee handles the details behind the scenes.
{% endhint %}

To learn more about how this works across the whole network:

{% content-ref url="../overview/features/fee-token.md" %}
[fee-token.md](../overview/features/fee-token.md)
{% endcontent-ref %}

Why some actions cost more than a normal transaction (extra gas and feature fees), and where every fee goes: see [Network Parameters](../overview/parameters/README.md).

## Advanced

{% hint style="info" %}
**For power users, optional.** If you run your own BeeZee node or prefer a specific provider, the advanced settings let you point the app at your own network endpoints instead of the defaults. Most people never need to touch this — the app works out of the box.
{% endhint %}
