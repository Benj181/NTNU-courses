# **This is my course work from NTNU MSc**

Sorted after courses

## **Note to self:**

### Install chocolatey <br>
 > `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))` <br>
 
  ### Install msys2 <br>
  > `choco install msys2 -y`<br> 

 


 ### To install python packages: <br> 
 > In mingw64 terminal in C:\tools\msys64\ <br>
 > - Run `pacman -S mingw-w64-clang-aarch64-python-(package)` to download packages <br>
 > - Run `pacman -Suy` to update all <br>



### To make virtual enviroment <br>
 > - <emsp> `mkdir -p ~/venvs` - lies in C:\tools\msys64\home\<username>\venvs <br>
 > - `python -m venv ~/venvs/myproj` to make new venv <br>
 > - `source ~/venvs/myproj/bin/activate` to activate <br>



