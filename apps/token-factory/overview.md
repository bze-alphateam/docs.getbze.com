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

# Overview

Token Factory lets anyone create their own token in minutes and then do everything a token needs: get it traded, give people a reason to hold it, reach new people, and get its logo into every wallet.

Your token works everywhere on BeeZee: it can be traded on the DEX, sent to other blockchains, and, once it has a liquidity pool with BZE, even used to pay the network's fees.

## Getting around

The menu at the top has three places:

* **Create**: the home page, where you start something new.
* **Tokens**: every token made with Token Factory, with the ones you created pinned on top. See [Managing Your Token](managing-your-token.md).
* **Rewards**: every staking reward on BeeZee, found by the token people stake. See [Growing Your Community](growing-your-community.md#the-rewards-directory).

You can browse Tokens and Rewards without connecting a wallet. Everything you see is read straight from the network.

## Six starting points

The home page asks **What are you building today?** and offers six starting points:

| Starting point | What it does |
| --- | --- |
| **Create a token** | Name, ticker and supply, minted to your wallet. Marked **Start here**. |
| **Create a DEX market** | Let people swap a pair instantly, or trade it with limit orders. |
| **Create staking rewards** | Pay people for staking a token: any token, not only yours. |
| **Grow a community** | Airdrops, a list of wallets, raffles, or reaching another community. |
| **Create a DAO** | Coming soon. |
| **Create a trading contest** | Coming soon. |

A starting point with options first opens a short **Choose** screen that compares them side by side, then takes you into the steps:

* **Create a DEX market** → **Liquidity pool** or **Order-book market**. See [Getting It Traded](markets-and-liquidity.md).
* **Create staking rewards** → **Simple reward** or **Compounded reward**, plus shortcuts for adding to a reward that already exists. See [Growing Your Community](growing-your-community.md).
* **Grow a community** → **Airdrop to stakers**, **Send to a list of wallets**, **Run a burning raffle** or **Reach another community**. See [Growing Your Community](growing-your-community.md).

{% hint style="info" %}
**DAO and trading contests aren't available yet.** Their tiles are shown dashed and marked **Coming soon**; they open nothing until they ship.
{% endhint %}

## Work on something that exists

Below the starting points, **Work on something that exists** is for tokens and rewards that are already on BeeZee. You don't have to be the one who created them:

* **Extend or fund a reward**: add days, a daily prize or an airdrop to any reward. It opens [Rewards](growing-your-community.md#the-rewards-directory).
* **Manage a token**: mint, edit details, logo and permissions. It opens [Tokens](managing-your-token.md); the actions that need the token's admin only appear for the admin, checked live.
* **Add or remove liquidity**: both live on the DEX, on each pool's page. See [Liquidity Pools](../dex/liquidity-pools.md).

## Pick up where you left off

With your wallet connected, the home page welcomes you back and, when there is something to finish, shows **Pick up where you left off** above a compact list of the starting points:

* a token you started creating in this browser, with the step you reached;
* a list of wallets you haven't finished sending;
* one suggestion for each token you created, read from the network: for example **Create a $PAGE/BZE pool** when nobody can buy it yet, **Make $PAGE stakable**, **Reward $PAGE/BZE liquidity**, or **Extend the daily prize** when one is about to end.

## How every flow works

Every flow in Token Factory follows the same four beats: **Pick**, **Fill in**, **Review**, **Done**.

* **One step at a time.** The current step is one open card, headed "Step 2 of 4" and its name. Steps you finished shrink to a one-line summary with an **Edit** button, and the steps still to come are greyed out. Scrolling only scrolls: it never moves you to another step.
* **No wallet needed to fill in.** You can explore every flow before connecting.
* **What will happen.** Next to the steps (below them on a phone), a live panel shows what you are about to create and, under **You will pay**, each cost, the network fee and whether your balance covers it.
* **The Review is always last.** It shows what **leaves your wallet**, what **you get**, and what is **permanent**, before you sign.
* **Then a Done screen.** It celebrates what you made and proposes one **Recommended next** step, carrying what you just created, plus two or three others. If you came from a token's page, a **Back to** button takes you there.

Creation fees are set by the network and can change through governance, so the app always reads the current amount for you. Check the **You will pay** panel, or a [block explorer](https://explorer.getbze.com/), rather than relying on a fixed number. If the app can't read a fee, it stops and asks you to refresh instead of guessing.

{% hint style="info" %}
**Guides and strategies.** The app keeps a link to these docs at the bottom of the home page. For step-by-step recipes that combine several flows, see [Guides and Strategies](playbooks.md).
{% endhint %}

{% content-ref url="creating-a-token.md" %}
[creating-a-token.md](creating-a-token.md)
{% endcontent-ref %}

{% content-ref url="markets-and-liquidity.md" %}
[markets-and-liquidity.md](markets-and-liquidity.md)
{% endcontent-ref %}

{% content-ref url="growing-your-community.md" %}
[growing-your-community.md](growing-your-community.md)
{% endcontent-ref %}

{% content-ref url="making-it-official.md" %}
[making-it-official.md](making-it-official.md)
{% endcontent-ref %}

{% content-ref url="managing-your-token.md" %}
[managing-your-token.md](managing-your-token.md)
{% endcontent-ref %}

{% content-ref url="playbooks.md" %}
[playbooks.md](playbooks.md)
{% endcontent-ref %}

{% hint style="info" %}
Connecting your wallet, buying BZE, moving tokens in from other chains, and choosing your fee token are shared across all the apps — see the [Using the Apps](../../using-the-apps/connecting-a-wallet.md) guides.
{% endhint %}

For the bigger picture of what token creators can build on BeeZee:

{% content-ref url="../../overview/features/creating-tokens.md" %}
[creating-tokens.md](../../overview/features/creating-tokens.md)
{% endcontent-ref %}
