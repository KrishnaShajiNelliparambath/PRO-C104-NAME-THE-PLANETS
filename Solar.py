import cv2

img=cv2.imread("C:/Users/Admin/Desktop/C Pro/PRO-104-Project-Image-main/solar-system.jpg")
text="Sun"

cv2.putText(img,
            "Sun",
            (100,100),
            cv2.FONT_HERSHEY_COMPLEX, 
            1.5,
            (0,0,255)
            )

cv2.putText(img,
            "Mercury",
            (120,190),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (128 ,128,128)
            )

cv2.putText(img,
            "Venus",
            (200,170),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Earth",
            (280,260),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,0)
            )

cv2.putText(img,
            "Moon",
            (320,160),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.3,
            (128 ,128,128)
            )

cv2.putText(img,
            "Mars",
            (390,170),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (0,0,120)
            )

cv2.putText(img,
            "Jupiter",
            (450,100),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (128 ,128,128)
            )

cv2.putText(img,
            "Saturn",
            (750,130),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (128 ,128,128)
            )

cv2.putText(img,
            "Uranus",
            (950,140),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,255,0)
            )

cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX, 
            0.5,
            (255,0,0)
            )


cv2.imshow("Ouput:",img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
