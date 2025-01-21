from fontPens import marginPen
from fontParts.world import RGlyph
#guideline = RGuideline()
f = CurrentFont()

##First Setting
bor_height = 460
baseline = 0

#for Vowel = top and _top
def anchor_function(g, x_value_top, x_value_bottom, y_value_top, y_value_bottom, x_adjust_top=0, x_adjust_bottom=0):    
    g.clearAnchors()
    g.appendAnchor ("top", (x_value_top+x_adjust_top, y_value_top))
    g.appendAnchor ("_top", (x_value_bottom+x_adjust_bottom, y_value_bottom))

##Color
yellow = (1, 0.91, 0.435, 1)
light_yellow = (1, 0.91, 0.435, 0.5)
green = (0.459, 0.91, 0.435, 1)
light_green = (0.459, 0.91, 0.435, 0.5)

#for Vowel bottom 
def anchor_function_bottom(g, x_value_underscoreBottom, x_value_bottom, y_value_underscoreBottom, y_value_bottom, x_adjust_underscoreBottom=0, x_adjust_bottom=0):    
    g.clearAnchors()
    g.appendAnchor ("_bottom", (x_value_underscoreBottom+x_adjust_underscoreBottom, y_value_underscoreBottom))
    g.appendAnchor ("bottom", (x_value_bottom+x_adjust_bottom, y_value_bottom))

##Color
yellow = (1, 0.91, 0.435, 1)
light_yellow = (1, 0.91, 0.435, 0.5)
green = (0.459, 0.91, 0.435, 1)
light_green = (0.459, 0.91, 0.435, 0.5)


#Minus Value
x_borWidth = -(f["th-bobaimai"].rightMargin)
print ("th-bobaimai width is ", x_borWidth)

for anchor in f["th-popla"].anchors:
    #print (anchor)
    popla_width = f["th-popla"].width
    print ("th-popla width is ", popla_width)
    if anchor.name == "top":
        print ("Popla top anchor x position is", anchor.x)
        anchor_top_x = anchor.x
        anchor_ascender_distance = -(popla_width - anchor_top_x)
        print ("distace from anchor top to right width is ", anchor_ascender_distance)


f.clearGuidelines()

#Set width guideline
borWidth_guideline = f.appendGuideline((x_borWidth, f.info.ascender), 90, name ="bor-width")
poPlaTopAnchor_guideline = f.appendGuideline((anchor_ascender_distance, f.info.ascender), 90, name ="popla top anchor")

#1-Base measurement happened in "th-sarai"
tonemarkbase_1 = f["th-sarai"]
marginPen_vertical = marginPen.MarginPen(f, x_borWidth, isHorizontal = False )
tonemarkbase_1.draw(marginPen_vertical)
##make the list of htting point
marginPen_vertical_hit_list = marginPen_vertical.getAll()
tonemark_height_1 = marginPen_vertical_hit_list[0]

#1-Set Height guideline 
tonemark_height_1_guide = f.appendGuideline((0, tonemark_height_1),0, name = "tonemark_1")

#2-Base measurement happended in "th-maiek.small"
tonemarkbase_2 = f["th-maiek.small"]
marginPen_vertical = marginPen.MarginPen(f, x_borWidth, isHorizontal = False )
tonemarkbase_2.draw(marginPen_vertical)
marginPen_vertical_hit_list = marginPen_vertical.getAll()
tonemark_height_2 = marginPen_vertical_hit_list[0]

#2-Set Height guideline
tonemark_height_2_guideline = f.appendGuideline((0, tonemark_height_2),0, name = "tonemark_2")

##Has th-saraii as a set up
##1 Group based on the tone-marks set
first_floor_normal = ["th-saraii", "th-maiek", "th-maitho", "th-maitri", "th-maichattawa", "th-thanthakhat", "th-maitaikhu", "th-yamakkan"]
for glyph_name in first_floor_normal:
    g = f[glyph_name]
    top_anchor_y_position = g.bounds[3]
    g.clearAnchors()
    print (g.name, "top anchor y value is ", top_anchor_y_position)
    anchor_function(g, x_borWidth, x_borWidth, top_anchor_y_position, bor_height )
    g.markColor = yellow


