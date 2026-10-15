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

# Making It Official

The **Make it official** goals help people recognise and trust your token:

* **Get my logo in every wallet**: list it in the Cosmos Chain Registry.
* **Give it a look**: a brand kit with colours and a font.
* **Prove the supply is fixed**: lock the supply forever.

## Get my logo in every wallet

Wallets, explorers and DEXes across the Cosmos world read token names and logos from one public list: the **Cosmos Chain Registry** on GitHub. Without it, wallets show a long code instead of your token's name and logo. Being listed is free: you send a request with your logo, and the registry's maintainers review it.

Token Factory's guide walks you through it in five steps, and keeps your progress in this browser:

1. **Prepare your logo.** Drop your file in and it's checked right in your browser (nothing is uploaded): **PNG or SVG** only (SVG is preferred, it stays sharp at every size), **square**, **under 250 KB**, and a lower-case file name. A JPG is refused, even renamed to .png, and an SVG must be real vector art, not a picture wrapped in SVG. You see a preview on a light and a dark wallet.
2. **Add your links (optional).** Your website and X (Twitter).
3. **Copy your registry entry.** The app writes it for you from your token's details; you don't need to edit it. Your token needs a description first.
4. **Send it to the registry.** With a free GitHub account, all in the browser: copy the registry, upload your logo, paste your entry, and open a pull request. The guide lists each click. Paste your pull request link back into the guide so it can follow it for you.
5. **Wait for the review.** It can take from a few days to a few weeks. The guide checks the registry and turns green once your token is listed. BeeZee apps show the logo after their next update; other wallets follow when they update their lists.

{% hint style="info" %}
**Stuck?** The guide lists the most common reasons a request is sent back (not square, over 250 KB, a renamed JPG, an upper-case file name, a missing comma) and links to the BeeZee community on Telegram and Discord.
{% endhint %}

## Give it a look: the brand kit

A **brand kit** gives your token its own look on its page in the [Communities app](../communities/README.md): a **font** (Inter, Roboto, Poppins, Montserrat, Space Grotesk or JetBrains Mono) and **eight colours**, a background, text, primary and secondary colour for both light and dark mode.

Set it from the **Profile** tab of your token's page. A live preview shows the result before you select **Save brand kit**. It's public, and apps that support brand kits pick it up right away. You can edit it or remove it later, as long as you still control the token.

## Prove the supply is fixed: lock the supply

While you control your token, buyers see it as **Mintable**: you could mint more. **Locking the supply** gives up that power for good, and everyone sees **Fixed supply** instead. It's the strongest trust signal a token can have, so do it **last**, once your setup is done.

Open the **Control** tab of your token's page and select **Lock TICKER forever…**. Before anything happens, the app shows you:

* **Before you lock, check your setup**: your name and description are final, the brand kit is set, the supply is what you want.
* **Frozen forever**: minting more, the name and description, the brand kit, and handing control to someone else.
* **Keeps working**: trading, pools and markets; holder rewards, airdrops and staking programs; anyone burning their own tokens; getting listed in the registry.

To confirm, tick that you understand it can't be undone **and** type your token's ticker exactly.

{% hint style="danger" %}
**Locking can never be undone**: not by you, not by BeeZee, not by anyone. A description or brand kit you haven't added by then can never be added. Only lock when you are sure.
{% endhint %}

## Hand over control

Instead of locking, you can hand control of your token to another address, for example a team wallet or a DAO. The **Control** tab has a **Hand over control** form for it.

{% hint style="warning" %}
**You lose all control.** The new address gets every power you had: minting, editing what wallets show, the brand kit, and handing control on. Triple-check the address before you confirm; there's no undo.
{% endhint %}

{% hint style="success" %}
**For example.** The book club's **$PAGE** has its pool, holder rewards and logo, and the supply feels right. To show members that no more $PAGE will ever appear, the club opens **Control**, checks the list, types `PAGE` and locks it. Everywhere, $PAGE now shows **Fixed supply**.
{% endhint %}

{% content-ref url="playbooks.md" %}
[playbooks.md](playbooks.md)
{% endcontent-ref %}
