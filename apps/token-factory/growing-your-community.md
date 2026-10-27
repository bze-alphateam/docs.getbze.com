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

# Growing Your Community

A token becomes a community when people have a reason to hold it, and when new people discover it. Two starting points on the Token Factory home do exactly that:

* **Create staking rewards**: pay people for staking a token, with a **Compounded reward** or a **Simple reward**.
* **Grow a community**: **Airdrop tokens** to a list of wallets, to a token's stakers or to a pool's liquidity providers, or run a **Burning raffle**.

{% hint style="info" %}
**It works for any token, not only yours.** Making a token stakable, daily prizes, airdrops, extending a reward: anyone can do these for any token on BeeZee. Paying for them doesn't make you the reward's owner, and it gives you no special rights over it.
{% endhint %}

Every flow ends on a Review that shows what leaves your wallet before you sign. Creation fees are set by the network and can change through governance, so the app always reads the current amount; check the **You will pay** panel (or a [block explorer](https://explorer.getbze.com/)) rather than relying on a fixed number.

Which actions have a fee, and where it goes: see [Rewards Parameters](../../overview/parameters/rewards.md).

## Simple or compounded?

Pick **Create staking rewards** and the **Choose** screen asks **Which kind of reward?** Both pay people who stake a token. It can be any token, pool shares (LP tokens) included, and it doesn't have to be yours. Each option shows its creation fee.

The **Compounded reward** is marked **Recommended**: it can do what a simple reward does and more later, while a simple reward can never change or become compounded. If you pick **Simple reward**, the app asks you to confirm first: **I understand, continue**, or **Create compounded reward** instead.

|                     | Simple reward                                         | Compounded reward                                              |
| ------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| **Reward tokens**   | One                                                   | Many, from anyone                                              |
| **You fund**        | Everything up front: the daily budget × the days      | Optional at creation; add daily prizes or airdrops any time    |
| **How long**        | A set number of days                                  | No end: it lasts as long as someone adds prizes                |
| **Per token**       | As many as people create                              | Only one per staked token                                      |
| **Leaving**         | A wait you choose (0 days or more)                    | A wait set by the network                                      |
| **Best for**        | Campaigns with an end date, rewarding liquidity       | Making a token stakable for good                               |

To add to a reward that already exists, find it in [Rewards](#the-rewards-directory) or on its token's page.

## Simple reward

A **simple reward** is a campaign: people stake one token for a set number of days and share a daily amount you pay for up front. It's the classic way to reward **liquidity providers**: they stake the LP tokens they got from adding to your pool.

1. **Stake: which token?** Any token, LP tokens included.
2. **Reward: what do they earn?** The **reward token** (paid from your wallet), the **daily reward** and for how many **days** (1 to 36,500). Each day's amount is split between all stakers, by how much each stakes.
3. **Rules: any conditions?** The **unstaking lock** in days (0 means people can leave any time) and an optional **minimum stake**.
4. **Review**: you pay the creation fee and the whole budget.

Select **Create simple reward** and confirm. People stake it on the [DEX Staking page](../dex/staking-and-earning.md) or on the token's page in the [Communities app](../communities/staking-programs.md); the Done screen recommends **Stake on DEX**, where you can see the reward live and share its link.

{% hint style="danger" %}
**The whole budget is committed when you sign.** The daily amount × the number of days leaves your wallet at once and is paid to stakers day by day. It can't be withdrawn, and the daily amount and the rules can never change.
{% endhint %}

### Extend a simple reward

Any running simple reward can be extended with more days, by anyone. Select **Extend** on the reward, in [Rewards](#the-rewards-directory) or on its token's page.

1. **Reward: which reward?** It shows what people stake, the daily reward and its end date.
2. **Extra days: how many more days?** The daily reward stays the same; you pay for the extra days up front, and the step shows the **new end date**.
3. **Review**: you pay the extra rewards. There is no creation fee.

{% hint style="info" %}
**Paying for days doesn't make you its owner.** Anyone can extend any simple reward, and extending it doesn't let you change it.
{% endhint %}

Once a simple reward has finished and every staker has left, anyone can **Delete** it to tidy up; nothing is paid out and nothing is lost.

## Compounded reward

A **compounded reward** makes a token stakable for good: there is one per token, and anyone can add prizes for its stakers, in any token, every day or once.

1. **Stake: which token?** Search for it in the list, LP tokens included. Two facts set by the network appear, fixed once it's created: the **unstaking lock**, and the **minimum stake** (often none). If the token is already stakable, **Continue to add a prize** takes you to adding a daily prize to it instead.
2. **First daily prize: add a reward for stakers?** Choose **Not now**, or **Add a daily prize** right away (see below). Stakers earn nothing until someone adds a prize.
3. **Review**: the creation fee, plus the first prize if you added one.

Select **Make TICKER stakable** and confirm. Holders stake it on the [DEX Staking page](../dex/staking-and-earning.md) or on the token's page in the [Communities app](../communities/holders-pool.md). The Done screen recommends **Stake on DEX**, and offers **Add more rewards** for another daily prize.

{% hint style="warning" %}
**A compounded reward can't be removed.** There is one per token, for good. Starting it gives you no special rights: anyone can add prizes to it.
{% endhint %}

### Add a daily prize

A compounded reward on its own pays nothing; a **daily prize** gives stakers something to earn.

Select **Add daily prize** on a compounded reward, in [Rewards](#the-rewards-directory) or on its token's page.

1. **Stake: which token?** Any token with a compounded reward, yours or not.
2. **Prize: what do they get every day?** The **reward token** (paid from your wallet; it can be your own token, BZE or any other), the **daily reward** and the number of payout **days** (1 to 36,500). Days with nobody staking are skipped, so a prize can run longer than its length in calendar days.
3. **Review**: you pay the daily reward × the days now, plus a one-time daily prize fee (and the new prize fee below, if it applies).

Select **Start daily prize** and confirm. Each day the prize is split between everyone staking, in proportion to their stake. Any running daily prize can be extended too: **Extend** adds days at the same daily reward, with no fee, and anyone can do it.

{% hint style="danger" %}
**The whole prize is locked when you sign.** It can't be cancelled or withdrawn, so pick amounts you are happy to give away.
{% endhint %}

### Prize tokens and the new prize fee

Each compounded reward can pay a limited number of different prize tokens, set by the network. The first time a token becomes a prize there, it takes one of those **prize slots** for good and you pay a one-time **new prize fee**. Paying with that same prize token again later, by you or anyone, has no prize fee. The step tells you which case applies before you sign, and stops you if all the slots are taken by other tokens.

## Airdrop tokens

**Airdrop tokens** puts tokens in many wallets at once. Pick **Grow a community** → **Airdrop tokens** on the home page, or **Airdrop** on any reward. The first step asks **Who gets the tokens?**

* **A list of wallets**: contest winners, early supporters, a snapshot of holders, a spreadsheet of bounty hunters.
* **Stakers of a token**: everyone staking a token **right now**, yours or not.
* **Liquidity providers**: everyone staking a pool's LP shares.

An airdrop is a one-time thank-you: it doesn't start a daily prize, and it can't be undone.

### To a list of wallets

There is no Token Factory fee, only the network fee.

1. **Token: what are you sending?** Any token your wallet holds.
2. **List: who gets it?** Choose how much each wallet gets:
   * **Same amount for everyone**: one amount, and wallets one per line.
   * **Amount per wallet**: one `address, amount` per line.

   Paste the list or upload a CSV or TXT file (up to 1 MB); the app offers an example file for each format. A list can hold up to 5,000 wallets. The app checks every line as you go: duplicates are merged, and **lines to fix** are left out until you correct them. Only BeeZee addresses (`bze1…`) work.
3. **Review**: the total sent to wallets and, for a long list, the number of transactions.

Select **Airdrop to N wallets** and confirm.

{% hint style="warning" %}
**Check the list twice.** Sent tokens can't be taken back, and tokens sent to a wrong address can't be recovered.
{% endhint %}

Up to 100 wallets go in one transaction. A longer list is sent in several, and your wallet asks you to approve each one. You can **Stop for now** at any time, or even close the page: your list and progress are kept in this browser for 30 days, and the home page offers to continue where it stopped. Wallets already paid won't be paid twice.

When it's done, the Done screen lets you **Download the report**: every address, its amount, whether it was sent, and the transaction.

### To stakers or liquidity providers

The airdrop is split between everyone staking the token right now, based on how much each one stakes.

1. **Stake: which token?** (or **which LP shares?**) Any token people can stake, yours or not.
2. **Reward**: when the token has more than one staking reward, pick which reward's stakers get it. Each option shows how much is staked in it.
   * Through the **compounded reward**, you can send any token.
   * Through a **simple reward**, you can send only that reward's own reward token: a one-time top-up for its stakers on top of the daily amount. It works even after the reward has finished, as long as people still stake in it.
3. **Amount: how much?** The token and the amount, paid from your wallet.
4. **Review**: the amount is shared among the stakers right away.

Select **Airdrop** and confirm. Through a simple reward there is no Token Factory fee. Through a compounded reward, the only fee is the new prize fee, and only if this is a new prize token for that reward.

{% hint style="info" %}
**Somebody has to be staking.** A reward nobody stakes in can't be picked, and the app checks again right before you sign, so nothing leaves your wallet when there's no one to pay. If the token has no staking reward at all, the app offers to create one.
{% endhint %}

### Reach another community

Airdropping to the stakers of a *different* token is a way to be discovered: your token lands in the wallets of people who are already active, and shows up as a prize on that token's Communities page. You don't need to own that token or ask its creator. Gift it once with an airdrop to its stakers, or every day with a [daily prize](#add-a-daily-prize) on its compounded reward, so new stakers get some too. If your token isn't stakable yet, make it stakable as well, so the people you reach have a reason to stay.

Adding a prize to another token's compounded reward doesn't make you its owner.

{% hint style="success" %}
**For example.** The book club makes **$PAGE** stakable first, so newcomers have a reason to keep it. Then it reaches the gaming guild: a 30-day $PAGE daily prize for everyone staking **$GUILD**. Every guild member who stakes now earns a little $PAGE each day, and finds the book club through it.
{% endhint %}

## Run a burning raffle

A **burning raffle** turns a prize pot into a game that also burns tokens. You fund the pot; people buy tickets on the [Burner](../burner/burning-raffles.md) for a chance to win part of it. Losing tickets make the pot bigger, and whatever is left at the end is **burned**. It's a way to contribute to a token and its community, not a bet you can win back: nothing returns to you.

1. **Token: which token?** Any token can be raffled, except halted ones, and each token can have only one raffle running at a time.
2. **Starting pot: how big is it?** It leaves your wallet now.
3. **How it plays: how does it play?** How many **days** it runs (1 to 180), the **ticket price**, the **win chance** (1 in N tickets wins) and what share of the pot a **winner gets** (%). Presets help you pick each one. For example: for 7 days, a ticket costs 10 $GUILD and has a 1 in 100 chance to win 50% of the pot.
4. **Review**: there is no Token Factory fee. Select **Start raffle** and confirm; the Done screen links to the raffle on Burner.

{% hint style="danger" %}
**A raffle can't be stopped or changed.** The pot leaves your wallet when you start, and whatever is left when it ends is burned. Nothing comes back to you.
{% endhint %}

## The Rewards directory

**Rewards**, in the top menu, lists every staking reward on BeeZee, grouped by the token people stake. You don't need a wallet to browse it, and anyone can extend or add to any of them. **Create a reward** at the top starts a new one.

* **Search by staked token**: find rewards by the token people stake.
* **Kind**: **All**, **Compounded** or **Simple**.
* **Filter**: **Any**, **Has stakers**, **Paying daily**, **Yours** (rewards on tokens you created), **Running** or **Finished**.
* **Sort**: **Most staked (USD)**, **Most prize tokens** or **A–Z**.

Each staked token is one compact row: what it earns, how much is staked and how many rewards it has. Open it to see its compounded reward first, then its simple rewards. Each reward has a short summary line (its unstaking lock, minimum stake and status, such as **Paying daily**, **Airdrops only**, **Running**, **Waiting for stakers** or **Finished**) and a **DEX** link that opens its page on the DEX.

* A **compounded reward** lists its daily prizes (for example "500 $PAGE / day · 16 / 30 days"), each with **Extend**, or **Nothing scheduled**. Its actions are **Add daily prize** and **Airdrop**.
* A **simple reward** shows its number, its daily amount and how many days have been paid, with **Extend**, **Airdrop** once someone stakes it, and **Delete** once it has finished and is empty.
* A token without a compounded reward offers **Make TICKER stakable** (LP shares excepted).

{% hint style="info" %}
**No owners, no staker counts.** The network doesn't record who created or funded a reward, so the directory never claims anyone owns one. It shows how much is staked (and its value in dollars when it has a price), not how many people stake.
{% endhint %}

{% hint style="success" %}
**For example.** The gaming guild has a $GUILD/BZE pool and wants it deeper. It creates a 30-day simple reward: stake the $GUILD/BZE LP token, share a daily $GUILD amount. Players who add liquidity now earn twice, from the pool's trading fees and from the reward. When it nears its end, a guild member extends it from **Rewards**.
{% endhint %}

{% content-ref url="playbooks.md" %}
[playbooks.md](playbooks.md)
{% endcontent-ref %}
