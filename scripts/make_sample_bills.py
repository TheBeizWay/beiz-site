"""Builds data/sample-bills.csv: six months of bills for a made-up building company,
with eight planted problems for the bill check demo. Deterministic (fixed seed)."""
import csv, random, datetime as dt
from pathlib import Path
random.seed(20261016)
START, END = dt.date(2026, 4, 1), dt.date(2026, 9, 30)
LIMIT = 5000
SUP = {  # name: (prefix, bills per month, low, high, terms, bank)
    "Wattlebird Electrical": ("WE-", 2, 900, 4400, 14, "633-012 1048 2271"),
    "Numbat Concrete": ("NC-", 1, 6200, 13800, 30, "082-145 6610 0937"),
    "Bluetongue Plumbing": ("BT", 2, 420, 2800, 14, "062-208 1033 4580"),
    "Lyrebird Hardware": ("LH", 3, 120, 1900, 30, "484-799 2219 0063"),
    "Possum Paint Supplies": ("PP-", 1, 600, 2400, 30, "014-288 7745 3310"),
    "Echidna Tiles": ("ET", 1, 1500, 4300, 30, "112-879 4401 2876"),
    "Magpie Waste Removal": ("MW", 1, 880, 880, 14, "733-150 9012 4471"),
    "Gecko Fleet Fuel": ("GF", 4, 180, 650, 14, "063-001 2280 1196"),
    "Platypus Glass": ("PG-", 0.5, 700, 3600, 30, "082-401 3365 7712"),
}
def wkday(d):
    while d.weekday() >= 5: d += dt.timedelta(days=1)
    return d
def money(x): return f"{x:.2f}"
rows, seq = [], {}
for name, (pre, per, lo, hi, terms, bank) in SUP.items():
    seq[name] = random.randint(1000, 2100)
    d = START
    while d <= END:
        d += dt.timedelta(days=max(3, int(random.gauss(30 / per, 3))))
        if d > END: break
        amt = lo if lo == hi else round(random.uniform(lo, hi), 2)
        if 4750 <= amt < LIMIT: amt = round(amt - 400, 2)
        seq[name] += 1
        inv = wkday(d)
        due = inv + dt.timedelta(days=terms)
        paid = wkday(due + dt.timedelta(days=random.randint(-3, 4)))
        rows.append(dict(ContactName=name, InvoiceNumber=f"{pre}{seq[name]}", InvoiceDate=inv, DueDate=due, Total=amt, PaidDate=paid, BankAccount=bank))
def add(name, num, inv, amt, paid=None, bank=None, terms=30):
    inv = dt.date(*inv); due = inv + dt.timedelta(days=terms)
    rows.append(dict(ContactName=name, InvoiceNumber=num, InvoiceDate=inv, DueDate=due, Total=amt,
                     PaidDate=paid or wkday(due), BankAccount=bank or SUP.get(name, ("", 0, 0, 0, 0, "036-110 5521 8090"))[5]))
# 1 possible duplicate: same supplier and amount, a week apart, invoice number tweaked
add("Wattlebird Electrical", "INV-2207", (2026, 8, 12), 3960.00, terms=14)
add("Wattlebird Electrical", "INV-2207A", (2026, 8, 19), 3960.00, terms=14)
# 2 same invoice number twice, second one with a decimal slip
add("Numbat Concrete", "NC-1180", (2026, 6, 3), 12480.00)
add("Numbat Concrete", "NC-1180", (2026, 7, 6), 1248.00)
# 3 bank details change on the last two Bluetongue bills
for r in [r for r in rows if r["ContactName"] == "Bluetongue Plumbing" and r["InvoiceDate"] >= dt.date(2026, 8, 20)][:2]:
    r["BankAccount"] = "082-991 5530 1192"
# 4 two payments made on a weekend
weekday_paid = [r for r in rows if r["ContactName"] in ("Lyrebird Hardware", "Echidna Tiles")]
weekday_paid[4]["PaidDate"] = dt.date(2026, 6, 13)   # Saturday
weekday_paid[-2]["PaidDate"] = dt.date(2026, 9, 6)   # Sunday
# 5 just under the approval limit
add("Lyrebird Hardware", "LH-3391", (2026, 7, 21), 4980.00)
# 6 split bills: same supplier, same day, each under the limit, together over it
add("Possum Paint Supplies", "PP-7702", (2026, 9, 9), 4600.00)
add("Possum Paint Supplies", "PP-7703", (2026, 9, 9), 3900.00)
# 7 new supplier whose first bill is large
add("Kookaburra Labour Hire", "KLH-0001", (2026, 9, 15), 18400.00, bank="036-110 5521 8090", terms=7)
rows.sort(key=lambda r: (r["InvoiceDate"], r["ContactName"]))
out = Path(__file__).resolve().parent.parent / "data" / "sample-bills.csv"
with out.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ContactName", "InvoiceNumber", "InvoiceDate", "DueDate", "Total", "PaidDate", "BankAccount"])
    for r in rows:
        w.writerow([r["ContactName"], r["InvoiceNumber"], r["InvoiceDate"].strftime("%d/%m/%Y"), r["DueDate"].strftime("%d/%m/%Y"),
                    money(r["Total"]), r["PaidDate"].strftime("%d/%m/%Y"), r["BankAccount"]])
print(len(rows), "bills,", money(sum(r["Total"] for r in rows)))
