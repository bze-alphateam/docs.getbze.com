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

BeeZee connects to other blockchains, so you can move assets in and out without asking anyone's permission. You'll find the bridge form right inside the wallet panel:

* **Deposit** brings assets *into* BeeZee from another connected chain.
* **Withdraw** sends assets *out* to a destination chain and recipient of your choice.

Either way, before you confirm you'll see the **estimated amount** you'll receive and an **estimated time** for the transfer to complete.

## Assets that can't be deposited

Now and then an asset is wound down and BeeZee stops accepting new deposits of it. When that happens it simply disappears from the **Deposit** list, and the form shows a short notice explaining why.

Right now that applies to **USDC.n**. On the Deposit form, and on its asset page in the DEX, you'll see the notice **"USDC.n is being retired"**: it's USDC issued on the Noble chain, which Circle is retiring, so new deposits to BeeZee are closed. You can still withdraw it to Noble, trade it and send it.

## Routes beyond the built-in connections

The wallet panel handles the chains that connect to BeeZee directly. For routes beyond those, the app hands off to an external bridging tool that can find a path — you carry on there, then come back to BeeZee when you're done.

## Tracking a transfer

Cross-chain transfers aren't instant — they can take a few minutes to settle. Once your wallet has signed, a confirmation pops up with a **View in Explorer** link so you can look the transaction up, and the coins show up in your balances once the transfer completes on the other side.

Purchases made with **Buy BZE** get a little more: they appear under **Recent Buys** in the wallet panel, where you can follow each step. Their **View on Explorer** button opens the cross-chain tracker of Skip, the routing service behind Buy BZE, because those transfers can hop across several networks.

{% hint style="info" %}
**Availability varies.** Deposits and withdrawals can be turned on or off depending on the app and the network you're using, so you may not see the bridge form everywhere.
{% endhint %}

Want the bigger picture on how BeeZee links up with other networks?

{% content-ref url="../overview/features/cross-chain-transfers.md" %}
[cross-chain-transfers.md](../overview/features/cross-chain-transfers.md)
{% endcontent-ref %}
