from argparse import ArgumentParser
from datetime import datetime
import logging
from os import path
from exifread import process_file
import os
import shutil

"""input_folder='/Users/Saunier/Desktop/enlaps_intern_test-master/dataset'
   output_folder='/Users/Saunier/Desktop/enlaps_intern_test-master/renamed_images' """


FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(levelname)8s : %(message)s"
logging.basicConfig(level="DEBUG", format=FORMAT)

def capture_date(image_path: str) -> datetime:
    """ Extract the capture date of an image file.

    Capture date refers to the DateTimeOriginal filed in the Exif data of the image file.

    :param image_path: Path to an image file
    :return: a datetime object
    """
    im = open(image_path, 'rb')
    tags = process_file(im)

    cap_date = datetime.now()
    logger = logging.getLogger(__name__)

    return datetime.strptime(str(tags.get('EXIF DateTimeOriginal')),'%Y:%m:%d %H:%M:%S')

def list_folder(input_folder: str):
    """ List the images of a folder
    :param input_forder: The input folder path
    :return: a list of filename
    """
    fichier=[]
    fichier=os.listdir(input_folder)

    logger = logging.getLogger(__name__)
    logger.debug("Listing content of {}".format(input_folder))

    return fichier



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
    """images_info = [(p, capture_date(p)) for p in images_path]"""

    images_info=[]
    nbr_image_traitee=0
    for p in images_path : #Changement de code car probleme avec la formule de images_info précédente et notamment capture_date(p)
        if(p== '.DS_Store'): #Gestion d'erreur
            nbr_image_traitee+=1

        else :
            original_path= "%s%s" % (input_folder,p)
            image_date=capture_date(original_path)
            tuple =(p,image_date)
            images_info.append(tuple)
            nbr_image_traitee+=1

    """print(nbr_image_traitee)""" #Pour savoir combien d'image ont été traité


    # print extracted dates
    for p,d in (images_info) :
        logger.debug("{} has been shot on {}".format(p,d.strftime('%Y-%m-%d %H:%M:%S')))

    #  Copy original files to destination folder with new name
    for p,d in images_info:
        original_path = path.join(input_folder,p)
        # Create new name forimages
        destination_path = output_folder
        try:
            logger.debug("copy {} to {}...".format(original_path, destination_path))
            image_date=capture_date(original_path)
            image_date=str(image_date)  #Sinon problème de type

            """f_1,f_2=image_date.split(' ')
            year,month,date=f_1.split(':')
            hour,minute,second=f_2.split(':')
            new_name= "%s%s%s%s%s%s%s%s%s%s%s" % (year,'-',month,'-',date,'_',hour,'-',minute,'-',second)""" #Cette partie marche avec test.py

            new_path= "%s%s%s" % (input_folder,image_date,'.jpg') #Changer image_date par new_name pour donner le nom approprié (output/2020-01-23_10-11-59.jpg)
            shutil.copy(original_path,new_path)   #On copie l'image pour ne pas modifier l'originale
            shutil.move(new_path,destination_path)  #On la déplace vers le dossier que l'on souhaite

            raise NotImplementedError("please implement me!")
        except Exception as e:
            logger.error("{} caught : '{}', continuing nonetheless".format(e.__class__.__name__, e))
