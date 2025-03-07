"""Unit tests for the HTML post-processor."""


import pytest
from sphinx.application import Sphinx

from sphinxawesome_theme import postprocess

from .util import parse_html


@pytest.mark.sphinx("html")
def test_get_filelist(app: Sphinx) -> None:
    """It gets the correct number of HTML files."""
    app.build()

    html_files = postprocess._get_html_files(app.outdir)
    assert len(html_files) == 3


def test_collapsible_nav() -> None:
    """It adds a span to nested links."""
    html = """
        <nav class="nav-toc">
            <ul>
                <li>
                    <a>Link 1</a>
                    <ul>
                      <li><a>Sublink1</a></li>
                      <li><a>Sublink2</a></li>
                    </ul>
                </li>
                <li><a>Link 2</a></li>
            </ul>
        </nav>
    """

    tree = parse_html(html)
    postprocess._collapsible_nav(tree)

    icons = tree("svg")
    assert len(icons) == 1
    assert icons[0]["class"] == ["expand"]
    assert icons[0].next_sibling.string == "Link 1"


def test_skip_collapsible_nav() -> None:
    """It skips adding it if it's already there."""
    html = """
        <nav class="nav-toc">
            <ul>
                <li >
                    <div class="nav-link">
                        <a>Link 1</a>
                    </div>
                    <ul>
                      <li><a>Sublink1</a></li>
                      <li><a>Sublink2</a></li>
                    </ul>
                </li>
                <li><a>Link 2</a></li>
            </ul>
        </nav>
    """

    tree = parse_html(html)
    postprocess._collapsible_nav(tree)

    navlinks = tree("div", class_="nav-link")
    assert len(navlinks) == 4

    icons = tree("svg")
    assert len(icons) == 0


def test_expand_current() -> None:
    """It adds a class to a li.current but not other li."""
    tree = parse_html("<li class='current'>current</li>")
    postprocess._expand_current(tree)
    assert "expanded" in tree.li["class"]

    tree = parse_html("<li>No current</li>")
    postprocess._expand_current(tree)
    assert not tree.li.has_attr("class")

    tree = parse_html("<li class='current expanded'>expanded</li>")
    postprocess._expand_current(tree)
    assert tree.li["class"].count("expanded") == 1


def test_unwrap_spans() -> None:
    """It unwraps span.pre elements."""
    tree = parse_html("<span class='pre'>Test</span>")
    postprocess._remove_span_pre(tree)
    span = tree("span")
    assert len(span) == 0
    assert str(tree) == "Test"


def test_exception(app: Sphinx) -> None:
    """It skips when an exception is raised."""
    e = Exception()
    postprocess.post_process_html(app, e)
