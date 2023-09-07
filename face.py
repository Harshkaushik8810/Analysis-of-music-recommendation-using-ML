from webcam import capture_image

def recog():
    import cv2
    import matplotlib.pyplot as plt
    from deepface import DeepFace
    a=capture_image()
    img = cv2.imread(a)
    
    # call imshow() using plt object

    # storing the result
    result = DeepFace.analyze(img,actions=['emotion'])
    # print result
    l=[]
    for i in (result[0].values()):
        l.append(i)
    return(l[1])

# emotion'='angry','happy', 'sad', 'surprise','neutral'



