##This code is creating the extra glyphs from the existing one, also bringing "anchor"
from fontPens import marginPen
from fontParts.world import RGlyph
f = CurrentFont()

##First Setting
bor_height = 460
baseline = 0
#Minus Value
x_borWidth = -(f["th-bobaimai"].rightMargin)
print ("th-bobaimai width is ", x_borWidth)

blue = (0.278, 0.631, 0.651, 1)




extra_sets_nikhahit= ["th-nikhahit_maitho" , "th-nikhahit_maitri"]
extra_sets_nikhahit_narrow = ["th-nikhahit_maitho.narrow" , "th-nikhahit_maitri.narrow"]
extra_sets_maihanakat= [ "th-maihan-akat_maitho" , "th-maihan-akat_maitri"]
extra_sets_maihanakat_narrow =[ "th-maihan-akat_maitho.narrow" , "th-maihan-akat_maitri.narrow"]

for glyph_name in extra_sets_nikhahit:
    g = f[glyph_name]
    g.clearAnchors()
    for nikhahit_anchor in f["th-nikhahit"].anchors:
        if nikhahit_anchor.name == "_top":
            g.appendAnchor(nikhahit_anchor.name, (nikhahit_anchor.x, nikhahit_anchor.y))
    for maitho_small_anchor in f["th-maitho.small"].anchors:
        if maitho_small_anchor.name == "top":
            g.appendAnchor(maitho_small_anchor.name, (maitho_small_anchor.x, g.bounds[3]))
    #g.markColor = blue

for glyph_name in extra_sets_nikhahit_narrow:
    g = f[glyph_name]
    g.clearAnchors()
    for nikhahit_anchor in f["th-nikhahit.narrow"].anchors:
        if nikhahit_anchor.name == "_top":
            g.appendAnchor(nikhahit_anchor.name, (nikhahit_anchor.x, nikhahit_anchor.y))
    for maitho_small_anchor in f["th-maitho.small"].anchors:
        if maitho_small_anchor.name == "top":
            g.appendAnchor(maitho_small_anchor.name, (maitho_small_anchor.x, g.bounds[3]))

for glyph_name in extra_sets_maihanakat: 
    g = f[glyph_name]
    g.clearAnchors() 
    for maihanakat_anchor in f["th-maihan-akat"].anchors:
        if maihanakat_anchor.name == "_top":
            g.appendAnchor(maihanakat_anchor.name, (maihanakat_anchor.x, maihanakat_anchor.y))
    for maitho_small_anchor in f["th-maitho.small"].anchors:
        if maitho_small_anchor.name == "top":
            g.appendAnchor(maitho_small_anchor.name, (maitho_small_anchor.x, g.bounds[3]))
    #g.markColor = blue

for glyph_name in extra_sets_maihanakat_narrow: 
    g = f[glyph_name]
    g.clearAnchors() 
    for maihanakat_narrow_anchor in f["th-maihan-akat.narrow"].anchors:
        if maihanakat_narrow_anchor.name == "_top":
            g.appendAnchor(maihanakat_narrow_anchor.name, (maihanakat_narrow_anchor.x, maihanakat_narrow_anchor.y))
    for maitho_small_anchor in f["th-maitho.small"].anchors:
        if maitho_small_anchor.name == "top":
            g.appendAnchor(maitho_small_anchor.name, (maihanakat_narrow_anchor.x, g.bounds[3]))

g.markColor = blue