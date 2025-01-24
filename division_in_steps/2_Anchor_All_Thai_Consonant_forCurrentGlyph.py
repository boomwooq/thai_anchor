##Using Margin Pen
from fontPens import marginPen
from fontParts.world import RGlyph
g = CurrentGlyph()
f = g.font


##First Setting
bor_height = 540
baseline = 0

##Color
color_1 = (0.75,1,0,1)
color_2 = (0.967,0.422,1,1)
color_3 = (1,0.568,0.654,1)
color_4 = (0.932,0.801,0.837,1)
color_5 = (0.921, 0.917, 0.875,1)
color_6 = (0.063, 0.85, 1,1)
color_7 = (0.063, 0.664, 0.714,1)
color_8 = (0.607, 0.980, 1, 1)
color_9 = (1, 0.857, 0, 1)
color_10 = (0.331, 0.481,1, 0.8)

#set y or height value for margin pen & guideline
y_value_top = bor_height
y_value_middle_1 = 224
y_value_middle_2 = 150
y_value_bottom = 0

def make_guideline(name, y_value):
    my_guideline = f.appendGuideline((0, y_value), 0)
    my_guideline.showMeasurements = True
    my_guideline.name = name

def margin_value_top(g, report = False):
    marginPen_top = marginPen.MarginPen(f, y_value_top)
    g.draw(marginPen_top)
    left_margin_top, right_hit_top = marginPen_top.getMargins()
    right_margin_top = g.width - right_hit_top
    if report is True:
        print ("Letter is ", g.name)
        print ("left margin top is ", left_margin_top)
        print ("right hit at x value top is ", right_hit_top)
        print ("right margin value top is ", right_margin_top)
    return right_hit_top

def margin_value_top_ascender(g, report = False):
    marginPen_top = marginPen.MarginPen(f, y_value_top)
    g.draw(marginPen_top)
    hit_points_list = marginPen_top.getAll()
    right_hit_1 = hit_points_list[-1] #get very right hit point
    right_hit_2 = hit_points_list[-2] #get second hit point from the right 
    return right_hit_2

def margin_value_middle(g, y_position, report = False):
    marginPen_middle = marginPen.MarginPen(f, y_position)
    g.draw(marginPen_middle)
    left_margin_middle, right_hit_middle = marginPen_middle.getMargins()
    right_margin_middle = g.width - right_hit_middle
    if report is True:
        print ("left margin middle is ", left_margin_middle)
        print ("right hit at x value middle is ", right_hit_middle)
        print ("right margin value middle is ", right_margin_middle)
    return right_hit_middle

def margin_value_bottom(g, report = False):
    marginPen_bottom = marginPen.MarginPen(f, y_value_bottom)
    g.draw(marginPen_bottom)
    left_margin_bottom, right_hit_bottom = marginPen_bottom.getMargins()
    right_margin_bottom = g.width - right_hit_bottom
    if report is True:
        print ("left margin bottom is ", left_margin_bottom)
        print ("right hit at x value bottom is ", right_hit_bottom)
        print ("right margin value bottom is ", right_margin_bottom)
    return right_hit_bottom

def descender_measurement(glyph_name, extra_y_offset=0):
    if glyph_name in f and f[glyph_name].contours:
        my_descender = f[glyph_name].bounds[1] + extra_y_offset
    else:
        my_descender = 0
        print(f'descender cannot be measured if there is no {glyph_name}')
    return my_descender

def anchor_function(g, x_value_top, x_value_bottom, y_value_top, y_value_bottom, x_adjust_top=0, x_adjust_bottom=0):    
    g.clearAnchors()
    g.appendAnchor ("top", (x_value_top+x_adjust_top, y_value_top))
    g.appendAnchor ("bottom", (x_value_bottom+x_adjust_bottom, y_value_bottom))


#Clear all guideline
#f.clearGuidelines()
for guideline in f.guidelines:
    print (guideline)
    if guideline.name not in ["bor-width", "popla top anchor", "tonemark_1", "tonemark_2", "tonemark_1_top", "bottom_top", "bottom_bottom"]:
        f.removeGuideline(guideline)

