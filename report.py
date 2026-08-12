from csvkit.parser import parse


def _is_numeric(values):
    return all(isinstance(v, (int, float)) for v in values if v is not None)


def _stats(values):
    numbers = [v for v in values if v is not None]
    if not numbers:
        return {"count": 0, "min": None, "max": None, "mean": None}
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
    }


def summarize(table):
    lines = [f"{len(table.rows)} rows, {len(table.header)} columns", ""]
    for name in table.header:
        values = table.column(name)
        if _is_numeric(values):
            s = _stats(values)
            if s["count"] == 0:
                lines.append(f"  {name}: empty")
            else:
                lines.append(
                    f"  {name}: n={s['count']} min={s['min']} "
                    f"max={s['max']} mean={s['mean']:.2f}"
                )
        else:
            distinct = len({v for v in values if v is not None})
            lines.append(f"  {name}: {distinct} distinct values")
    return "\n".join(lines)


def report(text, delimiter=","):
    return summarize(parse(text, delimiter=delimiter))
