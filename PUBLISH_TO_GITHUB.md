# How to Publish This Project on GitHub — Beginner Step-by-Step

This guide walks you from the downloaded project folder to a polished, public GitHub repository that you can show in interviews — plus how to link it from your GitHub profile.

> **Important first concept.** Your repo `suryakulshreshtha/SuryaKulshreshtha` is a *special* repo: because its name matches your username, its `README.md` is what shows on your GitHub **profile homepage**. **Do not** put this test framework inside that repo — it would clutter your profile. Instead you'll create a **brand-new repository** for the project, and then add a small link to it from your profile README. That's exactly what the steps below do.

---

## Part A — One-time setup (skip what you already have)

You already have Git and a GitHub account (your profile lists Git/GitHub), so you can likely jump to Part B. If you're on a fresh machine:

1. **Install Git** → https://git-scm.com/downloads
2. **Tell Git who you are** (run once per machine):
   ```bash
   git config --global user.name "Surya Kulshreshtha"
   git config --global user.email "your-github-email@example.com"
   ```
3. **Set up authentication.** GitHub no longer accepts your password on the command line. Easiest options:
   - **GitHub CLI** (recommended): install from https://cli.github.com, then run `gh auth login` and follow the prompts. This handles auth automatically.
   - **Or a Personal Access Token (PAT):** GitHub → *Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token*, tick the `repo` scope, copy the token, and paste it as the "password" when Git asks during your first push.

---

## Part B — Create the new repository on GitHub

You can do this in the browser (simplest for beginners) **or** with the GitHub CLI.

### Option 1 — In the browser
1. Go to https://github.com/new
2. **Repository name:** `ForkablePythonProjectShowcase`
3. **Description:** `End-to-end test automation framework: Playwright + Python + Pytest (UI, API, network mocking, POM, CI).`
4. **Visibility:** **Public** (so interviewers can see it).
5. **Do NOT** tick "Add a README", ".gitignore", or "license" — the project folder already has these, and adding them now causes a conflict on your first push.
6. Click **Create repository**. Leave that page open — you'll need the URL it shows.

### Option 2 — With GitHub CLI (one command)
```bash
gh repo create ForkablePythonProjectShowcase --public \
  --description "Playwright + Python + Pytest automation framework"
```

---

## Part C — Put the project under Git and push it

1. **Open a terminal in the project folder.** Unzip the project first if needed, then:
   ```bash
   cd path/to/ForkablePythonProjectShowcase
   ```
   (On Windows that might be `cd C:\Users\Surya\Downloads\ForkablePythonProjectShowcase`.)

2. **Initialise a Git repository** (turns the folder into a tracked repo):
   ```bash
   git init
   ```

3. **Set the default branch name to `main`** (GitHub's default; keeps things tidy):
   ```bash
   git branch -M main
   ```

4. **Stage every file** for the first commit:
   ```bash
   git add .
   ```
   > The included `.gitignore` automatically keeps junk out (`.venv/`, caches, reports, `auth.json`). Verify with `git status` — you should see your source files staged but **not** `.venv` or `reports`.

5. **Make your first commit** (a snapshot with a message):
   ```bash
   git commit -m "Initial commit: Playwright Python Pytest framework"
   ```

6. **Connect your local folder to the GitHub repo.** Copy the URL from Part B and run:
   ```bash
   git remote add origin https://github.com/suryakulshreshtha/ForkablePythonProjectShowcase.git
   ```

7. **Push your code up:**
   ```bash
   git push -u origin main
   ```
   If asked for a username/password, enter your GitHub username and your **PAT** as the password (not your account password). With GitHub CLI auth, it just works.

8. **Refresh the GitHub page** — your code and README are now live. 🎉

---

## Part D — Make the repo look professional (5-minute polish)

These small touches matter a lot to interviewers:

1. **Add topics/tags.** On the repo page, click the ⚙️ next to "About" and add: `playwright`, `python`, `pytest`, `test-automation`, `qa`, `api-testing`, `pom`, `ci-cd`.
2. **Confirm the About blurb** and (optionally) add your portfolio link `www.suryakulshreshtha.in`.
3. **Watch CI run.** Open the **Actions** tab — the included GitHub Actions workflow runs your whole suite on every push and uploads an HTML report. A green check on your repo is a strong signal.
   - First run note: if the badge in the README stays grey, edit the workflow badge URL or just let the Actions tab speak for itself.
4. **(Optional) Add a license.** GitHub → *Add file → Create new file → `LICENSE`* → choose MIT. Makes the repo clearly reusable.

---

## Part E — Link it from your GitHub profile

This is how recruiters who land on your profile discover the project. Edit the README in your **profile repo** (`suryakulshreshtha/SuryaKulshreshtha`) and add a "Projects" section. You can do it right in the browser: open the repo → click `README.md` → the ✏️ pencil → paste → commit.

Suggested snippet (drop it under your "Current Endeavour" area):

```markdown
### 🧪 Featured Project

**[Playwright Python Pytest Framework](https://github.com/suryakulshreshtha/ForkablePythonProjectShowcase)**
End-to-end test automation framework — UI + API testing, network mocking, Page Object Model, data-driven tests, Docker, and GitHub Actions CI. Built with Playwright, Python, and Pytest.
```

---

## Part F — Everyday Git commands (for when you keep improving it)

After the first push, your routine for any change is just three commands:

```bash
git add .
git commit -m "Add visual testing example"
git push
```

Tips that read well in interviews:
- **Commit in small, meaningful steps** with clear messages (e.g. `"Add API utils and booking tests"`), not one giant `"stuff"` commit.
- Consider a few separate commits that tell a story: *setup → POM → login tests → API tests → network mocking → CI*. It shows how you work.

---

## Quick sanity checklist before you share the link

- [ ] Repo is **Public**
- [ ] README renders nicely on the repo homepage
- [ ] `.venv/` and `reports/` are **not** in the repo (they're git-ignored)
- [ ] No real passwords/tokens committed (only public demo creds)
- [ ] **Actions** tab shows the workflow (green ideally)
- [ ] Topics/tags added
- [ ] Linked from your profile README

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `fatal: remote origin already exists` | `git remote remove origin` then re-add it |
| Push rejected / auth fails | Use a **PAT** as the password, or `gh auth login` |
| `.venv` got committed by mistake | `git rm -r --cached .venv` then commit again |
| First push rejected ("updates were rejected") | You added a README on GitHub — run `git pull --rebase origin main` then push |
| Wrong branch name | `git branch -M main` then `git push -u origin main` |
