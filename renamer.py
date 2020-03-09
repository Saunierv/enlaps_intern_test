from argparse import ArgumentParser
from datetime import datetime
import logging
from os import path


FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(levelname)8s : %(message)s"
logging.basicConfig(level="DEBUG", format=FORMAT)

def capture_date(image_path: str) -> datetime:
    """ Extract the capture date of an image file.

    Capture date refers to the DateTimeOriginal filed in the Exif data of the image file.

    :param image_path: Path to an image file
    :return: a datetime object
    """

    #TODO
    cap_date = datetime.now()
    logger = logging.getLogger(__name__)
    logger.debug("Not implemented")

    return cap_date

def list_folder(input_folder: str):
    """ List the images of a folder
    :param input_forder: The input folder path
    :return: a list of filename
    """

    # TODO
    logger = logging.getLogger(__name__)
    logger.debug("Listing content of {}".format(input_folder))
    logger.debug("Not implemented")

    return []

if __name__=="__main__":
    logger = logging.getLogger(__name__)
    parser = ArgumentParser(description="Image renamer tool")
    parser.add_argument('input_folder', help="Input folder containing images.")
    parser.add_argument('output_folder', help="Output folder for renamed images.")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    logger.info("Listing image files from {}:".format(input_folder))

    # Liste images
    images_path = list_folder(input_folder)

    # Associate image path to capture date in a list of tuples
    images_info = [(p, capture_date(p)) for p in images_path]

    # print extracted dates
    for p,d in images_info:
        logger.debug("{} has been shot on {}".format(p,d.strftime('%Y-%m-%d %H:%M:%S')))

    #  Copy original files to destination folder with new name
    for p,d in images_info:
        original_path = path.join(input_folder,p)
        # Create new name forimages
        destination_path = p # FIXME
        try:
            logger.debug("copy {} to {}...".format(original_path, destination_path))
            # TODO
            raise NotImplementedError("please implement me!")
        except Exception as e:
            logger.error("{} caught : '{}', continuing nonetheless".format(e.__class__.__name__, e))
