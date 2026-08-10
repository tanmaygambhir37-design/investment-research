# Morning email digest

Sends you one plain-text email each morning summarizing the last 24 hours of
your inbox. Runs on GitHub Actions, so there is no server and no app.

- `morning_digest.py` — reads Gmail, summarizes, sends the digest
- `get_gmail_token.py` — one-time helper to mint the OAuth refresh token
- `../.github/workflows/morning-digest.yml` — the daily schedule

The digest arrives at roughly 07:00 IST. Scheduled jobs on GitHub's shared
runners are frequently delayed by 5–20 minutes; that is normal and not a
failure.

## Setup

Roughly 20–30 minutes, almost all of it in the Google Cloud console. You only
do this once.

### 1. Create a Google Cloud project and enable the Gmail API

1. Go to <https://console.cloud.google.com/projectcreate> and create a
   project. Any name works.
2. With that project selected, open
   <https://console.cloud.google.com/apis/library/gmail.googleapis.com> and
   click **Enable**.

### 2. Configure the consent screen

1. Go to **APIs & Services → OAuth consent screen**.
2. Choose **External**, then fill in the app name and your own email where
   required.
3. On the **Test users** step, add your own Gmail address.
4. Finish the wizard.

> **Publish the app before you finish.** While the consent screen is in
> *Testing* mode, Google expires refresh tokens after 7 days and your digest
> will silently stop after a week. On the consent screen, click
> **Publish app**. You will see an "unverified app" warning when you
> authorize — that is expected for a personal script and safe to accept for
> your own account. Verification is only required for apps that other people
> use.

### 3. Create OAuth credentials

1. **APIs & Services → Credentials → Create credentials → OAuth client ID**.
2. Application type: **Desktop app**.
3. Copy the **client ID** and **client secret**.

### 4. Mint a refresh token

On your own machine, not in CI:

```bash
pip install requests
python scripts/get_gmail_token.py
```

Paste the client id and secret when prompted. A browser opens, you grant
access to your own mailbox, and the script prints three values.

The scopes requested are `gmail.readonly` and `gmail.send` — enough to read
your mail and send you the digest, and nothing else. No delete, no modify.

### 5. Get an OpenRouter key

Sign up at <https://openrouter.ai>, then create a key under **Keys**. The
free model tier costs nothing; the digest is one call a day.

### 6. Add the secrets to this repo

**Settings → Secrets and variables → Actions → New repository secret**:

| Secret | Value |
| --- | --- |
| `GMAIL_CLIENT_ID` | from step 3 |
| `GMAIL_CLIENT_SECRET` | from step 3 |
| `GMAIL_REFRESH_TOKEN` | from step 4 |
| `OPENROUTER_API_KEY` | from step 5 |

Optionally add a **variable** (not a secret) named `OPENROUTER_MODEL` to pin
a specific model slug. Left unset, the script tries several free models in
order until one answers.

### 7. Test it

**Actions → Morning email digest → Run workflow.** Check your inbox. The run
log shows how many messages were found and which model wrote the summary,
and never prints the mail itself.

## Tuning

Edit the workflow's `cron` to change the time — it is in UTC, so subtract
5:30 for IST. Edit `DIGEST_TIMEZONE` if you move.

What goes in which section is decided by `PROMPT` in `morning_digest.py`. If
the digest is giving you too much of something, change the wording there
rather than the code.

## If it stops arriving

The script is written so a broken model still produces an email — you get a
mechanically grouped list instead of a summary. So silence almost always
means Gmail auth, not the model.

- **Nothing arrives at all.** Check **Actions** for a failed run. A 400 on
  the token refresh means the refresh token died: re-run
  `get_gmail_token.py` and update the secret. The usual cause is the consent
  screen still being in Testing mode (see step 2).
- **The digest arrives but says the model was unavailable.** The free tier
  was rate-limited or the model slug was retired. Set the
  `OPENROUTER_MODEL` variable to a slug that currently exists on
  <https://openrouter.ai/models?max_price=0>.
- **GitHub disables the schedule.** Actions pauses cron on repos with no
  activity for 60 days. A push re-enables it.

## Cost and privacy

Free: GitHub Actions is free for public repos and this uses a couple of
minutes a day, and the OpenRouter free tier is one call daily.

Your email metadata — sender, subject, and Gmail's short preview snippet —
is sent to OpenRouter for summarizing. Full message bodies are never read or
transmitted. If that is more than you want to share with a third party,
remove `OPENROUTER_API_KEY` from the secrets: the script then sends the
mechanically grouped list, which never leaves Google and GitHub.
