;; Auto-generated. Do not edit!


(when (boundp 'ble_scanner::BLEBeacon)
  (if (not (find-package "BLE_SCANNER"))
    (make-package "BLE_SCANNER"))
  (shadow 'BLEBeacon (find-package "BLE_SCANNER")))
(unless (find-package "BLE_SCANNER::BLEBEACON")
  (make-package "BLE_SCANNER::BLEBEACON"))

(in-package "ROS")
;;//! \htmlinclude BLEBeacon.msg.html


(defclass ble_scanner::BLEBeacon
  :super ros::object
  :slots (_mac_address _rssi ))

(defmethod ble_scanner::BLEBeacon
  (:init
   (&key
    ((:mac_address __mac_address) "")
    ((:rssi __rssi) 0)
    )
   (send-super :init)
   (setq _mac_address (string __mac_address))
   (setq _rssi (round __rssi))
   self)
  (:mac_address
   (&optional __mac_address)
   (if __mac_address (setq _mac_address __mac_address)) _mac_address)
  (:rssi
   (&optional __rssi)
   (if __rssi (setq _rssi __rssi)) _rssi)
  (:serialization-length
   ()
   (+
    ;; string _mac_address
    4 (length _mac_address)
    ;; int16 _rssi
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _mac_address
       (write-long (length _mac_address) s) (princ _mac_address s)
     ;; int16 _rssi
       (write-word _rssi s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _mac_address
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _mac_address (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int16 _rssi
     (setq _rssi (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get ble_scanner::BLEBeacon :md5sum-) "b767afad314b67e2e2c82e2bb477f1fe")
(setf (get ble_scanner::BLEBeacon :datatype-) "ble_scanner/BLEBeacon")
(setf (get ble_scanner::BLEBeacon :definition-)
      "string mac_address # MAC address of an access point
int16 rssi         # signal strength [RSSI]

")



(provide :ble_scanner/BLEBeacon "b767afad314b67e2e2c82e2bb477f1fe")


