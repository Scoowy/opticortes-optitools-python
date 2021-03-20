# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['AppGraphic.py'],
             pathex=['C:\\Users\\Scoow\\Documents\\Proyectos\\PyCharm\\AppGraphic'],
             binaries=[],
             datas=[('README.md', '.')],
             hiddenimports=None,
             hookspath=None,
             runtime_hooks=None,
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5B")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5D")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Help")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5N")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Q")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Quick")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5R")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Sensors")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5SerialPort")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Sql")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Test")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5TextToSpeech")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Web")]
a.binaries = [x for x in a.binaries if not x[0].startswith("Qt5Xml")]

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='OptiTools',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='imgs\\OptiTool-Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='OptiTools')
