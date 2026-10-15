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

A token becomes a community when people have a reason to hold it, and when new people discover it. The goals in **Grow the community** on the Token Factory home do exactly that:

* **Make my token stakable**: holders stake it and share daily prizes.
* **Give a little every day**: add a daily prize for those stakers.
* **Gift my stakers, once**: split an amount between everyone staking a token, today.
* **Reach another community**: gift your token to the people who stake a different token.
* **Send to a list of wallets**: pay a list of addresses, from a contest, a snapshot or a spreadsheet.
* **Run a campaign with an end date**: a staking program for a set number of days, often for liquidity providers.

Not sure which one fits? Every reward page has an **ⓘ** button that opens a short guide comparing them. Its advice is a good one: start with holder rewards, and add a campaign or an airdrop later.

## Which reward fits?

|                       | Holder rewards                     | Staking program (campaign)        | Airdrop                                  |
| --------------------- | ---------------------------------- | --------------------------------- | ---------------------------------------- |
| **How long**          | No end date                        | A fixed number of days            | Once, today                              |
| **What people stake** | The token itself                   | Any token you pick, LP tokens too | Nothing new: it goes to current stakers  |
| **Prizes**            | Several prize tokens, each daily   | One prize token, paid daily       | Any token, one amount                    |
| **Leaving**           | A short wait set by the network    | A lock you choose (0 days or more) | —                                       |
| **Best for**          | Making a token worth holding       | Liquidity, launches, seasons      | Thank-yous and reaching new people       |

