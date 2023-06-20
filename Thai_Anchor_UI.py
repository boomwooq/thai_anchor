##Thai Anchor Consonants + Vowels
##Using Margin Pen
import ezui
from fontPens import marginPen
from fontParts.world import RGlyph
f = CurrentFont()

class DemoController(ezui.WindowController):

    def build(self):
        content = """
        All has to be filled!
        -----
        Bor Height [______] @borHeight
        Middle_1 [______] @middle_y_1
        Middle_2 [______] @middle_y_2
        Baseline [_0_] @baseline
        Popla_Distance [_40_] @distance
        -----
        (  X 1.Consonants X | 2.Vowels ) @convow
        * Grid
        > * GridRow
        >> (Run) @button 
        >> (Clear Anchor) @clear
        >> (Clear All) @clearAll
        -----        
        """
        descriptionData = dict(
            borHeight=dict(
                placeholder="Enter Thai Bor-Height",
                valueType="number"
            ),
            middle_y_1=dict(
                placeholder="y position mid curve: oang",
                valueType="number"
            ),
            middle_y_2=dict(
                placeholder="average y position at stem of: hohip, rorua, thothong",
                valueType="number"
            ),
            baseline=dict(
                placeholder="Baseline default is 0",
                valueType="number"
            ),
            distance=dict(
                placeholder="top anchor distance from th_ascender group",
                valueType="number"
            )
        )
        self.w = ezui.EZWindow(
            title="Thai Anchor",
            size=(400, "auto"),
            content=content,
            descriptionData=descriptionData,
            controller=self
        )

    def started(self):
        self.w.open()
    
##Button: Choices consonant/ vowel etc.
    def convowCallback(self, sender):
        print("convow:", sender.get())

        
##Button: "Clear Anchor"
    def clearCallback(self, sender):
        # for glyph in f.selectedGlyphs:
        #     glyph.clearAnchors()
        for glyphs in f:
            glyphs.clearAnchors()
        for all_guideline in f:
            f.clearGuidelines()

##Bottom "Clear All"
    def clearAllCallback(self, sender):
        # for glyph in f.selectedGlyphs:
        #     glyph.clearAnchors()
        for glyphs in f:
            glyphs.clearAnchors()
        for all_guideline in f:
            f.clearGuidelines()
        #print (self.w.content.setItemValues(None))
        for value in self.w.content.getItemValues():
            if value not in ["convow","baseline","distance"]:
                self.w.content.setItemValue(value, None)    

##Bottom "run" — input value   
    def buttonCallback(self, sender):
        data = self.w.content.getItemValues()
        print(data)
        print("borHeight is ", data['borHeight'])
        print("#1 middle y is ", data['middle_y_1'])
        print("#2 middle y is ", data['middle_y_2'])
        print("baseline is", data['baseline'])
        
        bor_height = data['borHeight']
        baseline = data['baseline']

