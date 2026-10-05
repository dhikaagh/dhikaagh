# Professional GitHub Profile Refresh

Status: planning approved by Dhika. Positioning, English copy, selected work, showcase permission, and visual direction are confirmed. Implementation has not been authorized.

Use [CONTEXT.md](../../CONTEXT.md) for profile terminology.

## Confirmed direction

- Audience: recruiters and engineering teams.
- Public-facing copy: concise, natural English.
- Visual direction: clean infrastructure, with a charcoal/navy banner and restrained cyan accents.
- Banner concept: delivery pipeline, not a recreation of the supplied terminal/pixel reference.
- Name and role remain readable from the first frame; motion is secondary to the content.
- Pipeline motion traces briefly on load, then settles.
- Decoration: minimal and focused on work. Remove the typing animation, closing GIF, contribution statistics, contribution snake, and view counter.

## Experience supplied by Dhika

These are self-reported capabilities, not independently verified credentials:

- Web development.
- CI/CD and deployment using GitHub Actions and GitLab CI/CD.
- Basic Docker knowledge.
- Server/VPS management.

Use specific, proportionate descriptions. Keep Docker at its stated level; avoid unsupported seniority, scale, uptime, or production reliability claims.

## Confirmed positioning

Primary title: **Full-Stack Software Engineer**.

Focus line: **Web applications · CI/CD · Deployment**.

The qualifier makes the software engineering role specific to frontend/backend web development. Delivery skills remain supporting capabilities, not a separate DevOps Engineer title.

Approved English intro:

> I build full-stack web applications and APIs, with hands-on experience in CI/CD, VPS deployment, and server management.

## Proposed content hierarchy

1. Banner and primary role.
2. Short professional introduction.
3. Selected work: project purpose, personal contribution, stack, and links.
4. Development and delivery: concise capabilities grounded in actual experience.
5. Tools: a curated set, rather than every technology encountered.
6. Contact: prioritize LinkedIn and email; publish a website link only when it exists.

## Public project findings

Research surfaced possible projects, but public visibility alone does not establish ownership or permission to showcase client work. The strongest deployment artifacts were also checked directly after the research report.

### Approved selected work

Dhika confirmed that both projects below may be showcased publicly and will remain public.

1. **[PaymentKit](https://github.com/dhikaagh/paymentkit)** — API development and delivery evidence. The repository contains a [multi-stage, non-root Dockerfile](https://github.com/dhikaagh/paymentkit/blob/main/api/Dockerfile). Its [GitHub Actions deployment workflow on `sapi`](https://github.com/dhikaagh/paymentkit/blob/sapi/.github/workflows/deploy.yml) builds/tests the API, publishes a container image, and deploys to a VPS. A [public run](https://github.com/dhikaagh/paymentkit/actions/runs/24311100626) has successful Build & Test and Deploy to VPS jobs. This supports a concrete CI/CD and deployment description, not an uptime or production-reliability claim. Treat this as an API/backend showcase; the README's advertised Next.js frontend was not found in the inspected main tree.
2. **[Messaging Bridge](https://github.com/dhikaagh/Messaging-Bridge-)** — a messaging/API integration candidate with [Hono and messaging-related dependencies](https://github.com/dhikaagh/Messaging-Bridge-/blob/main/package.json). Avoid unmeasured performance claims.

These selected examples are API/backend-oriented; do not present them as frontend evidence merely to balance the profile. Final descriptions must reflect Dhika's actual contributions rather than implying sole authorship from repository ownership.

Approved project copy:

- **PaymentKit:** A payment API with asynchronous processing, containerized services, and a GitHub Actions deployment workflow.
- **Messaging Bridge:** An API for integrating Telegram, email, and WhatsApp messaging.

### Evidence boundaries

- The research reported 16 public repositories and focused primarily on main branches, with PaymentKit's deployment branch/run checked separately.
- A successful workflow run does not establish that a service is currently live or comprehensively managed.
- GitLab CI/CD remains a capability supplied by Dhika; it was not independently demonstrated by the cited public GitHub artifacts.
- Private/client work is outside this profile version's scope, including client projects that happen to be publicly accessible now.

### Curated technology direction

Prioritize technologies relevant to the selected work: JavaScript/TypeScript, PHP, React, Tailwind, Laravel, Node.js/Hono, and the actual database/messaging tools used. Keep delivery tools in a separate compact group: GitHub Actions, GitLab CI/CD, Docker, and server/VPS management. This is a shortlist to curate, not a requirement to display every dependency or a claim of equal proficiency.

## Banner design proposal

- Background: charcoal navy `#0D1422`.
- Secondary surface: slate navy `#152238`.
- Main text: near-white `#E6EDF3`.
- Secondary text: muted slate `#94A3B8`.
- Flow accent: cyan `#4DC9D4`.
- Secondary accent, only if needed: blue `#3E83F8`.
- Display name: Dhika. Keep the name and complete role static and prominent.
- Use system sans-serif for the identity and restrained monospace labels for the pipeline. No external font loading.
- Aim for a wide banner of roughly 3:1, with generous spacing. Keep essential text readable when scaled down; reduce decorative details rather than shrinking the role to fit.

Conceptual layout, not a claim about a project's live infrastructure:

```text
DHIKA                                      BUILD → DEPLOY → RUN
Full-Stack Software Engineer                brief tracing accent
Web applications · CI/CD · Deployment
```

If the pipeline becomes too small on mobile, simplify it. The identity matters more than retaining every stage label.

## Proposed implementation

- Create a self-contained animated SVG at `img/profile-banner.svg` and embed it as an image in `README.md`; do not paste inline SVG or rely on JavaScript in the README.
- Keep important text static and visible when animation is disabled or unsupported. Include an accessible title/description, image alt text, and a reduced-motion fallback.
- Use a fixed dark banner surface that remains legible within both GitHub themes. Fonts and colors must work within the SVG image itself, rather than depending on README CSS.
- Remove `.github/workflows/snake.yml` when the snake is removed, so unused animation generation no longer runs.
- Start with SVG rather than a GIF or new build dependencies. Verify the hosted image on GitHub before deciding whether a GIF fallback is necessary.

## Verification before publishing

- Check the English copy and all profile claims against the agreed facts.
- Validate SVG XML and confirm first-frame/static readability.
- Review the banner at mobile width and in GitHub's light/dark themes.
- Verify the animation and reduced-motion behavior in the rendered image; do not assume local rendering proves GitHub behavior.
- Check project and contact links and confirm that only public or explicitly permitted information is shown.

## Selected-work boundaries

Use only public projects that Dhika is permitted to showcase and intends to keep public. Exclude freelance/client work even when its repository is temporarily public. One previously proposed client project was removed after Dhika clarified that it will become private; keep its name, links, and identifying details out of the profile plan.

PaymentKit and Messaging Bridge have been approved by Dhika for the public showcase. Changing another repository's visibility is a separate action and has not been requested for this session.

## Delivery sequence after approval

1. Finalize the concise English copy and any selected public projects.
2. Create and visually review the SVG banner before integrating it.
3. Update the README, remove unused decoration and the snake generator, and check the rendered GitHub profile.

No issue tracker setup, multi-session tickets, or new build pipeline is needed for this small change.

## Planning approval

Dhika approved this plan, including the English copy, selected work, and visual direction. Planning approval is not implementation permission: creating the SVG banner or editing the README requires a subsequent request.
