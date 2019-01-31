# Copyright (C) 2019 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.
import os

dir_output = r'D:\Working_on_currently\dlib_kkh_abstraction'
dll_paths = []
include_headers_examples = []

def gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies):
    fpath_out = os.path.join(dir_output, name_library.replace('.','_').replace(' ', '_') + '.props')
    with open(fpath_out, 'w') as fid:
        fid.write(f'''<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ImportGroup Label="PropertySheets" />
  <PropertyGroup Label="UserMacros" />
  <PropertyGroup />
  <ItemDefinitionGroup>
    <ClCompile>
      <AdditionalIncludeDirectories>{str_AdditionalIncludeDirectories};%(AdditionalIncludeDirectories)</AdditionalIncludeDirectories>
    </ClCompile>
    <Link>
      <AdditionalLibraryDirectories>{str_AdditionalLibraryDirectories};%(AdditionalLibraryDirectories)</AdditionalLibraryDirectories>
      <AdditionalDependencies>{str_AdditionalDependencies};%(AdditionalDependencies)</AdditionalDependencies>
    </Link>
  </ItemDefinitionGroup>
  <ItemGroup />
</Project>
        ''')

def format_example_include(str_ex):
    return '//' + '='*15 + '//\n' + str_ex + '\n//' + '='*15 + '//\n'

### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###

# name_library = r'opencv 4.0.1 release'
# str_AdditionalIncludeDirectories = r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\include'
# str_AdditionalLibraryDirectories = r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\x64\vc15\lib'
# str_AdditionalDependencies = r'opencv_world401.lib'
# dll_paths.append(r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\x64\vc15\bin')
# include_headers_examples.append(format_example_include('#include "opencv2/opencv.hpp"'))
# gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies)
#
# name_library = r'opencv 4.0.1 debug'
# str_AdditionalIncludeDirectories = r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\include'
# str_AdditionalLibraryDirectories = r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\x64\vc15\lib'
# str_AdditionalDependencies = r'opencv_world401d.lib'
# dll_paths.append(r'D:\OpenCV\opencv-4.0.1-vc14_vc15\opencv\build\x64\vc15\bin')
# include_headers_examples.append(format_example_include('#include "opencv2/opencv.hpp"'))
# gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies)


name_library = r'dlib 19.16 release'
str_AdditionalIncludeDirectories = r'D:\CPP_Libs\dlib-19.16_install\include'
str_AdditionalLibraryDirectories = r'D:\CPP_Libs\dlib-19.16_install\lib'
str_AdditionalDependencies = r'dlib19.16.0_release_64bit_msvc1916.lib'
# dll_paths.append()
include_headers_examples.append(format_example_include('#include <dlib/string.h>\n#include <dlib/image_io.h>'))
gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies)

name_library = r'dlib 19.16 debug'
str_AdditionalIncludeDirectories = r'D:\CPP_Libs\dlib-19.16_install\include'
str_AdditionalLibraryDirectories = r'D:\CPP_Libs\dlib-19.16_install\lib'
str_AdditionalDependencies = r'dlib19.16.0_debug_64bit_msvc1916.lib'
# dll_paths.append()
include_headers_examples.append(format_example_include('#include <dlib/string.h>\n#include <dlib/image_io.h>'))
gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies)


# name_library = r'Eigen 3.3.5'
# str_AdditionalIncludeDirectories = r'D:\CPP_Libs\Eigen_3_3_5'
# str_AdditionalLibraryDirectories = r''
# str_AdditionalDependencies = r''
# # dll_paths.append()
# include_headers_examples.append(format_example_include('#include <Eigen/Dense>'))
# gen_property_sheet(dir_output, name_library, str_AdditionalIncludeDirectories, str_AdditionalLibraryDirectories, str_AdditionalDependencies)

### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###
### ///////////////////////////////////////////////////////////////////// ###

print('Paste the below in Visual Studio project Property Pages > Debugging > Environment:')
print('path=%path%;' + ';'.join(dll_paths))

print('\nExamples of #include are shown below:\n')
for ex in include_headers_examples:
    print(ex)





