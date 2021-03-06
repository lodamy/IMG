import dicom
import matplotlib.pyplot as plt
import skimage.exposure
import skimage.io

from get_filename import getFileName

class convertDicomTojpg():
    def __init__(self):
        pass

    def vis_KP(self, im, pts):
        fig, ax = plt.subplots()
        ax.imshow(im, cmap='gray')
        ax.scatter(round(pts[0][0]), round(pts[0][1]), c='red')
        ax.scatter(round(pts[0][2]), round(pts[0][3]), c='green')
        ax.scatter(round(pts[0][4]), round(pts[0][5]), c='yellow')
        ax.scatter(round(pts[0][6]), round(pts[0][7]), c='white')
        ax.scatter(round(pts[0][8]), round(pts[0][9]), c='magenta')
        ax.scatter(round(pts[0][10]), round(pts[0][11]), c='cyan')
        plt.axis('on')
        plt.tight_layout()
        plt.draw()

    def imgnorm(self, img):
        img_norm = skimage.exposure.rescale_intensity(img)
        return img_norm

    def load_dcm(self, file_path):
        data_dicom = dicom.read_file(file_path)._get_pixel_array()
        return data_dicom

    def convert(self, dcmFile):
        dmc = self.load_dcm(dcmFile)
        img = self.imgnorm(dmc)
        get = getFileName()
        name = get.getName(dcmFile, '/')
        saveName = 'H:/code/medicalUI/imgs/convertImg/{}.jpg'.format(name)
        skimage.io.imsave(saveName, img)
        return saveName

if __name__ == '__main__':
    cdj = convertDicomTojpg()

    dmcFile = 'H:\code\medicalUI\imgs\dicom\9000099.dcm'
    dmc = cdj.load_dcm(dmcFile)
    img = cdj.imgnorm(dmc)

    get = getFileName()
    name = get.getName(dmcFile, '\\')

    saveName = 'H:\code\medicalUI\imgs\convertImg\{}.jpg'.format(name)
    print(saveName)
    skimage.io.imsave(saveName, img)