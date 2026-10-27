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

# USDC and Retired Tokens

BeeZee's dollar is now **USDC.inj**, the USDC that comes from the Injective chain. It replaces **USDC.n**, the USDC from the Noble chain, because Circle (the company behind USDC) is ending USDC on Noble. This page explains what changed, what to do if you still hold USDC.n, and the two tools BeeZee uses when a token is wound down: **halting** its trading and **closing** its deposits.

## Why USDC changed

In September 2026 Circle announced that it is [discontinuing USDC on Noble](https://www.circle.com/blog/circle-is-discontinuing-support-for-usdc-and-cctp-v1-on-noble). Noble was where BeeZee's USDC came from, so USDC.n is the token being retired. Circle's schedule:

* **13 October 2026**: no new USDC is issued on Noble.
* **31 October 2026**: moving USDC out of Noble gets gradually harder, as the limits on Circle's transfer route start shrinking.
* **12 January 2027**: USDC on Noble is paused. After that, Circle handles what's left through manual redemptions.

The wider Cosmos ecosystem picked the USDC issued on Injective as its new standard, and BeeZee followed.

## What changed on BeeZee

* **USDC.inj is BeeZee's USDC.** There is a **USDC.inj–BZE** liquidity pool and a **BZE/USDC.inj** order-book market, and the dollar prices you see across the apps are based on USDC.inj.
* **USDC.n deposits are closed.** Since the network upgrade of 26 October 2026, BeeZee no longer accepts new USDC.n from Noble. USDC.n is gone from the **Deposit** list, and the apps show a **"USDC.n is being retired"** notice instead (more in [Closed deposits](#closed-deposits) below).
* **The network's own USDC liquidity moves over.** Most of the USDC.n–BZE pool belonged to the network itself: its liquidity sat locked in the burner's black hole, where nobody could spend it. The same upgrade handed that share to the team, so they can withdraw it, move the USDC.n out of Noble, and add it to the new USDC.inj–BZE pool, locking it in the black hole again. Nothing else in the black hole was touched.
* **Leaving is always possible.** Withdrawing USDC.n back to Noble, sending it to another BeeZee address, and getting your tokens out of orders and pools all keep working.

## If you still hold USDC.n

Don't wait for January: the sooner you act, the easier it is. You have two ways out:

1. **Trade it on BeeZee.** While USDC.n can still be traded, swap it on the [DEX](../../apps/dex/swapping.md) for BZE or another token. You can then swap BZE for USDC.inj if you want to stay in dollars.
2. **Withdraw it to Noble.** Use **Withdraw** in the wallet panel to send it to your Noble address, then move it on from Noble with a bridging tool that still supports Noble USDC.

If your USDC.n sits in a **liquidity pool** or an **open order**, first [remove the liquidity](../../apps/dex/liquidity-pools.md) or cancel the order to bring it back to your wallet.

{% hint style="warning" %}
**USDC.n may be halted.** BeeZee can stop all trading of USDC.n through a governance vote (see [Halted tokens](#halted-tokens) below). If that happens, swapping it on BeeZee is no longer an option, but withdrawing it, sending it and taking it out of orders and pools still work.
{% endhint %}

{% hint style="success" %}
**For example.** A $PAGE book club member has 50 USDC.n in their wallet and 20 more in the USDC.n–BZE pool. They remove their liquidity, swap the 70 USDC.n for BZE on the DEX, then swap part of that BZE for USDC.inj. Their dollars now sit in the new USDC, all without leaving BeeZee.
{% endhint %}

## Halted tokens

When a token can no longer be trusted to keep its value, as with USDC.n, BeeZee can **halt** it. Halting is decided by **governance**: someone puts forward a proposal, and BZE stakers vote on it. Only a vote can halt a token, and only a vote can lift the halt. BZE itself can never be halted.

Once a token is halted, the network no longer exchanges it for anything, in any app:

* You can't **swap** it, **place orders** with it, or **add liquidity** to its pools. Orders already in the book stay there but won't fill.
* Nobody can **create a new market or pool** with it, and Token Factory no longer offers it for raffles or trading rewards.
* It can no longer be used to **pay transaction fees**.

You keep full control of what you own. You can still:

* **Cancel your open orders** and get the tokens back.
* **Remove your liquidity** from its pools.
* **Send it** to another address, or **withdraw** it to another chain.

In the DEX a halted token carries a red **Trading halted** badge, and its markets and pools show a notice explaining what is still possible. See [Trading halted](../../apps/dex/assets.md#trading-halted) for what you'll see there.

{% hint style="info" %}
**Nothing is halted by surprise.** A halt only takes effect once its governance proposal has passed, after a public vote. You can follow proposals and their results on the [block explorer](https://explorer.getbze.com/).
{% endhint %}

## Closed deposits

BeeZee can also stop accepting new deposits of a token from a given chain, so no fresh supply of a retiring token arrives. Right now that applies to one token:

* **USDC.n arriving from Noble.**

What this means for you:

* **In the apps**, the token simply disappears from the **Deposit** list, and a short notice explains why.
* **If you send it anyway**, for example from a wallet on Noble, BeeZee refuses the transfer and the tokens go back to your address on Noble. The refund happens automatically, but like any cross-chain transfer it can take a few minutes to show up.
* **Withdrawals are not affected.** You can always send the token *out* of BeeZee, and other tokens from the same chain still arrive normally.

The list of closed deposits is a network setting that only governance can change, so it can grow or shrink over time. The Deposit form always reflects the current list.

{% content-ref url="../../using-the-apps/deposits-and-withdrawals.md" %}
[deposits-and-withdrawals.md](../../using-the-apps/deposits-and-withdrawals.md)
{% endcontent-ref %}

{% content-ref url="../../apps/dex/assets.md" %}
[assets.md](../../apps/dex/assets.md)
{% endcontent-ref %}
