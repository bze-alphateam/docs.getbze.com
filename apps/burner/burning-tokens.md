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

# Burning Tokens

Burning means permanently destroying coins so they can never be used again. Every coin burned is gone for good, which lowers the amount in circulation. The Burner app is where BeeZee does this in the open, for anyone to see and take part in.

## Burning coins you hold

1. On the home page, click **Burn coins**.
2. **Pick a token** under **Select Token to Burn**. The list shows every token in your wallet with its balance, and once you pick one you see your **Available Balance**.
3. **Enter an amount**, or click **MAX** to fill in all of it. When the token is the one you pay network fees with (normally BZE), MAX leaves just enough behind to cover the fee.
4. Check the **You're about to burn** preview, then click **Burn it!** and approve in your wallet.

You can also burn from a coin's own page, where the coin is already picked for you. See [Coin Pages](coin-pages.md).

{% hint style="danger" %}
**Burning is permanent: no take-backs.** Once you confirm, those coins are gone forever. Nobody, including you, can recover them or undo the burn. Only burn what you truly mean to destroy.
{% endhint %}

## When the burn actually happens

Burning isn't instant. When you burn coins, they go into **the pot** and wait there until the next **scheduled burn**. The network runs that burn automatically every few weeks (how often is set by the network, currently every 4 weeks), and everything in the pot is destroyed together.

The home page shows what is waiting and when it goes:

* **Next burn in**: a live countdown to the next scheduled burn, in days, hours, minutes and seconds. When the pot is empty, it reads **No burning scheduled**.
* **Coins in the pot**: how many different coins are waiting for that burn.
* **Ready to Burn**: a card for every coin waiting in the pot, with the amount and its approximate value in US dollars. Click a card to open that coin's page.

## Not every coin burns the same way

This part surprises people, so here it is plainly. Depending on the kind of coin, the pot does one of three things:

* **BZE and community-created tokens are burned.** They're destroyed on the next scheduled burn.
* **Liquidity pool (LP) tokens are locked, not burned.** An LP token is a receipt for a share of a trading pool, so instead of being destroyed it's **locked forever** in an address nobody can ever move it from. The effect is the same: those tokens are out of circulation for good.
* **Bridged (IBC) tokens are swapped first.** A bridged token came from another blockchain, so it can't be destroyed here. Instead, the network swaps it to BZE and burns that BZE. This only works when the token has enough liquidity paired directly with BZE.

{% hint style="warning" %}
**Locking is just as final as burning.** On an LP token's page the button reads **Lock** instead of **Burn**, but the form that opens still says **Burn it!**, and from the **Burn coins** button on the home page it always does. Either way, LP tokens you send can never be recovered.
{% endhint %}

## What the home page shows

Below the countdown, the home page is a live picture of everything taken out of supply:

* **Total BZE incinerated**: all the BZE burned so far, with its approximate value in US dollars.
* **Total value locked forever**: the US dollar value of the LP tokens and other coins locked away for good. The **Forever Locked** table lists them, with **Coin**, **Name**, **Amount locked** and **USD value**.
* **Burn History Book**: the most recent burns, one row per coin, with the columns **Coin**, **Name**, **Amount burned** and **Block height**. Under each amount you'll see its approximate value, and under each block number the date of the burn.

Click any coin in these lists to open its page.

{% hint style="info" %}
**Dollar values use today's prices.** The US dollar amounts in the burn history (and everywhere else in the app) are worked out from each coin's current price, not the price on the day it was burned.
{% endhint %}

## Where do burned coins come from?

Not all burning is manual. Part of the fees collected across the whole BeeZee ecosystem is routed to the pot automatically, and the scheduled burn destroys it along with everything else. So supply keeps gently shrinking in the background, even when nobody is burning coins by hand. Your own burns simply add to that steady drip, and so do [burning raffles](burning-raffles.md), whose leftover pots are burned when they end.

{% hint style="success" %}
**For example.** The book club wraps up its reading year and decides to burn a stack of unused **$PAGE** from its treasury. A member clicks **Burn coins**, picks $PAGE, enters the amount and confirms. The $PAGE shows up under **Ready to Burn**, and when the countdown hits zero it's destroyed together with everything else in the pot, then appears in the **Burn History Book** for every member to see.
{% endhint %}

{% hint style="info" %}
You'll need a connected wallet before you can burn anything. Connecting your wallet is shared across all the apps; see [Connecting a Wallet](../../using-the-apps/connecting-a-wallet.md).
{% endhint %}

{% content-ref url="coin-pages.md" %}
[coin-pages.md](coin-pages.md)
{% endcontent-ref %}

{% content-ref url="../../overview/features/token-burning.md" %}
[token-burning.md](../../overview/features/token-burning.md)
{% endcontent-ref %}
