# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/New folder/Game/venv/game/main.py'],
             pathex=['D:\\New folder\\Game\\venv\\game'],
             binaries=[],
             datas=[('D:/New folder/Game/venv/game/score.dat', '.'), ('D:/New folder/Game/venv/Lib/site-packages/panda3d', 'panda3d/'), ('D:/New folder/Game/venv/Lib/site-packages/panda3d-1.10.9.dist-info', 'panda3d-1.10.9.dist-info/'), ('D:/New folder/Game/venv/Lib/site-packages/panda3d_tools', 'panda3d_tools/'), ('D:/New folder/Game/venv/Lib/site-packages/ursina', 'ursina/'), ('D:/New folder/Game/venv/Lib/site-packages/ursina-4.0.0-py3.9.egg-info', 'ursina-4.0.0-py3.9.egg-info/')],
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
splash = Splash('D:/New Folder/Game/venv/game/splash.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=None,
                text_size=12,
                minify_script=True)

exe = EXE(pyz,
          a.scripts, 
          splash,
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
               splash.binaries,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Snake')
