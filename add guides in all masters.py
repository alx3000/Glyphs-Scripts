# add guides in all masters

font = Glyphs.font
mylayer = font.selectedLayers[0]
glyph = mylayer.parent

for layer in glyph.layers:
	print(layer.name, layer.guides)

for selectedGuide in mylayer.guides:
	if selectedGuide.selected == True:
		for layer in glyph.layers:
			if layer == mylayer:
				continue
			newGuide = selectedGuide.copy()
			layer.guides.append(newGuide)