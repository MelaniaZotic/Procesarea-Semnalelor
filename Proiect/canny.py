import cv2
import numpy as np

# Inițializarea variabilelor globale
puncte = []  # Lista pentru a stoca punctele selectate
imagine = None  # Variabila pentru a stoca imaginea
scala_imagine = 0.2
def click_event(event, x, y, flags, param):
    global puncte, imagine
    if event == cv2.EVENT_LBUTTONDOWN:
        puncte.append((x, y))
        cv2.circle(imagine, (x, y), 5, (0, 255, 0), -1)
        if len(puncte) == 2:
            cv2.line(imagine, puncte[0], puncte[1], (255, 0, 0), 2)
            distanta = np.linalg.norm(np.array(puncte[0]) - np.array(puncte[1]))
            #print("Distanta:", distanta)
            distanta_mm = distanta * scala_imagine
            print("Distanta:", distanta_mm, "mm")
        cv2.imshow("Imagine cu Contururi", imagine)

def detectare_margini_canny(imagine):
    gray = cv2.cvtColor(imagine, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 100, 200)
    return canny


def calculare_dimensiune(path_imagine):
    global imagine
    imagine_originala = cv2.imread(path_imagine)
    imagine = detectare_margini_canny(imagine_originala)
    cv2.imshow("Imagine cu Contururi", imagine)
    cv2.setMouseCallback("Imagine cu Contururi", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Apelarea funcției
calculare_dimensiune('heart.png')