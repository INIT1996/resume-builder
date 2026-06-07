# HTML Pagination

Use this reference for every generated HTML resume, even when the content appears to fit on one A4 page. It defines the default A4 page structure and JavaScript paginator. Also use it when page margins disappear after printing, CSS-only page breaks create large blank gaps, split fragments lose formatting, or continuation headers repeat.

## Core Idea

Generate the resume as a normal linear source flow first, then run a small paginator after fonts and images are loaded. The paginator measures the rendered height of each content block and moves blocks into fixed A4 `.resume-page` containers. A page is full when adding the next block would exceed the available content height after top and bottom padding. If the content fits on one page, the paginator still produces one `.resume-page`; do not skip the pagination structure.

This prevents the browser from slicing one long document at arbitrary positions and keeps every printed page inside the same page padding.

The paginator must not stop at large top-level modules. If the next `.resume-block` does not fit but the remaining page still has useful space, split by the current page's measured remaining height. The fragment moved upward may be as small as one rendered text line. Only move the whole block to the next page when no safe fragment can fit.

When a module is split, preserve visual consistency. A moved line fragment should still use the same card system, bullet indentation, accent edge, background, border, and spacing rhythm as the original module. Do not place bare text directly on the page background. The remaining text and the rest of the module should become one continuation block; do not repeatedly split the same header or create several continuation labels for one logical module.

## Required Structure

Use a hidden source flow and an empty page container:

```html
<main id="resume-pages" class="resume-pages"></main>

<template id="resume-source">
  <section class="resume-block resume-hero">...</section>
  <section class="resume-block resume-section">...</section>
  <article class="resume-block resume-card">...</article>
</template>
```

Rules:

- Mark every top-level movable unit with `.resume-block`.
- Keep blocks small enough to move: section headings, short cards, skill groups, project bullet groups, education rows.
- Do not mark a whole long project list or full two-column grid as one unbreakable block.
- For long cards, split them into smaller `.resume-block` siblings, such as a card header with the first bullet, then a continued card for remaining bullet groups. This lets the paginator use leftover space instead of moving the whole card to the next page.
- For section blocks that contain a title and a large card, split them into a first fragment containing the section title and the first card fragment, then continuation card fragments.
- Avoid layouts where a sidebar must span multiple printed pages as one element. For print, prefer page-local sections or repeat compact sidebar information only when needed.
- Preserve formatting across fragments. Continuation fragments should remain cards or section/card fragments, not plain paragraphs unless the original module is also plain text.

## CSS Requirements

Use fixed A4 page geometry and padding. The padding is the page margin users see.

```css
@page {
  size: A4;
  margin: 0;
}

.resume-pages {
  background: #e5e7eb;
}

.resume-page {
  width: 210mm;
  height: 297mm;
  margin: 24px auto;
  padding: var(--page-padding, 16mm 18mm);
  background: #fff;
  overflow: hidden;
  box-sizing: border-box;
}

.resume-page-content {
  height: 100%;
}

.resume-page-content > .resume-block {
  margin-top: 0;
  margin-bottom: 0;
}

.resume-page-content > .resume-block + .resume-block {
  margin-top: 12px;
}

.resume-card--page-fragment {
  padding-top: 8px;
  padding-bottom: 8px;
}

.resume-line-fragment {
  padding-top: 6px;
  padding-bottom: 6px;
  background: rgba(255, 255, 255, 0.7);
}

.resume-line-fragment ul {
  padding-left: 18px;
}

.resume-line-fragment li {
  margin: 0;
}

@media print {
  body {
    margin: 0;
    background: #fff;
  }

  .resume-page {
    margin: 0;
    box-shadow: none;
    break-after: page;
  }

  .resume-page:last-child {
    break-after: auto;
  }
}
```

Do not set `@page` margins and `.resume-page` padding to both act as the same visual margin. Use `@page margin: 0` and let `.resume-page` padding be the controlled margin.

## Pagination Decision Order

Use this order so the paginator fills pages without creating duplicate headers:

1. Try to append the whole block to the current page.
2. If it does not fit and the current page has content, measure how much of the next block's first text item can fit in the remaining height.
3. If at least one useful text fragment fits, append that fragment to the current page using the same card/bullet formatting, then move the rest of the source block to the next page as one continuation block.
4. If no useful fragment fits, open a new page and try the whole block there.
5. Only when a block still does not fit on an empty page, split it into card or section fragments.
6. If an empty-page fragment is still too tall, mark it with `.resume-block--too-tall` and fix the source structure or spacing.

This order prevents two common failures: a split fragment calculated for the previous page but never appended, and a continuation block whose header is split repeatedly on the next page.

