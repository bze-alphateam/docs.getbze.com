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

# Getting a Token

Found a project you want to join? You don't have to go hunting for it on an exchange. Every token page in the [Communities app](https://communities.getbze.com) has its **own wallet**, dedicated to that token: get it, send it, burn it and collect your rewards without leaving the page.

## Opening the wallet

Select **Get TICKER** at the top of the page (or in the bar at the bottom on a phone), or the wallet button in the header. A drawer slides open, titled with the project's name, for example **Your Guild wallet**.

Not connected yet? The drawer asks you to **Connect wallet** first. Connecting works the same as in every BeeZee app.

{% content-ref url="../../using-the-apps/connecting-a-wallet.md" %}
[connecting-a-wallet.md](../../using-the-apps/connecting-a-wallet.md)
{% endcontent-ref %}

## Your balance and rewards

Once connected, the drawer opens with a card showing your **balance** of the token, its value in dollars when it has a price, and your address with a **Copy** button. Underneath, it adds up what you have elsewhere:

* **Holders pool**: what you stake in the token's holders pool.
* **Programs**: what you stake in its fixed-term programs.
* **Unlocking**: what's on its way back to you after an unstake.

When you have rewards waiting, a **Rewards ready** row lists them, in every prize token, and tells you where they come from (the pool, one or more programs). **Claim all** collects them all in a single transaction.

## Get: buy the token with an instant swap

The **Get TICKER** tab swaps something you already hold into the token:

1. Choose what to **Pay with**: any token in your wallet that can be swapped into this one.
2. Enter **You pay** (or tap **Max**) and see **You get**.
3. Check the **Price impact** (how much your own purchase moves the price) and the **Network fee**.
4. Pick your **Max slippage**: if the price moves against you by more than that before the swap settles, it's cancelled instead of going through at a bad rate.
5. Select **Get TICKER** and confirm in your wallet.

It's the same swap as the **Buy** side of the page's Trade section. If the token isn't in any liquidity pool yet, the tab says **Not tradable yet** instead.

## Send

The **Send** tab sends this token, and only this token, to another BeeZee address. Enter the **Recipient** and the **Amount** (**Max** keeps the network fee aside when you pay fees in the token), then confirm.

{% hint style="warning" %}
**Check the address twice.** Tokens sent to a wrong address can't be recovered.
{% endhint %}

## Burn

The **Burn** tab is the same burn form as the page's Burn section: enter the **Amount to burn**, check it, and confirm. Your tokens are queued for the next burn and destroyed for good.

{% hint style="danger" %}
**A burn can't be undone.** Only burn what you're happy to see gone for good.
{% endhint %}

## Other assets and settings

At the bottom of the drawer, **Other assets in this wallet** lists everything else you hold, the most valuable first (**Show** opens the list). Next to it are **Settings** and **Disconnect**.

**Settings** opens a panel of its own, even when you're not connected:

* **Appearance**: a **Dark mode** switch. The page switches to the dark colours of the token's brand kit.
* **Network fees**: the **Pay network fees in TICKER** switch, when the token can pay fees (see below).
* **Connection**: the connection status, and the **REST endpoint** and **RPC endpoint** the page uses. Advanced users can point it at their own node: **Validate** checks the addresses, **Save** keeps them, and **Reset to defaults** brings back the standard ones.

These settings are shared with the rest of the Communities app.

## Paying fees in the community's token

Every action costs a small network fee. On a token's page, that fee is paid **in the token itself, by default**, whenever the token can pay fees. Visitors can take part in everything the project offers without ever holding BZE; to them, it feels like the token's own network.

A token can pay fees when it has a liquidity pool paired with BZE that holds enough BZE (a minimum set by the network), and its trading isn't paused.

* **Prefer BZE?** Turn off **Pay network fees in TICKER** in **Settings**. The page remembers that choice for this token, in this browser.
* **Leaving the page puts BZE back.** Paying in the token only applies while you're on its page. When you go back to the directory or open another token, fees return to BZE (or to that other token). Even if you close the browser on a token page, the Communities app switches you back to BZE the next time you open the directory.

{% hint style="info" %}
**When the token can't pay fees yet.** If the token doesn't have a deep enough BZE pool, the page tells you plainly: the swap panels explain that the token runs on the BeeZee network and that each transaction needs a small amount of BZE for the network fee, the wallet shows **Network fees are paid in BZE** with how much you have available, and the footer shows **Runs on BeeZee**. A **Get BZE** button, when available, opens a panel to buy BZE with a coin from another network: choose the network to **Pay from**, the **Asset to pay with** and the amount, then see what **You get about** and when it **Arrives in**, usually within minutes.
{% endhint %}

{% content-ref url="../../overview/features/fee-token.md" %}
[fee-token.md](../../overview/features/fee-token.md)
{% endcontent-ref %}

{% hint style="success" %}
**For example.** A friend sends you the book club's page. You connect, open **Get PAGE**, pay with some BZE you had, and in a moment the drawer shows your new **$PAGE** balance. Now that you hold $PAGE, the fee for staking it is paid in $PAGE too: you never have to think about BZE. A week later, **Rewards ready** shows a little $PAGE and BZE, and **Claim all** brings them home.
{% endhint %}

Don't hold anything on BeeZee yet? You can also bring in funds from another network first:

{% content-ref url="../../using-the-apps/buying-bze.md" %}
[buying-bze.md](../../using-the-apps/buying-bze.md)
{% endcontent-ref %}
