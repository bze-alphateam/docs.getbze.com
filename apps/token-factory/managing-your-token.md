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

# Managing Your Token

**Tokens**, in the top menu, lists every token made with Token Factory, and every one of them has its own page. The page works for any token: anyone can see it and use the actions open to everyone, and the actions that need the token's **admin** only appear for the admin.

## The Tokens directory

Search by name, ticker or token ID, and filter by **All**, **Created by you** or **Stakable**. You don't need a wallet to browse.

* **Created by you** is pinned on top when your wallet is connected: the tokens whose ID carries your address. Each shows who holds admin today: **You are admin**, **Admin is** another address, or **Admin given up**.
* **All tokens** follows, each with whether it's stakable and how much is staked. **Show 20 more** loads the next ones.

Select a token to open its page. Admin rights are checked on the network every time you open one.

## The token's page

At the top you see the token's name and ticker, its token ID with a copy button, and its **Supply**, how much **You hold** and how much is **Staked**, with links to the token in the [Communities app](../communities/token-pages.md) and on the explorer. Badges tell anyone at a glance where it stands:

* **Mintable**: someone is still the admin and could mint more.
* **Fixed supply**: admin was renounced, so no new tokens can ever be minted.
* With your wallet connected, your own role: for example **Created by you · you are admin**, or **You are admin** on a token someone handed to you.

### Supply

* **Mint tokens** (admin only): select **Mint** to create more of the token, straight to your wallet. The form shows the new total supply. It costs only the network fee.
* **Burn tokens**: anyone can destroy the tokens they hold, in the [Burner](../burner/burning-tokens.md) app.
* **Run a burning raffle**: **Start raffle** to run one, or, while one is running, its pot, ticket price, win chance, what a winner gets and the time left, with a link to it on Burner. See [Growing Your Community](growing-your-community.md#run-a-burning-raffle).

{% hint style="warning" %}
**Minting more lowers the share every holder owns.** Use it thoughtfully: minting a lot, or often, can shake holders' trust.
{% endhint %}

### Details and look

* **Name, logo, description**: what wallets and the DEX show. Select **View** to see them. The admin can edit the name and description and saves the change on-chain after a review; wallets and explorers pick it up right away. The ticker, token ID and decimals can never change.
* **Get your logo in every wallet**: **View** opens the registry guide; once it's done, the item reads **Listed in the registry ✓**. See [Making It Official](making-it-official.md).
* **Brand kit**: a small preview of the colours and font of the token's Communities page. The admin gets **Edit brand kit**, which opens the brand kit editor, and can remove the kit. See [Making It Official](making-it-official.md#give-it-a-look-the-brand-kit).

### Trading

Where the token can be traded: its liquidity pools and order-book markets, whoever created them (the ones you created are marked), each with a **DEX** link, where you can add or remove liquidity. **Create DEX market** opens a new pool or market. See [Getting It Traded](markets-and-liquidity.md).

### Rewards

**Rewards on TICKER** lists everything paying the token's stakers, the same way as in [Rewards](growing-your-community.md#the-rewards-directory), and anyone can add to it:

* **Compounded reward**: its unstaking lock, minimum stake and status, and each daily prize with **Extend**, plus **Add daily prize** and a **DEX** link to the reward's page. If the token isn't stakable yet, **Make TICKER stakable** has a **Create** button that leads to the compounded reward form.
* **Simple rewards** where people stake this token or its LP shares, each with **Extend**, **Airdrop** once someone stakes it, and a **DEX** link.

To airdrop to the token's stakers, use **Airdrop tokens**. See [Growing Your Community](growing-your-community.md#airdrop-tokens).

## Permissions

The last section of the page says who the admin is, read live from the network: your wallet, another address, or **Admin given up**. If the app can't check, it says so and keeps the admin actions hidden until it knows.

The admin can mint more, edit the name and description, set the brand kit, and transfer or renounce admin. For the admin, this section has two actions.

### Transfer admin

Give admin rights to another address, for example a team multisig, a DAO or another wallet of yours. Enter the **new admin address**, then review: **you lose** every admin power, **they get** the same, and it's **permanent for you**: only the new admin can give it back.

{% hint style="warning" %}
**Triple-check the address.** Sent to the wrong one, it can't be fixed by anyone but that address's owner.
{% endhint %}

### Renounce admin

**Renounce admin** gives up admin for good: nobody, you included, can ever mint or edit the token again, and everyone sees **Fixed supply**. Select **Renounce…** and a review dialog shows:

* **Gone forever**: minting more, editing the name, logo and description, editing the brand kit, and handing admin to someone else.
* **Stays the same**: everyone keeps their tokens; pools, markets and rewards keep running; anyone can still burn the tokens they hold on Burner.
* **Supply, fixed from now on**, and a check of your setup: whether the description is filled in and the brand kit is set, because once you renounce they stay as they are.

To confirm, type the token's ticker exactly.

{% hint style="danger" %}
**Renouncing admin can never be undone**: not by you, not by BeeZee, not by anyone. A description or brand kit you haven't added by then can never be added. Token Factory never suggests it as a step; only do it when you are sure.
{% endhint %}

{% hint style="success" %}
**For example.** The gaming guild created **$GUILD** with the founder's wallet as admin. Once the guild has a team multisig, the founder opens **Permissions**, chooses **Transfer admin**, pastes the multisig's address and checks it twice. From then on, minting needs the whole team.
{% endhint %}

{% content-ref url="growing-your-community.md" %}
[growing-your-community.md](growing-your-community.md)
{% endcontent-ref %}
