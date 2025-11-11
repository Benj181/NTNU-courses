# **This is my course work from NTNU MSc**

Sorted after courses

## **Note to self:**

### Install chocolatey <br>
 > `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))` <br>
 
  ### Install msys2 <br>
  > `choco install msys2 -y`<br> 

 

### To use python
> Install arm64 or amd64 from https://www.python.org/downloads/windows/ (add to path) (better compatibility with amd64, but slower on arm64 machine)<br>
> `py -0` to check versions<br>
> Create venv with specific version `py -<version> -m venv .venv` (e.g -3.12)<br>
> Activate it `.venv\Scripts\Activate.ps1`<br>
> Make project file and run <br>
> > `python -m pip install --upgrade pip`<br>
> > `pip install -r requirements.txt`<br>
> > `pip install -e .`<br>



