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

# The Verified Badge

Across the BeeZee apps, some tokens and markets carry a small **Verified** badge. It's there to help you tell a well-known token from a look-alike at a glance. Anyone can create a token on BeeZee, and anyone can give it any name, so two tokens called "PAGE" can exist side by side. The badge tells you which ones the apps recognise.

You'll see it on the DEX (the **Assets** directory, **Exchange** markets and **Explore rewards**), on Burner coin pages, on Communities token pages and in the wallet panel.

## What Verified means, and what it doesn't

{% hint style="warning" %}
**Verified is only a badge.** It means the apps recognise where a token comes from, nothing more. It is **not** a KYC check of the people behind a token, **not** a legal or regulatory approval, **not** a security audit, and **not** any kind of official or government verification. It is not an endorsement by BeeZee, and it is not investment advice. A verified token can still lose value, and you should always do your own research before you trade.
{% endhint %}

In plain terms, Verified marks two kinds of tokens:

* **Tokens that come from outside BeeZee** and are known to the public token registry that wallets and exchanges across the Cosmos world share.
* **Tokens born on BeeZee**, starting with BZE itself, that have shown real activity on the network.

## How a token gets the badge

### Tokens bridged in from another blockchain

A token moved to BeeZee from another blockchain is verified when the shared public token registry knows it. That registry is the same list that gives the token its proper name and logo in wallets, so a verified bridged token shows its real name instead of a long code.

Sometimes the same token can reach BeeZee by two roads: straight from its home chain, or through another chain in between. The two copies are separate tokens on BeeZee. To keep things clear, the copy that arrived directly is the one that stays verified. A copy that took the detour loses the badge, and its name mentions the chain it came through, so you can tell them apart.

{% hint style="info" %}
If you see the same token twice and only one is verified, the verified one is usually the copy that came straight from its home chain. That's normally the one with the most trading and the deepest pools.
{% endhint %}

### Tokens created on BeeZee

**BZE** is always verified. Community tokens made with [Token Factory](../../apps/token-factory/README.md) are verified by the BZE team, who keep a list of community tokens that have shown real, lasting activity on the chain: people holding it, trading it and using it. New tokens start without the badge, and that's completely normal.

Getting your token's name and logo into the public registry, as described in [Making It Official](../../apps/token-factory/making-it-official.md), helps wallets show it properly, but on its own it doesn't add the Verified badge for a token created on BeeZee.

### Liquidity pool shares

When you add liquidity to a pool, you receive pool share tokens (LP tokens) in return. These are verified when the apps know both tokens in the pool, and they're named after them, for example **PAGE/BZE LP**.

### Markets

A trading pair on the **Exchange** is verified only when **both** of its tokens are verified. A $GUILD–BZE market is verified if $GUILD is; a market pairing an unverified token with BZE is not.

## Where the badge makes a difference

* **Lists put verified items first.** The DEX's Assets directory and Exchange show BZE first, then verified tokens and markets, then the rest. The wallet panel and the Burner's coin search do the same.
* **Filters let you hide the rest.** On the DEX, **Explore rewards** has a **Verified only** filter that's switched on to start with. The Communities directory has a **Verified** filter too.
* **Everything else is still there.** Unverified tokens and markets work exactly the same way. You can trade them, stake them and burn them. The badge only changes how they're shown.

{% hint style="success" %}
**For example.** The gaming guild has just launched **$GUILD**. For now it has no badge, so members find it by searching for its name and checking the creator on its [Assets](../../apps/dex/assets.md) page. Months later, with plenty of holders and steady trading, the BZE team adds $GUILD to its list. Now it shows the **Verified** badge, its $GUILD–BZE market is verified too, and both move up the lists, where new members find them more easily.
{% endhint %}

## Before you trade an unverified token

An unverified token isn't necessarily bad: it may simply be new. It's worth a closer look, though:

* **Check the creator and who controls the supply** on the token's page in [Assets](../../apps/dex/assets.md#who-controls-the-supply).
* **Look at the trading volume and the pools** it trades in.
* **Compare the name with the verified token** if one with the same name already exists. A look-alike is the most common trick.
* **Never trade more than you're comfortable losing**, whether a token is verified or not.
