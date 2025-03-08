import cv2
def captureImage():
    camera_name = 0
    vedioCapture = cv2.VideoCapture(camera_name)
    
    num_images = 500
    file_path = "/media/prethiviraj/R'kived Lab/Projects/2025/Computer vision/images_prethivi/"
    
    for i in range(num_images):
        success,frame = vedioCapture.read()
    
        if success == True:
            file_name = f'{file_path}image_file{i}.jpg'
            cv2.imwrite(file_name,frame)
            cv2.waitKey(0)
                
    
    vedioCapture.release()

cv2.destroyAllWindows()


def main():
    captureImage()
    
    
if __name__ == '__main__':
    main()

        
    
    
    