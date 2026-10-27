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

# DEX Parameters

These settings cover the DEX: opening markets and pools, the fees on order-book trades, and the extra gas that keeps the order book fast. On the BZE Explorer they're under [DEX](https://explorer.getbze.com/parameters#dex).

{% hint style="info" %}
Values are shown **at the time of writing**. Governance can change them, so check the [Chain parameters](https://explorer.getbze.com/parameters) page or a block explorer for the current ones. The apps always read the current values before you sign.
{% endhint %}

## Creating a market or a pool

**What it does.** A flat fee for opening a new **order-book market** or a new **liquidity pool**. Both cost the same.

**Who it affects.** Anyone creating a market or pool, usually a project launching its token. Trading on a market or pool afterwards doesn't pay it.

**At the time of writing:** **25,000 BZE**, or the same value in your preferred fee token.

**Where it goes.** The community pool.

**Why it exists.** Every market and pool lives on the network forever. The fee keeps the DEX free of empty, throwaway pairs and funds the community.

## Maker fee and taker fee

**What they do.** Flat fees on order-book trades. Which one you pay depends on whether your order waits in the book or fills straight away:

* A **maker** order rests in the book and gives others something to trade against. It pays the **maker fee**.
* A **taker** order fills immediately against an order that's already there. It pays the **taker fee**. Filling existing orders by picking them from the book always counts as taking, and pays the taker fee once per transaction.

**Who they affect.** Everyone placing orders on an order-book market. Swapping through a liquidity pool doesn't pay them; pools charge their own swap fee instead (see below).

**At the time of writing:** maker fee **0.001 BZE**, taker fee **0.1 BZE** per order. If you pay fees in another token, you pay the same value in it.

**Where they go.** Two separate settings decide the destination of each fee, either the **burner** or the **community pool**. At the time of writing both go to the **burner**, so every order-book trade burns a little BZE.

{% content-ref url="../../apps/dex/order-book-markets.md" %}
[order-book-markets.md](../../apps/dex/order-book-markets.md)
{% endcontent-ref %}

## Extra gas for orders

Orders aren't matched the moment you send them. They wait in a short **queue** and the network works through it at the end of each block. These settings add extra gas, and so a slightly larger network fee, to keep that queue moving when it gets busy.

| Setting                         | What it does                                                                                                                                    | At the time of writing                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Free queue length**           | How many orders can wait in the queue before new orders start paying extra.                                                                     | 100 orders                                             |
| **Busy-queue surcharge**        | Extra gas for a new order, for every order waiting beyond the free length. The busier the queue, the more a new order costs.                   | 25,000 gas per order over the limit                    |
| **Queue check**                 | Extra gas for every waiting order in the same market that the network checks to make sure your price is valid.                                  | 5,000 gas per waiting order                            |
| **Filling orders**              | Extra gas when you fill orders from the book, once to start and again for each order you fill, growing with every order in the batch.           | 5,000 gas, then more per order                          |
| **Orders handled per block**    | How many queued orders the network settles in each block. Anything left over is settled in the next one.                                        | 500 orders                                             |

**Who they affect.** On a normal day, almost nobody: the queue is short and empties every block, so a regular order pays no surcharge. They matter when someone floods the order book: each extra order costs more than the last, so spamming gets expensive fast while everyday traders stay unaffected.

**What it costs.** At the minimum gas price, 25,000 gas is about 0.00025 BZE. Even an order placed when the queue is 40 orders over the limit pays only about 0.01 BZE extra.

{% hint style="success" %}
**For example.** A bot sends hundreds of tiny $GUILD orders in one block. The first hundred cost a normal network fee. After that, each new order pays 25,000 more gas than the one before it, so the bot soon can't fit more into the block, while a guild member's single order a few blocks later pays the normal fee again.
{% endhint %}

## Pool swap fees are set per pool

A liquidity pool's **swap fee**, and how it's split between liquidity providers, the burner and the community treasury, isn't a network setting. Whoever creates the pool picks both, and they stay fixed for that pool's lifetime. You'll see them on every pool's page.

{% content-ref url="../../apps/dex/liquidity-pools.md" %}
[liquidity-pools.md](../../apps/dex/liquidity-pools.md)
{% endcontent-ref %}

## Other DEX settings

* **Minimum BZE liquidity for fee tokens** (100,000 BZE at the time of writing) also lives here. It decides which tokens can pay fees, so it's explained on the [Network Fees](network-fees.md) page.
* **The network's own coin** is set to BZE: the coin that fees are converted into. It doesn't change.

{% hint style="info" %}
**Halted tokens aren't a parameter.** Governance can pause trading in a specific token through a proposal of its own. Paused tokens are listed under [Halted denoms](https://explorer.getbze.com/parameters#halted) on the same explorer page.
{% endhint %}
