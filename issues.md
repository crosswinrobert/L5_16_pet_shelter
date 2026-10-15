\# Lab 5: Static Code Analysis — Issue Report



| Issue | Type | Original Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| SQL injection risk | Security | 10 | SQL values were inserted using string formatting. | Used parameterized SQLite queries. |

| Mutable default argument | Bug | 9 | The default list could be shared across calls. | Changed the default to `None` and initialized a new list. |

| Insecure pseudorandom generator | Security | 22 | `random.randint()` was unsuitable for security-sensitive randomness. | Used `secrets.randbelow()`. |

| Bare exception | Error handling | 29 | A bare exception could hide unexpected errors. | Removed the unnecessary handler and handled empty results explicitly. |

| Broad exception and silent failure | Error handling | 34–37 | Exceptions were caught and ignored. | Removed the unnecessary handler. |

| Missing docstrings | Code quality | Multiple | The module and functions lacked documentation. | Added descriptive docstrings. |

| Inconsistent function naming | Code quality | Multiple | Function names used camelCase. | Converted names to snake\_case. |

| Long lines | Formatting | 5, 10, 27 | Lines exceeded style limits. | Split statements across multiple lines. |

| Multiple statements on one line | Formatting | 41 | Conditional statements shared a line. | Used multiline conditional logic. |

| Global state | Code quality | 6, 16 | A global counter required a `global` statement. | Derived shelter status from the database. |



\## Verification Results



\- Initial Pylint score: 3.95/10.

\- Final Pylint score: 10.00/10.

\- Final Bandit result: No issues identified.

\- Final Flake8 result: No errors reported.

\- Program execution: Successful.



\## Conclusion



The static analysis tools identified security, error-handling, maintainability, and formatting issues. After fixing them, the program executed successfully and passed all three static analysis tools.

