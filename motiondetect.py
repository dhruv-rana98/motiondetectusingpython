import cv2

video = cv2.VideoCapture(0)
first_frame = None
a = 0

while True:
    a = a+1
    check, frame = video.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)             #covert to color by using cvtColor method
    #convert to gausian blur to increase efficiency

    gray_gauss = cv2.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray_gauss)
    threshold_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold_delta, None, iterations=2)
    cnts, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        #to draw a rectangle if contour is > 1000
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)    #the parameter use a follows(the frame u want to use to display, top left coordinated, bottom right coordinates, color of the rectangle , width of the border of rectangel )
    cv2.imshow("GrayFrame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", threshold_delta)
    cv2.imshow("COlor Frame final", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
