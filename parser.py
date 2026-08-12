"""csvkit.parser -- minimal CSV parsing with type inference."""

from dataclasses import dataclass, field


class ParseError(Exception):
    """Raised when the input text cannot be parsed as CSV."""


@dataclass
class Table:
    header: list
    rows: list = field(default_factory=list)

    def column(self, name):
        try:
            idx = self.header.index(name)
        except ValueError:
            raise KeyError(f"no such column: {name!r}")
        return [row[idx] for row in self.rows]


def _split_line(line, delimiter=","):
    fields = []
    current = []
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                current.append('"')
                i += 1
            else:
                in_quotes = not in_quotes
        elif ch == delimiter and not in_quotes:
            fields.append("".join(current))
            current = []
        else:
            current.append(ch)
        i += 1
    if in_quotes:
        raise ParseError(f"unterminated quote in line: {line!r}")
    fields.append("".join(current))
    return fields


def _coerce(value):
    text = value.strip()
    if text == "":
        return None
    for cast in (int, float):
        try:
            return cast(text)
        except ValueError:
            pass
    return text


def parse(text, delimiter=","):
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        raise ParseError("empty input")
    header = _split_line(lines[0], delimiter)
    table = Table(header=header)
    for number, line in enumerate(lines[1:], start=2):
        fields = _split_line(line, delimiter)
        if len(fields) != len(header):
            raise ParseError(
                f"line {number}: expected {len(header)} fields, got {len(fields)}"
            )
        table.rows.append([_coerce(f) for f in fields])
    return table