## JavaScript Paginator

Use this pattern in the generated HTML. Adjust selectors only if the HTML structure differs.

```html
<script>
async function paginateResume() {
  if (document.fonts && document.fonts.ready) {
    await document.fonts.ready;
  }

  const pagesRoot = document.getElementById("resume-pages");
  const sourceTemplate = document.getElementById("resume-source");
  const sourceBlocks = Array.from(sourceTemplate.content.children);
  pagesRoot.innerHTML = "";

  const createPage = () => {
    const page = document.createElement("section");
    page.className = "resume-page resume-template resume-template--ats-clean";
    const content = document.createElement("div");
    content.className = "resume-page-content";
    page.appendChild(content);
    pagesRoot.appendChild(page);
    return content;
  };

  let current = createPage();
  const getMaxHeight = () => current.getBoundingClientRect().height;

  const getUsedHeight = (container) => {
    const children = Array.from(container.children);
    if (!children.length) return 0;
    const containerTop = container.getBoundingClientRect().top;
    return Math.max(...children.map((child) => {
      const rect = child.getBoundingClientRect();
      const style = getComputedStyle(child);
      return rect.bottom - containerTop + parseFloat(style.marginBottom || "0");
    }));
  };

  const tryAppend = (block) => {
    current.appendChild(block);
    if (getUsedHeight(current) > getMaxHeight() + 1) {
      current.removeChild(block);
      return false;
    }
    return true;
  };

  const continuationLabel = (block) => {
    const title = block.querySelector(".resume-card-head h3")?.textContent.trim()
      || block.querySelector("h3")?.textContent.trim()
      || "Previous item";
    const label = document.createElement("p");
    label.className = "resume-continuation-label";
    label.textContent = `${title} · continued`;
    return label;
  };

  const cloneWithoutChildren = (block) => {
    const clone = block.cloneNode(false);
    clone.classList.add("resume-block");
    return clone;
  };

  const splitCard = (card) => {
    const list = card.querySelector(":scope > ul:not(.resume-tags)");
    const items = list ? Array.from(list.children) : [];
    if (items.length < 2) {
      return [];
    }

    const head = card.querySelector(":scope > .resume-card-head");
    const meta = card.querySelector(":scope > .resume-meta");
    const tags = card.querySelector(":scope > .resume-tags");

    return items.map((item, index) => {
      const fragment = cloneWithoutChildren(card);
      if (index === 0) {
        if (head) fragment.appendChild(head.cloneNode(true));
        if (meta) fragment.appendChild(meta.cloneNode(true));
      } else {
        fragment.classList.add("resume-card--continued");
        fragment.appendChild(continuationLabel(card));
      }

      const fragmentList = list.cloneNode(false);
      fragmentList.appendChild(item.cloneNode(true));
      fragment.appendChild(fragmentList);

      if (index === items.length - 1 && tags) {
        fragment.appendChild(tags.cloneNode(true));
      }
      return fragment;
    });
  };

  const splitSection = (section) => {
    const title = section.querySelector(":scope > .resume-section-title");
    const card = section.querySelector(":scope > .resume-card");
    const cardFragments = card ? splitCard(card) : [];
    if (!title || !cardFragments.length) {
      return [];
    }

    const first = cloneWithoutChildren(section);
    first.appendChild(title.cloneNode(true));
    first.appendChild(cardFragments[0]);
    return [first, ...cardFragments.slice(1)];
  };

  const splitBlock = (block) => {
    if (block.classList.contains("resume-card")) {
      return splitCard(block);
    }
    if (block.classList.contains("resume-section")) {
      return splitSection(block);
    }
    return [];
  };

  const compactForCurrentPage = (block) => {
    const compact = block.cloneNode(true);
    if (compact.classList.contains("resume-card")) {
      compact.classList.add("resume-card--page-fragment");
    }
    compact.querySelectorAll(".resume-card").forEach((card) => {
      card.classList.add("resume-card--page-fragment");
    });
    return compact;
  };

  const findFirstListItem = (block) => block.querySelector("li");

  const buildLineFragment = (text) => {
    const article = document.createElement("article");
    article.className = "resume-block resume-card resume-card--continued resume-card--page-fragment resume-line-fragment";
    const list = document.createElement("ul");
    const item = document.createElement("li");
    item.textContent = text;
    list.appendChild(item);
    article.appendChild(list);
    return article;
  };

  const buildRemainderFragment = (sourceBlock, remainderText) => {
    const clone = sourceBlock.cloneNode(true);
    clone.classList.add("resume-block", "resume-card--continued");
    clone.querySelectorAll(".resume-card").forEach((card) => {
      card.classList.add("resume-card--continued");
    });

    const firstItem = findFirstListItem(clone);
    if (firstItem) {
      firstItem.textContent = remainderText;
    }

    const firstCard = clone.classList.contains("resume-card")
      ? clone
      : clone.querySelector(".resume-card");
    if (firstCard && !firstCard.querySelector(":scope > .resume-continuation-label")) {
      firstCard.insertBefore(continuationLabel(sourceBlock), firstCard.firstChild);
    }

    clone.querySelectorAll(".resume-card-head").forEach((head) => head.remove());
    return clone;
  };

  const splitTextToFitCurrentPage = (block) => {
    if (!current.children.length) {
      return null;
    }

    const firstItem = findFirstListItem(block);
    const text = firstItem?.textContent.trim();
    if (!text || text.length < 8) {
      return null;
    }

    let low = 1;
    let high = text.length - 1;
    let best = 0;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const candidateText = text.slice(0, mid).replace(/[，。；、\s]+$/, "");
      const candidate = buildLineFragment(candidateText);
      current.appendChild(candidate);
      const fits = getUsedHeight(current) <= getMaxHeight() + 1;
      current.removeChild(candidate);

      if (fits) {
        best = candidateText.length;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    if (best < 4) {
      return null;
    }

    const prefix = text.slice(0, best).replace(/[，。；、\s]+$/, "");
    const suffix = text.slice(best).replace(/^[，。；、\s]+/, "");
    if (!prefix || !suffix) {
      return null;
    }

    return {
      head: buildLineFragment(prefix),
      tail: buildRemainderFragment(block, suffix)
    };
  };

  const appendAtomically = (block) => {
    if (tryAppend(block)) {
      return;
    }

    if (current.children.length) {
      const compact = compactForCurrentPage(block);
      if (tryAppend(compact)) {
        return;
      }
    }

    if (!current.children.length) {
      current.appendChild(block);
      block.classList.add("resume-block--too-tall");
      return;
    }

    current = createPage();
    if (!tryAppend(block)) {
      current.appendChild(block);
      block.classList.add("resume-block--too-tall");
    }
  };

  const appendBlock = (block) => {
    if (tryAppend(block)) {
      return;
    }

    const textSplit = splitTextToFitCurrentPage(block);
    if (textSplit && tryAppend(textSplit.head)) {
      current = createPage();
      appendBlock(textSplit.tail);
      return;
    }

    if (current.children.length) {
      current = createPage();
      appendBlock(block);
      return;
    }

    const fragments = splitBlock(block);
    if (fragments.length > 1) {
      for (const fragment of fragments) {
        appendAtomically(fragment);
      }
      return;
    }

    appendAtomically(block);
  };

  for (const original of sourceBlocks) {
    appendBlock(original.cloneNode(true));
  }
}

window.addEventListener("load", paginateResume);
window.addEventListener("resize", () => {
  clearTimeout(window.__resumePaginateTimer);
  window.__resumePaginateTimer = setTimeout(paginateResume, 120);
});
</script>
```

