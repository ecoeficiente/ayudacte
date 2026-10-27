#set text(font: "Arial", size: $fontsize$)
#set par(justify: false, leading: 0.65em, spacing: 6pt)
#set page(paper: "a4", margin: (top: 22mm, bottom: 22mm, left: 24mm, right: 20mm), numbering: "1",
  header: align(right, text(size: 8pt, fill: rgb("#5e666b"))[DesignBuilder CTE · Aurea Consulting]),
  footer: align(right, context text(size: 8pt)[#counter(page).display("1")]),
)
#let current-part = state("manual-part", none)
#let part(body) = current-part.update(body)
#set heading(numbering: none)
#set document(title: [$title$], author: "Aurea Consulting")
#show heading.where(level: 1): it => { pagebreak(weak: true); context { if current-part.get() != none { text(size: 9pt, fill: rgb("#5e666b"))[#current-part.get()]; v(3mm) } }; block(above: 1.2em, below: .8em)[#text(size: 20pt, weight: "bold", fill: rgb("#647f00"))[#it]] }
#show heading.where(level: 2): it => block(above: 1em, below: .5em)[#text(size: 14pt, weight: "bold", fill: rgb("#647f00"))[#it]]
#show heading.where(level: 3): it => block(above: .8em, below: .4em)[#text(size: 11pt, weight: "bold")[#it]]
#show raw: set text(font: "Consolas", size: 8pt)
#show link: set text(fill: rgb("#647f00"))
#show figure.where(kind: table): set text(size: 9pt)
#set table(inset: 4pt, stroke: .35pt + rgb("#ccd5df"))
#show: doc => {
  set par(justify: false, leading: 0.7em, spacing: 7pt)
  show heading.where(level: 2): set block(above: 15pt, below: 7pt)
  show heading.where(level: 3): set block(above: 12pt, below: 5pt)
  set table(inset: 5pt)
  set table.cell(breakable: false)
  show table: it => block(breakable: it.children.len() > 40)[#it]
  v(30mm)
  text(size: 30pt, weight: "bold", fill: rgb("#647f00"))[$title$]
  v(.5em)
  text(size: 13pt)[$subtitle$]
  v(.5em)
  text(size: 9pt)[Aurea Consulting · 25 de octubre de 2026]
  v(1em)
  pagebreak()
  outline(title: [Contenido], depth: 2)
  pagebreak()
  doc
}
