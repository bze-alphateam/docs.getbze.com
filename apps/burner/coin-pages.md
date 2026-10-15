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

# Coin Pages

Every coin has its own page in the Burner app, with everything about that coin's burns in one place. To open one, click a coin anywhere in the app (a **Ready to Burn** card, a row in the burn history or the locked list, a raffle), or use **Search Coin** in the top menu and type a name or ticker. Verified coins are listed first in the search.

## The top of the page

The page opens with the coin's logo, ticker and name, plus its coin ID. A green **✓ Verified** badge appears when the coin has been checked, which helps you tell a well-known token from a look-alike.

Next to it is the coin's action button:

* **Burn** followed by the ticker, for BZE, community tokens and bridged tokens.
* **Lock** followed by the ticker, for liquidity pool (LP) tokens, which are locked forever instead of burned.

The button opens the same burn form as the home page, with this coin already picked. See [Burning Tokens](burning-tokens.md) for how the form works.

{% hint style="info" %}
**While a coin has a raffle running, its Burn button disappears.** Instead, you'll see the raffle section with a **Join Raffle** button, so your coins go into the raffle's pot. See [Burning Raffles](burning-raffles.md).
{% endhint %}

## What each kind of coin shows

The rest of the page depends on the kind of coin.

**LP tokens** show **About Locking LP Coins**, a short note explaining that these coins are locked forever in a secure address rather than burned, and a **Forever Locked** card with how much of this coin is already locked and its approximate value.

**Bridged (IBC) tokens** show **About Burning IBC Coins**: since they come from another blockchain, the network swaps them to BZE and burns that BZE instead, and only when the token has enough liquidity paired directly with BZE. Because what gets burned is BZE, these pages don't keep a burn total of their own.

**BZE and community tokens** show:

* **Total burned** (for example **Total BZE Burned**): everything of this coin burned so far, labelled **All Time**, with its approximate value in US dollars.
* **Recent Burns**: a table of this coin's burns with **Amount Burned**, **USD Value**, **Block Height** and **Time**. If the coin has never been burned, you'll see **No Burns Yet** and a button to be the first.

{% hint style="info" %}
**Dollar values use today's prices.** The USD amounts on this page, including the value of past burns, are worked out from the coin's current price, not its price on the day it was burned.
{% endhint %}

## The next burn or lock

When some of this coin is waiting in the pot, a **Next Burning** card (or **Next Locking**, for LP tokens) shows how much will go on the next scheduled burn, its approximate value, and the date and time it happens in your local time.

## The raffle section

When the coin has a burning raffle running, a **Burning Raffle** section appears near the top with:

* The raffle's name, the **time left** and your **chance** of winning with each contribution, written as "1 in N".
* **Prize**: what a winning contribution receives right now.
* **Contribution**: the price of one contribution.
* **Total Won**: how much winners have taken from the pot so far, and by how many winners.
* A list of the **latest winners**, with your own wins tagged **YOU**.

The **Info** button explains how burning raffles work, and **Join Raffle** opens the form to take part. [Burning Raffles](burning-raffles.md) covers it all step by step.

{% hint style="success" %}
**For example.** A $GUILD member wants to see how much the guild has burned this season. They open **Search Coin**, type *GUILD* and pick the verified **$GUILD**. Its page shows **Total GUILD Burned** for all time, the **Recent Burns** table, and a **Next Burning** card for the $GUILD sitting in the pot right now. A raffle is running too, so instead of a Burn button there's **Join Raffle**.
{% endhint %}

{% content-ref url="burning-tokens.md" %}
[burning-tokens.md](burning-tokens.md)
{% endcontent-ref %}

{% content-ref url="burning-raffles.md" %}
[burning-raffles.md](burning-raffles.md)
{% endcontent-ref %}
