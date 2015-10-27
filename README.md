# TSSSF Card Resizer

Just a little utility that helps with resizing the full sized shipfic cards down to the thumbnail sized images that are used for the [TSSSF Card Database](http://tsssf.cards/)

## Using

This project runs on Python 2.7 and requires the PIL library to be installed. You can install this by running the following command

```
[sudo] pip install Pillow
```

This script assumes that the full size images are in the folder that the script is being run from and the images to output are to be outputted into a folder called thumb that is in the parent folder.

Resized images will be outputted with the same name

This can be changed by using the -i and -o arguments

```
python Card_Resizer.py -i {input_folder} -o {output_folder}
```


## Notes

This project utilizes the excellent PIL_Helper library that HorriblePeople wrote as part of their CardMachine project. Kudos to them for making it.
