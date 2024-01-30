import cv2
import numpy as np

# Inițializarea variabilelor globale
puncte = []  # Lista pentru a stoca punctele selectate
imagine_contururi = None  # Variabila pentru a stoca imaginea cu contururi
scala_imagine = 0.2
def click_event(event, x, y, flags, param):
    global puncte, imagine_contururi
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(puncte) < 2:  # Asigurăm că adăugăm doar două puncte
            puncte.append((x, y))
            cv2.circle(imagine_contururi, (x, y), 5, (0, 255, 0), -1)
            if len(puncte) == 2:
                cv2.line(imagine_contururi, puncte[0], puncte[1], (255, 0, 0), 2)
                distanta = np.linalg.norm(np.array(puncte[0]) - np.array(puncte[1]))
                #print("Distanta:", distanta)
                distanta_mm = distanta * scala_imagine
                print("Distanta:", distanta_mm, "mm")
                puncte.clear()  # Resetăm lista de puncte pentru noi măsurători
            cv2.imshow("Imagine cu Contururi Sobel", imagine_contururi)

def detectare_margini_sobel(imagine_gri):
    grad_x = cv2.Sobel(imagine_gri, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(imagine_gri, cv2.CV_64F, 0, 1, ksize=3)
    magnitudine = np.sqrt(grad_x**2 + grad_y**2)
    magnitudine = cv2.convertScaleAbs(magnitudine)
    return magnitudine

def calculare_dimensiune(path_imagine):
    global imagine_contururi
    imagine_gri = cv2.imread(path_imagine, 0)
    imagine_contururi = detectare_margini_sobel(imagine_gri)
    cv2.imshow("Imagine cu Contururi Sobel", imagine_contururi)
    cv2.setMouseCallback("Imagine cu Contururi Sobel", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

calculare_dimensiune('heart.png')