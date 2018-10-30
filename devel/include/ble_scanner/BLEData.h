// Generated by gencpp from file ble_scanner/BLEData.msg
// DO NOT EDIT!


#ifndef BLE_SCANNER_MESSAGE_BLEDATA_H
#define BLE_SCANNER_MESSAGE_BLEDATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <ble_scanner/BLEBeacon.h>

namespace ble_scanner
{
template <class ContainerAllocator>
struct BLEData_
{
  typedef BLEData_<ContainerAllocator> Type;

  BLEData_()
    : header()
    , data()  {
    }
  BLEData_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::ble_scanner::BLEBeacon_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::ble_scanner::BLEBeacon_<ContainerAllocator> >::other >  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::ble_scanner::BLEData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ble_scanner::BLEData_<ContainerAllocator> const> ConstPtr;

}; // struct BLEData_

typedef ::ble_scanner::BLEData_<std::allocator<void> > BLEData;

typedef boost::shared_ptr< ::ble_scanner::BLEData > BLEDataPtr;
typedef boost::shared_ptr< ::ble_scanner::BLEData const> BLEDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ble_scanner::BLEData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ble_scanner::BLEData_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ble_scanner

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'ble_scanner': ['/home/peter/ble_ws/src/ble_scanner/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ble_scanner::BLEData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ble_scanner::BLEData_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ble_scanner::BLEData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ble_scanner::BLEData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ble_scanner::BLEData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ble_scanner::BLEData_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ble_scanner::BLEData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c29e26215bed4fe2e33bea8e9a9a6399";
  }

  static const char* value(const ::ble_scanner::BLEData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc29e26215bed4fe2ULL;
  static const uint64_t static_value2 = 0xe33bea8e9a9a6399ULL;
};

template<class ContainerAllocator>
struct DataType< ::ble_scanner::BLEData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ble_scanner/BLEData";
  }

  static const char* value(const ::ble_scanner::BLEData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ble_scanner::BLEData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header       # timestamp\n\
BLEBeacon[] data  # BLE data of all beacons\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: ble_scanner/BLEBeacon\n\
string mac_address # MAC address of an access point\n\
int16 rssi         # signal strength [RSSI]\n\
";
  }

  static const char* value(const ::ble_scanner::BLEData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ble_scanner::BLEData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BLEData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ble_scanner::BLEData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ble_scanner::BLEData_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::ble_scanner::BLEBeacon_<ContainerAllocator> >::stream(s, indent + "    ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // BLE_SCANNER_MESSAGE_BLEDATA_H