##Consonant Button Selected
        if data['convow']==0 :
        ##First Setting
            #print (bor_height)
            ##Color
            color_1 = (0.75,1,0,1)
            color_2 = (0.967,0.422,1,1)
            color_3 = (1,0.568,0.654,1)
            color_4 = (0.932,0.801,0.837,1)
            color_5 = (0.921, 0.917, 0.875,1)
            color_6 = (0.063, 0.85, 1,1)
            color_7 = (1, 0.664, 0.714,1)
            color_8 = (0.607, 0.980, 1, 1)
            color_9 = (1, 0.857, 0, 1)
            color_10 = (0.331, 0.481,1, 0.8)

            #set y or height value for margin pen & guideline
            y_value_top = bor_height
            #print ("y_value_top is", y_value_top)
            y_value_middle_1 = data['middle_y_1']
            y_value_middle_2 = data['middle_y_2']
            y_value_bottom = data['baseline']

            #Clear all guideline
            #f.clearGuidelines()
            for guideline in f.guidelines:
                print (guideline)
                if guideline.name not in ["bor-width", "popla top anchor", "tonemark_1", "tonemark_2", "tonemark_1_top", "bottom_top", "bottom_bottom"]:
                    f.removeGuideline(guideline)

            #make guideline
            top_guideline = f.appendGuideline((0, y_value_top), 0)
            top_guideline.showMeasurements = True
            top_guideline.name = 'top'

            middle_guideline_1 = f.appendGuideline((0, y_value_middle_1), 0)
            middle_guideline_1.showMeasurements = True
            middle_guideline_1.name = 'middle_1'

            middle_guideline_2 = f.appendGuideline((0, y_value_middle_2), 0)
            middle_guideline_2.showMeasurements = True
            middle_guideline_2.name = 'middle_2'

            bottom_guideline = f.appendGuideline((0, y_value_bottom), 0)
            bottom_guideline.showMeasurements = True
            bottom_guideline.name = 'bottom'

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

            def anchor_function(g, x_value_top, x_value_bottom, y_value_top, y_value_bottom, x_adjust_top=0, x_adjust_bottom=0):    
                g.clearAnchors()
                g.appendAnchor ("top", (x_value_top+x_adjust_top, y_value_top))
                g.appendAnchor ("bottom", (x_value_bottom+x_adjust_bottom, y_value_bottom))

            #top_borHeight, bottom_curve_baseline
            group_1= ["th-bobaimai", "th-sorusi", "th-moma", "th-ngongu", "th-khokhai", "th-khokhuat", "th-khorakhang", "th-yoyak", "th-chochoe", "th-yoying.less", "th-thophuthao"]
            for glyph_name in group_1: 
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                if margin_value_bottom(g) < margin_value_middle(g, y_value_middle_1):
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline,0 , -10)
                else: 
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline,0 , 0)
                g.markColor = color_1
            print (margin_value_top(g, report = True))

            #top_borHeight_curve, bottom_baseline
            #middle_1
            group_2= ["th-kokai", "th-thothung", "th-phosamphao", "th-thothahan", "th-thonangmontho", "th-choching", "th-khokhwai", "th-khokhon", "th-sosala", "th-loling", "th-sosua"]
            for glyph_name in group_2:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline,-10 , 0)
                g.markColor = color_2

            #borHeight_middle, bottom_curve_baseline
            #middle_1
            group_3 = ["th-chochang", "th-soso"]
            for glyph_name in group_3:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , -10)
                g.markColor = color_3

            #borHeight_stright, top * bottom
            group_4 = ["th-nonu", "th-phophung", "th-nonen", "th-phophan"]
            for glyph_name in group_4:
                g = f[glyph_name]
                ## "if any" is for loop and loopless "th-phophan"
                if any ([margin_value_top(g) == margin_value_bottom(g), glyph_name=="th-phophan"]) : 
                    th_anchor_top = margin_value_top(g)
                    th_anchor_bottom = margin_value_bottom(g)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
                else: 
                    th_anchor_top = margin_value_top(g)
                    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
                g.markColor = color_4

            #borHeight_middle, bottom
            #middle_2
            group_5 = ["th-hohip", "th-rorua", "th-thothong"]
            for glyph_name in group_5:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_2)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_2)
                if g == f["th-hohip"]:
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
                else:
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , -10)
                g.markColor = color_5

            #borHeight_curve
            #middle_1
            group_6 = ["th-oang", "th-honokhuk", "th-chochan", "th-thothan.less", "th-wowaen", "th-dodek", "th-totao"]
            for glyph_name in group_6:
                g = f[glyph_name]
                if margin_value_middle(g, y_value_middle_1) - margin_value_middle(g, y_value_middle_2) > 10: 
                    th_anchor_top = margin_value_middle(g, y_value_middle_1)
                    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, -30 , -30)
                else:
                    th_anchor_top = margin_value_middle(g, y_value_middle_1)
                    th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, -10 , 0)
                g.markColor = color_6

            group_7 = ["th-lochula.short"]
            for glyph_name in group_7:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_bottom(g)
                anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0 , 0)
                g.markColor = color_7

            #borHeight_tpp_curve, middle_1, short ascender
            #middle_1
            group_8 = ["th-ru", "th-lu", "th-yoying", "th-dochada.short", "th-topatak.short"]
            #th_ascender_short is base on this glyph
            th_ascender_short = f["th-ru"].bounds[1]
            print ("group_8, thai short ascender is ", th_ascender_short)
            for glyph_name in group_8:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                if g == f["th-yoying"]:
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, g.bounds[1], 0, 0)
                else:
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_ascender_short, -10, 0)
                g.markColor = color_8

            #borHeight, middle_1, ascender
            #middle_1
            group_9 = ["th-dochada", "th-topatak", "th-thothan"]
            descender_overshoot = 10
            th_descender = f["th-dochada"].bounds[1] + descender_overshoot
            print ("th_descender is", th_descender)
            for glyph_name in group_9:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_middle(g, y_value_middle_1)
                if g == f["th-thothan"]:
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender, 0, 0)
                else: 
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, th_descender, 0, 0)
                g.markColor = color_9

            #top_bounds, bottom
            group_10 = ["th-lochula"]
            for glyph_name in group_10:
                g = f[glyph_name]
                th_anchor_top = margin_value_middle(g, y_value_middle_1)
                th_anchor_bottom = margin_value_bottom(g)
                #print (g.bounds)
                anchor_function(g, th_anchor_top, th_anchor_bottom, g.bounds[3], baseline , 0, 0)

            group_11 = ["th-popla", "th-fofan", "th-fofa"]
            #Set distance from stem, only minus value
            distance = -(data["distance"])
            for glyph_name in group_11:
                g = f[glyph_name]
                if g == f["th-popla"]:
                    th_anchor_top = margin_value_top_ascender(g) + distance
                    th_anchor_bottom = margin_value_top(g)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0, -10)
                else:
                    th_anchor_top = margin_value_top_ascender(g) + distance
                    th_anchor_bottom = margin_value_bottom(g)
                    anchor_function(g, th_anchor_top, th_anchor_bottom, bor_height, baseline, 0, 0)
                g.markColor = color_10
            print ("Thai Consonant Attached Anchor is done")

 ##Vowel Button is selected
    ##Guideline
        if data['convow']==1 :
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

##End Guideline 
            #1-Base measurement happened in "th-sarai"
            tonemarkbase_1 = f["th-sarai"]
            marginPen_vertical = marginPen.MarginPen(f, x_borWidth, isHorizontal = False )
            tonemarkbase_1.draw(marginPen_vertical)
            ##make the list of htting point
            marginPen_vertical_hit_list = marginPen_vertical.getAll()
            tonemark_height_1 = marginPen_vertical_hit_list[0]

            #2-Base measurement happended in "th-maiek.small"
            tonemarkbase_2 = f["th-maiek.small"]
            marginPen_vertical = marginPen.MarginPen(f, x_borWidth, isHorizontal = False )
            tonemarkbase_2.draw(marginPen_vertical)
            marginPen_vertical_hit_list = marginPen_vertical.getAll()
            tonemark_height_2 = marginPen_vertical_hit_list[0]

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
                    nikahit_top_x = nikahit_anchor.x
                    print ("Vowels Attachment is don")
                if nikahit_anchor.name == "_top":
                    print (nikhahit_w)

DemoController()
