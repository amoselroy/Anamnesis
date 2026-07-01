# WORLD PATTERN 2026-06-10 — Windows persistent environment variables override dot

*ID: passage-1d1c33f6-c8bb-4e25-9196-bebce0d13bf1*
*Created: 2026-06-10*

---

WORLD PATTERN 2026-06-10 — Windows persistent environment variables override dotenv loading — 2026-06-10

PRINCIPLE: On Windows, user-level environment variables persist across system restarts and are not overridden by `load_dotenv()` unless explicitly cleared, potentially causing local scripts to use stale credentials.

NARRATIVE: After an overnight system restart, Braindexer's condition detection diagnostics returned empty results despite the schema existing. Investigation revealed the local environment was connecting to an empty test database rather than the live production database. The `.env` file contained correct credentials, but `load_dotenv()` was not overriding existing environment variables. Windows has stored user-level env vars that survive restarts; `load_dotenv()` only loads from `.env` if the variable is not already set in the environment. The solution required explicitly clearing the persistent Windows env vars using `[System.Environment]::SetEnvironmentVariable()` with `$null`, then restarting PowerShell to allow the session to pick up the `.env` values. This differs from Unix-like systems where environment variables are typically session-scoped and don't persist after logout/restart. Development teams rotating credentials or using multiple environments should be aware that Windows environment variable clearing is not automatic on system restart.
