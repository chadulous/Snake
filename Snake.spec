# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/New folder/Game/venv/game/main.py'],
             pathex=['D:/New folder/Game/venv/Lib/site-packages', 'D:\\New folder\\Game\\venv\\game'],
             binaries=[],
             datas=[('D:/New folder/Game/venv/game/score.dat', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [('v', None, 'OPTION')],
          exclude_binaries=True,
          name='Snake',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='D:\\New folder\\Game\\venv\\game\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Snake')
