introToStrings = "In python, anything we enclose in single/double/triple quotes is a string.Strings are immutable sequences of unicode points.They can be indexed, sliced, concatenated and repeated. strings have many useful methods for manipulation and formatting. Python has predefined functions for string manipulation, such as len(), str(), and format()."
print(introToStrings[0:50])
print(introToStrings)


# Python string basics - runnable examples and notes
# Save as day_11_strings_basics.py and run with: python day_11_strings_basics.py

def show(title, value):
    print(f"--- {title} ---")
    print(value)
    print()

def main():
    # 1. Creation: single, double, triple quotes
    s1 = 'single quoted'
    s2 = "double quoted"
    s3 = """triple
quoted
multi-line"""
    s4 = '''also
multi-line'''
    show("s1, s2, s3 (multi-line)", f"{s1=!r}\n{s2=!r}\n{s3=!r}\n{s4=!r}")

    # 2. Escaping and raw strings
    escaped = "She said \"Hello\".\nNew line"
    raw = r"C:\Users\Name\new_folder\n"
    show("escaped vs raw", f"{escaped!r}\n{raw!r}")

    # 3. Immutability: you cannot change a character in place
    s = "immutable"
    try:
        s[0] = "I"
    except TypeError as e:
        show("immutability example (error)", e)

    # 4. Indexing and negative indices
    s = "Python"
    show("indexing", f"first={s[0]}, last={s[-1]}, penultimate={s[-2]}")

    # 5. Slicing: [start:stop:step], stop is exclusive
    s = "abcdefghijkl"
    show("slicing examples", f"s[:4]={s[:4]}, s[4:8]={s[4:8]}, s[::2]={s[::2]}, s[::-1]={s[::-1]}")

    # 6. Concatenation and repetition
    a = "Hello"
    b = "World"
    show("concat & repeat", f"a + ' ' + b = {(a + ' ' + b)!r}, a*3 = {(a*3)!r}")

    # 7. Membership and iteration
    show("membership & iteration", f"'y' in 'python' -> {'y' in 'python'}\ncharacters: {', '.join(list('cat'))}")

    # 8. Common useful methods
    sample = "  Python is Awesome!  "
    methods_demo = {
        "len": len(sample),
        "strip": sample.strip(),
        "lstrip": sample.lstrip(),
        "rstrip": sample.rstrip(),
        "lower": sample.lower(),
        "upper": sample.upper(),
        "capitalize": sample.capitalize(),
        "title": sample.title(),
        "swapcase": sample.swapcase(),
        "replace": sample.replace("Awesome", "great"),
        "split": sample.split(),           # splits on whitespace by default
        "split(',')": "a,b,c".split(","),
        "join": "-".join(["a", "b", "c"]),
        "find('is')": sample.find("is"),
        "rfind('o')": sample.rfind("o"),
        "count('o')": sample.count("o"),
        "startswith('  Py')": sample.startswith("  Py"),
        "endswith('  ')": sample.endswith("  "),
        "isalnum on 'abc123'": "abc123".isalnum(),
        "isalpha on 'abc'": "abc".isalpha(),
        "isdigit on '123'": "123".isdigit(),
        "isspace on '   '": "   ".isspace(),
        "zfill(10)": "42".zfill(10),
        "center(20)": "hi".center(20, "*"),
    }
    show("common methods", "\n".join(f"{k}: {v!r}" for k, v in methods_demo.items()))

    # 9. Partitioning (useful when you want head, sep, tail)
    p = "user@example.com"
    show("partition", p.partition("@"))        # ('user', '@', 'example.com')
    show("rpartition", "a,b,c".rpartition(","))# ('a,b', ',', 'c')

    # 10. Formatting: %, str.format, f-strings (recommended)
    name = "Alice"
    points = 95.1234
    show("formatting examples", "\n".join([
        "percent: %s scored %.2f%%" % (name, points),
        "format(): {} scored {:.1f}%".format(name, points),
        f"f-string: {name} scored {points:.3f}%",
        "alignment: " + f"|{name:<10}|{name:^10}|{name:>10}|"
    ]))

    # 11. ord, chr and encoding/bytes
    ch = "€"
    show("ord/chr/encoding", f"ord('A')={ord('A')}, chr(65)={chr(65)}\n{ch!r} encoded -> {ch.encode('utf-8')}")

    # 12. Bytes vs str
    b = b"hello"
    s_from_bytes = b.decode("utf-8")
    show("bytes vs str", f"bytes: {b}, decoded: {s_from_bytes!r}")

    # 13. Unicode note: len() counts code points, not user-perceived graphemes
    heart = "❤️"     # might be two code points depending on sequence
    show("unicode length", f"{heart!r} len() = {len(heart)}")

    # 14. Translation using maketrans/translate
    trans = str.maketrans("aeiou", "12345")
    show("translate", f"translate vowels: {'example'.translate(trans)!r}")

    # 15. Splitting lines and keeping line breaks
    text = "line1\nline2\r\nline3"
    show("splitlines", f"{text.splitlines()}")

    # 16. Performance tips:
    # - Strings are immutable: use join() to build a large string from pieces.
    # - For many small concatenations, accumulate in a list and ''.join(list).
    parts = []
    for i in range(5):
        parts.append(str(i))
    show("join performance pattern", f"joined = {','.join(parts)!r}")

    # 17. Comparison: lexicographic, case-sensitive
    show("comparison", f"'a' < 'b' -> {'a' < 'b'}, 'A' < 'a' -> {'A' < 'a'}")

    # 18. Useful small recipes
    url = "https://example.com/path/"
    show("rstrip slash", f"url.rstrip('/') -> {url.rstrip('/')!r}")

    # 19. Safety when formatting untrusted input: prefer explicit formatting and validate.
    user_input = "<script>"
    show("escape for HTML (simple)", f"replace '<' and '>' -> {user_input.replace('<','&lt;').replace('>','&gt;')!r}")

    # 20. Summary (printed for convenience)
    summary = [
        "Strings are immutable sequences of Unicode code points.",
        "Use indexing/slicing to access parts. Negative indexes count from end.",
        "Use join() to concatenate many pieces efficiently.",
        "Use str methods for common tasks (split, strip, replace, find, startswith...).",
        "Use f-strings for readable, modern formatting (Python 3.6+).",
        "Be aware of encoding when converting to/from bytes (utf-8 common)."
    ]
    show("summary", "\n".join(summary))


def free_vars(*names):
    """Remove named variables from module globals (if present) and run GC."""
    import gc
    g = globals()
    for n in names:
        g.pop(n, None)
    gc.collect()


if __name__ == "__main__":
    main()