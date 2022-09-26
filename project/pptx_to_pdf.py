import aspose.slides as slides
import aspose.pydrawing as drawing

pres = slides.Presentation("./media/ch12.pptx")

# Loop through slides
for index in range(pres.slides.length):
    # Get reference of slide
    slide = pres.slides[index]
    # Define custom size
    size = drawing.Size(960, 720)

    # Save as PNG
    slide.get_thumbnail(size).save("./file_thumbnail/slide_{i}.png".format(i = index), drawing.imaging.ImageFormat.png)