make_guideline('top', y_value_top)
make_guideline('middle_1', y_value_middle_1)
make_guideline('middle_2', y_value_middle_2)
make_guideline('bottom', y_value_bottom)

#top_borHeight, bottom_curve_baseline
group_1 = ["th-bobaimai", "th-sorusi", "th-moma", "th-ngongu", "th-khokhai", "th-khokhuat", "th-khorakhang", "th-yoyak", "th-chochoe", "th-yoying.less", "th-thophuthao"]

#top_borHeight_curve, bottom_baseline
#middle_1
group_2 = ["th-kokai", "th-thothung", "th-phosamphao", "th-thothahan", "th-thonangmontho", "th-choching", "th-khokhwai", "th-khokhon", "th-sosala", "th-loling", "th-sosua"]

#borHeight_middle, bottom_curve_baseline
#middle_1
group_3 = ["th-chochang", "th-soso"]

#borHeight_stright, top * bottom
group_4 = ["th-nonu", "th-phophung", "th-nonen", "th-phophan"]

#borHeight_middle, bottom
#middle_2
group_5 = ["th-hohip", "th-rorua", "th-thothong"]

#borHeight_curve
#middle_1
group_6 = ["th-oang", "th-honokhuk", "th-chochan", "th-thothan.less", "th-wowaen", "th-lochula.short", "th-dodek", "th-totao"]

#borHeight_middle, bottom
#middle_1
group_7 = ["th-lochula.short", "th-dodek", "th-totao"]

#borHeight_tpp_curve, middle_1, short descender
#middle_1
group_8 = ["th-ru", "th-lu", "th-yoying", "th-dochada.short", "th-topatak.short"]

#borHeight, middle_1, descender
#middle_1
group_9 = ["th-dochada", "th-topatak", "th-thothan"]

#top_bounds, bottom
group_10 = ["th-lochula"]

group_11 = ["th-popla", "th-fofan", "th-fofa"]

th_descender_short = descender_measurement('th-ru')
th_descender = descender_measurement('th-dochada', 10)


glyph_name = g.name
if glyph_name in group_1:
    th_anchor_top = margin_value_top(g)
    th_anchor_bottom = margin_value_top(g)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , -10)
    g.markColor = color_1
    #print (margin_value_top(g, report = True))

elif glyph_name in group_2:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_bottom(g)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, -10 , 0)
    g.markColor = color_2

elif glyph_name in group_3:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , -10)
    g.markColor = color_3

elif glyph_name in group_4:
    th_anchor_top = margin_value_top(g)
    th_anchor_bottom = margin_value_bottom(g)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
    g.markColor = color_4
elif glyph_name in group_5:
    th_anchor_top = margin_value_middle(g, y_value_middle_2)
    th_anchor_bottom = margin_value_middle(g, y_value_middle_2)
    if g == f["th-hohip"]:
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
    else:
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , -10)
    g.markColor = color_5

elif glyph_name in group_6:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, -30 , -30)
    g.markColor = color_6

elif glyph_name in group_7:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_bottom(g)
    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, -10, 0)
    g.markColor = color_7

elif glyph_name in group_8:
    print ("group_8, thai short ascender is ", th_descender_short)
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_bottom(g)
    if g.name == "th-yoying":
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender_short, 0, 0)
    else:
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender_short, -10, 0)
    g.markColor = color_8

elif glyph_name in group_9:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
    if g.name == "th-thothan":
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender, -30, 0)
    else: 
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender, -10, 0)
    g.markColor = color_9

elif glyph_name in group_10:
    th_anchor_top = margin_value_middle(g, y_value_middle_1)
    th_anchor_bottom = margin_value_bottom(g)
    #print (g.bounds)
    anchor_function(g, th_anchor_top, th_anchor_bottom, g.bounds[3], baseline , 0, 0)

elif glyph_name in group_11:
    # Set padding from stem, only minus value
    stem_padding = -40
    if g.name == "th-popla":
        th_anchor_top = margin_value_top_ascender(g) + stem_padding
        th_anchor_bottom = margin_value_top(g)
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0, -10)
    else:
        th_anchor_top = margin_value_top_ascender(g) + stem_padding
        th_anchor_bottom = margin_value_bottom(g)
        anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0, 0)
    g.markColor = color_10


print ("done")