import os
import glob

image_width = 384
image_height = 288

CAVIAR_TRAIN_DATA_SET_PATH = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/train/labels'
CAVIAR_TRAIN_DATA_SET_PATH1 = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/train/labels1'
CAVIAR_TEST_DATA_SET_PATH = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/test/labels'
CAVIAR_TEST_DATA_SET_PATH1 = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/test/labels1'
CAVIAR_VALIDATION_DATA_SET_PATH = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/val/labels'
CAVIAR_VALIDATION_DATA_SET_PATH1 = '/media/samx/WORK/NEW/CAVIAR_DATA_SET/val/labels1'

ANNOTATION_FOLDERS = []
ANNOTATION_FOLDERS.append(CAVIAR_TRAIN_DATA_SET_PATH)
ANNOTATION_FOLDERS.append(CAVIAR_TEST_DATA_SET_PATH)
ANNOTATION_FOLDERS.append(CAVIAR_VALIDATION_DATA_SET_PATH)

TRANSFORMATION_FOLDERS = []
TRANSFORMATION_FOLDERS.append(CAVIAR_TRAIN_DATA_SET_PATH1)
TRANSFORMATION_FOLDERS.append(CAVIAR_TEST_DATA_SET_PATH1)
TRANSFORMATION_FOLDERS.append(CAVIAR_VALIDATION_DATA_SET_PATH1)

def safe_division(x, y):
    if y == 0:
        return 0
    return round(x / y, 4)
def normalize_annotations():

    COUNT = 0
    for ANNOTATION_FOLDER in ANNOTATION_FOLDERS:
        TRANSFORMATION_FOLDER = TRANSFORMATION_FOLDERS[COUNT]
        COUNT = COUNT + 1
        os.chdir(ANNOTATION_FOLDER)
        file_list = os.listdir(ANNOTATION_FOLDER)
        file_list.sort()
        for file in file_list:
            with open(file) as f:
                result = []
                lines = f.read().splitlines()
                for line in lines:
                    bbox_string = ""
                    yolo_bboxes = []
                    elements = line.split(' ')
                    class_value = elements[0]
                    xc = safe_division(int(elements[1]), image_width)
                    yc = safe_division(int(elements[2]), image_height)
                    w = safe_division(int(elements[3]), image_width)
                    h = safe_division(int(elements[4]), image_height)
                    yolo_bboxes.append(class_value)
                    yolo_bboxes.append(str(xc))
                    yolo_bboxes.append(str(yc))
                    yolo_bboxes.append(str(w))
                    yolo_bboxes.append(str(h))
                    bbox_string = " ".join([str(x) for x in yolo_bboxes])
                    result.append(bbox_string)

            # Write YOLO TXT
            if result:
                with open(os.path.join(TRANSFORMATION_FOLDER, file), "w", encoding="utf-8") as f:
                    f.write("\n".join(result))

if __name__ == '__main__':
    normalize_annotations()
