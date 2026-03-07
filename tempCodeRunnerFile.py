
            cv2.circle(frame,(x1,y1),8,(0,255,0),-1)
            cv2.circle(frame,(x2,y2),8,(0,255,0),-1)
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),2)

            cv2.putText(frame,f"Distance: {int(distance)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
            cv2.putText(frame,f"Gestures: {gesture}",(20,80),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255),2)
    cv2.imshow("Gesture Detection",frame)
    key=cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break
cap.release()
cv2.destroyAllWindows()
