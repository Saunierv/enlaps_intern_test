from argparse import ArgumentParser
from datetime import datetime
import logging
from os import path
from exifread import process_file
import os
import shutil


#TODO donner le chemin des dossiers input et output
input_folder=''
output_folder=''

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
    logger.debug("Not implemented")

    return tags['EXIF DateTimeOriginal']

def list_folder(input_folder: str):
    """ List the images of a folder
    :param input_forder: The input folder path
    :return: a list of filename
    """
    fichier=[]
    fichier=os.listdir(input_folder)

    logger = logging.getLogger(__name__)
    logger.debug("Listing content of {}".format(input_folder))
    logger.debug("Not implemented")

    return fichier


images_path = list_folder(input_folder)


d=0
images_info=[]
for p in images_path :
    """print(p)"""
    if(p== '.DS_Store'):
        d+=1

    else :
        original_path= "%s%s" % (input_folder,p)
        """print(new_path)"""
        image_date=capture_date(original_path)
        """image_date.strftime=('%Y:%m:%d %H:%M:%S')""" #convertir des datetime.datetime en string
        """image_date_bis=datetime.strptime(image_date,'%Y:%m:%d %H:%M:%S')""" #convertir des string en datetime.datetime
        """print(image_date)"""
        d+=1
        tuple =(p,image_date)
        """print(tuple)"""
        images_info.append(tuple)
        """print(images_info)"""
        """print(d)""" #print le nombre d'image traitée
        """print(tuple[1])"""

        image_date=str(image_date)
        f_1,f_2=image_date.split(' ')
        year,month,date=f_1.split(':')
        hour,minute,second=f_2.split(':')
        new_name= "%s%s%s%s%s%s%s%s%s%s%s" % (year,'-',month,'-',date,'_',hour,'-',minute,'-',second)   #output/2020-01-23_10-11-59.jpg
        """print(new_name)"""
        new_path= "%s%s%s" % (input_folder,new_name,'.jpg')
        """print(new_path)"""
        shutil.copy(original_path,new_path)
        shutil.move(new_path,output_folder)







