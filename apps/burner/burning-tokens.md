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

# Burning Tokens

Burning means permanently destroying coins so they can never be used again. It's a simple idea with a real effect: every coin burned is gone for good, which lowers the total amount in circulation. The Burner app — themed as "the burning pot" — is where BeeZee does this out in the open, for anyone to see and take part in.

## Burning coins you hold

1. On the home page, click **Burn Coins Now**.
2. **Pick a token you hold.** The picker is searchable and shows your balances.
3. **Enter an amount.** Type how much you want to burn, or use the **Max** button to send all of it.
4. **Confirm.** Your wallet asks you to approve, and your coins are handed to the pot.

{% hint style="danger" %}
**Burning is permanent — there are no take-backs.** Once you confirm, those coins are gone forever. Nobody, including you, can recover them or undo the burn. Only burn what you truly mean to destroy.
{% endhint %}

## When the burn actually happens

Burning isn't instant. When you burn coins, they're sent to **the pot** and wait there until the next **scheduled burn**, which happens once a week. On the burn, everything in the pot is destroyed together.

So the home page always shows you two things:

* A **Ready to Burn** list — the coins currently waiting in the pot for the next burn.
* A **countdown** to the next scheduled burn, so you know exactly when it'll go up in smoke.

## Not every coin burns the same way

This part surprises people, so here it is plainly. Depending on the kind of coin, the pot does one of three things:

* **Native BZE and community-created tokens are burned.** Straightforward — they're destroyed on the next burn.
* **Liquidity pool (LP) tokens can't be burned.** An LP token is a receipt for a share of a shared trading pool, and destroying it would strand the funds behind it. Instead, these are **locked forever** in an address that has no key, so no one can ever move them again. For these, the app shows a **Lock** button rather than **Burn** — the effect is the same permanence, just achieved by locking away instead of destroying.
* **Bridged (IBC) tokens are swapped first.** A bridged token is one that arrived from another blockchain. It can't be burned directly, so the pot first swaps it to BZE — which needs a BZE liquidity pool to swap through — and then burns that BZE.

{% hint style="warning" %}
Locking LP tokens is just as final as burning. Locked tokens go to a no-key address and can never be recovered — treat the **Lock** button with the same care as **Burn**.
{% endhint %}

## What the home dashboard shows

The Burner home page is a live picture of everything that's been taken out of supply:

* **Total BZE burned** all-time.
* **Total value locked forever** — the LP tokens and other assets held in no-key addresses.
* A **burn history** — recent burns with the amount, the value at the time, and when they happened.
* A **coin search**, so you can look up any specific token quickly.

## Where do burned coins come from?

Not all burning is manual. Part of the fees collected across the whole BeeZee ecosystem is quietly routed to the burner and destroyed over time. That means supply keeps gently shrinking in the background, even when nobody is burning coins by hand. Your own burns simply add to that steady drip.

{% hint style="info" %}
You'll need a connected wallet before you can burn anything. Connecting your wallet is shared across all the apps — see [Connecting a Wallet](../../using-the-apps/connecting-a-wallet.md).
{% endhint %}

{% content-ref url="../../overview/features/token-burning.md" %}
[token-burning.md](../../overview/features/token-burning.md)
{% endcontent-ref %}
