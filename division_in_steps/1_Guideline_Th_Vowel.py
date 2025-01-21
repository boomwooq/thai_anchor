##Thai Vowels guideline setup
from fontPens import marginPen
from fontParts.world import RGlyph
#guideline = RGuideline()
f = CurrentFont()

##First Setting
bor_height = 470
baseline = 0


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
tonemarkbase_1 = f["th-saraii"]
marginPen_vertical = marginPen.MarginPen(f, x_borWidth, isHorizontal = False )
tonemarkbase_1.draw(marginPen_vertical)
##make the list of htting point
marginPen_vertical_hit_list = marginPen_vertical.getAll()
tonemark_height_1 = marginPen_vertical_hit_list[0]
tonemark_height_1_top = marginPen_vertical_hit_list[-1]

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

#Set the first height "top" anchor position
print (tonemark_height_1_top)
tonemark_height_1_top = f.appendGuideline((0,tonemark_height_1_top),0, name = "tonemark_1_top")

#Bottom-top
bottom_h_top = (f["th-sarau"].bounds[3])
bottom_h_bottom = (f["th-sarau"].bounds[1])
print (bottom_h_bottom)
bottom_top_guideline = f.appendGuideline((0, bottom_h_top),0, name = "bottom_top")
bottom_bottom_guideline = f.appendGuideline((0, bottom_h_bottom), 0, name = "bottom_bottom")