import cv2

# 將haarcascade_frontalface_default.xml的檔案位置放在cascPath
cascPath = "C:\\users\\bread\\AppData\\Roaming\\Python\\Python37\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascPath) #告訴OpenCV使用人臉辨識分類器

img = cv2.imread('D:\\jupyter\\Image.jpg')  #讀取圖檔
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #將圖片轉成灰階影像(加快檢測速度)

#偵測臉部
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor = 1.08,     #每次搜尋方塊漸少的比例
    minNeighbors = 10,       #每個目標至少檢測10次以上，才被認為人臉存在
    minSize = (30, 30))     #設定數據搜尋的最小尺寸

# 繪製人臉的方框
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #(0, 0, 255)欄位可以改變方框顏色(Blue,Green,Red)
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
cv2.imshow('img', img)  #顯示圖片
cv2.imwrite("D:\\jupyter\\images.jpg", img)  #保存圖片
cv2.waitKey(0)  #等待按下任一按鍵
cv2.destroyAllWindows() #關閉視窗
