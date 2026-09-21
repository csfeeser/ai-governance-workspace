"""Render a workspace tab (document, table, or form) to a PDF."""
import io
import os
from datetime import date
from html import escape
from html.parser import HTMLParser

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle)

FONT_SETS = [
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
     "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf"),
    ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf",
     "C:/Windows/Fonts/ariali.ttf", "C:/Windows/Fonts/arialbi.ttf"),
]


def _register_fonts():
    for files in FONT_SETS:
        if all(os.path.exists(p) for p in files):
            for name, path in zip(("Body", "Body-Bold", "Body-Italic", "Body-BoldItalic"), files):
                pdfmetrics.registerFont(TTFont(name, path))
            pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                          italic="Body-Italic", boldItalic="Body-BoldItalic")
            return "Body", True
    return "Helvetica", False


FONT, UNICODE_OK = _register_fonts()

GREY = colors.HexColor("#666666")
RULE = colors.HexColor("#cccccc")


def clean(text):
    """Make text safe for the chosen font."""
    if UNICODE_OK:
        return text
    return text.encode("cp1252", "replace").decode("cp1252")


def styles():
    base = getSampleStyleSheet()["Normal"]
    body = ParagraphStyle("body", parent=base, fontName=FONT, fontSize=10, leading=14, spaceAfter=6)
    return {
        "body": body,
        "h1": ParagraphStyle("h1", parent=body, fontSize=18, leading=22, spaceBefore=4, spaceAfter=8,
                             fontName=FONT + "-Bold"),
        "h2": ParagraphStyle("h2", parent=body, fontSize=13, leading=17, spaceBefore=10, spaceAfter=4,
                             fontName=FONT + "-Bold"),
        "h3": ParagraphStyle("h3", parent=body, fontSize=11, leading=15, spaceBefore=8, spaceAfter=3,
                             fontName=FONT + "-Bold"),
        "quote": ParagraphStyle("quote", parent=body, leftIndent=14, textColor=GREY),
        "li": ParagraphStyle("li", parent=body, leftIndent=16, bulletIndent=4, spaceAfter=2),
        "cell": ParagraphStyle("cell", parent=body, fontSize=8, leading=10, spaceAfter=0),
        "hcell": ParagraphStyle("hcell", parent=body, fontSize=8, leading=10, spaceAfter=0,
                                fontName=FONT + "-Bold"),
        "label": ParagraphStyle("label", parent=body, fontName=FONT + "-Bold", spaceAfter=1),
        "answer": ParagraphStyle("answer", parent=body, leftIndent=10, spaceAfter=8),
        "muted": ParagraphStyle("muted", parent=body, textColor=GREY, leftIndent=10, spaceAfter=8),
    }


# --------------------------------------------------------- markdown -> flowables

INLINE = {"strong": "b", "b": "b", "em": "i", "i": "i"}


class HtmlToFlowables(HTMLParser):
    """Convert the small HTML subset that `markdown` emits into reportlab flowables."""

    def __init__(self, st):
        super().__init__(convert_charrefs=True)
        self.st = st
        self.flow = []
        self.buf = None      # current inline text buffer
        self.kind = None     # block kind: h1/h2/h3/p/li/quote/cell
        self.list_stack = []
        self.table = None    # list of rows while inside <table>
        self.row = None
        self.head_row = False

    def _open(self, kind):
        self.buf, self.kind = [], kind

    def _close(self):
        if self.buf is None:
            return
        text = "".join(self.buf).strip()
        kind, self.buf, self.kind = self.kind, None, None
        if kind == "cell":
            style = self.st["hcell"] if self.head_row else self.st["cell"]
            self.row.append(Paragraph(text, style))
        elif not text:
            return
        elif kind == "li":
            bullet = "\u2022" if UNICODE_OK else "-"
            if self.list_stack and self.list_stack[-1][0] == "ol":
                self.list_stack[-1][1] += 1
                bullet = f"{self.list_stack[-1][1]}."
            self.flow.append(Paragraph(text, self.st["li"], bulletText=bullet))
        else:
            self.flow.append(Paragraph(text, self.st.get(kind, self.st["body"])))

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3", "h4"):
            self._open("h3" if tag == "h4" else tag)
        elif tag == "p" and self.kind is None:
            self._open("p")
        elif tag == "blockquote":
            self._open("quote")
        elif tag in ("ul", "ol"):
            self._close()
            self.list_stack.append([tag, 0])
        elif tag == "li":
            self._close()
            self._open("li")
        elif tag == "table":
            self.table = []
        elif tag == "tr":
            self.row = []
            self.head_row = False
        elif tag == "th":
            self.head_row = True
            self._open("cell")
        elif tag == "td":
            self._open("cell")
        elif tag == "hr":
            self.flow.append(HRFlowable(width="100%", color=RULE, spaceBefore=6, spaceAfter=6))
        elif tag == "br" and self.buf is not None:
            self.buf.append("<br/>")
        elif tag in INLINE and self.buf is not None:
            self.buf.append(f"<{INLINE[tag]}>")
        elif tag == "code" and self.buf is not None:
            self.buf.append('<font color="#444444">')

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "p", "blockquote", "li", "th", "td"):
            self._close()
        elif tag in ("ul", "ol"):
            self.list_stack.pop()
        elif tag == "tr":
            self.table.append(self.row)
        elif tag == "table":
            self.flow.append(make_table(self.table))
            self.flow.append(Spacer(1, 8))
            self.table = None
        elif tag in INLINE and self.buf is not None:
            self.buf.append(f"</{INLINE[tag]}>")
        elif tag == "code" and self.buf is not None:
            self.buf.append("</font>")

    def handle_data(self, data):
        if self.buf is not None:
            self.buf.append(escape(clean(data)))


