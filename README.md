# hr_law_compliance
# KSA Leave Rules

Custom Frappe app to implement Saudi Arabia sick leave rules (120 days):
- 30 days full pay
- 60 days 75% pay
- 30 days unpaid

## Features
- Automatic sick leave splitting
- Rolling 12-month calculation
- Payroll compatible
- Upgrade safe

## Installation

```bash
bench get-app https://github.com/your-org/ksa_leave_rules.git
bench --site yoursite install-app ksa_leave_rules
bench migrate
