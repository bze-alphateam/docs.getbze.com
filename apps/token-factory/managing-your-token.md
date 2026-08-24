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

The **Manage** tab is your control room. It lists everything you've created in Token Factory — your tokens, along with any markets, liquidity pools, and reward programs you've set up — all in one place so you can keep an eye on your whole project.

## The trust badge

Every token you've made shows a badge that tells anyone, at a glance, what kind of token it is:

* **Fixed supply** — admin has been renounced, so no new tokens can ever be minted. What you see is what there will always be.
* **Mintable** — you still hold admin and could mint more supply later.

This badge is a big part of how holders judge a token, so it's worth understanding which one yours carries.

## Token actions

The actions below are available only to the token's **admin** — if you renounced admin, most of these are gone for good.

### Mint

Create more of your token, minted straight to your wallet. Handy when your project grows and you need more supply to distribute.

{% hint style="warning" %}
**Minting dilutes existing holders.** Every new token you mint makes each existing token a smaller slice of the total. Use it thoughtfully — minting a lot, or often, can shake holders' trust.
{% endhint %}

### Burn

Permanently remove tokens from your own balance, shrinking the total supply. You can burn here in Token Factory, or use the dedicated **Burner** app for the same job.

### Edit metadata

Update your token's **name** and **description** as your project evolves. Two things can never change, though: the **symbol** (ticker) and the number of **decimals** are locked from creation so that everyone across the network always refers to your token the same way.

### Transfer admin

Hand admin control to another wallet address — useful if a project moves to a team wallet or a new owner.

{% hint style="warning" %}
**You are handing over full control.** The address you transfer to gains every admin power you have — minting, burning, editing, even renouncing. Double-check the address before you confirm; there's no undo if you send it to the wrong place.
{% endhint %}

### Renounce admin (Danger zone)

Renouncing gives up your admin power for good and flips your token to **Fixed supply** — provably, permanently, so holders can trust the supply will never grow. Because it's such a final step, it lives in a **Danger zone** and asks you to **type your token's ticker** to confirm you really mean it.

{% hint style="danger" %}
**This cannot be undone.** Once you renounce, no one — including you — can ever mint more, edit details, or reclaim control. Only do this when you're certain you want your token's supply fixed forever.
{% endhint %}

{% hint style="success" %}
**For example.** The book club's **$PAGE** has settled into a steady membership and the supply feels right. To reassure members that no more $PAGE will ever appear, the club opens the Danger zone, types `PAGE` to confirm, and renounces admin. The badge flips to **Fixed supply**, and from now on $PAGE is provably capped.
{% endhint %}