first_floor_normal_fix_y = ["th-sarauee", "th-maihan-akat", "th-sarai", "th-saraue", "th-sarauee", "th-nikhahit"]
for glyph_name in first_floor_normal_fix_y:
    g = f[glyph_name]
    g.clearAnchors()
    for saraii_anchor in f["th-saraii"].anchors:
        print (saraii_anchor)
        g.appendAnchor(saraii_anchor.name, (saraii_anchor.x, saraii_anchor.y))
    if g == f["th-maihan-akat"]:
        for anchor_top in g.anchors:
            if anchor_top.name == "top":
                print ("original anchor top of maihan-akat is ", anchor_top.name, anchor_top.y)
                anchor_top.y += -10
                anchor_top.changed()
    if g == f["th-sarai"]:
        for anchor_top in g.anchors:
            if anchor_top.name == "top":
                print ("original anchor top of maihan-akat is ", anchor_top.name, anchor_top.y)
                anchor_top.y += -10
                anchor_top.changed()
    g.markColor = light_yellow
                
first_floor_narrow = ["th-saraii.narrow", "th-maiek.narrow", "th-maitho.narrow", "th-maitri.narrow", "th-maichattawa.narrow", "th-thanthakhat.narrow", "th-maitaikhu.narrow"]
for glyph_name in first_floor_narrow:
    g = f[glyph_name]
    top_anchor_y_position = g.bounds[3]
    g.clearAnchors()
    anchor_function(g, anchor_ascender_distance, anchor_ascender_distance, top_anchor_y_position, bor_height)
    g.markColor = green

first_floor_narrow_fix_y = ["th-maihan-akat.narrow", "th-sarai.narrow", "th-saraue.narrow", "th-sarauee.narrow", "th-nikhahit.narrow"]
for glyph_name in first_floor_narrow_fix_y:
    g = f[glyph_name]
    g.clearAnchors()
    for saraii_anchor_narrow in f["th-saraii.narrow"].anchors:
        #print (saraii_anchor)
        g.appendAnchor(saraii_anchor_narrow.name, (saraii_anchor_narrow.x, saraii_anchor_narrow.y))
    if g == f["th-maihan-akat.narrow"]:
        for anchor_top in g.anchors:
            if anchor_top.name == "top":
                print ("original anchor top of maihan-akat is ", anchor_top.name, anchor_top.y)
                anchor_top.y += -10
                anchor_top.changed()
    if g == f["th-sarai.narrow"]:
        for anchor_top in g.anchors:
            if anchor_top.name == "top":
                print ("original anchor top of maihan-akat is ", anchor_top.name, anchor_top.y)
                anchor_top.y += -10
                anchor_top.changed()
    g.markColor = light_green

second_floor_underscoreTop_y = f["th-saraii"].bounds[3]
print ("")
print ("second floor calculation start here...")
print ("_top y position is ", second_floor_underscoreTop_y)

second_floor_set = ["th-maiek.small", "th-maitho.small", "th-maitri.small", "th-maichattawa.small", "th-thanthakhat.small"]
for glyph_name in second_floor_set:
    g = f[glyph_name]
    g.clearAnchors()
    try: 
        top_anchor_y_position = f[glyph_name].bounds[3]
        print (top_anchor_y_position)
        anchor_function(g, x_borWidth, x_borWidth, top_anchor_y_position, second_floor_underscoreTop_y )
        g.markColor = None
    #Not exist
    except TypeError:
        g.markColor = (1,0,0,1)
        pass

vowel_bottom_set = ["th-sarau", "th-sarauu", "th-phinthu"]
for glyph_name in vowel_bottom_set:
    g = f[glyph_name]
    print(g.bounds)
    g.clearAnchors()
    anchor_function_bottom(g, x_borWidth, x_borWidth, baseline, g.bounds[1] )

#Center Nikhahit
#Find width of Nikhahit
nikhahit = f["th-nikhahit"]
nikhahit_w = nikhahit.bounds[2] - nikhahit.bounds[0]
print ("Nikhahit width is ", nikhahit_w)

#Find width of Maiek
maiek_small = f["th-maiek.small"]
maiek_small_w = maiek_small.bounds[2] - maiek_small.bounds[0]
print ("Mai-ek.small width is ", maiek_small_w)
print ("")
print ("Nikhahit right edge x position is ", nikhahit.bounds[2])

for nikahit_anchor in nikhahit.anchors:
    if nikahit_anchor.name == "top":
        
        print ("Nikhahit old 'top' anchor is ", nikahit_anchor.x)
        nikhahit_top_new_anchor = -(((nikhahit_w - maiek_small_w)/2)- nikhahit.bounds[2])
        nikahit_anchor.x = nikhahit_top_new_anchor
        print ("Nikhahit new 'top' anchor is ", nikahit_anchor.x)



