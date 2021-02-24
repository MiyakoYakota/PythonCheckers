# DoorDash Checker

Checks ``email:password`` combos against [https://api.doordash.com/v2/auth/web_login/](https://api.doordash.com/v2/auth/web_login/). 

----

## Requirements

Proxies Required: :ballot_box_with_check:

Proxies Supported: SOCKS5, SOCKS5 Authenticated

## Getting Started

- Install [Python](https://www.python.org/downloads/) (add to path while installing).
- Place your proxies into the same folder as the checker in ``proxies.txt``
- Place your combos into the same folder as the checker in ``combo.txt``
- Open your checker folder in PowerShell/CMD (``Shift+Right-Click`` ->`` Open in PowerShell/CMD``)
- Start the checker: ``python .\checker.py``

## Output:

Accounts are outputted into the following format:

```
{username}:{password} | Name: {first_name} {last_name} | Phone Number: {phone_number} | Default Address: {printable_address} | Default Card: {default_card_type}*{default_card_last4} Expires {default_card_exp_month}/{default_card_exp_year} | Alcohol Allowed: {True | False}
```

