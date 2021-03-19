# OptiTools

Proyecto de desarrollo de un conjunto de herramientas que faciliten el cálculo y procesos básicos más usados dentro de 
la empresa **OptiCortes**.

## Commands
### Compilar arcivos `.ui -> .py`

Comando que compila un archivo `.ui` generado por QtDesigner a un archivo `.py`.

```commandline
pyuic5 .\path\to\file.ui -o .\out\path\file.py
```

### Compilar arcivos `.qrc -> .py`

Comando que compila un archivo `resources.qrc` generado por QtDesigner a un archivo `resources.py`.

```commandline
pysrc5 .\path\to\resources.qrc -o .\out\path\resources.py
```

### Build `.exe`

Comando que compila y genera el ejecutable de la aplicación en formato `.exe`.

```commandline
pyinstaller --noconfirm --log-level=WARN ^
    --onedir --noconsole --clean ^
    --name=OptiTools ^
    --add-data="README.md;." ^
    --icon=.\imgs\OptiTool-Icon.ico ^
    .\AppGraphic.py
```

o, ejecutar `build-command.bat`, el cual contiene las instrucciones anteriores.

```commandline
build-command.bat
```