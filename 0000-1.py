__author__ = 'vovo'

import Image
import PSDraw

im = Image.open("/home/vovo/show-me-the-code/show-me-the-code/2.png")
title = "12"
box = (1*72, 2*72, 7*72, 10*72)

ps = PSDraw.PSDraw()
ps.begin_document(title)

ps.image(box,im,75)
ps.rectangle(box)

ps.setfont("HelveticaNarrow-Bold", 36)
w, h, b = ps.textsize(title)
ps.text((4*72-w/2, 1*72-h), title)
ps.end_document()