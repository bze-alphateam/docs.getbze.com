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

# Token Pages

Every community token gets its own page in the Communities app, and that page is built to be the **project's own website**. There's no BeeZee menu bar and no shared directory around it: just the token's name, its colours, its font and everything its community offers, from staking to trading to burns. A project can share the link as its home on the web.

## Made in the project's colours

The page is drawn with the token's **brand kit**: its background, text, primary and secondary colours, and its font. The creator sets these in Token Factory, with separate colours for light and dark mode. Switch between the two with the moon or sun button in the header and the page follows the kit's colours for that mode. A token without a brand kit gets a clean default look.

{% content-ref url="../token-factory/making-it-official.md" %}
[making-it-official.md](../token-factory/making-it-official.md)
{% endcontent-ref %}

## Finding your way around

The header shows the token's logo and name, links to each part of the page (**Stake**, **Earn**, **Trade**, **Burn** and **Token**), the light/dark switch and your wallet button. A section only appears in the menu when the page has it: **Earn** needs something that pays the token, and **Trade** needs a liquidity pool. On a phone the links fold into a menu, and a bar at the bottom keeps **Get TICKER** and **Stake TICKER** within thumb's reach.

The wallet button shows your balance of the token once you're connected, or **Connect** before that. It opens the page's own wallet, covered in [Getting a Token](getting-a-token.md).

## The top of the page

The first thing visitors see is the token's **ticker**, a **Verified** tag when it has been checked, its **name** and the project's **description**. When the token has a market, its **price** in US dollars shows with its change today. Two buttons start the most common journeys: **Get TICKER** opens the wallet ready to swap into the token, and **Stake TICKER** jumps to the staking section.

## Key numbers

Right under it, a strip of key numbers sums up the project:

* **Market cap**: the supply times the price.
* **Supply**: how many tokens exist right now.
* **Staked**: how much is staked in the holders pool and in running staking programs.
* **Burned**: how much has been burned so far.
* **24h volume**: how much was traded in the token's pools over the last day.

A number only shows when it can be worked out: a token without a price has no market cap, and one without a pool has no volume.

## Stake

**Stake your TICKER** is always on the page. It starts with the token's **holders pool**, where holders stake the token itself and share daily prizes, and continues with any **fixed-term programs** that stake the token.

{% content-ref url="holders-pool.md" %}
[holders-pool.md](holders-pool.md)
{% endcontent-ref %}

{% content-ref url="staking-programs.md" %}
[staking-programs.md](staking-programs.md)
{% endcontent-ref %}

## Earn: ways to earn the token

**Ways to earn TICKER** is for people who don't hold the token yet. It lists everywhere you can stake **another** token and get paid in this one:

* staking programs whose prize is this token, and
* other tokens' holders pools that pay this token as one of their prizes.

Each card shows the token you'd stake (an LP token shows both tokens of its pool, like **GUILD/BZE LP**), whether it's a **Holders pool** or a **Fixed-term program**, its **APR** when it can be worked out, how much of this token is **paid out daily**, the **Unlock time**, and how long it runs (**Funded for** a holders pool, **Ends in** a program). A holders pool that also pays other prizes says so (**Also pays …**). The best APR comes first.

Pick one and **Stake** opens right there, for the other token. The section is hidden when nothing pays this token.

{% hint style="success" %}
**For example.** The book club gifts 30 days of **$PAGE** to everyone staking **$GUILD** in the guild's holders pool. On the $PAGE page, **Ways to earn PAGE** now shows a **$GUILD** card: "**Holders pool**", the $PAGE paid out daily, and "Also pays GUILD". A gamer who holds $GUILD but has never heard of the book club can stake from that card and start earning $PAGE.
{% endhint %}

## Trade: buy and sell

When the token sits in at least one liquidity pool, **Buy and sell TICKER** appears.

### The price chart

