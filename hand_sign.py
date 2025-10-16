import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def recognize_gesture(hand_landmarks, handedness):

    landmarks = hand_landmarks.landmark

    wrist = landmarks[mp_hands.HandLandmark.WRIST]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks[mp_hands.HandLandmark.THUMB_MCP]

    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_pip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP]
    index_mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP]

    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    middle_pip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
    middle_mcp = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    ring_pip = landmarks[mp_hands.HandLandmark.RING_FINGER_PIP]
    ring_mcp = landmarks[mp_hands.HandLandmark.RING_FINGER_MCP]

    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    pinky_pip = landmarks[mp_hands.HandLandmark.PINKY_PIP]
    pinky_mcp = landmarks[mp_hands.HandLandmark.PINKY_MCP]

    ref_dist = np.sqrt((wrist.x - middle_mcp.x) ** 2 + (wrist.y - middle_mcp.y) ** 2)

    def is_finger_extended(tip, pip, mcp):
        return np.sqrt((tip.x - mcp.x) ** 2 + (tip.y - mcp.y) ** 2) > \
            np.sqrt((pip.x - mcp.x) ** 2 + (pip.y - mcp.y) ** 2)

    index_extended = is_finger_extended(index_tip, index_pip, index_mcp)
    middle_extended = is_finger_extended(middle_tip, middle_pip, middle_mcp)
    ring_extended = is_finger_extended(ring_tip, ring_pip, ring_mcp)
    pinky_extended = is_finger_extended(pinky_tip, pinky_pip, pinky_mcp)

    index_curled = not is_finger_extended(index_tip, index_pip, index_mcp)
    middle_curled = not is_finger_extended(middle_tip, middle_pip, middle_mcp)
    ring_curled = not is_finger_extended(ring_tip, ring_pip, ring_mcp)
    pinky_curled = not is_finger_extended(pinky_tip, pinky_pip, pinky_mcp)

    is_right_hand = handedness == "Right"
    if is_right_hand:
        thumb_extended = thumb_tip.x < thumb_ip.x
    else:  # Left hand
        thumb_extended = thumb_tip.x > thumb_ip.x

    extended_fingers_count = sum([index_extended, middle_extended, ring_extended, pinky_extended])

    thumb_index_dist = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) / ref_dist
    thumb_middle_dist = np.sqrt((thumb_tip.x - middle_tip.x) ** 2 + (thumb_tip.y - middle_tip.y) ** 2) / ref_dist
    index_middle_dist = np.sqrt((index_tip.x - middle_tip.x) ** 2 + (index_tip.y - middle_tip.y) ** 2) / ref_dist

    if extended_fingers_count == 0 and thumb_extended and thumb_tip.y > thumb_ip.y:
        if np.sqrt((thumb_tip.x - index_mcp.x) ** 2 + (thumb_tip.y - index_mcp.y) ** 2) < ref_dist * 0.4:
            return "️ ASL: A"

    if extended_fingers_count == 0 and not thumb_extended:
        if (thumb_tip.y > middle_pip.y and
                ((is_right_hand and thumb_tip.x > index_pip.x) or
                 (not is_right_hand and thumb_tip.x < index_pip.x))):
            return " ASL: S"

    if extended_fingers_count == 4 and not thumb_extended:
        return " ASL: B"

    if index_extended and middle_curled and ring_curled and pinky_curled and thumb_middle_dist < 0.2:
        return " ASL: D"

    if index_extended and thumb_extended and extended_fingers_count == 1:
        return " ASL: L"

    if middle_extended and ring_extended and pinky_extended and thumb_index_dist < 0.15:
        return "👌 OK / ASL: F"

    if index_extended and pinky_extended and thumb_extended and middle_curled and ring_curled:
        return "🤟 I Love You (ASL)"

    if index_extended and middle_extended and ring_extended and pinky_curled and thumb_index_dist > 0.3:
        return "🖐️ THREE / ASL: W"

    if index_extended and middle_extended and ring_curled and pinky_curled:
        if index_middle_dist > 0.25:
            return "✌️ PEACE / ASL: V"
        elif index_middle_dist < 0.1:
            return "🆄 ASL: U"
        elif (is_right_hand and index_tip.x > middle_tip.x) or (not is_right_hand and index_tip.x < middle_tip.x):
            return "🆁 ASL: R"
        else:
            return "🅷 ASL: H"

    if pinky_extended and thumb_extended and index_curled and middle_curled and ring_curled:
        return "🤙 CALL ME / SHAKA / ASL: Y"

    if thumb_extended and thumb_tip.y < thumb_ip.y < thumb_mcp.y and extended_fingers_count == 0:
        return "👍 THUMBS UP"

    if thumb_extended and thumb_tip.y > thumb_ip.y > thumb_mcp.y and extended_fingers_count == 0:
        return "👎 THUMBS DOWN"

    if extended_fingers_count == 4 and thumb_extended:
        return "✋ OPEN HAND / STOP / FIVE"

    if extended_fingers_count == 0 and not thumb_extended:
        return "✊ FIST"

    if index_extended and extended_fingers_count == 1:
        return "☝️ POINTING / ONE"

    if middle_extended and extended_fingers_count == 1:
        return "🖕 GIVING THE GOOSE"

    if index_extended and pinky_extended and extended_fingers_count == 2:
        return "🤘 ROCK ON"

    return " UNKNOWN GESTURE"

def decode_hand_signs():
    cap = cv2.VideoCapture(0)
    print("Hand Sign Decoder Started! Press 'q' to quit.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Failed to capture frame.")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )

                hand_label = results.multi_handedness[idx].classification[0].label
                gesture = recognize_gesture(hand_landmarks, hand_label)

                cv2.putText(
                    frame, f"{hand_label.upper()}: {gesture}",
                    (10, 30 + (idx * 40)), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2, cv2.LINE_AA
                )

        cv2.imshow('Hand Sign Decoder', frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    hands.close()


if __name__ == "__main__":
    try:
        decode_hand_signs()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nPlease make sure you have the required libraries installed:")
        print("pip install opencv-python mediapipe numpy")