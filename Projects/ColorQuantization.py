import numpy
import numpy as np
import cv2
from sklearn.cluster import KMeans

def process(image_path: str, k:int = 8):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clustered = KMeans(n_clusters=k)
    labels = clustered.fit_predict(image)
    quanted = clustered.cluster_centers_.astype("uint8")[labels]

    quanted = quanted.reshape((h, w, 3))
    quanted = cv2.cvtColor(quanted, cv2.COLOR_LAB2BGR)

    image = image.reshape((h, w, 3))
    image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

    return quanted


def compare(image_path: str, k:int = 8):
    image = cv2.imread(image_path)
    h, w = image.shape[:2]

    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clustered = KMeans(n_clusters=k)
    labels = clustered.fit_predict(image)
    quanted = clustered.cluster_centers_.astype("uint8")[labels]

    quanted = quanted.reshape((h, w, 3))
    quanted = cv2.cvtColor(quanted, cv2.COLOR_LAB2BGR)

    image = image.reshape((h, w, 3))
    image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

    return numpy.hstack((image, quanted))


filename = input('Please provide filename:\n')
k = int(input("Provide k value: "))
quantified_image = process(filename, k)

cv2.imshow('Finished!', quantified_image)
cv2.waitKey(0)