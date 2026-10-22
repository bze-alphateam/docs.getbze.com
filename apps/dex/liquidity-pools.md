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

# Liquidity Pools

Every instant swap on BeeZee trades against a **liquidity pool**: a shared pot that holds two tokens so people can swap between them. Anyone can help fill those pots, and when you do, you earn a slice of the fees from every trade that passes through.

## How it works

A pool holds two tokens in balance, say $PAGE and BZE. Traders swap one for the other, and each swap pays a small fee, part of which is added back to the pool. When **you add liquidity**, you put in some of both tokens and receive **LP tokens** (the app also calls them **LP shares**). Think of them as a receipt for your share of the pool. Your share grows more valuable as fees pile up, and you can hand your LP tokens back any time to withdraw your share plus your earnings.

This is also what makes BeeZee's fee-token feature tick: once a token has a healthy pool paired with BZE, that token can be used to pay the network's fees, so a community can run entirely on its own token.

## Browsing pools

The **Pools** tab lists every pool. You can **search** by token symbol and **sort** by:

* **24h Volume**: how much has traded in the last day.
* **Total Liquidity**: how much is in the pool. Deeper pools mean smaller price impact on trades.
* **APR**: an estimate of the yearly return from fees, so you can compare pools at a glance.

Pools you're already in are gathered at the top under **My Pools** (with a **Manage** button), and everything else sits under **All Pools**.

## Inside a pool

Open any pool to see its **Pool Details**:

* **The two tokens and their Rate**: how much of each token the pool holds, and the price of one in the other, both ways round.
* **Total Liquidity**, **Volume (24h)** and **Fees (24h)**: how big the pool is, how much traded through it in the last day, and the fees that trading paid.
* **APR**: an estimate of the yearly return for liquidity providers, based on current conditions.
* **Locked Forever**: liquidity that has been sent to the Burner and can never be withdrawn by anyone. It's a strong sign of commitment, because that part of the pool can't be pulled out from under traders. Select **See in Burner App** to see it on the token's page there.
* **Locked in Boost Rewards**: liquidity that providers have locked into simple rewards (see [Boost Rewards](#boost-rewards) below).
* **Trading Fee**: the pool's fee on every swap, and how it's split between **LP Rewards** (you, the liquidity providers), **Protocol** (development and maintenance) and **Buyback & Burn**, which uses its share to buy back BZE and burn it.

Some pools also show a **Supported by BZE Community** box. It means the BZE Community validator on the other token's home chain puts its whole commission towards keeping this pool deep. If you hold that token on its home chain, **Delegate to BZE Community** lets you stake it there, earning staking rewards while helping this pool.

Once you've added liquidity, **Your Shares** shows your **LP Shares**, what they're worth in each token (**Shares Assets**), and any **Boost Rewards** waiting for you.

## Adding liquidity

1. Open the pool and choose the **Add Liquidity** tab.
2. Enter an amount for **one** side. The app fills in the matching amount of the other token automatically, to keep the pool balanced. **MAX** uses your whole balance, keeping the network fee back.
3. Check the preview: **Expected LP Tokens** is what you should receive, and **Minimum LP Tokens** is the least you'll accept. If the pool moves so much that you'd get fewer, the deposit is cancelled instead.
4. If you like, adjust **Slippage** with the settings icon: **0.5%** (the default), **1%**, **3%**, or a custom value. The app warns you if you go above 5%.
5. Confirm, and you receive **LP tokens** representing your share.

## Removing liquidity

1. Open the pool and choose the **Remove Liquidity** tab.
2. Pick how much to take out: drag the **Amount to Remove** slider, tap **25%**, **50%**, **75%** or **100%**, or type an exact number of LP shares (**MAX** takes them all).
3. The preview shows **You will receive** for each token, and **Minimum received** after your **Slippage Tolerance**, which you can change the same way as when adding.
4. Confirm, and your share of both tokens (including the fees you've earned) comes back to your wallet.

{% hint style="info" %}
**A word on impermanent loss.** When the two tokens' prices drift apart, the value of your deposit can end up a little lower than if you'd simply held the two tokens on their own. The fees you earn are there to make up for it, but it's an honest trade-off worth knowing before you add liquidity. Deep, steady pairs tend to feel it least.
{% endhint %}

## Boost Rewards

Some pools let you go a step further. In the **Boost Rewards** tab you can **lock your LP shares** into a simple reward to earn **extra token rewards** on top of your normal share of trading fees.

A pool can have several simple rewards at once, so start by choosing one under **Select a Simple Reward**. Each card shows:

* **Daily Distribution**: how much the reward shares out each day, between everyone locked in it.
* **Unlock Period**: how many days you wait for your LP shares after you unlock them.
* **Remaining Days**: how many of its days are left. Rewards marked **Ended** can't be joined.

Then enter the **Amount of LP Shares to Lock**. Simple rewards can set a **minimum**, and the app tells you if your first lock is below it. Before you commit, it shows your **Estimated Daily Rewards** (and the reward's new APR, if your stake changes it noticeably) along with the **Unlocking Period**. Select **Lock LP Shares** to join.

Your locked shares then appear under **Your Shares**, with what they're earning each day:

* **Claim** collects the boost rewards you've earned so far.
* **Unlock** starts the unlock period for your shares in that reward. They come back after the waiting time, and the countdown shows under **Your Shares** until they do.

Boost Rewards are simple rewards, so they're listed under **Simple rewards** on the DEX's **Staking** page too, so you can also follow, claim and unstake them from there.

{% hint style="warning" %}
**Locking has a lock-up.** While your LP shares are locked, you can't remove that liquidity, and when you decide to unlock there's a **waiting time** before you get them back, during which they earn nothing. You can unlock whenever you like, but the waiting time always applies. Only lock what you're comfortable leaving in place.
{% endhint %}

{% hint style="success" %}
**For example.** The book club seeds a **$PAGE–BZE** pool so members can swap in and out easily. A few keen members add liquidity, earn a cut of every trade, and then lock their LP shares in Boost Rewards to pick up extra $PAGE on top. And because the pool exists, members can now pay their fees in $PAGE too.
{% endhint %}

## Halted pools

If one of a pool's tokens is marked **Trading halted**, the pool shows a red badge, swaps no longer pass through it, and the **Add Liquidity** tab is replaced by a notice. Your existing position isn't stuck: you can still remove your liquidity at any time. See [Trading halted](assets.md#trading-halted).

{% hint style="info" %}
Starting a brand-new pool or market for a token that doesn't have one yet happens in **Token Factory**.
{% endhint %}

{% content-ref url="../token-factory/markets-and-liquidity.md" %}
[markets-and-liquidity.md](../token-factory/markets-and-liquidity.md)
{% endcontent-ref %}

{% content-ref url="../burner/coin-pages.md" %}
[coin-pages.md](../burner/coin-pages.md)
{% endcontent-ref %}
