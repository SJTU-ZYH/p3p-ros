cmake_minimum_required(VERSION 3.0.2)
project(p3p_pkg)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++11 -O2 ${SSE_FLAGS} -msse4")
add_definitions("-DENABLE_SSE")
LIST(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

find_package(OpenCV 3 REQUIRED)
find_package(Sophus REQUIRED)
find_package(FMT REQUIRED)
find_package(CSparse REQUIRED)
find_package(G2O REQUIRED)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cv_bridge
  image_transport
)

## System dependencies are found with CMake's conventions
find_package(Boost REQUIRED COMPONENTS system)
find_package(OpenCV 3 REQUIRED)
find_package(G2O REQUIRED)
find_package(Sophus REQUIRED)
find_package(FMT REQUIRED)
find_package(CSparse REQUIRED)
SET(G2O_LIBS g2o_csparse_extension g2o_stuff g2o_core cxsparse)

catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS roscpp rospy std_msgs cv_bridge
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${PROJECT_SOURCE_DIR}
  ${OpenCV_INCLUDE_DIRS}
  ${G2O_INCLUDE_DIRS}
  ${CSPARSE_INCLUDE_DIR}
  ${Sophus_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
)

add_executable(p3p_3d3d src/p3p_3d3d.cpp)

#
target_link_libraries(p3p_3d3d
        g2o_core g2o_stuff fmt::fmt
        ${catkin_LIBRARIES}
        ${OpenCV_LIBS})
# target_link_libraries(${PROJECT_NAME}_node
#         g2o_core g2o_stuff fmt::fmt
#         ${OpenCV_LIBS})
