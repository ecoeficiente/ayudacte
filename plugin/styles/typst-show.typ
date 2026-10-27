// Apply the manual's print settings to Quarto's book template.
#import "@preview/orange-book:0.7.1": book, part, chapter, appendices

#show pagebreak.where(to: "odd"): it => pagebreak(weak: true)

#set text(font: "$mainfont$")
#show raw: set text(font: "Consolas")
#set page(
  numbering: none,
  footer: context {
    // The cover has zero margins; omit its footer to avoid clipping.
    if counter(page).get().first() > 1 {
      align(right, text(8.5pt, fill: rgb("#5E666B"), counter(page).display("1")))
    }
  },
)

#show: doc => book(
  title: [$title$],
  subtitle: [$subtitle$],
  author: "$for(by-author)$$it.name.literal$$sep$, $endfor$",
  date: "$date$",
  lang: "$lang$",
  paper-size: "$papersize$",
  margin: (top: $margin.top$, right: $margin.right$, bottom: $margin.bottom$, left: $margin.left$),
  font-size: $fontsize$,
  main-color: rgb("#647F00"),
  cover-background: rgb("#EAF1D4"),
  copyright: none,
  heading-style: 1,
  padded-heading-number: false,
  first-line-indent: false,
  outline-depth: $toc-depth$,
  outline-small-depth: 1,
  supplement-chapter: "$quarto.language.crossref-ch-prefix$",
  {
    set par(leading: $linestretch$ * 0.65em, spacing: 6pt)
    doc
  },
)
