### 12 Regex

Regular Expressions (Regex) are used for searching, matching, and manipulating strings. Python's `re` module provides support for working with Regex.

#### Literal Characters

Most characters, including all letters and digits, match themselves literally in a pattern.

#### Special Characters

Some characters have special meanings in a regex pattern:

- `.`: Matches any character except a newline.
- `^`: Matches the start of a string.
- `$`: Matches the end of a string.
- `*`: Matches 0 or more repetitions of the preceding character.
- `+`: Matches 1 or more repetitions of the preceding character.
- `?`: Matches 0 or 1 repetition of the preceding character.
- `|`: Acts like an OR operator.

#### Character Classes

Enclosed between square brackets `[]`, character classes allow you to match any single character within the brackets.

- `[aeiou]`: Matches any vowel.
- `[0-9]`: Matches any digit.
- `[A-Za-z]`: Matches any uppercase or lowercase letter.

#### Predefined Character Classes

These are shortcuts for common character classes.

- `\d`: Matches any digit (equivalent to `[0-9]`).
- `\D`: Matches any non-digit.
- `\w`: Matches any alphanumeric character (equivalent to `[a-zA-Z0-9_]`).
- `\W`: Matches any non-alphanumeric character.
- `\s`: Matches any whitespace character (spaces, tabs, line breaks).
- `\S`: Matches any non-whitespace character.

#### Quantifiers

Quantifiers specify how many times the preceding element can occur.

- `{n}`: Exactly n occurrences.
- `{n,}`: At least n occurrences.
- `{n,m}`: Between n and m occurrences.

#### Groups and Capturing

Parentheses `()` are used to define groups, which can be referenced and captured.

- `(abc)`: Matches the exact sequence 'abc'.
- `(a|b)`: Matches either 'a' or 'b'.

#### Escape Sequences

A backslash `\` is used to escape a character that has a special meaning in regex, allowing it to be treated as a literal character.
