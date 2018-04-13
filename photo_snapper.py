import boto3
import cv2
from PIL import Image
from past.builtins import raw_input

class PhotoSnapper:
    camera = cv2.VideoCapture(0)

    @classmethod
    def snap(cls):
        """

        :return:
        """
        raw_input('Press Enter to capture')
        return_value, image = cls.camera.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image)
        return img.tobytes()

    def dispatch_to_rekognition(self, imgstr: bytes):
        client = boto3.client('rekognition', 'us-west-2')
        response = client.search_faces_by_image(
            CollectionId='BigBrotherCollection',
            Image={'Bytes': imgstr}
        )

        return response


if __name__ == "__main__":
    photosnapper = PhotoSnapper()
    img_str = photosnapper.snap()
    photosnapper.dispatch_to_rekognition(img_str)
