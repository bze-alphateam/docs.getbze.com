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

# Burning Raffles

A burning raffle is a way to help burn a coin and maybe get a little something back for it. It's a contribution, not a bet: what you put in goes into the raffle's **pot**, and whatever is left in the pot when the raffle ends is **burned**. Along the way, each contribution gives you a chance to win a share of that pot. Win or not, you've helped take coins out of supply.

## How a raffle works

Raffles aren't started from the Burner app: they're created in the Factory (see [Run a burning raffle](../token-factory/growing-your-community.md#run-a-burning-raffle)). Whoever starts one picks the coin, puts up the starting pot and chooses the raffle's settings: the price of a contribution, the chance of winning, the share of the pot a winner receives and how long it runs. The Burner app then lists every raffle that's running.

From there:

1. **You contribute.** Each contribution costs a fixed price in the raffle's coin, and it goes into the pot.
2. **Each contribution is drawn on its own.** The network draws your first contribution 2 blocks after you join, then the next one in the following block, and so on, one per block. Five contributions means five separate draws.
3. **Winners take a share of the pot.** A winning contribution receives a percentage of the pot as it stands at that moment, paid straight to your wallet. A contribution that doesn't win stays in the pot, so the prize grows as people take part.
4. **The rest is burned.** When the raffle ends, everything still in the pot is destroyed.

Your chance is shown as "**1 in N**", and it applies to **each contribution**: with a 1 in 10 chance, every contribution you make has its own 1 in 10 chance to win. More contributions give you more chances, but never a guaranteed win.

{% hint style="warning" %}
**Only contribute what you're happy to burn.** Your contributions can't be taken back, and any one of them may well not win. Think of the prize as a thank-you, not something to count on.
{% endhint %}

## Finding raffles

Click **Raffles** in the top menu (or **Join a raffle** on the home page) to open **Burning raffles**. The raffles that are running come first, under **Active raffles**. Each card shows the coin, the **time left**, your **chance**, the current **Prize** and the price of one **Contribution**.

Below the list, **What are burning raffles?** explains how raffles work. It ends with a link to the **Factory**, in case you'd like to run a raffle for your own token.

Click a raffle card (**Click to contribute**) to open that coin's page, where you join. When nothing is running, the page says **No Active Raffles**.

## Taking part

1. On the coin's page, find the **Burning raffle** section and click **Join raffle**.
2. The form shows the **Current prize**, **Your chance** and your **Available Balance**.
3. Enter the **Number of Contributions**. The price per contribution is shown underneath, and **Total Cost** adds it up for you.
4. Click **Join raffle** and approve in your wallet.

New contributions stop being accepted in the last couple of hours before a raffle ends.

## Seeing your results

As your draws happen, a full-screen animation on the coin's page reveals them one by one ("Contribution 1 of 5", then the next), showing **YOU WON!** with the amount, or better luck next time. When every draw is done, a **Summary** shows your total won and how many contributions won and lost.

{% hint style="info" %}
**You don't have to watch.** Close the animation whenever you like. As long as the Burner app stays open, each result still arrives as a notification, followed by a final summary. Any winnings are paid to your wallet either way.
{% endhint %}

## Winners

Each coin's raffle section shows **Total won** so far and by how many winners, plus a list of the latest winners. Your own wins are tagged **YOU**, so they're easy to spot.

{% hint style="success" %}
**For example.** The gaming guild starts a raffle on **$GUILD** to celebrate a new season. Members join with a few contributions each, and every contribution that doesn't win makes the pot (and the prize) a little bigger. A handful of members win a share along the way, and when the raffle ends, everything left in the pot is burned. The community ends the event with less $GUILD in supply and a bit of shared fun.
{% endhint %}

{% hint style="info" %}
You'll need a connected wallet to join a raffle. Connecting your wallet is shared across all the apps; see [Connecting a Wallet](../../using-the-apps/connecting-a-wallet.md).
{% endhint %}

{% content-ref url="coin-pages.md" %}
[coin-pages.md](coin-pages.md)
{% endcontent-ref %}
