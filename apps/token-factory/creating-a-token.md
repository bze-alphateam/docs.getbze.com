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

Creating your own token takes a few minutes and no coding. On the Token Factory home, pick **Create a token** (it's marked **Start here**). Four short steps follow, and everything is shown before you sign.

## Step 1: Details

**What is it called?**

* **Name**: the full, friendly name (2 to 64 characters).
* **Ticker**: the short symbol people see everywhere, like $PAGE or $GUILD (3 to 12 letters and digits, starting with a letter). The ticker is permanent.
* **Description** (optional): a sentence or two about what your token is for, up to 512 characters. Wallets show it, and you can add or change it later from your token's page.

BeeZee gives your token a unique **token ID** made from your address and the ticker, so it can never clash with anyone else's. The app shows it as you type. If you already created a token with the same ticker, it asks you to pick another one.

## Step 2: Supply

**How many to start with?** Type an amount or pick one of the presets (100,000 / 1 million / 21 million). All of it is minted to your wallet when the token is created; you decide later how much to sell, put in a pool or give away.

Every token on BeeZee uses the same **6 decimals**, so there is nothing to set: a shared standard keeps tokens consistent across all the apps.

## Step 3: Permissions

**Who can change it later?** The token's **admin** can mint more and edit its details. Choose:

* **My wallet**: you stay the admin. Best while the project is young.
* **Another address**: a team or multisig wallet becomes the admin from the start. Paste its BeeZee address (`bze1…`).

{% hint style="warning" %}
**Check the address twice.** If you pick another address, that address gets the admin rights from the very first block, and only its owner can give them back.
{% endhint %}

You can transfer or renounce admin later, on the token's page under **Permissions**. See [Managing Your Token](managing-your-token.md#permissions).

## Step 4: Review and create

**Everything right?** The Review lists:

* **Leaves your wallet**: the token creation fee.
* **You get**: the whole supply, in your wallet.
* **Admin**: your wallet or the address you chose, and what the admin can do.
* **Permanent**: the ticker in the token's address.

The token creation fee is set by the network and can change through governance, so the app reads the current amount for you (you can also check it on a [block explorer](https://explorer.getbze.com/)).

Why there's a fee and where it goes: see [Token Factory Parameters](../../overview/parameters/token-factory.md).

Select **Create token** and confirm in your wallet. One transaction creates the token, mints the whole supply to you and saves its name and description.

{% hint style="info" %}
**Your draft is saved.** The steps keep what you typed in this browser, so you can leave and come back. With your wallet connected, the home page offers to continue where you stopped.
{% endhint %}

## Your token is live

The Done screen confirms your token is live and suggests what to do next, the recommended step first:

* **Let people buy it**: create a liquidity pool.
* **Get your logo in every wallet**: the registry guide.
* **Give it a look**: a brand kit for its Communities page.
* **Allow limit orders too**: an order-book market.

Do them now or later: they also wait for you on your token's page, as setup chips that tick themselves off when they are done.

{% hint style="danger" %}
**Renouncing admin is permanent, and it's never a launch step.** Some projects later give up admin so nobody can ever mint more. That lives on the token's page under **Permissions**, behind its own review, and nothing in the app suggests it as a next step. Only do it once you are certain: nobody, you included, can ever mint or edit the token again. See [Managing Your Token](managing-your-token.md#renounce-admin).
{% endhint %}

{% hint style="info" %}
**Why no logo field?** Logos don't come from Token Factory. Wallets, explorers and DEXes read them from the Cosmos Chain Registry, and the app walks you through adding yours. See [Making It Official](making-it-official.md).
{% endhint %}

{% hint style="success" %}
**For example.** Your online book club launches **$PAGE**: name "Page Turner", ticker PAGE, a short description, 1 million tokens, and the club's wallet as admin. A minute after confirming, the full supply is in the club's wallet, and the Done screen recommends the next stop: a $PAGE/BZE pool so members can buy some.
{% endhint %}

{% content-ref url="markets-and-liquidity.md" %}
[markets-and-liquidity.md](markets-and-liquidity.md)
{% endcontent-ref %}
