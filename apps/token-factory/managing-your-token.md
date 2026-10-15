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

# Managing Your Token

**Manage** opens **Your tokens**: everything created by your connected wallet, read straight from the network.

## Your tokens

Each token shows its name and ticker, its total supply, its token ID with a copy button, and how far its setup is ("4 of 6 set up · no pool yet"). A badge tells anyone at a glance what kind of token it is:

* **Mintable**: someone still controls it and could mint more.
* **Fixed supply**: the supply was locked, so no new tokens can ever be minted.

Below your tokens, **Markets and pools you created** lists your pools (with their swap fee and a quick **Add liquidity**) and your markets. Select **Open** on a token to go to its page.

## Your token's page

Your token's page has six tabs.

### Overview

The token's key numbers (total supply, how much is in your wallet, how much holders stake, where it trades) and a **setup checklist**: description, brand kit, liquidity pool, holder rewards, logo in every wallet and, optionally, an order-book market. The checklist is read from the network, so it stays current however you did each step, and each item has a button to do it.

### Supply

* **Mint more**: create more of your token, straight to your wallet. The form shows the new total supply.
* **Burn**: destroy some of the tokens you hold, shrinking the supply. You can also burn in the [Burner](../burner/README.md) app, where anyone can burn the tokens they hold and see the burn history.

Mint and burn cost only the network fee.

{% hint style="warning" %}
**Minting more lowers the share every holder owns.** Use it thoughtfully: minting a lot, or often, can shake holders' trust.
{% endhint %}

### Profile

* **What wallets show**: edit the token's **name** and **description**. You review the change before **Save on-chain**, and wallets and explorers pick it up right away. The ticker, token ID and decimals can never change.
* **Brand kit**: your token's colours and font on its Communities page.
* **Logo**: a link to the registry guide that gets your logo into every wallet.

### Trading

The pools and order-book markets with your token, including ones other people created (yours are marked **You created it**), with buttons to add liquidity, reward liquidity providers or view them on the DEX.

### Rewards

Your token's **holder rewards** and the **staking programs** that involve it. See [Growing Your Community](growing-your-community.md).

### Control

Who controls the token, and the two ways to give that up: **lock the supply** forever, or **hand over control** to another address. See [Making It Official](making-it-official.md).

{% hint style="info" %}
**After locking or handing over,** the actions that need control (minting, editing what wallets show, the brand kit) disappear from your token's page. Everything else keeps working: trading, rewards, and burning the tokens you hold.
{% endhint %}

## Rewards on BeeZee

The **Rewards** page lists every holder reward and staking program on BeeZee, yours first. From there you can make any token stakable, airdrop to its stakers, add a daily prize, or extend a staking program.

{% content-ref url="growing-your-community.md" %}
[growing-your-community.md](growing-your-community.md)
{% endcontent-ref %}
