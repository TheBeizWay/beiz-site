"""Oversight page for beiz.com.au: human in the loop and organisation in the loop.
No statistics or client claims here. Add nothing that is not true."""
from layout import page, phero, cta_band, related


def oversight_pages():
    hero = phero(
        "Oversight",
        "People approve. The organisation owns.",
        "A person clicking approve is not the same as someone being accountable. Beiz builds both layers: a human checkpoint on each risky action, and an organisation that owns the workflow, reviews the pattern and can show its working to a board or an auditor.",
        [("/oversight/", "Oversight")],
        [("/contact/?topic=Controlled%20AI%20workflows#form", "Plan my controls"), ("/ai-check/", "Free Privacy Act check")],
    )

    layers = '''<section><div class="wrap">
  <p class="eyebrow">Two layers</p>
  <h2>Human in the loop, and organisation in the loop</h2>
  <div class="cards two">
    <div class="card"><span class="k">Layer 1 · Human in the loop</span><h3>Who approves this action?</h3><p>Each agent has a job description and limits. Routine, reversible work can run; anything that touches money, customers or decisions about people stops and asks a named person. Every approval, hold and block is logged.</p></div>
    <div class="card"><span class="k">Layer 2 · Organisation in the loop</span><h3>Who owns the workflow?</h3><p>Every AI tool has a named owner. Someone reviews approvals and overrides on a schedule, escalation paths are written down, and the decision log is kept so the organisation can answer “what did the AI do last Tuesday, and who checked it?”.</p></div>
  </div>
  <p class="fine">A human approval step only counts if the reviewer understands the action, has time to look, and can say no without penalty. That is a design question for the organisation, not just a button.</p>
</div></section>'''

    tiers = '''<section class="band"><div class="wrap">
  <p class="eyebrow">Risk tiers</p>
  <h2>Match the checkpoint to the risk</h2>
  <p class="lede">Too few checkpoints is unsafe. Too many and people stop using the tool. The sprint sets a tier for every AI tool and workflow.</p>
  <div class="tablewrap"><table class="pt">
    <thead><tr><th>Tier</th><th>Example</th><th>Default control</th></tr></thead>
    <tbody>
      <tr><td>Read-only</td><td>Summarising a report or flagging an odd invoice</td><td>Allow; sample-check monthly</td></tr>
      <tr><td>Drafts</td><td>Draft email, draft journal, draft reply</td><td>Allow; a person sends or posts</td></tr>
      <tr><td>Writes internally</td><td>Coding a transaction, updating a record</td><td>Batch review by a named reviewer</td></tr>
      <tr><td>External or financial</td><td>Paying a bill, sending to a customer, changing bank details</td><td>Hold; one-by-one approval with a dollar threshold</td></tr>
      <tr><td>Decisions about people</td><td>Hiring, pay, credit or eligibility</td><td>Block for AI alone; person decides and records why</td></tr>
    </tbody>
  </table></div>
</div></section>'''

    packet = '''<section><div class="wrap">
  <p class="eyebrow">The decision record</p>
  <h2>What a good approval record contains</h2>
  <ul class="ticks">
    <li><b>Action:</b> what the agent proposes to do.</li>
    <li><b>Reason and evidence:</b> why, with the source records.</li>
    <li><b>Exposure:</b> the dollar amount or people affected.</li>
    <li><b>Alternatives:</b> what else was considered, and what happens if nobody acts.</li>
    <li><b>Approver and time:</b> a named person, not “the team”.</li>
    <li><b>Outcome and any later change:</b> if the plan changes after approval, it is approved again.</li>
  </ul>
  <p class="muted" style="margin-top:14px">A chat transcript is not an audit record. This is.</p>
</div></section>'''

    rhythm = '''<section class="band"><div class="wrap">
  <p class="eyebrow">Keeping it honest</p>
  <h2>The monthly review</h2>
  <p class="lede">The organisation layer is a habit, not a document. In monthly controls operations, the decision log is reviewed for approval patterns, overrides, holds that were waved through, and tools that appeared since last time. Findings go to the named owner, and anything the board should see goes in a short note.</p>
  <p class="fine">Australian AI guidance recommends practices like these, including registers, accountability and human oversight, but it is voluntary. The Privacy Act automated-decision rules starting 10 December 2026 apply only to organisations the Act covers. Legal wording stays with your lawyer.</p>
</div></section>'''

    rel = '<section><div class="wrap"><p class="eyebrow">Keep exploring</p>' + related([("/services/human-in-the-loop/", "Offshore & AI oversight"), ("/services/ai-governance/", "AI governance"), ("/services/privacy-sprint/", "Privacy Act module"), ("/trust/", "Why trust Beiz"), ("/try/", "Try the demos")]) + "</div></section>"

    body = hero + layers + tiers + packet + rhythm + rel + cta_band("Not sure which tier your AI tools sit in?", "Book a free 20-minute call. We will walk through the tools your team already uses and where a person needs to be in the loop.")
    return {"/oversight/": page("/oversight/", "Human and organisation in the loop", "People approve, the organisation owns: risk tiers, named owners, approval records and a monthly review for the AI your team already uses.", body)}
