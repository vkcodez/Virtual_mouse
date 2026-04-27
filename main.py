import cv2
import pyautogui
import math
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing

# Setup
cap = cv2.VideoCapture(0)
detector = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
sw, sh = pyautogui.size()

while True:
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = detector.process(rgb_frame)
    
    if res.multi_hand_landmarks:
        for landmarks in res.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            pts = landmarks.landmark
            
            # Get pixel coordinates for tips
            # Thumb: 4, Index: 8, Middle: 12, Ring: 16, Pinky: 20
            def get_coords(id):
                return int(pts[id].x * w), int(pts[id].y * h)

            t_x, t_y = get_coords(4)
            i_x, i_y = get_coords(8)
            m_x, m_y = get_coords(12)
            r_x, r_y = get_coords(16)
            p_x, p_y = get_coords(20)

            # 1. MOVEMENT (Index)
            pyautogui.moveTo(sw/w*i_x, sh/h*i_y, _pause=False)

            # 2. LEFT CLICK (Index + Thumb)
            if math.hypot(i_x-t_x, i_y-t_y) < 30:
                pyautogui.click()
                pyautogui.sleep(0.1)

            # 3. RIGHT CLICK (Index + Middle)
            if math.hypot(i_x-m_x, i_y-m_y) < 30:
                pyautogui.right_Click()
                pyautogui.sleep(0.2)

            # 4. SCROLL UP (Middle + Ring)
            if math.hypot(m_x-r_x, m_y-r_y) < 30:
                pyautogui.scroll(100)

            # 5. SCROLL DOWN (Ring + Pinky)
            if math.hypot(r_x-p_x, r_y-p_y) < 30:
                pyautogui.scroll(-100)

    cv2.imshow("Virtual Mouse Controller", frame)
    
    # 3. HOW TO STOP
    # Option A: Press ESC on the keyboard
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()