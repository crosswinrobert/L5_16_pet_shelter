\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, poor coding practices, and formatting problems early in development. It improves code quality, readability, maintainability, and security.



\## 2. What are the differences between Pylint, Bandit, and Flake8?



Pylint checks overall code quality, naming conventions, documentation, and potential programming errors. Bandit focuses on common security vulnerabilities and insecure coding patterns. Flake8 checks Python style and formatting issues, including line length, whitespace, and certain programming mistakes.



\## 3. What issues were found and how were they fixed?



The original program contained unsafe SQL string construction, a mutable default argument, an insecure pseudorandom generator for adoption codes, overly broad exception handling, missing docstrings, inconsistent naming, and formatting violations. Parameterized SQL queries, a `None` default, the `secrets` module, clearer exception handling, documentation, consistent naming, and proper formatting were used to address these issues.



\## 4. How does static analysis contribute to software quality and maintainability?



Static analysis provides automated feedback before code is deployed. It helps developers detect issues consistently, reduce security risks, enforce coding standards, and make programs easier to understand and maintain. Using multiple tools provides broader coverage than relying on a single tool.