Every form shows a **You will pay** panel before you sign: each cost, the network fee, and whether your balance covers it. Creation fees are set by the network and can change through governance, so the app always reads the current amount; check the panel (or a [block explorer](https://explorer.getbze.com/)) rather than relying on a fixed number.

## Holder rewards: make your token stakable

**Holder rewards** let anyone who holds your token stake it and share daily prizes. There is one per token and it never ends: you, or anyone else, keep it going by adding prizes.

Open **Make my token stakable** from the home page, or the **Rewards** tab of your token's workspace. Before you create it you see two facts the network sets and that stay fixed for this token:

* **Unstaking wait**: how many days stakers wait to get their tokens back after they unstake.
* **Minimum stake**: the smallest amount someone can stake (often no minimum).

Confirm with **Make TICKER stakable** and pay the holder rewards fee. From then on the panel shows **Live**, how much is **Staked by holders**, the daily prizes that are running and the prize tokens used.

{% hint style="info" %}
**You don't have to be the creator.** Holder rewards are usually started by the token's team, but anyone can make any token stakable, and starting it gives no special rights. Holders stake in the [Communities app](../communities/holders-pool.md), on the token's page.
{% endhint %}

## Give a little every day: daily prizes

Holder rewards on their own pay nothing; a **daily prize** gives stakers something to earn. Choose:

1. **What do you give?** The prize token, paid from your wallet. It can be your own token, BZE or any other token.
2. **How much a day?**
3. **For how many days?** Between 1 and 36,500 payout days. Days with nobody staking are skipped, so a prize can run longer than its length in calendar days.

Each day the prize is split between everyone staking, in proportion to their stake.

{% hint style="danger" %}
**The whole prize is locked when you sign.** The daily prize × the number of days leaves your wallet at once. It can't be cancelled or withdrawn, so pick amounts you are happy to give away.
{% endhint %}

### Prize tokens and the new prize fee

Each token's holder rewards can pay a limited number of different prize tokens, set by the network. The first time a token becomes a prize, it takes one of those **prize slots** for good and you pay a one-time **new prize fee**. Paying with that same prize token again later, by you or anyone, has no prize fee. The form tells you which case applies before you sign, and stops you if all the slots are taken by other tokens.

### Extending a daily prize

Any running daily prize has an **Extend** button. Add more days and only those extra days are locked; there is no fee. Anyone can extend any schedule.

## Gift my stakers, once

An **airdrop** splits an amount between everyone staking a token **right now**, based on how much each one stakes. It's a thank-you, and it doesn't start a daily prize. Pick the prize token and the amount (the form shows an example: what someone with 1% of the stake would get), then **Airdrop now**.

The only fee is the new prize fee, and only if this is a new prize token for that token.

{% hint style="info" %}
**Somebody has to be staking.** If nobody stakes the token yet there's no one to pay, so the app won't let you send it and nothing leaves your wallet.
{% endhint %}

## Reach another community

**Reach another community** gifts your token to the people who stake a *different* token. They see it in their wallet, and your token shows up as a prize on that token's Communities page. You don't need to own that token or ask its creator.

1. **Which community?** Only tokens whose holder rewards have stakers are listed, most staked first. Your own tokens are marked **Yours**.
2. **What do you give them?** Your token (or any other) and the amount.
3. **All at once, or a little every day?**
   * **All at once, now**: everyone staking today gets their share.
   * **Every day for N days**: your token becomes a daily prize there, so new stakers get some too.

Confirm with **Send the gift** or **Start the daily gift**. The fees are the same as an airdrop or a daily prize.

{% hint style="success" %}
**For example.** The book club makes **$PAGE** stakable first, so newcomers have a reason to keep it. Then it reaches the gaming guild: 30 days of $PAGE as a daily prize for everyone staking **$GUILD**. Every guild member who stakes now earns a little $PAGE each day, and finds the book club through it.
{% endhint %}

## Send to a list of wallets

**Send to a list of wallets** pays many addresses at once: contest winners, a snapshot of holders, a team, a spreadsheet of bounty hunters. There is no Factory fee, only the network fee.

1. **What do you send?** Any token you hold.
2. **Who gets it, and how much?**
   * **Same for everyone**: one amount, and a list of wallets, one per line.
   * **Amount per wallet**: one `address, amount` per line.

Paste the list or use **Upload CSV or TXT** (up to 1 MB; **Download an example file** shows the format). Commas, semicolons, tabs or spaces all work between fields, a header line is skipped, and lines starting with `#` are ignored. A list can hold up to 5,000 wallets.

The app checks every line as you go: **wallets ready**, **duplicates** (merged into one; with amounts per wallet, their amounts are added up), and **lines to fix**, which are left out until you correct them. Only BeeZee addresses (`bze1…`) work; an address from another network is flagged.

{% hint style="warning" %}
**Check the list twice.** Tokens sent to a wrong address can't be recovered.
{% endhint %}

### Long lists

Up to 100 wallets go in one transaction. A longer list is sent in several transactions, and you approve each one in your wallet (**Start sending**, then **Send the next transaction**). You can **Stop for now** at any time, or even close the tab: your list and progress are kept in this browser for 30 days, and when you come back the app offers to **Continue** where you left off. Wallets already paid are marked and won't be paid twice.

When at least one transaction is sent you can **Download report (CSV)**: every address, its amount, whether it was sent, and the transaction hash.

## Run a campaign with an end date

A **staking program** is a campaign: people stake one token for a set number of days and earn a daily prize you fund upfront. It's the classic way to reward **liquidity providers**: they stake the LP tokens they got from adding to your pool.

1. **What do people stake?** Any token, LP tokens included.
2. **What do they earn, and for how long?** The prize token, the prize per day and the number of days (1 to 36,500).
3. **Rules for stakers**: an optional **lock period** (0 means they can leave any time) and an optional **minimum stake**.

Confirm with **Start the program** and pay the staking program fee. People join it on your token's page in the [Communities app](../communities/staking-programs.md) or on the [DEX Staking page](../dex/staking-and-earning.md).

{% hint style="danger" %}
**The whole prize is paid upfront and can't be withdrawn.** The prize per day × the number of days leaves your wallet when you sign and is paid to stakers day by day.
{% endhint %}

Anyone can **Extend** a running program with more days, not only the one who started it, and there is no fee for that. Once a program has finished and every staker has left, anyone can delete it to tidy up; nothing is paid out and nothing is lost.

{% hint style="success" %}
**For example.** The gaming guild has a $GUILD–BZE pool and wants it deeper. It runs a 30-day campaign: stake the $GUILD–BZE LP token, earn a daily $GUILD prize. Players who add liquidity now earn twice, from the pool's trading fees and from the campaign.
{% endhint %}

## Rewards on BeeZee

The **Rewards** page (linked from **Manage** and from every reward form) is a directory of every holder reward and staking program on BeeZee. You don't need a wallet to browse it.

* **Holder rewards**: your tokens first (with buttons to make them stakable, airdrop or add a daily prize), then every token, with filters (**Has stakers**, **Paying now**) and sorting by stake, prize tokens or name.
* **Staking programs**: the programs with your tokens (staked, in an LP token, or paid as a prize) first, then every other program, with **Running** and **Finished** filters.

{% content-ref url="playbooks.md" %}
[playbooks.md](playbooks.md)
{% endcontent-ref %}
