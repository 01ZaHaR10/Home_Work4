from PIL import ImageColor
colors_list = list(ImageColor.colormap.keys())
colors_dict = dict((colors_list[i], ImageColor.getcolor(colors_list[i], "RGB" )) for i in range(len(colors_list)))
for i in colors_dict.keys():
    print(f"Color - {i} : RGB - {colors_dict[i]}")