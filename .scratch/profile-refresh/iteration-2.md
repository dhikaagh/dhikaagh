# Profile Refresh — Iteration 2

Status: approved by Dhika for implementation, commit, and push. Implementation is complete locally and undergoing verification.

Baseline: implemented version at `a6966ed`; see [the first plan](plan.md) and [profile terminology](../../CONTEXT.md).

For this iteration, the decisions below supersede version 1's one-shot animation and stats-removal requirements. All retained positioning, truthfulness, and client-work boundaries still apply.

## Confirmed changes

- The banner must animate repeatedly, like a GIF, rather than tracing once and stopping.
- Chosen motion: a cyan flow marker travels through Build → Deploy → Run, pauses briefly, and repeats.
- Keep SVG as the proposed format; GIF-like motion does not require raster GIF output.
- Technology presentation must include visible names as well as icons. Logo-only rows and hover tooltips do not satisfy this requirement.
- Add a **📊 GitHub Stats** section with three Summary Cards plus a contribution streak card.
- The banner opens automatically and loops, with a native hide/show control. The primary role and introduction remain outside the collapsible banner.
- Make the lower profile more complete through labeled tech-stack presentation and statistics, without inventing new background, work, or learning claims.

## Retained baseline

- Primary identity: Full-Stack Software Engineer.
- Public copy remains English, with web development, CI/CD and deployment as the focus.
- Preserve charcoal/navy surfaces and restrained cyan accents unless a later decision changes them.
- Keep essential identity text static and readable from the first frame.
- PaymentKit and Messaging Bridge remain the approved showcase projects, with proportionate personal-contribution statements.
- Client/private work remains excluded, even if a repository is temporarily public.
- Docker remains qualified at the stated basic level.
- LinkedIn and email remain primary contacts.

## Banner proposal

- Use a relaxed loop of roughly 6–8 seconds, with a brief hold before the next cycle. Exact timing will be tuned visually.
- The marker represents conceptual delivery flow, not current infrastructure status. Avoid uptime counters, health labels, or fake build results.
- Keep the name, role, and focus line outside animation.
- Respect `prefers-reduced-motion`: show a static diagram when motion is reduced or unsupported.
- Ensure mobile still has a small readable flow treatment; the current implementation hides the whole pipeline below 600px, so simply adding `infinite` is not sufficient for mobile.
- Use an initially open `<details>` container with an English `<summary>` such as “Banner animation · hide/show.” This lets visitors hide ongoing motion without JavaScript. GitHub's Markdown API was checked and preserves the open container, summary, and image. Keep the primary role/introduction outside that container.
- No JavaScript, external fonts, animation library, or GIF conversion pipeline is needed.
- Version the embedded image URL (`img/profile-banner.svg?v=2`) to avoid reusing a cached version-1 one-shot banner.

## Technology presentation

Group technologies so the page communicates capability rather than showing an undifferentiated wall of logos:

1. Frontend: React, Next.js, Tailwind CSS.
2. Backend: Node.js, Hono, Laravel.
3. Languages and data: JavaScript, TypeScript, PHP, MySQL, PostgreSQL, RabbitMQ.
4. Delivery and tools: GitHub Actions, GitLab CI/CD, Docker (basics), Linux, Git.

Pair each icon with a visible technology name, or provide an immediately adjacent, matching plain-text list. Tooltip-only and alt-only naming do not satisfy the requirement when images are visible. Keep real text names readable if an icon service fails. Groups should wrap on mobile; a wide table is not required.

## Proposed page hierarchy

1. Banner, role, and concise introduction.
2. Selected work with purpose, contributions, stack, and links.
3. Development and delivery capabilities.
4. Tech stack: grouped icons plus names.
5. 📊 GitHub Stats: supplementary activity information.
6. Contact.

No new employer, seniority, certification, learning-topic, or client-project claims are implied by making the profile more complete.

## Reference inspection

