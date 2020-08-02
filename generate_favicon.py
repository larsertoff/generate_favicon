import os
from PIL import Image
import pilkit.processors

class GenerateFavicon():
    '''
    Class that takes a png and saves .ico(s)
    '''

    def __init__(self):
        self.cwd = os.getcwd()
        self.icon_sizes = [
    		["favicon16", (16, 16)],
            ["favicon32", (32, 32)],
		    ["favicon64", (64, 64)],
		    ["favicon128", (128, 128)],
		    ["favicon255", (255, 255)]]

    def convert_png_to_ico(self, filepath: str):
        '''
        Takes a filepath (str) including image file name,
        appends it to the current working directory
        where .ico files (faviconXX.ico) are saved
        the sizes are defined in the icon_sizes attributes.
        '''

        file_path = os.path.join(self.cwd, filepath)

        if os.path.exists(file_path):
            for size in self.icon_sizes:
                image = Image.open(filepath)
                # Resize image
                processor = pilkit.processors.ProcessorPipeline([pilkit.processors.ResizeToFit(size[1][0], size[1][1])])
                result = processor.process(image)
                background = Image.new('RGBA', size[1], (255, 255, 255, 0))
                background.paste(result, (int((size[1][0] - result.size[0]) / 2), int((size[1][1] - result.size[1]) / 2)))
                background.save(size[0] + ".ico")

            return 'Favicon generated!'
        else:
            return 'The path: ' + file_path + ' does not exist'






