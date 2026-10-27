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

# Deposits & Withdrawals

BeeZee connects to other blockchains, so you can move assets in and out without asking anyone's permission. Tap **Deposit / Withdraw** in the wallet panel:

* **Deposit** brings assets *into* BeeZee from another connected chain. That includes BZE and tokens created on BeeZee that you hold elsewhere, say on Osmosis: pick the coin, then the **Source** network it's on, and connect your wallet there when asked.
* **Withdraw** sends assets *out* to a destination chain and recipient of your choice. Only coins that a connected chain can receive are listed.

Either way, before you confirm you'll see the **estimated amount** you'll receive and an **estimated time** for the transfer to complete.

## Assets that can't be deposited

Now and then an asset is wound down and BeeZee stops accepting new deposits of it. When that happens it simply disappears from the **Deposit** list, and the form shows a short notice explaining why.

Right now that applies to **USDC.n**. On the Deposit form, and on its asset page in the DEX, you'll see the notice **"USDC.n is being retired"**: it's USDC issued on the Noble chain, which Circle is retiring, so new deposits to BeeZee are closed. You can still withdraw it to Noble, trade it and send it.

If you send a closed asset to BeeZee anyway, for example straight from a wallet on Noble, BeeZee refuses the transfer and the tokens are returned to your address on the sending chain. The refund is automatic but, like any cross-chain transfer, can take a few minutes. Withdrawals are never affected: you can always send the asset back out. The [USDC and Retired Tokens](../overview/features/usdc-and-retired-tokens.md) page explains the move from USDC.n to USDC.inj and what to do if you still hold USDC.n.

## Routes beyond the built-in connections

The wallet panel handles the chains that connect to BeeZee directly. For routes beyond those, the **Use Skip.go** button opens Skip.go, an external bridging tool that can find a path — you carry on there, then come back to BeeZee when you're done.

## Tracking a transfer

Cross-chain transfers aren't instant — they can take a few minutes to settle. Once your wallet has signed, a confirmation pops up; for a withdrawal it has a **View on Explorer** button so you can look the transaction up. The coins show up in your balances, or on the other chain, once the transfer completes on the other side.

Purchases made with **Buy BZE** get a little more: your latest one appears under **Latest Buy** in the wallet panel. Tap it to open its **Transaction Details** and follow each hop across the networks; **View on chain explorer** opens the transaction on the explorer of the network you paid from.

{% hint style="info" %}
**Only when there's something to move.** The **Deposit / Withdraw** button appears only when you can actually use it: when there's a coin you could deposit, or you hold one that can leave BeeZee. If only one direction is possible, the form shows just that one. Deposits and withdrawals can also be turned off depending on the app and the network you're using.
{% endhint %}

Want the bigger picture on how BeeZee links up with other networks?

{% content-ref url="../overview/features/cross-chain-transfers.md" %}
[cross-chain-transfers.md](../overview/features/cross-chain-transfers.md)
{% endcontent-ref %}
