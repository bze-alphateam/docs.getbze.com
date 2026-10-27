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

# Blocks & Transactions

Every few seconds the network adds a new **block**: a page in BeeZee's shared record book, holding the **transactions** people sent in that moment. The explorer lets you read both, in plain words.

## Blocks

The [Blocks page](https://explorer.getbze.com/blocks) lists the latest blocks, newest first, with each block's height (its number), time, the validator that proposed it, and how many transactions it holds.

Open a block to see its **Overview** (time, proposer, fees collected, how long it took since the previous block) and the **Transactions in this block**. Use the arrows to step to the previous or next block.

### Where the funds went in this block

Not everything that moves coins is a transaction. Every block, the network also pays out staking rewards, collects fees, runs scheduled payouts from reward programs, burns coins in the Burner and settles cross-chain transfers. Most explorers hide this. The BZE Explorer shows it in a **Where the funds went in this block** panel, grouped as **Fees**, **DEX**, **Staking**, **Rewards programs**, **Burner**, **Cross-chain**, **Governance**, **Payments** and **Other**. Select **Show all transfers, one by one** for the full list.

**Example:** the Burner burns the coins it collected. You won't find a transaction for it, but the block where it happens shows the burn under **Burner**.

### Future block

Want to know when a block in the future will arrive, say the height a network upgrade is scheduled for? Open **Future block** (linked in the page footer). Type a **block height** to get an estimated date and time, or type a **date and time** to get the block height expected then. The page explains its estimate, which uses the recent average block time, so the further away the block, the rougher the guess.

If you open a block that hasn't been produced yet, the explorer says so and shows the block as soon as it appears.

## Transactions

The [Transactions page](https://explorer.getbze.com/txs) is "everything people did on the chain, newest first, each in one line". Switch between **All**, **Success** and **Failed**; the last one helps when you are hunting for a problem.

Each line says **what happened** in words rather than codes, for example:

* **Swap 50 USDC → BZE**
* **Buy order · 1,000 BZE at 0.0125 USDC**
* **Add liquidity to the USDC/BZE pool**
* **Join the PAGE raffle · 2 tickets**
* **Mint 1,000,000 GUILD to …**
* **Cross-chain transfer received: 320 USDC to …**
* **Vote No on proposal #14**

## A transaction's page

Paste a transaction hash into the search box (or follow a **View on Explorer** link from any BZE app) to open it. You will find:

* **What happened**: each action in the transaction, explained, with the accounts, tokens and amounts involved.
* **Where the funds went**: the coins that actually moved, step by step, including fees, DEX trades and rewards. Select **Show steps** to expand it.
* **Overview**: the block, time, the **Fee** and who paid it, the **Memo** and who signed.
* **Why it failed**: for a failed transaction, the reason in plain words. A failed transaction changes nothing except the fee it paid.

When the action is something you can do yourself, a link takes you to the right app, for example **Vote on Staking** on a governance vote.

{% hint style="info" %}
**Just sent something?** If you open a transaction the moment you sent it, the page says **Looking for this transaction…** and fills in on its own as soon as it is in a block, usually within a few seconds.
{% endhint %}

For traders, transaction pages are the receipts of the DEX: every order, fill, swap and liquidity change is spelled out with the market, the price and the amounts. To see everything one account did, open the account instead: see [Accounts](accounts.md).

{% content-ref url="accounts.md" %}
[accounts.md](accounts.md)
{% endcontent-ref %}
