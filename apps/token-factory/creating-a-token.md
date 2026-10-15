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

# Creating a Token

Creating your own token takes a few minutes and no coding. On the Token Factory home, pick **Create my token**. The form asks one question at a time, and everything is shown before you sign.

## The three questions

### 1. Name and ticker

Give your token a **name**, the full, friendly name (2 to 64 characters), and a **ticker**, the short symbol people see everywhere, like $PAGE or $GUILD (3 to 12 letters and digits, starting with a letter).

BeeZee gives your token a unique **token ID** made from your address and the ticker, so it can never clash with anyone else's. The app shows it as you type. If you already created a token with the same ticker, it asks you to pick another one.

Every token on BeeZee uses the same **6 decimals**, so there is nothing to set: a shared standard keeps tokens consistent across all the apps.

### 2. Describe it (optional)

A sentence or two about what your token is for, up to 512 characters. Wallets show it. You can **Skip** it and add it later from your token's page.

### 3. How many to create?

Choose the **amount** to create, or use one of the presets (100,000 / 1 million / 100 million / 1 billion). All of it goes to your wallet when the token is created; you decide later how much to sell, put in a pool or give away.

## Review and create

On the side, a **Preview** shows your token as people will see it, and **You will pay** shows the token creation fee. The fee is set by the network and can change through governance, so the app reads the current amount for you (you can also check it on a [block explorer](https://explorer.getbze.com/)).

When it all looks right, select **Create TICKER** and confirm in your wallet. One transaction creates the token, mints the whole supply to you and saves its name and description.

{% hint style="info" %}
**Your draft is saved.** The form keeps what you typed in this browser, so you can leave and come back. **Start over** clears it.
{% endhint %}

## You keep control

You keep control of your new token: you can mint more, edit its description and set its brand kit. Until you decide otherwise, buyers see it as **Mintable**.

When your setup is done you can **lock the supply** forever from the token's page, so everyone sees **Fixed supply**. That's a separate, deliberate step, and it's best done last. See [Making It Official](making-it-official.md).

## Your token is live

Right after creating, a launch screen confirms your token is live and lists the next steps, each with its fee:

* **Give it a look**: set a brand kit.
* **Let people buy it**: create a liquidity pool.
* **Reward the people who hold it**: set up holder rewards.
* **Get its logo in every wallet**: list it in the Cosmos Chain Registry.
* **Last: lock the supply (optional)**.

Do them now or later: they stay on your token's page, ticking themselves off as they are done. The launch screen also shows your token ID with a copy button, and links to view your token on the DEX and the transaction. **Allow limit orders too** opens an order-book market for it.

{% hint style="info" %}
**Why no logo field?** Logos don't come from Token Factory. Wallets, explorers and DEXes read them from the Cosmos Chain Registry, and the app walks you through adding yours.
{% endhint %}

{% hint style="success" %}
**For example.** Your online book club launches **$PAGE**: name "Page Turner", ticker PAGE, a short description, and 1 million tokens. A minute after confirming, the full supply is in the club's wallet, ready to share. Next stop: a $PAGE–BZE pool so members can buy some.
{% endhint %}

{% content-ref url="markets-and-liquidity.md" %}
[markets-and-liquidity.md](markets-and-liquidity.md)
{% endcontent-ref %}
