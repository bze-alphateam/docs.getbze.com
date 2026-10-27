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

# Network Parameters

BeeZee's features run on a set of **network parameters**: the settings that decide how much it costs to create a token, how often the burner burns, what a trade on an order book pays and where those fees end up. They're not hidden in the apps. They live on the blockchain itself, the same for everyone, and the community can change them by voting on a governance proposal.

This section explains, feature by feature, what each setting means for you. It answers the questions people ask most: **why did this action cost more than a normal transaction, and where did my fee go?**

{% hint style="info" %}
**The numbers here are examples, not promises.** Every value on these pages is what the network used **at the time of writing**. Governance can change any of them, and the apps always read the current values before you sign. To see what's set right now, open the [Chain parameters](https://explorer.getbze.com/parameters) page of the BZE Explorer, or any block explorer.
{% endhint %}

## Three kinds of cost

When you do something on BeeZee, you can meet up to three kinds of cost. The app's review step shows all of them before you sign.

### 1. The network fee

Every transaction pays a small **network fee**. It's worked out from the **gas** your transaction uses (a measure of how much work it asks of the network) multiplied by a **gas price**. The network sets a minimum gas price, so nobody can flood it with free transactions. This fee rewards the validators and stakers who keep BeeZee running.

### 2. Extra gas

Some actions ask the network to do more work than a plain transfer, now or later: placing an order the network has to match, unstaking tokens it will release days from now, filling a batch of orders. For those, the network adds a fixed amount of **extra gas** on top of what the transaction itself uses. Extra gas simply makes your network fee a bit larger; it goes to the same place as the rest of the network fee.

Extra gas exists for two reasons: it makes you pay fairly for the work you leave behind, and it makes spamming the network expensive, which keeps it fast and cheap for everyone else.

### 3. Feature fees

A few actions carry a fixed **feature fee** on top of the network fee: creating a token, opening a market or pool, starting a reward, trading on an order book. These are flat amounts set by governance. They keep the network free of throwaway tokens and empty markets, and they feed the community pool and the burner.

## Where the fees go

| What you pay                                                  | Where it goes                                          |
| ------------------------------------------------------------- | ------------------------------------------------------ |
| Network fee (including any extra gas)                         | The validators and stakers who secure the network      |
| Order-book trading fees (maker and taker)                     | The **burner**: burned on the next scheduled burn      |
| Creating a token, a market or a pool                          | The **community pool**                                 |
| Starting or adding to rewards                                 | The **community pool**                                 |
| CoinTrunk: paid articles, and a share of every tip            | The **community pool**                                 |
| A liquidity pool's swap fee                                   | Split as the pool's creator chose: providers, burner, treasury |

The **community pool** is the network's shared treasury. It's spent only through governance proposals that BZE stakers vote on, typically to fund development and growth. The **burner** destroys the BZE it collects, so fees from everyday trading steadily shrink the supply.

## Paying in your own token

Feature fees are set in BZE, but you don't need BZE to pay them. If you've picked another **preferred fee token** in [Fees & Settings](../../using-the-apps/fees-and-settings.md), the network works out how much of your token covers the fee, swaps it to BZE through that token's pool, and sends the BZE where it belongs. You only need enough of your token. If the swap isn't possible, for example when the pool has become too small, the fee is taken in BZE instead. CoinTrunk's paid-article fee is the one exception: it's always paid in BZE.

{% content-ref url="../features/fee-token.md" %}
[fee-token.md](../features/fee-token.md)
{% endcontent-ref %}

## Parameters by feature

{% content-ref url="network-fees.md" %}
[network-fees.md](network-fees.md)
{% endcontent-ref %}

{% content-ref url="dex.md" %}
[dex.md](dex.md)
{% endcontent-ref %}

{% content-ref url="token-factory.md" %}
[token-factory.md](token-factory.md)
{% endcontent-ref %}

{% content-ref url="rewards.md" %}
[rewards.md](rewards.md)
{% endcontent-ref %}

{% content-ref url="burner.md" %}
[burner.md](burner.md)
{% endcontent-ref %}

{% content-ref url="cointrunk.md" %}
[cointrunk.md](cointrunk.md)
{% endcontent-ref %}

The network's general settings, such as staking, inflation, penalties and voting, work the same way as on other proof-of-stake chains, and you'll find them on the same [Chain parameters](https://explorer.getbze.com/parameters) page. The pages above cover the features BeeZee built itself.

## How a parameter changes

Anyone can put forward a governance proposal to change a parameter. BZE stakers vote on it, and if it passes, the new value applies to everyone from that moment, with no app update needed. The apps pick up the change automatically. You can follow open proposals on the [Proposals](https://explorer.getbze.com/proposals) page of the BZE Explorer.
