# Investment Research — Tanmay Gambhir

I'm a Chartered Accountant (four years, PwC) starting the Bocconi × ESSEC Master in Management.
This portfolio is me doing the actual work — venture memos, full DCF and LBO models rebuilt from
scratch, and an adversarial red-team pass on my own conclusions — instead of just reading about
deals. Everything is researched and cited from public sources.

**Live site:** https://tanmaygambhir37-design.github.io/investment-research/

**New session? Start with the playbooks — read the relevant one before writing anything new:**
- [`MEMO_PLAYBOOK.md`](MEMO_PLAYBOOK.md) — for writing-led pieces (like the Dust memo): structure,
  sourcing, data integrity, and voice, extracted from real corrections.
- [`MODEL_PLAYBOOK.md`](MODEL_PLAYBOOK.md) — for pieces that need a valuation (a DCF or LBO built as a
  live Excel workbook, like Technogym and Recordati). The method, the modeling rules, how to adapt the
  kit to a **new company**, and how to ship the finished analysis to the site. Reference architectures,
  reconstruction scripts and verification live in [`model-kit/`](model-kit/).

## Coverage

| Piece | Type | Links |
|---|---|---|
| Dust (dust.tt) | VC memo — Series B follow-on review | [Memo](https://tanmaygambhir37-design.github.io/investment-research/dust/) |
| Technogym | DCF valuation | [Analysis](https://tanmaygambhir37-design.github.io/investment-research/technogym/) |
| Recordati | LBO model | [Analysis](https://tanmaygambhir37-design.github.io/investment-research/recordati/) |
| AI Semiconductor Supply Chain | Industry map (working draft) | [`industry/ai-semiconductor-supply-chain`](industry/ai-semiconductor-supply-chain) |
| Red-Team | Adversarial review of the above, per piece | [Index](https://tanmaygambhir37-design.github.io/investment-research/red-team/) |

## Process

Idea → Research → Hypothesis → Model → Memo → Red-Team → Decision. Every piece is expected to
carry a 30-second summary, a full write-up, a downloadable model (where applicable), and a
red-team page attacking its own assumptions. See `MEMO_PLAYBOOK.md` for the full rule set behind
each stage.

## Methodology

- **Public sources only.** Filings, offer documents, press coverage, earnings calls, review
  platforms, customer case studies. Every claim traces to a citation.
- **Confidence tiers.** Each figure is graded High / Medium / Low / Not Disclosed. Company-reported
  numbers are treated as directionally credible, never as audited fact.
- **No invented numbers.** Undisclosed metrics are shown as "Not Disclosed" and framed as risks,
  not estimated into existence.
- **Base rates over stories**, with explicit, falsifiable "what would change my mind" triggers.

## Site docs

- `MEMO_PLAYBOOK.md` — how to write the next memo without repeating past mistakes.
- `SITE_AUDIT.md` — last full audit of the site's structure and copy.
- `IMPLEMENTATION_PLAN.md` — open backlog, in priority order.

## Disclaimer

Independent research; not affiliated with, or endorsed by, any company or deal covered. Not
investment advice.
