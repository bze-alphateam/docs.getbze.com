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

Creating your own token takes a few minutes and no coding. Open the **Create** tab in Token Factory and a guided wizard walks you through four short steps — you can move back and forth before anything is final.

## The four steps

### 1. Identity

Give your token a **name** (the full, human-friendly name) and a **symbol** — the short ticker people will see everywhere, like $PAGE or $GUILD. Pick something clear and memorable; this is how your token shows up on the DEX, in wallets, and in every app.

Behind the scenes, BeeZee also assigns your token a unique ID automatically so it can never clash with anyone else's. You don't need to think about it — it's just there to keep your token one-of-a-kind.

### 2. Metadata

Add an optional **description** — a sentence or two about what your token is for. It's a nice touch that helps people understand your project at a glance, but you can leave it blank and add it later.

### 3. Supply & Admin

Choose your **initial supply** — how many tokens to create at launch. This whole amount is minted straight to your wallet, so you start holding everything and can distribute it however you like.

The number of **decimals** is fixed at the BeeZee standard, the same for every token on the network. That's on purpose: a shared standard keeps tokens consistent and predictable across all the apps, so it isn't something you set.

This step also holds the one big decision — your **admin** choice — covered on its own below.

### 4. Review

A final summary shows everything you picked. Check it over, confirm in your wallet, and your token is created on the blockchain. Your initial supply lands in your wallet right away.

## The big decision: keep or renounce admin

Being the **admin** means holding the keys to your token — the power to change it after launch. You choose upfront how much of that power you want to keep, and it comes down to a trade-off between flexibility and trust.

**Keep admin (flexible).** You stay in control. Later on you can mint more supply, burn tokens, and edit your token's details. This is the right choice for most projects that are still growing and want room to adapt. The trade-off: holders have to trust you not to mint a flood of new tokens and dilute them.

**Renounce at creation (maximum trust).** You give up all admin power the moment the token is born. The supply is fixed forever — no one can ever mint more, not even you. This is the strongest possible signal to holders that what they see is what they get, but it's a one-way door.

{% hint style="danger" %}
**Renouncing is irreversible.** Once you renounce admin, there is no take-back — you can never mint, edit, or reclaim control again. Only choose this at creation if you are certain you want a permanently fixed supply. If you're unsure, keep admin for now; you can always renounce later from the Manage console.
{% endhint %}

## After you create

Your token now exists and works everywhere on BeeZee. From here you can:

* **View it on the DEX or a [block explorer](https://explorer.getbze.com/)** to see it live on the network.
* **Create a market or a liquidity pool** so people can actually trade it.
* **Set up staking rewards** to grow a community around it.

{% hint style="success" %}
**For example.** Your online book club launches **$PAGE**. In the wizard you name it, set an initial supply, and decide to *keep admin* for now — the club is young and you might want to mint more for new members later. A minute after confirming, the full supply is in your wallet, ready to share. Next stop: giving $PAGE a market so members can get some.
{% endhint %}

{% content-ref url="markets-and-liquidity.md" %}
[markets-and-liquidity.md](markets-and-liquidity.md)
{% endcontent-ref %}