User reference: [KittodGG's profile repository](https://github.com/KittodGG/KittodGG/tree/main).

Inspected [the main README](https://raw.githubusercontent.com/KittodGG/KittodGG/main/README.md) and [the animated SVG source](https://raw.githubusercontent.com/KittodGG/KittodGG/main/assets/animated-terminal.svg).

- The reference has an animated hero, Quick Bio, categorized stack badges, grouped/collapsible projects, a substantial stats grid, and a view-counter footer.
- Its banner is SVG, not GIF. Typing/name reveal runs once; taglines, caret and ambient effects repeat. Dhika's selected effect is a flow marker instead, not a copy of the terminal/pixel presentation.
- Its three Summary Cards return substantive SVGs. Its separate activity-graph endpoint returned HTTP 402 / deployment disabled during inspection; do not reuse that failing host.
- The language card uses repository counts, not code-volume shares. Use an accurate caption such as “Languages by repository,” rather than implying skill levels.
- Borrow structural ideas, not the friend's personal facts, projects, tools, numerical metrics, or profile-view counter.

## Statistics requirements

- Use Dhika's account (`dhikaagh`), never the reference account or copied numerical values.
- Statistics are supplementary activity/code information, not proficiency scores or the principal evidence of engineering ability.
- Preserve plain-text profile content independently of external cards.
- Check returned image content, not only HTTP status: some providers return error SVGs with HTTP 200.
- Use the selected Summary Cards and streak providers below. Hosted-card reliability cannot be guaranteed from one successful check.
- Match light/dark GitHub themes, keep descriptive alt text, and allow cards to stack on mobile.
- Avoid setup requiring a private-account token, hosting deployment, or new workflow unless the user explicitly chooses that trade-off.

## Selected statistics layout and providers

Layout:

```text
📊 GitHub Stats
[          Activity / contribution overview          ]
[ GitHub statistics ] [ Languages by repository count ]
[                 Contribution streak                ]
```

Use **GitHub Profile Summary Cards**:

```text
https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=dhikaagh&theme=github_dark
https://github-profile-summary-cards.vercel.app/api/cards/stats?username=dhikaagh&theme=github_dark
https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=dhikaagh&theme=github_dark
```

Use **GitHub Readme Streak Stats**:

```text
https://streak-stats.demolab.com?user=dhikaagh&theme=github-dark-blue&hide_border=true
```

During planning, the four dark-theme URLs and one light variant were checked. During implementation, all eight final light/dark URLs returned HTTP 200 with parseable, substantive SVG content for `dhikaagh`, including the streak `theme=default` light variant. Prefer provider-supported themes over assuming arbitrary custom-color query parameters are honored. These checks establish current availability, not guaranteed future uptime or data freshness.

Use GitHub-compatible `<picture>` sources for light/dark variants. The two smaller cards should have sensible pixel widths and wrap when space is insufficient, rather than being forced to 49% width on narrow mobile screens. Keep overview and streak centered with descriptive alt text. No access token, hosting deployment, or generation workflow has been needed for the verified public endpoints.

## Verification for a later implementation

- Extend the existing dependency-free README/SVG checks for the revised loop, static identity, labeled technologies, and selected stats.
- Update the old retired-decoration check to allow the explicitly approved streak provider. Preserve unrelated protections against old snake, typing, closing GIF, and view-counter decoration.
- Inspect the real hosted animation, including repeat behavior, reduced motion, and mobile presentation. A static SVG rasterization does not verify animation.
- Validate stats image contents and GitHub Markdown embedding, with readable fallbacks when external cards are unavailable.

## Implementation verification

- Seven dependency-free profile checks pass: `python3 -B -m unittest discover -s tests -v`.
- All 25 external image URLs were checked: 17 technology icons and eight light/dark stats variants. SVGs were parsed, the Hono PNG signature was validated, and stats SVGs were checked for substantive content rather than only HTTP success.
- GitHub's Markdown API preserves the initially open banner control, primary role outside it, 17 visible technology names/icons, four stats cards, and four dark-mode sources. It also preserves the banner's `?v=2` query.
- Native static SVG previews were inspected at 1000 × 320 and 360 × 116. The intended mobile layout was explicitly selected in the renderer; this is not a claim that a browser breakpoint was tested.
- Animation is declared as a continuous seven-second CSS loop, with a reduced-motion static fallback. The earlier environment could not complete headless browser rendering, so source checks and static previews do not claim actual in-browser loop or media-preference verification. Inspect those in the hosted image after publication.

## Approval

Dhika selected “Setujui, implementasikan dan push.” This explicitly authorizes the second-iteration README/banner changes, checks, review, commit, and push. It does not authorize changes to other repositories or their visibility.