## Handling Oversized Blocks

If a block receives `.resume-block--too-tall`, do not ignore it. Fix it by one of these methods:

- Split the block into smaller `.resume-block` units and let the paginator pull the first fragment into the current page when space allows.
- If even the first fragment is too tall for the remaining space, split the first text item by measured rendered height and move only the amount of text that fits, even if that is just one line. Keep the moved fragment in the same visual format as the original card or section. Keep the remaining text and the rest of the module together as a single continuation block.
- If the first fragment narrowly does not fit, try a compact page-fragment style with reduced card padding and bullet spacing before opening a new page.
- Reduce only visual spacing, card padding, or section gap.
- Let bullet groups split while keeping headings with the first bullet.
- Move decorative elements out of print mode.
- Do not create multiple repeated continuation headers for the same source module.

Do not solve oversized blocks by removing real resume content unless the user explicitly asked for compression.

## Verification

After pagination, inspect the rendered pages:

- Every page has visible top and bottom padding.
- No heading is pressed against the page top or bottom.
- No content is clipped by `.resume-page { overflow: hidden; }`.
- No `.resume-block--too-tall` elements remain unresolved.
- Print preview shows one A4 page per `.resume-page`.
- The last page may have whitespace, but earlier pages should not have large blank gaps unless the next block truly cannot be split.
- Split fragments preserve the source module's formatting: card border/background, accent edge, bullet indentation, and spacing remain consistent.
- A module that is split across pages has at most one continuation label per continuation block; the same header is not repeated several times in a row.
