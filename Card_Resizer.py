import os, glob
import PIL_Helper
import argparse

VASSAL_SCALE=(260,359)

def main(input_folder=".", output_folder="../thumb"):
    CleanDirectory(output_folder, "", "*.*")
    for image_file in glob.glob(os.path.join(input_folder, '*.png')):
        image_filename = os.path.basename(image_file)
        # print("Current file: {}").format(image_file)

        print("Resizing Image: {}").format(image_filename)
        image = PIL_Helper.LoadImage(image_file)
        image_thumb = PIL_Helper.ResizeImage(image, VASSAL_SCALE)
        SaveCard(os.path.join(output_folder, image_filename), image_thumb)

def SaveCard(filepath, image, scale=1, convert_to_cmyk=False):
    '''
    If the filepath already exists, insert _001 just before the
    extension. If that exists, increment the number until we get to
    a filepath that doesn't exist yet.
    '''
    if os.path.exists(filepath):
        basepath, extension = os.path.splitext(filepath)
        i = 0
        while os.path.exists(filepath):
            i += 1
            filepath = "{}_{:>03}{}".format(basepath, i, extension)
    w,h = image.size
    new_w = int(scale*w)
    new_h = int(scale*h)
    image = PIL_Helper.ResizeImage(image, (new_w, new_h))
    if convert_to_cmyk:
        PIL_Helper.ConvertToCmyk(image)
    image.save(filepath, dpi=(300,300))

def Delete(filename):
    filelist = glob.glob(filename)
    for f in filelist:
        os.remove(f)

def CleanDirectory(path=".", mkdir="workspace", rmstring="*.*"):
    dir_path = os.path.join(path, mkdir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        Delete(os.path.join(dir_path, rmstring))
    return dir_path

if __name__ == '__main__':
    # To run this script, you have two options:
    # 1) Run it from the command line with arguments. E.g.:
    #       python GameGen -b TSSSF -f "Core 1.0.3/cards.pon"
    # 2) Comment out "main(args.basedir, args.set_file)" in this file
    #       and add a new line with the proper folder and card set
    #       in the arguments.
    # See the main() docstring for more info on the use of the arguments
    parser = argparse.ArgumentParser(prog="GameGen")

    parser.add_argument('-i', '--input-folder', \
                        help="Location of folder of images to be parsed",
                        default=".")
    parser.add_argument('-o', '--output-folder',
                        help="Location of output folder to stored resized images",
                        default="../thumb")

    args = parser.parse_args()

    main(args.input_folder, args.output_folder)
