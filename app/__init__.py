from imutils.video import VideoStream
from imutils.video import FPS
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import time
import cv2
import pytesseract
import re

# Width and Height must be multiples of 32
width, height = 320, 320
# Probability threshold to determine text
probability = 0.9

(W, H) = (None, None)
(newW, newH) = (width, height)
(rW, rH) = (None, None)

# Loading pretrained EAST text detector
layerNames = [
    "feature_fusion/Conv_7/Sigmoid",
    "feature_fusion/concat_3"]

net = cv2.dnn.readNet("frozen_east_text_detection.pb")
fps = FPS().start()


# Extracts bounding box coordinates for a region of text
# Defines probability of text being detected
def _decode_predictions(score, geo):
    (numRows, numCols) = score.shape[2:4]
    rectangle = []
    conf = []

    for y in range(0, numRows):
        scoresData = score[0, 0, y]
        xData0 = geo[0, 0, y]
        xData1 = geo[0, 1, y]
        xData2 = geo[0, 2, y]
        xData3 = geo[0, 3, y]
        anglesData = geo[0, 4, y]

        for x in range(0, numCols):
            if scoresData[x] < probability:
                continue

            (offsetX, offsetY) = (x * 4.0, y * 4.0)

            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            Ex = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            Ey = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            sX = int(Ex - w)
            sY = int(Ey - h)

            rectangle.append((sX, sY, Ex, Ey))
            conf.append(scoresData[x])

    return rectangle, conf


def _text_recognition_by_region(region):
    text = pytesseract.image_to_string(region)

    # Text is filtered using a Regex
    text = re.sub('[^a-zA-Z]+', '', text)

    # Conditional to detect whether the text not empty,
    # is longer than two and less than 9 characters long
    if text != "" and 2 < len(text) < 9:
        mWidth, mHeight = 600, 600

        # Create second frame to output results
        message = np.zeros((mWidth, mHeight, 3), np.uint8)
        message[:, 0:mWidth] = (255, 255, 255)
        message = cv2.putText(message, 'Text detected:', (100, 150)
                              , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        message = cv2.putText(message, text, (200, 400)
                              , cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Result", message)
    return None


def _detect_text(vs, frameWidth, frameHeight, ratioWidth, ratioHeight):
    while True:
        frame = vs.read()

        # Resize frame, maintaining aspect ratio
        frame = imutils.resize(frame, width=1000)
        orig = frame.copy()

        # If frame dimensions are None, we must still compute the
        # ratio of old frame dimensions to new ones.
        if frameWidth is None or frameHeight is None:
            (frameHeight, frameWidth) = frame.shape[:2]
            ratioWidth = frameWidth / float(newW)
            ratioHeight = frameHeight / float(newH)

        frame = cv2.resize(frame, (newW, newH))

        # Create a blob from the frame, perform a forward pass to the model
        # and obtain two output layer sets
        blob = cv2.dnn.blobFromImage(frame, 1.0, (newW, newH),
                                     (123.68, 116.78, 103.94), swapRB=True, crop=False)
        net.setInput(blob)
        (scores, geometry) = net.forward(layerNames)

        # Decode the predictions
        (rects, confidences) = _decode_predictions(scores, geometry)

        # Suppress the weak, overlapping bounding boxes
        boxes = non_max_suppression(np.array(rects), probs=confidences)
        for (startX, startY, endX, endY) in boxes:

            # Create a Region of Interest to decode the text
            roi = frame[startY - 15:endY + 15, startX - 15:endX + 15]

            if roi is not None:
                _text_recognition_by_region(roi)

            # Creates the bounding boxes around detected text
            startX = int(startX * ratioWidth)
            startY = int(startY * ratioHeight)
            endX = int(endX * ratioWidth)
            endY = int(endY * ratioHeight)
            cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)

        fps.update()
        cv2.imshow("Text Detection", orig)
        # Awaits user input 'q' to end the program
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break


def launch_app(path: str):
    pytesseract.pytesseract.tesseract_cmd = path

    # Preparing video stream
    videoStream = VideoStream(src=0).start()
    time.sleep(1.0)

    _detect_text(videoStream, W, H, rW, rH)

    fps.stop()
    videoStream.stop()
    cv2.destroyAllWindows()
