# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rPose_pkg: 2 messages, 0 services")

set(MSG_I_FLAGS "-IrPose_pkg:/home/zyh/p3p-ros/src/rPose_pkg/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rPose_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_custom_target(_rPose_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rPose_pkg" "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" ""
)

get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_custom_target(_rPose_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rPose_pkg" "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" "rPose_pkg/BoundingBox:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rPose_pkg
)
_generate_msg_cpp(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rPose_pkg
)

### Generating Services

### Generating Module File
_generate_module_cpp(rPose_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rPose_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rPose_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rPose_pkg_generate_messages rPose_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_cpp _rPose_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_cpp _rPose_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rPose_pkg_gencpp)
add_dependencies(rPose_pkg_gencpp rPose_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rPose_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rPose_pkg
)
_generate_msg_eus(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rPose_pkg
)

### Generating Services

### Generating Module File
_generate_module_eus(rPose_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rPose_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(rPose_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(rPose_pkg_generate_messages rPose_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_eus _rPose_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_eus _rPose_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rPose_pkg_geneus)
add_dependencies(rPose_pkg_geneus rPose_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rPose_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rPose_pkg
)
_generate_msg_lisp(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rPose_pkg
)

### Generating Services

### Generating Module File
_generate_module_lisp(rPose_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rPose_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rPose_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rPose_pkg_generate_messages rPose_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_lisp _rPose_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_lisp _rPose_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rPose_pkg_genlisp)
add_dependencies(rPose_pkg_genlisp rPose_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rPose_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rPose_pkg
)
_generate_msg_nodejs(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rPose_pkg
)

### Generating Services

### Generating Module File
_generate_module_nodejs(rPose_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rPose_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(rPose_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(rPose_pkg_generate_messages rPose_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_nodejs _rPose_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_nodejs _rPose_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rPose_pkg_gennodejs)
add_dependencies(rPose_pkg_gennodejs rPose_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rPose_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg
)
_generate_msg_py(rPose_pkg
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg"
  "${MSG_I_FLAGS}"
  "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg
)

### Generating Services

### Generating Module File
_generate_module_py(rPose_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rPose_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rPose_pkg_generate_messages rPose_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBox.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_py _rPose_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/zyh/p3p-ros/src/rPose_pkg/msg/BoundingBoxes.msg" NAME_WE)
add_dependencies(rPose_pkg_generate_messages_py _rPose_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rPose_pkg_genpy)
add_dependencies(rPose_pkg_genpy rPose_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rPose_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rPose_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rPose_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(rPose_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rPose_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rPose_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(rPose_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rPose_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rPose_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(rPose_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rPose_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rPose_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(rPose_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rPose_pkg
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(rPose_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
