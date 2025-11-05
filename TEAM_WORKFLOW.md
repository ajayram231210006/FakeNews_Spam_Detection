
---

# 🧩 Team Workflow Guide

**Repository:** `FakeNews_Spam_Detection`
**Purpose:** To maintain a clean, stable, and reproducible collaborative workflow.

---

## 🎯 Objectives

* Keep the repository **clean, reviewable, and stable**.
* Ensure all changes are **tested and reviewed** before merging.
* Protect **sensitive data** and enforce **reproducibility**.

---

## ⚙️ Core Principles

* **`main` is protected** — never push directly.
* **One task = one branch + one PR.**
* Make **small, frequent commits** with meaningful messages.
* **CI/tests must pass** before merging.

---

## 🚀 Quick Overview (TL;DR)

1. Create a branch from `main`.
2. Make changes and add tests (if applicable).
3. Commit with clear messages.
4. Push your branch and open a PR.
5. Request review and address feedback.
6. Merge after CI passes ✅ and at least one approval.

---

## 🌿 Branching Strategy

* Always branch off the **latest `main`**.
* **Branch name formats:**

  * `feature/<your-name>-<short-desc>` → e.g. `feature/ajay-add-feature-extraction`
  * `fix/<issue-number>-<short-desc>` → e.g. `fix/12-fix-tokenizer-bug`
  * `chore/<short-desc>` → e.g. `chore/update-deps`
  * `experiment/<short-desc>` → for exploratory work (review before merge)

---

## 💻 Common Git Commands

### Keep your local main updated:

```bash
git checkout main
git pull origin main
```

### Create a branch:

```bash
git checkout -b feature/<your-name>-<short-desc>
```

### Stage & commit:

```bash
git add <files>
git commit -m "type(scope): short summary

Longer description if needed (wrap at ~72 chars)."
```

### Push your branch:

```bash
git push origin feature/<your-name>-<short-desc>
```

---

## 🧾 Commit Message Conventions

| Prefix      | Purpose                           |
| :---------- | :-------------------------------- |
| `feat:`     | New feature                       |
| `fix:`      | Bug fix                           |
| `docs:`     | Documentation only changes        |
| `style:`    | Formatting, no code change        |
| `refactor:` | Code restructure, no new features |
| `test:`     | Adding or fixing tests            |
| `chore:`    | Maintenance tasks                 |

**Examples:**

* `feat(model): add TF-IDF feature extraction`
* `fix(preprocessing): handle empty text inputs`

---

## 🔄 Pull Request (PR) Process

* Open a **PR against `main`** with:

  * ✅ Clear title and purpose
  * 🧠 What changed and why
  * 🧩 How to test locally
* Link related issue(s): `Closes #<issue-number>`
* Assign reviewers and wait for **at least one approval**
* Merge only when **CI passes** (preferably green ✅)

---

## 🧮 PR Checklist

* [ ] PR description explains **why** and **what**
* [ ] Builds locally & tests pass
* [ ] Includes/updates tests
* [ ] No sensitive data (datasets, keys, credentials)
* [ ] Code is readable & documented
* [ ] Dependencies are justified
* [ ] Lint/style checks passed

---

## 🧠 Testing & CI

* Add **unit tests** for core logic.
* Keep **notebooks reproducible** — no large raw data commits.
* **CI must pass** before merging.

---

## 📂 Data Handling

* `data/` is **git-ignored** — never commit raw data or credentials.
* Include **download/preprocess scripts** in `scripts/` or `docs/`.
* Use **sample/synthetic data** for tests and CI.

---

## 🚢 Releases & `main`

* `main` should **always be deployable**.
* After merge, CI must confirm no regressions.
* Tag releases or maintain a **CHANGELOG**.

---

## 🧯 Reverting & Emergency Fixes

* For urgent fixes → small, focused `fix/...` branch + PR.
* If regression occurs → revert the PR or create a hotfix branch.

---

## 💬 Communication

* Mention reviewers in PRs and be responsive.
* Discuss large or uncertain changes in **Issues** or **draft PRs**.
* Use **GitHub Issues** to track bugs, ideas, and progress.

---

## 🧰 Useful Commands (Quick Reference)

```bash
git checkout main && git pull origin main   # update local main
git checkout -b feature/yourname-shortdesc  # create branch
git push -u origin feature/yourname-shortdesc  # push branch
git fetch origin && git rebase origin/main  # optional rebase
```

---

## 🧑‍💻 Contacts / Reviewers

**Maintainer:** [@ajayram231210006](https://github.com/ajayram231210006)
Other reviewers can be added in PRs.

---

## 📝 Example PR Template

**Title:** `feat(<area>): short summary`

**Description:**

* **Summary:** What changed and why
* **How to test:**

  * Steps to reproduce locally
* **Related issues:** `Closes #X`

**Notes:**

* Add context, screenshots, or details if needed.

---

## 🌟 Final Notes

* Prefer **small, focused PRs** for faster review.
* Unsure about design? → open a **draft PR** or **issue** first.
* Thanks for contributing 🙌 — let’s keep the repo clean, reproducible & collaborative.

---

