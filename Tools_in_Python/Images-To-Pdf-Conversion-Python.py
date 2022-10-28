from PIL import Image

def Images_Pdf(filename, output):
    images = []
    
    for file in filename:
        im = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
        
        images[0].save(output, save_all=True, append_images=images[1:])
        
# Image Path, output pdf
Images_Pdf(["binod_mirror.png", "binod.png", "binod.jpg"], "ouput.pdf")