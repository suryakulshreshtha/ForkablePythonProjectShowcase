# 🎭 Playwright Python Pytest Framework

> An end-to-end test automation framework built with **Playwright + Python + Pytest**, applying the concepts from the *Playwright Python Automation Testing* course. UI automation, API testing, network mocking, the Page Object Model, data-driven tests, Docker, and CI — all in one runnable project.

![Playwright](https://img.shields.io/badge/Playwright-1.56-2EAD33?logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0-0A9EDC?logo=pytest&logoColor=white)
[![CI](https://github.com/suryakulshreshtha/ForkablePythonProjectShowcase/actions/workflows/tests.yml/badge.svg)](https://github.com/suryakulshreshtha/ForkablePythonProjectShowcase/actions/workflows/tests.yml)

---

## What this project demonstrates

| Skill | Where to look | Course concept |
|---|---|---|
| **Page Object Model** | `pages/` | Centralised locators + actions; fluent page returns |
| **Semantic locators** | `pages/login_page.py` | `get_by_role`, `get_by_placeholder` before CSS |
| **Web-first assertions** | every test | `expect()` with auto-retry |
| **Parametrized / data-driven** | `tests/test_login.py`, `data/credentials.json` | one test, many data sets, external JSON |
| **Fixtures & scopes** | `conftest.py` | session-scoped data, page-flow fixtures, `yield` teardown |
| **Dynamic UI handling** | `tests/test_inventory.py` | locator `filter()`, dropdowns, list assertions |
| **API testing** | `tests/test_api.py`, `utils/api_utils.py` | `APIRequestContext`, token auth, reusable utils |
| **Network mocking** | `tests/test_network_mock.py` | `route.fulfill` (mock) and `route.abort` (block) |
| **Async API (bonus)** | `examples/async_example.py` | the async style, shown alongside the sync suite |
| **CI/CD** | `.github/workflows/tests.yml` | GitHub Actions + trace/screenshot artifacts |
| **Containerisation** | `Dockerfile` | official Playwright image for consistent runs |

**Applications under test (public demo sites, no signup):**
- UI → [saucedemo.com](https://www.saucedemo.com)
- API → [restful-booker](https://restful-booker.herokuapp.com)

---

## Project structure

```
ForkablePythonProjectShowcase/
├── pages/                  # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                  # Test suites
│   ├── test_login.py       # POM + parametrization + expect()
│   ├── test_inventory.py   # filtering, sorting, cart assertions
│   ├── test_api.py         # REST API testing
│   └── test_network_mock.py# route fulfill / abort
├── utils/
│   ├── api_utils.py        # reusable API layer
│   └── config.py           # env-driven config
├── data/
│   └── credentials.json    # external test data
├── examples/
│   └── async_example.py    # standalone async-API demo
├── .github/workflows/
│   └── tests.yml           # CI pipeline
├── conftest.py             # shared fixtures
├── pytest.ini              # config + markers
├── requirements.txt
└── Dockerfile
```

---

## Getting started

### 1. Clone and enter the project
```bash
git clone https://github.com/<your-username>/ForkablePythonProjectShowcase.git
cd ForkablePythonProjectShowcase
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### 3. Install dependencies + browsers
```bash
pip install -r requirements.txt
playwright install               # downloads Chromium/Firefox/WebKit
```

### 4. Run the tests
```bash
pytest                           # all tests, headless
pytest --headed                  # watch the browser
pytest --browser firefox         # pick an engine
pytest -m smoke                  # only smoke-tagged tests
pytest -m api                    # only API tests
pytest -n auto                   # parallel (pytest-xdist)
python examples/async_example.py # run the async demo script
```

An HTML report is written to `reports/report.html` after each run.

### 5. Debug a failure
```bash
PWDEBUG=1 pytest tests/test_login.py     # step through with Inspector
pytest --tracing retain-on-failure       # capture a trace on failure
playwright show-trace test-results/.../trace.zip
```

---

## Run in Docker
```bash
docker build -t pw-framework .
docker run --rm pw-framework
```

---

## Design notes

- **Sync API by default.** `pytest-playwright` ships sync fixtures (`page`, `context`, `browser`), which keep the suite simple and avoid event-loop conflicts with `pytest-asyncio`. The async API is demonstrated separately in `examples/async_example.py` so both styles are covered.
- **Assertions live in tests**, not in page objects. Page objects model *behaviour*; tests own *verification*.
- **No hard-coded data.** Credentials come from `data/credentials.json`; URLs from environment variables (`utils/config.py`) so the same suite runs against any environment.
- **Secrets never committed.** Only public demo credentials are stored; real secrets would be injected via env vars / CI secrets (`.gitignore` already excludes `auth.json`).

---

## Built while learning

This framework was built to consolidate and showcase the skills from the *Playwright Python Automation Testing* course — turning the syllabus (Python basics → Pytest → Playwright UI → API → network mocking → framework design → CI) into a working, runnable portfolio project.
