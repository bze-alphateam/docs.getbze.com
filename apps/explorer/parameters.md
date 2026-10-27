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

# Chain Parameters

Many numbers in these docs come with a caveat: *set by the network, can change through governance*. Fees, the unstaking period, the DEX's maker and taker fees, the cost of creating a token, the voting rules. The explorer's [Parameters page](https://explorer.getbze.com/parameters) is where you read their current values.

The values are read live from the chain. Nobody can edit them by hand: a value only changes when a governance proposal passes, and the proposal that last changed each one is linked next to it, so you can always see who decided what, and when.

## Reading the page

The parameters are grouped by topic, each with a sentence saying what it covers:

* **Fees**: what every transaction pays, and what happens to fees paid in other tokens.
* **Staking**: the unstaking period, the number of active validator seats, the lowest commission allowed.
* **Rewards & inflation**: inflation right now and its range, the community pool's share.
* **Validator penalties**: the uptime a validator needs, how long it is jailed for downtime, and the penalties for downtime and for double-signing.
* **Governance**: the deposit needed to start a vote, the voting period, and the quorum, pass and veto thresholds.
* **DEX**, **Factory**, **Rewards programs**, **Burner** and **CoinTrunk**: the fees and limits of each BZE app.

Each row has a friendly name and its value in normal units, for example a fee in BZE rather than in the chain's smallest unit. Open **info** on a row for what it means and the value exactly as the chain stores it. Rarely needed settings are tucked away as **advanced**, and every group can be copied as JSON.

{% hint style="success" %}
**Example:** you are about to create $GUILD and want to know the creation fee before you start. Open **Parameters**, select **Factory**, and the current fee is right there, along with the proposal that last set it.
{% endhint %}

## Module accounts

The **Module accounts** list names the accounts that belong to the network itself, such as the community pool and the Burner, with their addresses. Open any of them to see what it holds and how its coins move (see [Accounts](accounts.md#accounts-that-belong-to-the-chain)).

## Halted denoms

Governance can pause a token on the network, for example when its home network has a problem. The **Halted denoms** section lists every paused token. While a token is halted there is no trading, no swaps, no new pools and it can't be used to pay fees. Cancelling your orders, removing liquidity and transfers still work, so you can always get your coins out. Another proposal lifts the halt. If the list is empty, the page simply says **No denom is halted**.

{% content-ref url="../../using-the-apps/fees-and-settings.md" %}
[fees-and-settings.md](../../using-the-apps/fees-and-settings.md)
{% endcontent-ref %}
