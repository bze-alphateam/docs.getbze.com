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

Two things help people recognise and trust your token: its **logo in every wallet**, and a **brand kit** that gives it its own look. Both start from your token's page in Token Factory (see [Managing Your Token](managing-your-token.md)), and both are suggested on the Done screen right after you create a token.

## Get your logo in every wallet

Wallets, explorers and DEXes across the Cosmos world read token names and logos from one public list: the **Cosmos Chain Registry** on GitHub. Without an entry, most wallets show your token as a long code with no logo, which looks like a scam even when it isn't. Being listed is free, and nothing is signed: you prepare the files in Token Factory and open a request on GitHub, and the registry's maintainers review it.

Open the guide from your token's page: **Get your logo in every wallet** in its details, or the **Logo in wallets** setup chip. The guide has five steps and keeps your progress in this browser:

1. **Logo: prepare your logo.** Drop your file in and it's checked right in your browser (nothing is uploaded): **PNG or SVG** only (SVG is preferred, it stays sharp at every size), **square**, **under 250 KB**, and a lower-case file name. A JPG is refused, even renamed to .png, and an SVG must be real vector art with under 1,000 shapes, not a picture wrapped in SVG. You see a preview on a light and a dark wallet.
2. **Links: add your links (optional).** Your website and X (Twitter), as full `https://` links.
3. **Entry: copy your registry entry.** The app writes it for you from your token's details; you won't need to edit it. Your token needs a description first, because wallets show it.
4. **Submit: send it to the registry.** With a free GitHub account, all in the browser, no coding: make your own copy of the registry, upload your logo, paste your entry, and open a pull request. The guide lists each click. Paste your pull request link back into the guide so it can follow it for you.
5. **Review: wait for the registry team.** It usually takes a few days, sometimes longer. The guide checks the registry and moves on once your token is listed. BeeZee apps show the logo after their next update; other wallets follow when they update their lists.

{% hint style="info" %}
**The registry only lists mainnet tokens.** On a test network you can prepare every file, and submit them once your token is on mainnet.
{% endhint %}

{% hint style="info" %}
**Stuck?** The guide lists the most common reasons a request is sent back (not square, over 250 KB, a renamed JPG, an upper-case file name, a missing comma in the list) and links to the BeeZee community on Telegram and Discord.
{% endhint %}

## Give it a look: the brand kit

A **brand kit** gives your token its own look on its page in the [Communities app](../communities/README.md): a **font** (Inter, Roboto, Poppins, Montserrat, Space Grotesk or JetBrains Mono) and **eight colours**, a background, text, primary and secondary colour for both light and dark mode.

Set it from **Details and look** on your token's page. A live preview shows the result before you save it. It's public, and apps that support brand kits pick it up right away. Only the token's admin can set, edit or remove it.

{% hint style="warning" %}
**Set it while you are the admin.** If admin is ever renounced, the brand kit is frozen as it is: a brand kit that was never set can never be added. See [Permissions](managing-your-token.md#permissions).
{% endhint %}

{% hint style="success" %}
**For example.** The book club gives **$PAGE** a warm paper-and-ink brand kit, then runs the registry guide: a square SVG of an open book, the club's website, and the entry the guide wrote. A few days later the pull request is merged and $PAGE shows its logo in wallets.
{% endhint %}

{% content-ref url="managing-your-token.md" %}
[managing-your-token.md](managing-your-token.md)
{% endcontent-ref %}
