from fasthtml import *
from fasthtml import FastHTML
from fasthtml.common import *

css = Style(":root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive; }")
app = FastHTML(hdrs=(picolink, css))

page = Html(
    Head(Title("Some Page")),
    Body(
        Div(
            "Some Text, ",
            A("A link", href="https://example.com"),
            Img(src="https://placehold.com/200", cls="myclass"),
        )
    ),
)


@app.get("/")
def home():
    # return "<h1>Hello World</h1>"
    return Title("Hello World"), Main(H1("Hello, World"), cls="container")


@app.get("/page")
def page_html():
    return to_xml(page)
