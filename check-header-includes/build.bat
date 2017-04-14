@echo OFF

set PROJECT_DIR=%2
set PROJ_NAME=%3
set BUILD_LOG=%4

set BUILD=/BUILD
if "%1"=="rebuild" set BUILD=/REBUILD

set CONFIG="Debug|x64"

set DEVENV_ARGS=%PROJECT_DIR%\%PROJ_NAME%.vcxproj /PROJECT %PROJ_NAME%.vcxproj %BUILD% %CONFIG%

call "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat" amd64 >nul

::echo %DEVENV_ARGS%
del %BUILD_LOG%
set _IsNativeEnvironment=true
devenv %DEVENV_ARGS% > %BUILD_LOG%
