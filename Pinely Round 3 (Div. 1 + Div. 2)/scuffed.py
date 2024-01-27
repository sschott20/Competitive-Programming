import re

comment_re = re.compile(
    r"(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?", re.DOTALL | re.MULTILINE
)


def comment_replacer(match):
    start, mid, end = match.group(1, 2, 3)
    if mid is None:
        # single line comment
        return ""
    elif start is not None or end is not None:
        # multi line comment at start or end of a line
        return ""
    elif "\n" in mid:
        # multi line comment with line break
        return "\n"
    else:
        # multi line comment without line break
        return " "


def remove_comments(text):
    return comment_re.sub(comment_replacer, text)


f = open("c2.py", "r")
text = f.read()
fp = open("c3.py", "w")
fp.write(remove_comments(text))
