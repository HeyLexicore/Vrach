import cv2

text = open("Video.txt","w",encoding="utf-8")


v = cv2.VideoCapture("BadApple.flv")

fps = int(v.get(cv2.CAP_PROP_FPS))
max = int(v.get(cv2.CAP_PROP_FRAME_COUNT))
width = 25
height = 25

text.write(f'{width}\n{height}\n{fps}\n')
success = True
c = 1
for i in range(max-1):

    success, image = v.read()
    frame = ""
    try:
        image = cv2.resize(image, (width, height))
    except TypeError:
        success = False
        continue
    for k in range(height):

        for j in range(width):
            color = image[j,k]
            frame +=f"{color[0]*256*256+color[1]*256+color[2]}?"
    text.write(frame[:-1]+"\n")


    print(str(int(c / (max - 1) * 100)) + "%", str(c) + "/" + str(int(max - 1)))

    c +=1
print("Done")


