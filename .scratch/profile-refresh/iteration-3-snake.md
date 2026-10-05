# Profile Refresh — Iteration 3: Contribution Snake

Status: implemented locally and verified. No commit or push has been performed.

Baseline: the live profile at `e5d5750` includes the looping delivery banner, labeled tech stack, and GitHub Stats section. The earlier refresh deliberately removed the old contribution snake as distracting decoration. This plan intentionally supersedes that one narrow decision while retaining the profile's positioning, evidence, accessibility, and client-work boundaries.

## Recommendation

Add the snake as a small, optional visual under the existing GitHub Stats section, before Contact. It can add personality and make contribution activity visually memorable, but it must remain supplementary evidence—not a proficiency score, work claim, or replacement for Selected work.

Keep the existing banner, stats cards, and streak card. Do not put the snake inside the banner or add another stats provider.

Proposed hierarchy:

```text
📊 GitHub Stats
[ existing activity / stats / language / streak cards ]

🐍 Contribution Activity · hide/show
[ light or dark generated contribution snake ]

Contact
```

Use an initially open native `<details>` control so visitors can hide the animation without JavaScript. This also prevents the lower page from feeling like an unavoidable wall of moving images.

## Minimal implementation

### 1. Regenerate the existing workflow

Restore `.github/workflows/snake.yml`, based on the repository's former `Platane/snk@v3` workflow, with only the required outputs:

- `github-contribution-grid-snake.svg`
- `github-contribution-grid-snake-dark.svg?palette=github-dark`

Publish the generated files to the existing `output` branch. Use `github_user_name: dhikaagh`; never copy another account's output.

Triggers:

- daily scheduled refresh, which is sufficient for contribution activity;
- `workflow_dispatch` for the first generation and manual recovery.

Do not trigger on every `main` push unless a live profile change proves that is needed. The profile README does not need a new build system or a committed generated SVG.

The workflow must grant only the contents write permission needed to publish the generated branch. At implementation time, pin action references to reviewed immutable commits if the repository's current action policy requires it; otherwise preserve the small existing workflow rather than introducing extra tooling.

### 2. Add one README section

After the existing streak card and before Contact, add an English section such as:

```html
<details open>
<summary>🐍 Contribution activity · hide/show</summary>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)"
      srcset="https://raw.githubusercontent.com/dhikaagh/dhikaagh/output/github-contribution-grid-snake-dark.svg" />
    <img src="https://raw.githubusercontent.com/dhikaagh/dhikaagh/output/github-contribution-grid-snake.svg"
      width="100%" alt="Animated contribution activity graph for dhikaagh" />
  </picture>
</p>

</details>
```

Keep the wording factual: “Contribution activity” is safer than implying skill, consistency, or engineering performance. Preserve the existing stats disclaimer.

### 3. Extend the dependency-free checks

Update `tests/test_profile.py` to verify:

- the snake section has one accessible image and one dark-mode source;
- both URLs use the `dhikaagh/dhikaagh` `output` branch and the expected filenames;
- the workflow uses `dhikaagh`, publishes both light/dark outputs, has scheduled and manual triggers, and grants contents write access;
- the retired-decoration test no longer rejects the explicitly approved snake, while it continues to reject typing SVGs, the closing GIF, view counter, and unrelated old decoration;
- the existing banner, project, tech-stack, and stats protections remain unchanged.

Do not make ordinary unit tests depend on the network. Check hosted output separately during verification.

## Verification before publishing

1. Run `python3 -B -m unittest discover -s tests -v`.
2. Run the workflow manually and confirm the `output` branch contains both substantive SVGs for `dhikaagh`.
3. Check both raw URLs return SVG content, not an HTTP-200 error document.
4. Inspect the GitHub-rendered README in light and dark themes, including the native hide/show control and narrow-width wrapping.
5. Confirm the existing profile copy still presents the snake as supplementary activity, not as a skill rating or professional claim.
6. Run Standards and Spec review against the current `main` before commit.

## Acceptance criteria

- The live README shows one optional contribution snake below the existing stats.
- Light and dark GitHub themes select the matching generated SVG.
- The animation can be hidden without JavaScript.
- The workflow refreshes the artifact daily and manually, without running on every README push.
- No new dependency, token, hosting deployment, or change to other repositories is introduced.
- All existing profile tests pass, plus the new snake-specific checks.
- No client/private project, unsupported metric, or copied profile fact is added.

## Risks and rollback

- Scheduled GitHub Actions can be delayed or disabled; the stats cards and plain-text profile remain useful without the snake.
- The generated SVG is an external branch artifact and can fail independently of the README. Verify its content, not only HTTP status.
- A snake plus four stats cards may be visually busy. If it dominates the profile, first keep it collapsed by default or remove only this section and workflow; do not weaken the core profile content.
- Rollback is limited to removing the snake section and `.github/workflows/snake.yml`, then deleting the generated `output` branch if it has no other use.

## Implementation verification

- Added the optional snake section to `README.md` with native hide/show control and light/dark sources.
- Added `.github/workflows/snake.yml` with daily and manual triggers, `dhikaagh`, and contents-write permission.
- Extended the dependency-free profile checks; `python3 -B -m unittest discover -s tests -v` passes all 9 tests.
- `git diff --check` passes.
- The existing light/dark `origin/output` SVGs returned HTTP 200 and parsed as substantive SVG documents.
- GitHub-rendered Markdown and the newly added workflow will need live verification after publication.

Approval of this plan authorizes implementation of the profile README, test, and workflow only. It does not authorize changes to other repositories or their visibility.
