import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalTrueColorFormatter
import pytest
from pytest import param

from gruvbox import GruvboxStyle


def highlight(code: str) -> str:
    """Highlight code in true color (24-bit) with the GruvboxStyle."""
    return pygments.highlight(
        code=code,
        lexer=PythonLexer(),
        formatter=TerminalTrueColorFormatter(style=GruvboxStyle),
    )


@pytest.mark.parametrize(
    "code,expected",
    [
        param(
            "# This is a comment.",
            "\x1b[38;2;146;131;116m# This is a comment.\x1b[39m\n",
            id="Comment",
        ),
        param(
            "err?",
            "\x1b[38;2;235;219;178merr\x1b[39m\x1b[38;2;251;73;52m?\x1b[39m\n",
            id="Error",
        ),
        param(
            "from gruvbox import GruvboxStyle",
            "\x1b[38;2;131;165;152mfrom\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mgruvbox\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;131;165;152mimport\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mGruvboxStyle\x1b[39m\n",  # noqa: E501
            id="Keyword.Namespace",
        ),
        param("None", "\x1b[38;2;254;128;25mNone\x1b[39m\n", id="Keyword.Constant",),
        param("int", "\x1b[38;2;250;189;47mint\x1b[39m\n", id="Keyword.Type",),
        param(
            "try:\n    pass\nexcept:\n    raise",
            "\x1b[38;2;251;73;52mtry\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\n\x1b[38;2;235;219;178m    \x1b[39m\x1b[38;2;251;73;52mpass\x1b[39m\n\x1b[38;2;251;73;52mexcept\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\n\x1b[38;2;235;219;178m    \x1b[39m\x1b[38;2;251;73;52mraise\x1b[39m\n",  # noqa: E501
            id="Keyword",
        ),
        param(
            "def method(self, other): ...",
            "\x1b[38;2;251;73;52mdef\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;142;192;124mmethod\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;131;165;152mself\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mother\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\n",  # noqa: E501
            id="Name.Builtin.Pseudo",
        ),
        param(
            "list(map(lambda n: n + 1, range(5)))",
            "\x1b[38;2;250;189;47mlist\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;250;189;47mmap\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;251;73;52mlambda\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mn\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mn\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m+\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m1\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;250;189;47mrange\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;211;134;155m5\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n",  # noqa: E501
            id="Name.Builtin",
        ),
        param(
            "class IsDismissed: ...",
            "\x1b[38;2;251;73;52mclass\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;250;189;47mIsDismissed\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\n",  # noqa: E501
            id="Name.Class",
        ),
        param(
            "@decorator\ndef function(): ...",
            "\x1b[38;2;184;187;38;01m@decorator\x1b[39;00m\n\x1b[38;2;251;73;52mdef\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;142;192;124mfunction\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\n",  # noqa: E501
            id="Name.Decorator",
        ),
        param(
            'raise KeyError("Wrong lock.")',
            '\x1b[38;2;251;73;52mraise\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mKeyError\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;184;187;38mWrong lock.\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n',  # noqa: E501
            id="Name.Exception",
        ),
        param(
            "def foo(bar: int, baz: Optional[str] = None) -> None: ...",
            "\x1b[38;2;251;73;52mdef\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;142;192;124mfoo\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;235;219;178mbar\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;250;189;47mint\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mbaz\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mOptional\x1b[39m\x1b[38;2;235;219;178m[\x1b[39m\x1b[38;2;250;189;47mstr\x1b[39m\x1b[38;2;235;219;178m]\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m=\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;254;128;25mNone\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m-\x1b[39m\x1b[38;2;235;219;178m>\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;254;128;25mNone\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\n",  # noqa: E501
            id="Name.Function",
        ),
        param(
            'class IsDismissed:\n    __slots__ = ("attr",)',
            '\x1b[38;2;251;73;52mclass\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;250;189;47mIsDismissed\x1b[39m\x1b[38;2;235;219;178m:\x1b[39m\n\x1b[38;2;235;219;178m    \x1b[39m\x1b[38;2;254;128;25m__slots__\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m=\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;184;187;38mattr\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n',  # noqa: E501
            id="Name.Variable.Magic",
        ),
        param(
            "life = 42",
            "\x1b[38;2;235;219;178mlife\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m=\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m42\x1b[39m\n",  # noqa: E501
            id="Name",
        ),
        param(
            "0b1101001", "\x1b[38;2;211;134;155m0b1101001\x1b[39m\n", id="Number.Bin",
        ),
        param("105.0", "\x1b[38;2;211;134;155m105.0\x1b[39m\n", id="Number.Float",),
        param("0x69", "\x1b[38;2;211;134;155m0x69\x1b[39m\n", id="Number.Hex",),
        param("105", "\x1b[38;2;211;134;155m105\x1b[39m\n", id="Number.Integer",),
        param("0o151", "\x1b[38;2;211;134;155m0o151\x1b[39m\n", id="Number.Oct",),
        param(
            "x is not y and w is (y or z)",
            "\x1b[38;2;235;219;178mx\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mis\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mnot\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178my\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mand\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mw\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mis\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;235;219;178my\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;251;73;52mor\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178mz\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n",  # noqa: E501
            id="Operator.Word",
        ),
        param(
            "3 != 4, 5 == 5, 0b001 << 3",
            "\x1b[38;2;211;134;155m3\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m!=\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m4\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m5\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m==\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m5\x1b[39m\x1b[38;2;235;219;178m,\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m0b001\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m<<\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;211;134;155m3\x1b[39m\n",  # noqa: E501
            id="Operator",
        ),
        param(
            'f"f-strings {rule}"',
            '\x1b[38;2;235;219;178mf\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;184;187;38mf-strings \x1b[39m\x1b[38;2;254;128;25m{\x1b[39m\x1b[38;2;235;219;178mrule\x1b[39m\x1b[38;2;254;128;25m}\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\n',  # noqa: E501
            id="String.Affix",
        ),
        param(
            '"""This is a docstring."""',
            '\x1b[38;2;184;187;38m"""This is a docstring."""\x1b[39m\n',
            id="String.Doc",
        ),
        param(
            '"\\n\\t"',
            '\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;254;128;25m\\n\x1b[39m\x1b[38;2;254;128;25m\\t\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\n',  # noqa: E501
            id="String.Escape",
        ),
        param(
            '"%s" % "{xyzzy}".format(xyzzy="plugh")',
            '\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;254;128;25m%s\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;235;219;178m%\x1b[39m\x1b[38;2;235;219;178m \x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;254;128;25m{xyzzy}\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178mformat\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;235;219;178mxyzzy\x1b[39m\x1b[38;2;235;219;178m=\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;184;187;38mplugh\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n',  # noqa: E501
            id="String.Interpol",
        ),
        param(
            '"This is a string."',
            '\x1b[38;2;184;187;38m"\x1b[39m\x1b[38;2;184;187;38mThis is a string.\x1b[39m\x1b[38;2;184;187;38m"\x1b[39m\n',  # noqa: E501
            id="String",
        ),
        param(
            "    \n    ",
            "\x1b[38;2;235;219;178m    \x1b[39m\n\x1b[38;2;235;219;178m    \x1b[39m\n",
            id="Text",
        ),
        param(
            "[].reverse()",
            "\x1b[38;2;235;219;178m[\x1b[39m\x1b[38;2;235;219;178m]\x1b[39m\x1b[38;2;235;219;178m.\x1b[39m\x1b[38;2;235;219;178mreverse\x1b[39m\x1b[38;2;235;219;178m(\x1b[39m\x1b[38;2;235;219;178m)\x1b[39m\n",  # noqa: E501
            id="Token.Punctuation",
        ),
    ],
)
def test_highlighting(code: str, expected: str) -> None:
    """The given code should highlight as expected."""
    assert highlight(code) == expected
