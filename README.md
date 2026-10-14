# Super30 — Python Loops & Functions Assignment

**Student:** Kaushilendra Kumar Singh (Kaushal Singh)  
**Batch:** Super30, September 2026 — Pod 2  
**Assignment:** Python Loops & Functions (20 questions, 25 marks)  
**Original due date:** 5 October 2026, 8:20 PM

## Overview
Twenty standalone beginner-friendly Python 3 programs covering `for` loops, nested loops, `while` loops, conditional logic, functions, lists, dictionaries, and interactive menus. Each file has a module description and comments. No third-party packages required.

## Setup and run
1. Install Python 3.9 or newer.
2. Clone the repository: `git clone <YOUR_REPOSITORY_URL>` and `cd super30-python-loops-functions-assignment`.
3. Run any question, for example: `python 01_number_analyzer.py`.
4. Follow the prompts in the terminal. For menu-driven programs, choose the Exit option to finish.
5. Run automated tests: `python -m unittest discover -s tests -v`.

On some systems use `python3` instead of `python`.

## Completed questions
| # | File | Main concept |
|---|---|---|
| 01 | `01_number_analyzer.py` | for loop, parity counters |
| 02 | `02_multiplication_table.py` | range and configurable end |
| 03 | `03_sum_average.py` | manual accumulation |
| 04 | `04_max_min.py` | comparison tracking |
| 05 | `05_character_frequency.py` | dictionary frequency |
| 06 | `06_text_counter.py` | character classification |
| 07 | `07_prime_finder.py` | nested loops, primality |
| 08 | `08_pattern_generator.py` | nested pattern loops |
| 09 | `09_student_marks.py` | aggregate student marks |
| 10 | `10_atm_simulator.py` | while loop, ATM menu |
| 11 | `11_password_retry.py` | limited retries |
| 12 | `12_guessing_game.py` | random, indefinite loop |
| 13 | `13_menu_calculator.py` | menu and zero division |
| 14 | `14_my_sum.py` | custom reusable function |
| 15 | `15_analyze_number.py` | return multiple properties |
| 16 | `16_student_grade.py` | five subjects and grades |
| 17 | `17_shopping_cart.py` | functions and cart dictionary |
| 18 | `18_employee_salary.py` | employee calculations |
| 19 | `19_bank_account.py` | transactions and history |
| 20 | `20_student_registration_system.py` | CRUD, dictionary, menus |

## Design choices and explanations
- **`for` loops:** Best when traversing a known sequence, such as 1 through N, five subjects, or a list of marks.
- **Nested `for` loops:** Used for primes (candidate number and divisors) and patterns (rows and columns).
- **`while` loops:** Best when repetition depends on user choices or an unknown number of attempts, such as ATM, guessing game, calculator, and student registration.
- **Functions:** Reusable named pieces of logic with parameters and return values; they make tests possible without keyboard input.
- **Lists:** Store ordered marks or results. **Dictionaries:** Map characters to counts, item names to prices/quantities, and student IDs to records.
- **Validation:** Negative deposits, zero division, invalid marks, duplicate student IDs and empty collections are handled where relevant.

## Example outputs
**Q1:** Input `5` → `1 is Odd` through `5 is Odd`, `Even: 2; Odd: 3`.  
**Q5:** Input `banana` → `'b': 1`, `'a': 3`, `'n': 2`.  
**Q7:** Range `1` to `10` → `2 3 5 7`.  
**Q8:** Rows `3` → `1`, `1 2`, `1 2 3`.  
**Q14:** Input `1 2 3` → `Sum: 6.0`.

## Assumptions
- Marks are 0–100; a score of 40 passes Q9.
- Q16 grades: A ≥90, B ≥75, C ≥60, D ≥40, otherwise Fail; grade uses overall percentage.
- Q6 counts English A–Z as vowels/consonants; other letters are classified as special. Any whitespace counts in the `spaces` category.
- Q17 uses item name as key; adding an existing item increases quantity and uses the latest unit price.
- Q18 tax is calculated on gross salary (basic + bonus).
- Q20 records are stored in memory for the current run (not persisted to disk); ties for top student select the first inserted record.
- Monetary values are educational floating-point examples, not suitable for production banking or accounting.

## GitHub submission
Create a repository named `super30-python-loops-functions-assignment`. From this folder:
```bash
git init
git add .
git commit -m "Complete Super30 Python loops and functions assignment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/super30-python-loops-functions-assignment.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username and create the empty repository first. A public or private repository is acceptable per the assignment.

## Video explanation
Use `VIDEO_EXPLANATION_GUIDE.md` as a guide. Show the actual code and run the programs yourself; explain the reasoning rather than reading the source aloud. Include at least one debugging problem you genuinely encountered.
