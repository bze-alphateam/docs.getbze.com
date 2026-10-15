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

# Swapping Tokens

Swapping is the simplest way to trade on BeeZee: pick what you have, pick what you want, and the app handles the rest in a single click. It's the home page of the DEX, and for most people it's all they'll ever need.

## Making a swap

1. **Choose your "From" token**, the one you're paying with. The picker is searchable and shows your balances, so you always know what you can spend.
2. **Choose your "To" token**, the one you want to receive. The round arrow button between the two swaps them around.
3. **Enter an amount.** Type how much you want to spend, or use **MAX** and the **25% / 50% / 75% / 100%** shortcuts to spend part or all of your balance. You can also type the amount you'd like to *receive*, and the app works backwards to fill in the rest.
4. **Select Swap.** Your wallet asks you to approve, and the swap settles on the blockchain. No middleman ever holds your funds.

{% hint style="info" %}
**MAX and the percentage buttons keep the network fee back.** When you're spending the same token you pay fees with, they leave enough behind to cover the fee, so the swap doesn't fail for want of a few cents.
{% endhint %}

Behind the scenes, your swap trades against **liquidity pools**: shared pots of two tokens that anyone can trade between. The app automatically finds the best path for your trade, and sometimes hops through several pools to get you a better result. Open **Trade Route** to see the tokens it passes through and each pool's fee along the way.

## What you see before you confirm

Swapping is instant, but you're never trading blind. As soon as you enter an amount, a summary shows:

* **Minimum Output**: the least you'll receive once your slippage protection (below) is taken into account. If the price moves so much that you'd get less, the swap is cancelled instead.
* **Price Impact**: how much your own trade moves the price. Smaller is better; it turns yellow, then red, as it grows. A big number usually means the pool is small compared to your trade.
* **Swap Fee**: the pool's trading fee, which goes to the people who provide its liquidity (and, depending on the pool, to the protocol and to buyback & burn).
* **Taker Fee**: a small flat fee every swap pays to the network, currently 0.1 BZE, as shown in the app. If you've chosen another token for fees in Settings, the app shows roughly what it costs in that token. Click **Taker Fee** for the details, including the estimated **network fee** your swap pays on top.
* **Rate**: how much of the "To" token you get for one "From" token.

### Max slippage

Prices can move in the moment between quoting your swap and settling it. **Max slippage** is your safety net: it sets how far the price may move against you before the swap is cancelled. It sits right in the **Minimum Output** line ("0.5% max slippage · Change"); select **Change** and pick **0.1%**, **0.5%**, **1%** or **2%**, or type a **Custom %** of up to 50%.

The default is 0.5%. Whatever you choose is remembered on this device for 30 days after your last change, so you don't have to set it again each visit.

Tighter protection is safer, but in a fast-moving or thinly traded market a very tight setting may cause swaps to fail. Loosen it a little if that happens, and keep an eye on **Minimum Output** as you do.

{% hint style="success" %}
**For example.** Your book club runs on **$PAGE**. A member wants some to join in, so they open the DEX, choose BZE as the "From" token and $PAGE as the "To" token, tap **50%**, check the **Minimum Output**, and confirm. The app routes it through the $PAGE–BZE pool and their $PAGE lands in seconds, with no need to hunt for a market or set a price.
{% endhint %}

## When a swap can't go through

The app tells you plainly what's happening:

* **Insufficient Balance**: you don't have enough of the "From" token for the amount entered. Lower the amount or top up.
* **Not enough left for fees**: you have the amount itself, but not the network and taker fees on top of it. Lower the amount a little (or use **MAX**, which works this out for you).
* **No Route Found**: there's no pool, or chain of pools, connecting those two tokens yet. Try a different pair, or someone can create a pool for it in Token Factory.

Tokens marked **Trading halted** don't appear in the swap pickers at all, and routes never pass through their pools. See [Trading halted](assets.md#trading-halted) for what that means.

## Your recent swaps

With your wallet connected, **Your Recent Swaps** keeps a running history of what you've traded, so you can glance back at what went through without leaving the page.

{% hint style="info" %}
Connecting your wallet, buying BZE, choosing your fee token and moving tokens in from other chains are shared across all the apps. See the [Using the Apps](../../using-the-apps/connecting-a-wallet.md) guides, and [Fees & Settings](../../using-the-apps/fees-and-settings.md) for paying fees in another token.
{% endhint %}
