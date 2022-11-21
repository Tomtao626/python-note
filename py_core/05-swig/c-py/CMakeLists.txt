cmake_minimum_required(VERSION 3.23)
project(05_swig C)

set(CMAKE_C_STANDARD 11)

add_executable(05_swig
        example.c
        example.i
        example_wrap.c)
find_package(PythonLibs REQUIRED)
include_directories(/Library/Frameworks/Python.framework/Versions/3.9/include/)