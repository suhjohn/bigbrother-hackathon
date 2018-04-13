from io import BytesIO

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
        return_value, img_arr = cls.camera.read()
        img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img_arr)

        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        imgstr = buffered.getvalue()
        return imgstr

    def dispatch_to_rekognition(self, imgstr: bytes):
        client = boto3.client('rekognition', 'us-west-2')
        response = client.search_faces_by_image(
            CollectionId='BigBrotherCollection',
            Image={'Bytes': imgstr}
        )

        return response

    def get_name(self, response):
        """
        {
            'FaceMatches': [
                {'Face': {'BoundingBox': {'Height': 0.6000000238418579,
                                           'Left': 0.14000000059604645,
                                           'Top': 0.23874999582767487,
                                           'Width': 0.800000011920929},
                           'Confidence': 99.9966049194336,
                           'ExternalImageId': 'john',
                           'FaceId': '6a616b4f-318b-45a4-bfd9-7bc913cb96bf',
                           'ImageId': '4590573f-f356-5032-ba8d-98d76f0be676'},
                  'Similarity': 98.7904281616211}
                  ],
            'SearchedFaceConfidence': 99.99746704101562}
        :param response:
        :return:
        """
        face_matches = response.get("FaceMatches")
        if not face_matches:
            return None
        face = face_matches[0]
        name = face["Face"]["ExternalImageId"]
        return name


if __name__ == "__main__":
    photosnapper = PhotoSnapper()
    img_str = photosnapper.snap()
    photosnapper.dispatch_to_rekognition(img_str)
