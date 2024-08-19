from nudenet import NudeDetector


def get_nude_net(img):
    nude_detector = NudeDetector()
    result = nude_detector.detect(img)
    # print(result)
    return result

