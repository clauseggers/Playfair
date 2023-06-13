"""
Fractions
=========

This plugin implements centered nut fractions for proportional
numerator and denominator glyphs for up to four digits. (In
theory it would be possible to expand this to an arbitrary
number of digits, but I can't work out the patterns used in
centering the glyphs. Any help would be appreciated...)

It works as follows. First, it replaces one fraction-slash glyph
with up to four fraction-slashes in a row, depending on the
number of glyphs on the top or bottom of the fraction, whichever
is the greater. For example, a fraction with two numerator
glyphs and four denominator glyphs would be have four fraction
slashes.

Next, it centers the glyphs over the fraction on the top and
bottom.

Finally, it overlaps the fraction slashes by a user-specified
value, which you will have to determine by experiment, but is
likely to be somewhere around the width of the fraction slash
minus the width of an average numerator/denominator glyph.

Here is a typical use::

  LoadPlugin Fractions;
  Feature dnom { Substitute /dnom$/~dnom -> /.dnom$/; };
  Feature numr { Substitute /numr$/~numr -> /.numr$/; };
  Feature frac {
   Fractions /numr$/ fraction /dnom$/ 152;
  };

This says "Make a ``dnom`` feature by lopping the ``.dnom`` part
off every glyph which ends with ``dnom`` and substituting those
glyphs with the ``.dnom`` forms (and similarly for ``numr``).
Then make a fraction feature from the glyphs ending ``numr``, the
``fraction`` glyph and the glyphs ending ``dnom``, with multiple
fraction slashes overlapping by 152 units.

For this to work:

* The fraction slash needs to be a flat bar! We can't make nut
 fractions from diagonal fraction slashes...
* The numerator and denominator glyphs need to be aligned above
 and below the fraction slash bar respectively.

"""

import fontFeatures
from fez import FEZVerb
from glyphtools import bin_glyphs_by_metric, get_glyph_metrics
from itertools import product

PARSEOPTS = dict(use_helpers=True)

Fractions_GRAMMAR = """
?start: action
action: glyphselector glyphselector glyphselector integer_container
"""

GRAMMAR = ""

VERBS = ["Fractions"]

BIN_COUNT = 3
SUPPORTED_DIGITS = 4


class Fractions(FEZVerb):
  def position(self, which, formulas, overlap):
    count = len(formulas)
    for slash_count in range(SUPPORTED_DIGITS, count - 1, -1):
      context = [self.fraction] * slash_count
      if which == "numerator":
        binned_glyphs = self.binned_numerator
        kwargs = {"postcontext": context}
      else:
        binned_glyphs = self.binned_denominator
        kwargs = {"precontext": context}

      slash_width = get_glyph_metrics(self.parser.font, self.fraction[0])["width"]
      slash_width = slash_width * slash_count - overlap * (slash_count - 1)

      for things in product(*([binned_glyphs] * count)):
        glyphs = [x[0] for x in things]
        widths = [x[1] for x in things]
        placements = [f(slash_width, widths) for f in formulas]
        if which == "denominator":
          placements = [x - slash_width for x in placements]
        self.rules.append(
          fontFeatures.Positioning(
            glyphs,
            [
              fontFeatures.ValueRecord(xAdvance=-int(w), xPlacement=p)
              for w, p in zip(widths, placements)
            ],
            **kwargs
          )
        )

  def action(self, args):
    numerator, fraction, denominator = [
      a.resolve(self.parser.fontfeatures, self.parser.font) for a in args[0:3]
    ]
    overlap = args[3].resolve_as_integer()
    assert len(fraction) == 1
    self.fraction = fraction

    self.binned_numerator = bin_glyphs_by_metric(
      self.parser.font, numerator, "width", BIN_COUNT
    )
    self.binned_denominator = bin_glyphs_by_metric(
      self.parser.font, denominator, "width", BIN_COUNT
    )
    self.rules = []

    # Expand the slashes
    for digit_count in range(SUPPORTED_DIGITS, 1, -1):
      self.rules.append(
        fontFeatures.Substitution(
          [fraction],
          [fraction] * digit_count,
          precontext=[numerator] * digit_count,
        )
      )
      self.rules.append(
        fontFeatures.Substitution(
          [fraction],
          [fraction] * digit_count,
          postcontext=[denominator] * digit_count,
        )
      )

    # Center the glyphs
    center_one = [lambda slash_width, widths: int(slash_width / 2 - widths[0] / 2)]
    center_two = [
      lambda slash_width, widths: int(slash_width / 2 - widths[0]),
      lambda slash_width, widths: int(slash_width / 2),
    ]
    center_three = [
      lambda slash_width, widths: int(
        slash_width / 2 - widths[0] - widths[1] / 2
      ),
      lambda slash_width, widths: int(slash_width / 2 - widths[1] / 2),
      lambda slash_width, widths: int(slash_width / 2 + widths[1] / 2),
    ]
    center_four = [
      lambda slash_width, widths: int(slash_width / 2 - widths[0] - widths[1]),
      lambda slash_width, widths: int(slash_width / 2 - widths[1]),
      lambda slash_width, widths: int(slash_width / 2),
      lambda slash_width, widths: int(slash_width / 2 + widths[1]),
    ]
    for which in ["numerator", "denominator"]:
      self.position(which, formulas=center_four, overlap=overlap)
      self.position(which, formulas=center_three, overlap=overlap)
      self.position(which, formulas=center_two, overlap=overlap)
      self.position(which, formulas=center_one, overlap=overlap)

    # Also overlap the fractions
    self.rules.append(
      fontFeatures.Positioning(
        [fraction],
        [fontFeatures.ValueRecord(xAdvance=-overlap)],
        postcontext=[fraction],
      )
    )

    return self.rules
