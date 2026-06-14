"""Google Fonts Glyphsets.

Definitions of codepoint groups from the Google Fonts "glyphsets" repository.
These groups can be used to filter the glyphs in a font to only those that are
relevant for a particular script, or to limit the number of glyphs in a font to
reduce its size.
"""

from torchfont._torchfont import (
    LATIN_CORE,  # noqa: F401
    LATIN_KERNEL,  # noqa: F401
    get_glyphset_codepoints,  # noqa: F401
)
