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

* **Create staking rewards**: pay people for staking a token, with a **Simple reward** or a **Compounded reward**.
* **Grow a community**: **Airdrop to stakers**, **Send to a list of wallets**, **Run a burning raffle** or **Reach another community**.

{% hint style="info" %}
**It works for any token, not only yours.** Making a token stakable, daily prizes, airdrops, extending a simple reward: anyone can do these for any token on BeeZee. Paying for them doesn't make you the reward's owner, and it gives you no special rights over it.
{% endhint %}

Every flow ends on a Review that shows what leaves your wallet before you sign. Creation fees are set by the network and can change through governance, so the app always reads the current amount; check the **You will pay** panel (or a [block explorer](https://explorer.getbze.com/)) rather than relying on a fixed number.

Which actions have a fee, and where it goes: see [Rewards Parameters](../../overview/parameters/rewards.md).

## Simple or compounded?

Pick **Create staking rewards** and the **Choose** screen asks **Which kind of reward?** Both pay people who stake a token. It can be any token, pool shares (LP tokens) included, and it doesn't have to be yours.

|                     | Simple reward                                         | Compounded reward                                              |
| ------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| **Reward tokens**   | One                                                   | Many, from anyone                                              |
| **You fund**        | Everything up front: the daily budget × the days      | Optional at creation; add daily prizes or airdrops any time    |
| **How long**        | A set number of days                                  | No end: it lasts as long as someone adds prizes                |
| **Per token**       | As many as people create                              | Only one per staked token                                      |
| **Leaving**         | A wait you choose (0 days or more)                    | A wait set by the network                                      |
| **Best for**        | Campaigns with an end date, rewarding liquidity       | Making a token stakable for good                               |

Below the two options, **Add to a reward that already exists** has three shortcuts: **Extend a simple reward**, **Add a daily prize**, and **Airdrop to stakers, once**.

## Simple reward

A **simple reward** is a campaign: people stake one token for a set number of days and share a daily amount you pay for up front. It's the classic way to reward **liquidity providers**: they stake the LP tokens they got from adding to your pool.

1. **What to stake: which token do people stake?** Any token, LP tokens included.
2. **Reward & budget: what do they earn?** The reward token (paid from your wallet), the amount **shared every day** and **for how many days** (1 to 36,500). Each day's amount is split between all stakers, by how much each stakes.
3. **Rules: any conditions?** The **wait after unstaking** in days (0 means people can leave any time) and an optional **minimum stake**.
4. **Review**: the creation fee and the whole budget leave your wallet.

Select **Create simple reward** and confirm. People stake it on the [DEX Staking page](../dex/staking-and-earning.md) or on the token's page in the [Communities app](../communities/staking-programs.md); the Done screen gives you a staking link to share.

{% hint style="danger" %}
**The whole budget is committed when you sign.** The daily amount × the number of days leaves your wallet at once and is paid to stakers day by day. It can't be withdrawn, and the daily amount and the rules can never change.
{% endhint %}

### Extend a simple reward

Any running simple reward can be extended with more days, by anyone. Open **Extend** on the reward (in [Rewards](#the-rewards-directory) or on its token's page), or **Extend a simple reward** from the Choose screen and search by staked token.

1. **Reward: which reward?** It shows what people stake, the daily amount and the days left.
2. **Extra days: how many more days?** The daily amount stays the same; you pay for the extra days up front.
3. **Review**: the extra tokens leave your wallet, and you see the new end date. There is no creation fee.

{% hint style="info" %}
**Paying for days doesn't make you its owner.** Anyone can extend any simple reward, and extending it doesn't let you change it.
{% endhint %}

Once a simple reward has finished and every staker has left, anyone can **Delete** it to tidy up; nothing is paid out and nothing is lost.

## Compounded reward

A **compounded reward** makes a token stakable for good: there is one per token, and anyone can add prizes for its stakers, in any token, every day or once.

1. **Token: which token should people stake?** Pick it from the list, LP tokens included. Two facts set by the network appear, fixed once it's created: how long **unstaking takes**, and the **minimum stake** (often none). If the token already has a compounded reward, you add prizes to that one instead.
2. **First daily prize: fund it now?** Optional. Choose **Not now**, or **Add a daily prize** right away (see below). Stakers earn nothing until someone adds a prize.
3. **Review**: the creation fee, plus the first prize if you added one.

Select **Make TICKER stakable** and confirm. Holders stake it on the token's page in the [Communities app](../communities/holders-pool.md). The Done screen recommends adding a daily prize, sending people to stake, or asking a partner to add prizes.

{% hint style="warning" %}
**A compounded reward can't be removed.** There is one per token, for good. Starting it gives you no special rights: anyone can add prizes to it.
{% endhint %}

### Add a daily prize

A compounded reward on its own pays nothing; a **daily prize** gives stakers something to earn.

1. **Whose stakers get it?** Any token with a compounded reward, yours or not.
2. **What do they get every day?** The prize token (paid from your wallet; it can be your own token, BZE or any other), the amount per day and the number of payout days (1 to 36,500). Days with nobody staking are skipped, so a prize can run longer than its length in calendar days.
3. **Review**: the daily amount × the days leaves your wallet now.

Each day the prize is split between everyone staking, in proportion to their stake. Any running daily prize can be extended the same way: **Extend prize** adds days at the same daily amount, with no fee, and anyone can do it.

{% hint style="danger" %}
**The whole prize is locked when you sign.** It can't be cancelled or withdrawn, so pick amounts you are happy to give away.
{% endhint %}

### Prize tokens and the new prize fee

Each compounded reward can pay a limited number of different prize tokens, set by the network. The first time a token becomes a prize there, it takes one of those **prize slots** for good and you pay a one-time **new prize fee**. Paying with that same prize token again later, by you or anyone, has no prize fee. The step tells you which case applies before you sign, and stops you if all the slots are taken by other tokens.

## Airdrop to stakers

An **airdrop** splits an amount between everyone staking a token **right now**, based on how much each one stakes. It's a thank-you, and it doesn't start a daily prize. Any token's stakers, yours or not.

1. **Staked token: which token's stakers?**
2. **Prize & amount: what do they get?** The prize token (paid from your wallet) and the amount.
3. **Review**: the amount leaves your wallet now; an airdrop can't be undone.

The only fee is the new prize fee, and only if this is a new prize token for that reward.

{% hint style="info" %}
**Somebody has to be staking.** The app checks right before you sign. If nobody stakes the token yet there's no one to pay, so it won't let you send it and nothing leaves your wallet.
{% endhint %}

## Send to a list of wallets

**Send to a list of wallets** pays many addresses at once: contest winners, early supporters, a snapshot of holders, a spreadsheet of bounty hunters. There is no Token Factory fee, only the network fee.

1. **Token: what are you sending?** Any token your wallet holds.
2. **List: who gets it?** Choose how much each wallet gets:
   * **Same amount for everyone**: one amount, and wallets one per line.
   * **Amount per wallet**: one `address, amount` per line.

   Paste the list or upload a CSV or TXT file (up to 1 MB); the app offers an example file for each format. A list can hold up to 5,000 wallets. The app checks every line as you go: duplicates are merged, and **lines to fix** are left out until you correct them. Only BeeZee addresses (`bze1…`) work.
3. **Review**: the total that leaves your wallet and the number of transactions.

{% hint style="warning" %}
**Check the list twice.** Sent tokens can't be taken back, and tokens sent to a wrong address can't be recovered.
{% endhint %}

### Long lists

Up to 100 wallets go in one transaction. A longer list is sent in several, and your wallet asks you to approve each one. You can **Stop for now** at any time, or even close the page: your list and progress are kept in this browser for 30 days, and the home page offers to resume where it stopped. Wallets already paid won't be paid twice.

When it's done, the Done screen lets you **Download the report**: every address, its amount, whether it was sent, and the transaction.

## Run a burning raffle

A **burning raffle** turns a prize pot into a game that also burns tokens. You fund the pot; people buy tickets on the [Burner](../burner/burning-raffles.md) for a chance to win part of it. Losing tickets make the pot bigger, and whatever is left at the end is **burned**. It's a way to contribute to a token and its community, not a bet you can win back: nothing returns to you.

1. **Token: which token is the raffle in?** Any token can be raffled, except halted ones, and each token can have only one raffle running at a time.
2. **Prize pot: how big is it?** It leaves your wallet now.
3. **How it plays**: how many **days** it runs (1 to 180), the **ticket price**, the chance to win (**1 ticket in how many wins?**) and the **share of the pot** a winner gets. A plain sentence sums it up, for example: "For 7 days, anyone can pay 10 $GUILD for a ticket. Each ticket has a 1 in 100 chance to win 50% of the pot."
4. **Review**: there is no Token Factory fee.

{% hint style="danger" %}
**A raffle can't be stopped or changed.** The pot leaves your wallet when you start, and whatever is left when it ends is burned. Nothing comes back to you.
{% endhint %}

## Reach another community

**Reach another community** gifts your token to the people who stake a *different* token. They see it in their wallet, and your token shows up as a prize on that token's Communities page. You don't need to own that token or ask its creator.

1. **Community: whose stakers do you want to reach?** Any token with a compounded reward, yours or not. The step shows how much is staked, and the app checks right before you sign that someone is staking.
2. **Gift: what do you give them?** Your token (or any other) and the amount. If your gift isn't stakable yet, the app suggests making it stakable, so the people you reach have a reason to stay.
3. **How: once, or every day?**
   * **Once, right now**: everyone staking today gets their share, like an airdrop.
   * **Every day for N days**: your token becomes a daily prize there, so new stakers get some too.
4. **Review**: gifts can't be taken back. The fees are the same as an airdrop or a daily prize.

Adding a prize to another token's compounded reward doesn't make you its owner.

{% hint style="success" %}
**For example.** The book club makes **$PAGE** stakable first, so newcomers have a reason to keep it. Then it reaches the gaming guild: 30 days of $PAGE as a daily prize for everyone staking **$GUILD**. Every guild member who stakes now earns a little $PAGE each day, and finds the book club through it.
{% endhint %}

## The Rewards directory

**Rewards**, in the top menu, lists every staking reward on BeeZee. You don't need a wallet to browse it, and anyone can extend or add to any of them.

* **Search by staked token**: find a reward by the token people stake.
* **Kind**: **All**, **Compounded** or **Simple**.
* **Filters**: **Has stakers**, **Paying now**, or **Created by you** (rewards on tokens you created); for simple rewards, **Running** or **Finished**.
* **Sort**: **Most staked (USD)**, **Most prize tokens** or **A–Z**.

A compounded reward shows what is staked, its daily prizes (each with **Extend** and when it was last paid) and its prize tokens, with **Add daily prize**, **Airdrop once** and **Open token**. A simple reward shows what people stake and earn and when it ends, with **Extend** (and **Delete** once it's finished and empty), plus a link to stake it.

{% hint style="info" %}
**No owners, no staker counts.** The network doesn't record who created or funded a reward, so the directory never claims anyone owns one. It shows how much is staked (and its value in dollars when it has a price), not how many people stake.
{% endhint %}

{% hint style="success" %}
**For example.** The gaming guild has a $GUILD/BZE pool and wants it deeper. It creates a 30-day simple reward: stake the $GUILD/BZE LP token, share a daily $GUILD amount. Players who add liquidity now earn twice, from the pool's trading fees and from the reward. When it nears its end, a guild member extends it from **Rewards**.
{% endhint %}

{% content-ref url="playbooks.md" %}
[playbooks.md](playbooks.md)
{% endcontent-ref %}