The chart shows the token's price in one of its pools, against the pool's other token. The most liquid pool is picked first; when there are several, chips under the chart (like **GUILD / BZE**) switch between them. **7D**, **30D** and **90D** set the time range, and the latest price sits above the line. A quiet range simply says **No trades in this range yet**.

### The Buy/Sell panel

Next to the chart, flip between **Buy** and **Sell**:

* **Buy**: choose what to **Pay with** (any token in your wallet that can be swapped into this one), enter **You pay**, and see **You get**.
* **Sell**: enter **You sell**, choose what you **Receive**, and see the amount.

Both show the **Price impact** (how much your own trade moves the price), the **Network fee**, and a **Max slippage** you can pick: if the price moves against you by more than that before the swap settles, it's cancelled instead of going through at a bad rate. **Max** fills in your whole balance while keeping the fee aside.

### Liquidity pools

Under the chart, **Liquidity pools** lists every pool that holds the token, the deepest first, with its **Liquidity**, **24h volume**, **APR** and **Your share**. Liquidity providers earn a share of every swap fee in the pool.

* **Add liquidity**: enter an amount of either token and the other one fills in at the pool's current ratio. The form shows roughly what share of the pool you'd own afterwards.
* **Remove**: choose **How much of your liquidity** to take back (25%, 50%, 75% or all of it) and see what **You receive about** in each token.

Both forms have a **Max slippage** too. On a phone, each pool is shown as a card.

{% content-ref url="../dex/liquidity-pools.md" %}
[liquidity-pools.md](../dex/liquidity-pools.md)
{% endcontent-ref %}

## Burn

**Every burn makes TICKER scarcer** is always on the page. Burning removes tokens from circulation for good, and this section makes it visible.

* **Burned forever** shows the total burned so far, its value in dollars when there's a price, and what share of the **original supply** that is, with a bar to match. (The original supply is today's supply plus everything already burned.)
* **Next burn** counts down to the next burn and shows how much of the token is **queued** for it, or says **No burn scheduled**.
* **Burn history** lists past burns with their **Amount**, **Value**, **Block** and **Date**.

Anyone can join in: **Burn TICKER** opens a short form. Enter the **Amount to burn**, check it, and select **Confirm burn**. Your tokens are queued for the next burn.

{% hint style="danger" %}
**A burn can't be undone.** The tokens you send are destroyed at the next burn and never come back. The form asks you to confirm for exactly that reason.
{% endhint %}

### The burn raffle

When a burning raffle is running for the token, a **Burn raffle** card appears under the next burn. It shows the **Ticket** price, the **Current pot**, the **Win chance** of each ticket (written as "1 in N"), the **Prize now** and when the raffle **Ends in**. Ticket purchases go into the pot, winners are paid from it, and whatever is left in the pot when the raffle ends is burned.

**Buy tickets** opens a small form: choose how many **Tickets**, check the **Total cost** and **Each ticket's chance**, and buy. Each ticket is then drawn, one per block, and marked **Won** with its amount or **No win**. You can close the window while it draws; the remaining results arrive as notifications. **Recent winners** lists the latest winners and what they took home.

{% hint style="info" %}
**Raffles aren't started from the apps.** There's no button to launch a raffle on a token page, or anywhere else in the apps. When one is running for a token, its page shows the raffle card automatically.
{% endhint %}

{% content-ref url="../burner/burning-raffles.md" %}
[burning-raffles.md](../burner/burning-raffles.md)
{% endcontent-ref %}

## Token details

At the bottom, **Token details** lists the **Ticker**, the **Decimals**, the **Supply control** (whether the creator can still mint more, or has given that up for good), the **Creator** and the token's full ID (shown as **Denom**) with a **Copy** button.

{% hint style="success" %}
**For example.** The gaming guild gives **$GUILD** a brand kit in purple and gold with the Space Grotesk font, then shares its Communities page as the guild's website. Members land on a page that looks like the guild's own: the price at the top, **Stake GUILD** one tap away, a chart of the $GUILD–BZE pool, and a burn counter that ticks down to the next burn.
{% endhint %}
