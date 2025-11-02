```markdown
# Team Workflow Guide

A concise, practical guide to contributing to the FakeNews_Spam_Detection repository.

Purpose
- Keep the repository clean, reviewable, and stable.
- Ensure changes are tested and reviewed before reaching `main`.
- Protect sensitive data and enforce reproducible work.

Principles
- main is protected — never push directly.
- One task = one branch, one focused PR.
- Small, frequent commits with meaningful messages.
- Automated checks (CI/tests) run on PRs — green must pass before merge.

Quick overview (TL;DR)
1. Create a branch from `main`.
2. Make changes and add tests where applicable.
3. Commit with clear messages.
4. Push branch and open a PR.
5. Request review, address feedback.
6. Merge after CI passes and at least one approval.

Branching strategy
- Always branch off the latest `main`.
- Branch name formats:
  - feature/<your-name>-<short-desc> e.g. feature/ajay-add-feature-extraction
  - fix/<issue-number>-<short-desc> e.g. fix/12-fix-tokenizer-bug
  - chore/<short-desc> e.g. chore/update-deps
  - experiment/<short-desc> for exploratory work (do not merge to main without review)

Commands
- Keep your local main up-to-date:
  - git checkout main
  - git pull origin main
- Create a branch:
  - git checkout -b feature/<your-name>-<short-desc>
- Stage & commit:
  - git add <files>
  - git commit -m "type(scope): short summary

    Longer description if needed (wrap at ~72 chars)."
- Push:
  - git push origin feature/<your-name>-<short-desc>

Commit message conventions
- Use imperative, concise summaries.
- Optional emoji or conventional prefixes:
  - feat: new feature
  - fix: bug fix
  - docs: documentation only changes
  - style: formatting, no code change
  - refactor: code change that neither fixes a bug nor adds a feature
  - test: adding or fixing tests
  - chore: maintenance
- Example:
  - feat(model): add TF-IDF feature extraction
  - fix(preprocessing): handle empty text inputs

Pull Request (PR) process
- Open a PR against `main` with a clear title and description:
  - What changed and why
  - What files/areas to review
  - How to test locally
- Link related issue(s) if any: Closes #<issue-number>
- Assign reviewers and/or request specific teammates.
- At least one approval required before merging (preferably 2 for larger changes).
- Wait for CI to pass before merging.

PR checklist (what reviewers and authors should verify)
- [ ] PR description explains the why and what.
- [ ] Branch builds locally and tests pass.
- [ ] Automated tests (unit/integration) included or updated where relevant.
- [ ] No sensitive data (datasets, credentials, keys) committed.
- [ ] Code is adequately documented and readable.
- [ ] New dependencies are justified.
- [ ] Linting/style standards followed.

Testing & CI
- Add unit tests for core logic where feasible.
- Keep notebooks reproducible — avoid committing large raw data.
- CI runs on PRs; fix failing checks before merging.

Data handling
- data/ is ignored in this repo. Do not commit raw datasets, API keys, or credentials.
- If a dataset is required, include instructions or a script to download/preprocess it in scripts/ or docs/.
- Use sample or synthetic data for tests and CI.

Releases & main
- main should always be in a deployable state.
- After merge, CI should confirm no regressions.
- Use tags or changelogs for release notes when publishing versions.

Reverting & emergency fixes
- For urgent fixes use a small, well-tested PR (branch fix/...).
- If a merge introduces regressions, revert the PR or create a hotfix branch and follow the normal PR review flow.

Communication
- Mention reviewers in PRs and be responsive to feedback.
- For design or large changes, open an issue or draft PR first to discuss.
- Use the repository Issues for tracking tasks/bugs.

Useful commands (reference)
- Update local main: git checkout main && git pull origin main
- Create branch: git checkout -b feature/yourname-shortdesc
- Push branch: git push -u origin feature/yourname-shortdesc
- Rebase branch onto latest main (optional): git fetch origin && git rebase origin/main
- Merge PR on GitHub once approved and CI is green

Contacts / Reviewers
- Maintainer: @ajayram231210006
- Add other reviewers as appropriate in PRs.

Example PR template (suggested)
Title: feat(<area>): short summary

Description:
- Summary: What changed and why
- How to test:
  - Steps to reproduce locally
- Related issues: Closes #X

Notes:
- Any extra context or screenshots

Final notes
- Small, focused PRs are the fastest to review and merge.
- If you're unsure, ask before implementing — open an issue or draft PR to discuss design choices.
- Thank you for contributing — let's keep the codebase clean, reproducible, and collaborative!

```