def make_table(rows, col_widths=None):
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


# ------------------------------------------------------------------- renderers

def doc_flowables(tab, st):
    import markdown
    html = markdown.markdown(tab["markdown"], extensions=["tables", "sane_lists"])
    conv = HtmlToFlowables(st)
    conv.feed(html)
    return conv.flow


def table_flowables(tab, st, answers):
    cols = tab["columns"]
    editable = tab["editable"]
    header = [Paragraph(escape(clean(c)), st["hcell"]) for c in cols]
    data = [header]
    for i, row in enumerate(tab["rows"]):
        cells = []
        for c in cols:
            val = answers.get(f"t:{tab['id']}:{i}:{c}", "") if c in editable else row[c]
            cells.append(Paragraph(escape(clean(val)), st["cell"]))
        data.append(cells)
    # Give wider columns to longer content (capped so one column cannot take the page).
    weights = [26 if c in editable else max(6, min(60, max(len(c), *(len(r[c]) for r in tab["rows"]))))
               for c in cols]
    usable = (landscape(letter)[0] if len(cols) > 5 else letter[0]) - 1.2 * inch
    widths = [usable * w / sum(weights) for w in weights]
    return [make_table(data, widths)]


def form_flowables(tab, st, answers):
    flow = [Paragraph(escape(clean(tab["heading"])), st["h1"])]
    if tab.get("intro"):
        flow.append(Paragraph(f"<i>{escape(clean(tab['intro']))}</i>", st["body"]))
    for sec in tab["sections"]:
        flow.append(Paragraph(escape(clean(sec["title"])), st["h2"]))
        if sec.get("help"):
            flow.append(Paragraph(f"<i>{escape(clean(sec['help']))}</i>", st["muted"]))
        for f in sec["fields"]:
            flow.append(Paragraph(escape(clean(f["label"])), st["label"]))
            value = answers.get(f"f:{f['id']}", "").strip()
            if value:
                flow.append(Paragraph(escape(clean(value)).replace("\n", "<br/>"), st["answer"]))
            else:
                flow.append(Paragraph("(not answered)", st["muted"]))
    return flow


def render(lab_title, tab, answers):
    st = styles()
    if tab["type"] == "doc":
        story = doc_flowables(tab, st)
    elif tab["type"] == "table":
        story = [Paragraph(escape(clean(tab["title"])), st["h1"])] + table_flowables(tab, st, answers)
    else:
        story = form_flowables(tab, st, answers)

    wide = tab["type"] == "table" and len(tab["columns"]) > 5
    pagesize = landscape(letter) if wide else letter
    footer_text = clean(f"{lab_title} | {tab['title']} | {date.today().isoformat()}")

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT, 8)
        canvas.setFillColor(GREY)
        canvas.drawString(0.6 * inch, 0.4 * inch, footer_text)
        canvas.drawRightString(pagesize[0] - 0.6 * inch, 0.4 * inch, f"Page {doc.page}")
        canvas.restoreState()

    buf = io.BytesIO()
    SimpleDocTemplate(buf, pagesize=pagesize, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                      topMargin=0.6 * inch, bottomMargin=0.7 * inch,
                      title=f"{lab_title}: {tab['title']}").build(
        story, onFirstPage=footer, onLaterPages=footer)
    return buf.getvalue()
