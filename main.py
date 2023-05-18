import cv2 as cv
from matplotlib import pyplot as plt


def canny():
    img = cv.imread("./img/silde3.png", 0)
    canny = cv.Canny(img, 150, 200)

    title = ["Original Image", "Canny"]
    images = [img, canny]

    for i in range(len(images)):
        plt.subplot(2, 2, i+1), plt.imshow(images[i], 'ocean')
        plt.title(title[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

    img_2 = cv.imread("./img/sunflower.jpg", 0)
    canny_2 = cv.Canny(img_2, 150, 200)

    title_2 = ["Original Image", "Canny"]
    images_2 = [img_2, canny_2]

    for i in range(len(images_2)):
        plt.subplot(2, 2, i+1), plt.imshow(images_2[i], 'twilight')
        plt.title(title_2[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

    img_3 = cv.imread("./img/lambo.jpg", 0)
    canny_3 = cv.Canny(img_3, 150, 200)

    title_3 = ["Original Image", "Canny"]
    images_3 = [img_3, canny_3]

    for i in range(len(images_3)):
        plt.subplot(2, 2, i+1), plt.imshow(images_3[i], 'hot')
        plt.title(title_3[i])
        plt.xticks([]), plt.yticks([])

    plt.show()




if __name__ == '__main__':
    canny()
