import sys
import os
import subprocess

# 自动安装缺失的依赖
try:
    import numpy as np
except ImportError:
    print("numpy 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    import numpy as np

try:
    import sounddevice as sd
except ImportError:
    print("sounddevice 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sounddevice", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    import sounddevice as sd

try:
    import soundcard
except ImportError:
    print("soundcard 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "soundcard", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    import soundcard

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, 
        QLabel, QPushButton, QHBoxLayout, QGroupBox, QTextEdit,
        QDockWidget, QFrame
    )
    from PyQt5.QtGui import (
        QPixmap, QPainter, QColor, QBrush, QPen, 
        QFont, QFontDatabase, QFontMetrics, QPainterPath
    )
    from PyQt5.QtCore import (
        Qt, QThread, pyqtSignal, QTimer, QSize, QPoint, QRectF,
        QPropertyAnimation, QEasingCurve, QAbstractAnimation
    )
except ImportError:
    print("PyQt5 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, 
        QLabel, QPushButton, QHBoxLayout, QGroupBox, QTextEdit,
        QDockWidget, QFrame
    )
    from PyQt5.QtGui import (
        QPixmap, QPainter, QColor, QBrush, QPen, 
        QFont, QFontDatabase, QFontMetrics, QPainterPath
    )
    from PyQt5.QtCore import (
        Qt, QThread, pyqtSignal, QTimer, QSize, QPoint, QRectF,
        QPropertyAnimation, QEasingCurve, QAbstractAnimation
    )

try:
    from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
    from winsdk.windows.storage.streams import DataReader, InputStreamOptions
except ImportError:
    print("winsdk 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "winsdk", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
    from winsdk.windows.storage.streams import DataReader, InputStreamOptions

try:
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    print("pycaw 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pycaw", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

try:
    from PIL import Image
except ImportError:
    print("Pillow 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    from PIL import Image

try:
    import requests
except ImportError:
    print("requests 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    import requests

try:
    from mutagen import File
    from mutagen.id3 import ID3, COMM
    from mutagen.flac import FLAC
    from mutagen.oggvorbis import OggVorbis
    from mutagen.mp4 import MP4
    MUTAGEN_AVAILABLE = True
except ImportError:
    print("mutagen 未安装，正在安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mutagen", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
    from mutagen import File
    from mutagen.id3 import ID3, COMM
    from mutagen.flac import FLAC
    from mutagen.oggvorbis import OggVorbis
    from mutagen.mp4 import MP4
    MUTAGEN_AVAILABLE = True


# ================================================
# 配置参数
# ================================================

# 环境变量设置
qt_plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Python', 'Lib', 'site-packages', 'PyQt5', 'Qt5', 'plugins')
os.environ['QT_PLUGIN_PATH'] = qt_plugin_path


# 歌词相关配置

# 歌词开关配置
EMBEDDED_LYRIC_ENABLED    = 1      # 内嵌歌词开关：0 = 关闭，1 = 开启（开启时优先获取音频文件内嵌歌词）
LOCAL_LYRIC_ENABLED       = 1      # 本地歌词开关：0 = 关闭，1 = 开启（开启时优先获取本地歌词）
AUTO_SCAN_ENABLED         = 1      # 自动扫描目录开关：0 = 关闭，1 = 开启  我的音乐、我的视频、下载、桌面
VIDEO_LYRIC_ENABLED       = 0      # 视频文件歌词适配开关：0 = 关闭（忽略视频文件的歌词适配），1 = 开启（适配视频文件歌词）

# 共用目录配置
LYRIC_DIR                 = ""     # 自定义歌词目录：留空使用默认预设目录，否则使用指定目录（示例：LYRIC_DIR = "D:\Lyrics"）

# 在线歌词配置
NETWORK_LYRIC_ENABLED     = 1      # 联网获取歌词开关：0 = 关闭，1 = 开启

# 通用歌词配置
LYRIC_OFFSET              = 1.0    # 歌词偏移参数：正数表示提前显示，负数表示延迟显示（单位：秒）


# 悬浮歌词配置
FLOAT_LYRIC_ENABLED = 1      # 悬浮歌词开关：0 = 关闭，1 = 开启
FLOAT_LYRIC_BACKGROUND_OPACITY  = 0.0    # 背景透明度：0.0-1.0，0.0为完全透明，1.0为完全不透明
FLOAT_LYRIC_TEXT_COLOR = "green" # 文本颜色：当前歌词颜色
FLOAT_LYRIC_TEXT_OPACITY        = 0.8    # 文本透明度：0.0-1.0，0.0为完全透明，1.0为完全不透明
FLOAT_LYRIC_TEXT_SIZE           = 40     # 文本大小：当前歌词字体大小（像素）
FLOAT_LYRIC_TEXT_WEIGHT         = 700    # 文本粗细：1-1000，700为bold
FLOAT_LYRIC_DISPLAY_MODE        = 1      # 显示模式：0 = 单行显示，1 = 双行显示
FLOAT_LYRIC_HEIGHT              = 200    # 窗口高度：悬浮歌词窗口高度（像素）
FLOAT_LYRIC_BORDER_RADIUS       = 10     # 边框圆角：背景边框圆角（像素）
FLOAT_LYRIC_PADDING             = 0      # 内边距：文本与背景的间距（像素）
FLOAT_LYRIC_BACKGROUND_PENETRATION = 1   # 背景穿透/锁定布局：0 = 不锁定（允许拖拽，不穿透），1 = 锁定（禁止拖拽，允许点击穿透）
FLOAT_LYRIC_BOTTOM_MARGIN       = 40     # 屏幕下方间距：悬浮窗口底部到屏幕底部的距离（像素）
FLOAT_LYRIC_SHADOW_BLUR_RADIUS  = 3      # 阴影模糊半径：0-20，值越大阴影越柔和
FLOAT_LYRIC_SHADOW_OFFSET_X     = 3      # 阴影水平偏移：-10到10，正值向右偏移，负值向左偏移
FLOAT_LYRIC_SHADOW_OFFSET_Y     = 2      # 阴影垂直偏移：-10到10，正值向下偏移，负值向上偏移
FLOAT_LYRIC_SHADOW_OPACITY      = 200    # 阴影透明度：0-255，0为完全透明，255为完全不透明


# 音频可视化配置
VISUALIZATION_STYLE = 3  # 可视化样式：3 = 圆形频谱，4 = 波浪形，5 = 关闭


# 灵动岛配置
DYNAMIC_ISLAND_ENABLED   = 1      # 灵动岛模式开关：0 = 关闭，1 = 开启
DYNAMIC_ISLAND_OPACITY   = 0.9    # 灵动岛透明度：0.0-1.0，0.0为完全透明，1.0为完全不透明


# ================================================
# 导入模块
# ================================================

import asyncio
import ctypes
from ctypes import wintypes
from io import BytesIO
import tempfile
import threading
import urllib.request
import json
import urllib.parse

# Windows API相关定义
user32 = ctypes.windll.user32

# 窗口样式常量
GWL_STYLE = -16
WS_MAXIMIZE = 0x01000000

# 矩形结构体
class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]

# MusicLyricDownloader 类 - 从 a.py 集成
class MusicLyricDownloader:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

    # --- 网易云部分 ---
    def search_netease(self, keyword):
        search_url = "https://music.163.com/api/search/get/web"
        params = {'s': keyword, 'type': 1, 'limit': 5, 'offset': 0}
        try:
            import requests
            res = requests.get(search_url, params=params, headers=self.headers)
            songs = res.json().get('result', {}).get('songs', [])
            return [{'id': s['id'], 'title': s['name'], 'artist': s['artists'][0]['name'], 'source': '网易云'} for s in songs]
        except Exception as e:
            print(f"网易云搜索失败: {e}")
            return []

    def get_netease_lyric(self, song_id):
        url = f"https://music.163.com/api/song/lyric?id={song_id}&lv=1&kv=1&tv=-1"
        import requests
        res = requests.get(url, headers=self.headers)
        data = res.json()
        lyric = data.get('lrc', {}).get('lyric', '暂无歌词')
        tlyric = data.get('tlyric', {}).get('lyric', '')
        return f"{lyric}\n{'-'*20}\n翻译：\n{tlyric}" if tlyric else lyric

    # --- QQ 音乐部分 ---
    def search_qq(self, keyword):
        search_url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
        params = {'w': keyword, 'n': 5, 'format': 'json'}
        try:
            import requests
            res = requests.get(search_url, params=params, headers=self.headers)
            # 兼容处理可能的 JSONP
            content = res.text
            if content.startswith('callback(') or content.startswith('jsonp('):
                content = content[content.find('(')+1 : content.rfind(')')]
            import json
            data = json.loads(content)
            songs = data.get('data', {}).get('song', {}).get('list', [])
            return [{'mid': s['songmid'], 'title': s['songname'], 'artist': s['singer'][0]['name'], 'source': 'QQ音乐'} for s in songs]
        except Exception as e:
            print(f"QQ音乐搜索失败: {e}")
            return []

    def get_qq_lyric(self, song_mid):
        lyric_url = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg"
        params = {
            'songmid': song_mid,
            'format': 'json',
            'nobase64': 0,
            'g_tk': '5381'
        }
        # QQ 音乐必须校验 Referer
        qq_headers = self.headers.copy()
        qq_headers['Referer'] = 'https://y.qq.com/'
        
        import requests
        import base64
        res = requests.get(lyric_url, params=params, headers=qq_headers)
        data = res.json()
        lyric_base64 = data.get('lyric', '')
        if lyric_base64:
            return base64.b64decode(lyric_base64).decode('utf-8')
        return "暂无歌词"



def get_special_folder_path(csidl):
    """
    获取Windows特殊文件夹路径
    :param csidl: 特殊文件夹ID
    :return: 文件夹路径
    """
    try:
        import ctypes
        from ctypes import wintypes
        
        # 定义结构体
        class SHITEMID(ctypes.Structure):
            _fields_ = [
                ('cb', wintypes.USHORT),
                ('abID', ctypes.c_ubyte * 1)
            ]
        
        class ITEMIDLIST(ctypes.Structure):
            _fields_ = [
                ('mkid', SHITEMID)
            ]
        
        # 加载shell32.dll
        shell32 = ctypes.windll.shell32
        
        # 定义函数原型
        SHGetSpecialFolderLocation = shell32.SHGetSpecialFolderLocation
        SHGetSpecialFolderLocation.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ITEMIDLIST))]
        SHGetSpecialFolderLocation.restype = wintypes.BOOL
        
        SHGetPathFromIDListW = shell32.SHGetPathFromIDListW
        SHGetPathFromIDListW.argtypes = [ctypes.POINTER(ITEMIDLIST), ctypes.c_wchar_p]
        SHGetPathFromIDListW.restype = wintypes.BOOL
        
        # 调用函数获取文件夹路径
        pidl = ctypes.POINTER(ITEMIDLIST)()
        if SHGetSpecialFolderLocation(0, csidl, ctypes.byref(pidl)):
            path = ctypes.create_unicode_buffer(260)
            if SHGetPathFromIDListW(pidl, path):
                return path.value
        
        # 尝试使用SHGetFolderPathW函数
        try:
            SHGetFolderPathW = shell32.SHGetFolderPathW
            SHGetFolderPathW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD, ctypes.c_wchar_p]
            SHGetFolderPathW.restype = ctypes.c_long  # 使用c_long代替HRESULT
            
            path = ctypes.create_unicode_buffer(260)
            result = SHGetFolderPathW(0, csidl, None, 0, path)
            if result == 0:  # S_OK
                return path.value
        except Exception as e:
            print(f"尝试使用SHGetFolderPathW时出错: {e}")
        
        return ""
    except Exception as e:
        print(f"获取特殊文件夹路径时出错: {e}")
        return ""

def get_default_music_folder():
    """
    获取系统默认的音乐文件夹路径
    :return: 音乐文件夹路径
    """
    # CSIDL_MYMUSIC = 13
    return get_special_folder_path(13)

def get_default_videos_folder():
    """
    获取系统默认的视频文件夹路径
    :return: 视频文件夹路径
    """
    # CSIDL_MYVIDEO = 14
    return get_special_folder_path(14)

def get_default_downloads_folder():
    """
    获取系统默认的下载文件夹路径
    :return: 下载文件夹路径
    """
    # 尝试使用多种方法获取下载文件夹路径
    
    # 方法1: 使用环境变量USERPROFILE拼接Downloads
    downloads_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads')
    if downloads_path and os.path.exists(downloads_path):
        return downloads_path
    
    # 方法2: 尝试使用KNOWNFOLDERID via winreg
    try:
        import winreg
        
        # 下载文件夹的GUID
        DOWNLOADS_GUID = '{374DE290-123F-4565-9164-39C4925E467B}'
        
        # 打开注册表
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders') as key:
            # 查询下载文件夹路径
            downloads_path, _ = winreg.QueryValueEx(key, DOWNLOADS_GUID)
            if downloads_path and os.path.exists(downloads_path):
                # 替换环境变量
                if downloads_path.startswith('%'):
                    downloads_path = os.path.expandvars(downloads_path)
                return downloads_path
    except Exception as e:
        print(f"尝试使用注册表获取下载文件夹路径时出错: {e}")
    
    # 方法3: 回退到CSIDL_DOWNLOADS（0x0013）
    csidl_path = get_special_folder_path(0x0013)
    if csidl_path and os.path.exists(csidl_path) and 'Downloads' in csidl_path:
        return csidl_path
    
    # 最后尝试常见的下载文件夹路径
    common_paths = [
        os.path.expandvars(r'%USERPROFILE%\Downloads'),
        os.path.expandvars(r'%HOMEPATH%\Downloads'),
        os.path.expandvars(r'%SYSTEMDRIVE%\Users\%USERNAME%\Downloads')
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return ""

def get_default_desktop_folder():
    """
    获取系统默认的桌面文件夹路径
    :return: 桌面文件夹路径
    """
    # CSIDL_DESKTOP = 0x0000
    return get_special_folder_path(0x0000)

def search_audio_file(artist_name, song_name):
    """
    在系统默认目录和自定义目录中搜索音频或视频文件
    :param artist_name: 歌手名
    :param song_name: 歌曲名
    :return: 找到的文件路径，如果没有找到则返回空字符串
    """
    if AUTO_SCAN_ENABLED != 1:
        return ""
    
    # 支持的音频文件扩展名
    audio_extensions = ['.mp3', '.flac', '.ogg', '.mp4', '.m4a', '.wav', '.wma']
    # 支持的视频文件扩展名
    video_extensions = ['.mkv', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']
    
    # 构建搜索目录列表
    search_dirs = []
    
    # 检查是否是视频文件
    is_video = any(ext in song_name.lower() for ext in video_extensions)
    
    # 提取文件名（不含扩展名）
    song_basename = os.path.splitext(song_name)[0]
    
    # 存储已添加的目录，避免重复
    added_dirs = set()
    
    # 添加自定义扫描目录
    if LYRIC_DIR and os.path.exists(LYRIC_DIR) and LYRIC_DIR not in added_dirs:
        search_dirs.append(LYRIC_DIR)
        added_dirs.add(LYRIC_DIR)
    
    # 根据文件类型调整搜索顺序
    if is_video:
        # 视频文件优先搜索视频文件夹
        videos_folder = get_default_videos_folder()
        if videos_folder and os.path.exists(videos_folder) and videos_folder not in added_dirs:
            search_dirs.append(videos_folder)
            added_dirs.add(videos_folder)
    else:
        # 音频文件优先搜索音乐文件夹
        music_folder = get_default_music_folder()
        if music_folder and os.path.exists(music_folder) and music_folder not in added_dirs:
            search_dirs.append(music_folder)
            added_dirs.add(music_folder)
    
    # 添加其他默认目录
    # 音乐文件夹（如果尚未添加）
    music_folder = get_default_music_folder()
    if music_folder and os.path.exists(music_folder) and music_folder not in added_dirs:
        search_dirs.append(music_folder)
        added_dirs.add(music_folder)
    
    # 视频文件夹（如果尚未添加）
    videos_folder = get_default_videos_folder()
    if videos_folder and os.path.exists(videos_folder) and videos_folder not in added_dirs:
        search_dirs.append(videos_folder)
        added_dirs.add(videos_folder)
    
    # 下载文件夹
    downloads_folder = get_default_downloads_folder()
    if downloads_folder and os.path.exists(downloads_folder) and downloads_folder not in added_dirs:
        search_dirs.append(downloads_folder)
        added_dirs.add(downloads_folder)
    
    # 桌面文件夹
    desktop_folder = get_default_desktop_folder()
    if desktop_folder and os.path.exists(desktop_folder) and desktop_folder not in added_dirs:
        search_dirs.append(desktop_folder)
        added_dirs.add(desktop_folder)
    
    # 显示已添加的搜索目录列表
    print("[歌词搜索过程] 已添加的搜索目录列表:")
    for i, search_dir in enumerate(search_dirs, 1):
        print(f"[歌词搜索过程] {i}. {search_dir}")
    
    # 遍历搜索目录
    for search_dir in search_dirs:
        # 存储所有匹配的文件，以便后续排序
        matched_files = []
        
        for root, _, files in os.walk(search_dir):
            for file in files:
                # 检查文件扩展名
                ext = os.path.splitext(file)[1].lower()
                if ext not in audio_extensions and ext not in video_extensions:
                    continue
                
                # 计算匹配分数
                match_score = 0
                file_lower = file.lower()
                file_basename = os.path.splitext(file)[0].lower()
                song_basename_lower = song_basename.lower()
                
                # 处理全角和半角字符的转换
                def to_half_width(s):
                    """将全角字符转换为半角字符"""
                    res = []
                    for char in s:
                        code = ord(char)
                        if code == 0x3000:
                            res.append(' ')
                        elif 0xFF01 <= code <= 0xFF5E:
                            res.append(chr(code - 0xFEE0))
                        else:
                            res.append(char)
                    return ''.join(res)
                
                # 转换为半角并去除特殊字符
                def normalize_string(s):
                    s = to_half_width(s)
                    import re
                    # 去除特殊字符，保留字母、数字、中文、空格和常见的歌曲标题符号
                    s = re.sub(r'[^\w\s\u4e00-\u9fa5+\-]', '', s)
                    return s.strip().lower()
                
                # 标准化字符串
                normalized_file = normalize_string(file)
                normalized_song = normalize_string(song_name)
                normalized_artist = normalize_string(artist_name)
                
                # 只在找到匹配文件时显示详细日志
                # 移除所有文件的标准化日志，只保留最终候选文件的日志
                
                # 检查是否是同名文件（不考虑扩展名）
                if normalize_string(song_basename) == normalize_string(file_basename):
                    match_score = 10  # 最高分数，同名文件
                else:
                    # 即使有歌手名，也要依次检查所有匹配条件
                    # 检查是否同时包含歌手名和歌曲名
                    if normalized_artist and normalized_song:
                        if normalized_artist in normalized_file and normalized_song in normalized_file:
                            match_score = 9  # 高分数
                        # 检查歌手名相似度和歌曲名完全匹配
                        elif normalized_artist and normalized_song in normalized_file:
                            # 计算歌手名相似度
                            if normalized_artist and any(artist_part in normalized_file for artist_part in normalized_artist.split()):
                                # 检查歌手名的核心部分是否匹配
                                # 例如：モーニング娘。'24 和 モーニング娘。
                                # 提取核心歌手名，去除后缀和特殊字符
                                core_artist = normalized_artist
                                # 处理带撇号的情况，如 '24
                                if "'" in core_artist:
                                    core_artist = core_artist.split("'")[0]
                                # 处理带数字后缀的情况，如 2024
                                import re
                                core_artist = re.sub(r'\s*\d+$', '', core_artist)
                                # 处理带连字符的情况，如 - 2024
                                core_artist = re.sub(r'\s*-\s*\d+$', '', core_artist)
                                # 去除多余空格
                                core_artist = core_artist.strip()
                                
                                if core_artist and core_artist in normalized_file:
                                    match_score = 8  # 较高分数
                                else:
                                    match_score = 5  # 中等分数
                    
                    # 检查是否只包含歌曲名（无论是否有歌手名）
                    if match_score < 7 and normalized_song:
                        # 确保歌曲名完全匹配，而不是部分匹配
                        # 例如："元気+" 应该匹配 "元気+"，而不是 "Be 元気"
                        import re
                        # 不使用单词边界，因为特殊字符可能会影响匹配
                        if normalized_song in normalized_file:
                            match_score = 7  # 中等分数
                    
                    # 检查是否只包含歌手名（只有在没有歌曲名或歌曲名不匹配时）
                    if match_score < 3 and normalized_artist:
                        if normalized_artist in normalized_file:
                            match_score = 3  # 最低分数
                        # 检查歌手名相似度
                        elif any(artist_part in normalized_file for artist_part in normalized_artist.split()):
                            match_score = 2  # 更低分数
                
                # 如果有匹配，添加到列表
                if match_score > 0:
                    matched_files.append((match_score, os.path.join(root, file)))
        
        # 按匹配分数排序，分数高的排在前面
        matched_files.sort(reverse=True, key=lambda x: x[0])
        
        # 显示前3个可能的文件（如果有）
        if matched_files:
            print(f"[歌词搜索过程] 找到 {len(matched_files)} 个可能的文件，显示前3个:")
            for i, (score, file_path) in enumerate(matched_files[:3], 1):
                print(f"[歌词搜索过程] {i}. {file_path} (匹配分数: {score})")
        
        # 返回分数最高的文件
        if matched_files:
            best_match = matched_files[0][1]
            return best_match
    
    return ""

def get_embedded_lyric(file_path):
    """
    从音频或视频文件中提取内嵌歌词/字幕，只保留带时间轴的歌词段
    :param file_path: 音频或视频文件路径
    :return: 获取到的歌词，如果没有获取到则返回空字符串
    """
    if not MUTAGEN_AVAILABLE:
        return ""
    
    if not file_path or not os.path.exists(file_path):
        return ""
    
    try:
        # 检查文件扩展名
        ext = os.path.splitext(file_path)[1].lower()
        # 支持的视频文件扩展名
        video_extensions = ['.mkv', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']
        
        # 检查是否是视频文件
        is_video = ext in video_extensions
        
        if is_video:
            # 对于视频文件，尝试使用其他方法提取字幕
            # 这里可以添加对视频文件字幕提取的代码
            # 暂时返回空字符串，后续可以扩展
            return ""
        else:
            # 尝试直接使用ID3打开文件
            try:
                audio = ID3(file_path)
            except Exception as e:
                # 尝试使用File打开文件
                audio = File(file_path)
                if not audio:
                    return ""
            
            # 提取歌词
            lyric = ""
            
            # 根据不同的音频格式提取歌词
            if isinstance(audio, ID3):
                # MP3文件，使用ID3标签
                
                # 1. 检查USLT标签（标准内嵌歌词标签）
                try:
                    # 直接获取所有USLT标签
                    uslt_tags = [key for key in audio.keys() if key.startswith('USLT::')]
                    
                    for key in uslt_tags:
                        try:
                            # 提取USLT标签内容
                            uslt_frame = audio[key]
                            
                            # 尝试直接访问text属性
                            if hasattr(uslt_frame, 'text'):
                                try:
                                    # 尝试直接获取文本
                                    text = uslt_frame.text
                                    
                                    if isinstance(text, list):
                                        for i, item in enumerate(text):
                                            try:
                                                if isinstance(item, bytes):
                                                    # 尝试不同编码解码
                                                    encodings = ['utf-8', 'gbk', 'shift-jis', 'latin-1']
                                                    for encoding in encodings:
                                                        try:
                                                            decoded = item.decode(encoding)
                                                            uslt_content = decoded
                                                            break
                                                        except Exception as e:
                                                            pass
                                                else:
                                                    uslt_content = str(item)
                                            except Exception as e:
                                                pass
                                    else:
                                        uslt_content = str(text)
                                except Exception as e:
                                    # 尝试其他方法获取内容
                                    try:
                                        uslt_content = str(uslt_frame)
                                    except Exception as e:
                                        uslt_content = ""
                            else:
                                # 尝试直接转换为字符串
                                try:
                                    uslt_content = str(uslt_frame)
                                except Exception as e:
                                    uslt_content = ""
                            
                            # 检查是否提取到内容
                            if uslt_content:
                                # 检查是否包含时间轴
                                import re
                                time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                                if re.search(time_pattern, uslt_content):
                                    lyric = uslt_content
                                    break
                        except Exception as e:
                            pass
                except Exception as e:
                    pass
                
                # 2. 检查COMM标签（评论标签，有时也用于存储歌词）
                if not lyric:
                    for key in audio.keys():
                        if key.startswith('COMM::'):
                            try:
                                # 提取COMM标签内容
                                comm_frame = audio[key]
                                
                                # 尝试直接访问text属性
                                if hasattr(comm_frame, 'text'):
                                    try:
                                        # 尝试直接获取文本
                                        text = comm_frame.text
                                        
                                        if isinstance(text, list):
                                            for i, item in enumerate(text):
                                                try:
                                                    if isinstance(item, bytes):
                                                        # 尝试不同编码解码
                                                        encodings = ['utf-8', 'gbk', 'shift-jis', 'latin-1']
                                                        for encoding in encodings:
                                                            try:
                                                                decoded = item.decode(encoding)
                                                                comm_content = decoded
                                                                break
                                                            except Exception as e:
                                                                pass
                                                    else:
                                                        comm_content = str(item)
                                                except Exception as e:
                                                    pass
                                        else:
                                            comm_content = str(text)
                                    except Exception as e:
                                        # 尝试其他方法获取内容
                                        try:
                                            comm_content = str(comm_frame)
                                        except Exception as e:
                                            comm_content = ""
                                else:
                                    # 尝试直接转换为字符串
                                    try:
                                        comm_content = str(comm_frame)
                                    except Exception as e:
                                        comm_content = ""
                                
                                # 检查是否提取到内容
                                if comm_content:
                                    # 检查是否包含时间轴
                                    import re
                                    time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                                    if re.search(time_pattern, comm_content):
                                        lyric = comm_content
                                        break
                            except Exception as e:
                                pass
            elif isinstance(audio, FLAC):
                # FLAC文件
                if 'lyrics' in audio:
                    flac_content = audio['lyrics'][0]
                    # 检查是否包含时间轴
                    import re
                    time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                    if re.search(time_pattern, flac_content):
                        lyric = flac_content
            elif isinstance(audio, OggVorbis):
                # OGG文件
                if 'lyrics' in audio:
                    ogg_content = audio['lyrics'][0]
                    # 检查是否包含时间轴
                    import re
                    time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                    if re.search(time_pattern, ogg_content):
                        lyric = ogg_content
            elif isinstance(audio, MP4):
                # MP4文件
                if 'a9lyr' in audio:
                    mp4_content = audio['a9lyr'][0]
                    # 检查是否包含时间轴
                    import re
                    time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                    if re.search(time_pattern, mp4_content):
                        lyric = mp4_content
            
            # 尝试通用方法
            if not lyric:
                if hasattr(audio, 'items'):
                    for key, value in audio.items():
                        if 'lyric' in key.lower() or 'text' in key.lower():
                            # 提取内容
                            content = ""
                            if isinstance(value, list) and value:
                                content = value[0]
                            elif isinstance(value, str):
                                content = value
                            
                            # 检查是否包含时间轴
                            import re
                            time_pattern = r'\[\d{2}:\d{2}(\.\d{2,3})?\]'
                            if content and re.search(time_pattern, content):
                                lyric = content
                                break
            
            # 过滤歌词，只保留带时间轴的行
            if lyric:
                import re
                # 匹配时间轴格式：[mm:ss.xx] 或 [mm:ss]
                time_pattern = r'^\[\d{2}:\d{2}(\.\d{2,3})?\]'
                
                # 分割歌词为行
                lines = lyric.split('\n')
                filtered_lines = []
                
                for line in lines:
                    line = line.strip()
                    # 只保留带时间轴的行
                    if re.match(time_pattern, line):
                        filtered_lines.append(line)
                
                # 重新组合歌词
                filtered_lyric = '\n'.join(filtered_lines)
                
                if filtered_lyric:
                    return filtered_lyric
            
            return ""
    except Exception as e:
        return ""

def get_local_lyric(artist_name, track_name):
    """
    从本地搜索歌词文件
    :param artist_name: 歌手名
    :param track_name: 歌曲名
    :return: 获取到的歌词，如果没有获取到则返回空字符串
    """
    # 如果本地歌词开关关闭，直接返回空字符串
    if LOCAL_LYRIC_ENABLED == 0:
        return ""
    
    try:
        # 构建搜索目录列表（使用内嵌歌词目录）
        search_dirs = []
        
        # 如果设置了自定义目录，添加到搜索列表
        if LYRIC_DIR:
            search_dirs.append(LYRIC_DIR)
        else:
            # 否则使用系统默认目录（与内嵌歌词搜索目录相同）
            # 获取用户目录
            user_profile = os.environ.get('USERPROFILE', '')
            # 添加常见的音乐和下载目录
            if user_profile:
                search_dirs.append(os.path.join(user_profile, 'Music'))
                search_dirs.append(os.path.join(user_profile, 'Videos'))
                search_dirs.append(os.path.join(user_profile, 'Downloads'))
                search_dirs.append(os.path.join(user_profile, 'Desktop'))
        
        # 生成可能的歌词文件名格式
        possible_filenames = []
        
        # 格式1: 歌手 - 歌曲名.lrc
        if artist_name and track_name:
            possible_filenames.append(f"{artist_name} - {track_name}.lrc")
        
        # 格式2: 歌曲名.lrc
        if track_name:
            possible_filenames.append(f"{track_name}.lrc")
        
        # 格式3: 歌手 - 歌曲名 (简化版).lrc（移除括号和特殊字符）
        import re
        if artist_name and track_name:
            # 简化歌曲名（移除括号及其内容、特殊字符）
            simplified_track = re.sub(r'\s*\([^)]*\)\s*', '', track_name)
            simplified_track = re.sub(r'\s*\[[^\]]*\]\s*', '', simplified_track)
            simplified_track = re.sub(r'[^\w\s-]', '', simplified_track).strip()
            simplified_artist = re.sub(r'[^\w\s-]', '', artist_name).strip()
            if simplified_artist and simplified_track:
                possible_filenames.append(f"{simplified_artist} - {simplified_track}.lrc")
        
        # 格式4: 歌曲名 (简化版).lrc
        if track_name:
            simplified_track = re.sub(r'\s*\([^)]*\)\s*', '', track_name)
            simplified_track = re.sub(r'\s*\[[^\]]*\]\s*', '', simplified_track)
            simplified_track = re.sub(r'[^\w\s-]', '', simplified_track).strip()
            if simplified_track:
                possible_filenames.append(f"{simplified_track}.lrc")
        
        # 搜索歌词文件
        for search_dir in search_dirs:
            if not os.path.exists(search_dir):
                continue
            
            for filename in possible_filenames:
                # 尝试不同的编码读取文件
                lyric_path = os.path.join(search_dir, filename)
                if os.path.exists(lyric_path):
                    # 尝试使用不同编码读取文件
                    encodings = ['utf-8', 'gbk', 'gb2312', 'utf-16']
                    for encoding in encodings:
                        try:
                            with open(lyric_path, 'r', encoding=encoding) as f:
                                content = f.read()
                            # 检查是否包含时间标签
                            if re.search(r'\[\d{2}:\d{2}\.\d{2,3}\]', content):
                                return content
                            else:
                                break
                        except UnicodeDecodeError:
                            continue
    except Exception as e:
        pass
    return ""

# 悬浮歌词窗口类
class LyricFloatWindow(QWidget):
    """
    桌面悬浮歌词窗口
    """
    def __init__(self, parent=None):
        # 先设置窗口为隐藏状态
        super().__init__(parent)
        self.hide()
        
        self.setWindowTitle("悬浮歌词")
        
        # 导入全局配置
        global FLOAT_LYRIC_BACKGROUND_PENETRATION
        
        # 根据背景穿透参数设置窗口属性
        if FLOAT_LYRIC_BACKGROUND_PENETRATION == 1:
            # 锁定布局，允许点击穿透
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool | Qt.WindowTransparentForInput)
        else:
            # 不锁定布局，不允许点击穿透
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
            
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 初始化歌词相关属性
        self.current_parsed_lyric = []
        self.current_time = 0
        self.lyric_offset = LYRIC_OFFSET
        
        # 导入全局配置
        global FLOAT_LYRIC_HEIGHT
        
        # 动态计算窗口宽度：屏幕宽度的3/4
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.dynamic_width = int(screen_geometry.width() * 0.75)
        
        # 设置窗口大小
        self.setFixedSize(self.dynamic_width, FLOAT_LYRIC_HEIGHT)
        
        # 初始化UI
        self.init_ui()
        
        # 初始化拖拽相关属性
        self.dragging = False
        self.drag_position = QPoint()
        self.background_penetration = FLOAT_LYRIC_BACKGROUND_PENETRATION
        
        # 初始化动画相关属性
        self.show_animation = None
        self.hide_animation = None
        
        # 初始状态为隐藏
        self.visible = False
        
        # 将窗口默认位置设置到屏幕之外
        x = (screen_geometry.width() - self.width()) // 2
        y = screen_geometry.height() + 100  # 屏幕下方外
        self.move(x, y)
        
        # 确保窗口保持隐藏状态
        self.hide()
    
    def init_ui(self):
        """
        初始化UI
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 导入全局配置
        global FLOAT_LYRIC_TEXT_SIZE, FLOAT_LYRIC_TEXT_COLOR, FLOAT_LYRIC_TEXT_WEIGHT
        global FLOAT_LYRIC_TEXT_OPACITY
        global FLOAT_LYRIC_BACKGROUND_OPACITY, FLOAT_LYRIC_BORDER_RADIUS, FLOAT_LYRIC_PADDING
        global FLOAT_LYRIC_SHADOW_BLUR_RADIUS, FLOAT_LYRIC_SHADOW_OFFSET_X, FLOAT_LYRIC_SHADOW_OFFSET_Y
        global FLOAT_LYRIC_SHADOW_OPACITY
        
        # 处理文本颜色和透明度
        if FLOAT_LYRIC_TEXT_COLOR.lower() == "white":
            # 白色文本，应用透明度
            r, g, b = 255, 255, 255
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "red":
            r, g, b = 255, 100, 100  # 降低红色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "blue":
            r, g, b = 100, 100, 255  # 降低蓝色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "green":
            r, g, b = 100, 255, 100  # 降低绿色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "yellow":
            r, g, b = 255, 255, 100  # 降低黄色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "purple":
            r, g, b = 200, 100, 200  # 降低紫色饱和度
        else:
            # 其他颜色，使用默认白色
            r, g, b = 255, 255, 255
        
        # 以1080P为基准动态调整字体大小
        screen = QApplication.primaryScreen()
        # 获取屏幕分辨率
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        # 以1080P（1920x1080）为基准，根据屏幕高度计算缩放比例
        base_height = 1080  # 1080P的高度
        # 使用平方根函数平滑缩放比例，避免高分辨率下字体过大
        import math
        scale_factor = math.sqrt(screen_height / base_height)
        # 设置最大缩放比例上限为1.5
        max_scale = 1.5
        scale_factor = min(scale_factor, max_scale)
        # 根据缩放比例调整字体大小
        adjusted_text_size = int(FLOAT_LYRIC_TEXT_SIZE * scale_factor)
        print(f"[悬浮歌词] 屏幕分辨率: {screen_width}x{screen_height}, 缩放比例: {scale_factor:.2f}, 调整后字体大小: {adjusted_text_size}px")
        
        # 创建弹簧，将标签推到底部
        from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)
        
        # 创建单个歌词标签，支持双行显示双语字幕
        self.lyric_label = QLabel("歌词将在此显示")
        self.lyric_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.lyric_label.setWordWrap(True)  # 支持自动换行
        self.lyric_label.setStyleSheet(f"""
            QLabel {{
                font-size: {adjusted_text_size}px;
                color: rgba({r}, {g}, {b}, {FLOAT_LYRIC_TEXT_OPACITY});
                font-weight: {FLOAT_LYRIC_TEXT_WEIGHT};
                background-color: rgba(0, 0, 0, {FLOAT_LYRIC_BACKGROUND_OPACITY});
                border-radius: {FLOAT_LYRIC_BORDER_RADIUS}px;
                padding: {FLOAT_LYRIC_PADDING}px;
            }}
        """)
        
        # 添加文本阴影效果
        from PyQt5.QtWidgets import QGraphicsDropShadowEffect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(FLOAT_LYRIC_SHADOW_BLUR_RADIUS)
        shadow.setOffset(FLOAT_LYRIC_SHADOW_OFFSET_X, FLOAT_LYRIC_SHADOW_OFFSET_Y)
        shadow.setColor(QColor(0, 0, 0, FLOAT_LYRIC_SHADOW_OPACITY))
        self.lyric_label.setGraphicsEffect(shadow)
        
        layout.addWidget(self.lyric_label)
        self.setLayout(layout)
        
        # 确保窗口保持隐藏状态
        self.hide()
    
    def update_lyric(self, parsed_lyric, current_time):
        """
        更新歌词显示
        :param parsed_lyric: 解析后的歌词列表
        :param current_time: 当前播放时间（秒）
        """
        # 检查是否正在播放隐藏动画（显示动画期间允许更新歌词）
        is_hiding_animating = hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running
        
        # 当隐藏动画正在播放时，不更新歌词，保持当前显示的文本
        if is_hiding_animating:
            return
        
        # 只有当解析后的歌词列表不为空时，才更新歌词
        if parsed_lyric:
            self.current_parsed_lyric = parsed_lyric
            self.current_time = current_time
            self.display_current_lyric()
        else:
            pass
    
    def display_current_lyric(self):
        """
        显示当前时间对应的歌词，支持双语字幕双行显示
        """
        # 检查是否正在播放隐藏动画（显示动画期间允许更新歌词）
        is_hiding_animating = hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running
        
        # 当隐藏动画正在播放时，不更新歌词，保持当前显示的文本
        if is_hiding_animating:
            return
        
        # 只有当歌词列表不为空时，才更新歌词显示
        if not self.current_parsed_lyric:
            self.lyric_label.setText("")
            return
        
        adjusted_time = self.current_time + self.lyric_offset
        
        last_non_empty_lyric = ""
        current_lyric = ""
        found_current = False
        next_lyric = ""
        next_lyric_time = None
        
        # 遍历歌词，查找当前歌词和下一句歌词
        for i, (time, content) in enumerate(self.current_parsed_lyric):
            # 过滤掉0.000秒的内容，通常是歌曲标题、版权信息等非歌词内容
            if time == 0.0 and content:
                # 跳过0.000秒的内容
                continue
                
            # 记录下一句歌词信息
            if i < len(self.current_parsed_lyric) - 1:
                next_lyric_time = self.current_parsed_lyric[i+1][0]
                next_lyric = self.current_parsed_lyric[i+1][1]
            
            if time <= adjusted_time:
                if content:
                    last_non_empty_lyric = content
                    current_lyric = content
                
                if i < len(self.current_parsed_lyric) - 1:
                    if adjusted_time < next_lyric_time:
                        blank_duration = next_lyric_time - time
                        if not content:
                            if blank_duration < 3.0:
                                current_lyric = last_non_empty_lyric
                            else:
                                # 检查是否接近下一句歌词（小于0.5秒）
                                if next_lyric_time and (next_lyric_time - adjusted_time) < 0.5:
                                    # 如果接近下一句歌词，且下一句歌词非空，使用下一句歌词
                                    if next_lyric:
                                        current_lyric = next_lyric
                                    else:
                                        current_lyric = ""
                                else:
                                    current_lyric = ""
                        else:
                            current_lyric = content
                        found_current = True
                        break
                else:
                    # 最后一句歌词
                    current_lyric = content if content else last_non_empty_lyric
                    found_current = True
                    break
        
        # 如果没有找到当前歌词，检查是否接近下一句歌词
        if not found_current:
            # 遍历查找下一句歌词
            for i, (time, content) in enumerate(self.current_parsed_lyric):
                if time > adjusted_time:
                    # 找到下一句歌词
                    next_lyric_time = time
                    next_lyric = content
                    break
            
            # 如果接近下一句歌词（小于0.5秒），且下一句歌词非空，使用下一句歌词
            if next_lyric_time and (next_lyric_time - adjusted_time) < 0.5:
                if next_lyric:
                    current_lyric = next_lyric
        
        # 处理双语字幕，将' / '替换为换行符实现双行显示
        if current_lyric and ' / ' in current_lyric:
            display_lyric = current_lyric.replace(' / ', '\n')
        else:
            display_lyric = current_lyric
        
        # 只更新歌词内容，不隐藏窗口
        self.lyric_label.setText(display_lyric)
    
    # 实现拖拽功能
    def mousePressEvent(self, event):
        # 只有在非背景穿透模式下才允许拖拽
        if not self.background_penetration and event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        # 只有在非背景穿透模式下才允许拖拽
        if not self.background_penetration and self.dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        self.dragging = False
    
    # 实现右键菜单功能（关闭和颜色切换）
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        # 关闭选项
        close_action = menu.addAction("关闭")
        close_action.triggered.connect(self.close)
        
        # 颜色切换选项
        color_menu = menu.addMenu("歌词颜色")
        colors = ["白色", "红色", "蓝色", "绿色", "黄色", "紫色"]
        for color in colors:
            color_action = color_menu.addAction(color)
            color_action.triggered.connect(lambda checked, c=color: self.change_lyric_color(c))
        
        menu.exec_(event.globalPos())
    
    def change_lyric_color(self, color):
        """更改歌词颜色"""
        # 颜色映射
        color_map = {
            "白色": "white",
            "红色": "red",
            "蓝色": "blue",
            "绿色": "green",
            "黄色": "yellow",
            "紫色": "purple"
        }
        
        # 获取颜色值
        color_value = color_map.get(color, "white")
        
        # 更新全局配置
        global FLOAT_LYRIC_TEXT_COLOR
        FLOAT_LYRIC_TEXT_COLOR = color_value
        
        # 更新标签样式
        self.update_lyric_style()
        
        # 保存配置到文件
        try:
            with open(__file__, 'r', encoding='utf-8') as f:
                content = f.read()
            # 使用正则表达式替换配置区的FLOAT_LYRIC_TEXT_COLOR的值，确保只匹配配置行
            import re
            # 只匹配以FLOAT_LYRIC_TEXT_COLOR开头的行，避免影响其他代码
            new_content = re.sub(r'^FLOAT_LYRIC_TEXT_COLOR\s*=\s*"[^"]*"', f'FLOAT_LYRIC_TEXT_COLOR = "{color_value}"', content, flags=re.MULTILINE)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"已将代码中的FLOAT_LYRIC_TEXT_COLOR修改为{color_value}")
        except Exception as e:
            print(f"修改代码文件时发生错误：{e}")
        
        print(f"切换歌词颜色为: {color}")
    
    def update_lyric_style(self):
        """更新歌词样式"""
        # 导入全局配置
        global FLOAT_LYRIC_TEXT_SIZE, FLOAT_LYRIC_TEXT_COLOR, FLOAT_LYRIC_TEXT_WEIGHT
        global FLOAT_LYRIC_TEXT_OPACITY
        global FLOAT_LYRIC_BACKGROUND_OPACITY, FLOAT_LYRIC_BORDER_RADIUS, FLOAT_LYRIC_PADDING
        global FLOAT_LYRIC_SHADOW_BLUR_RADIUS, FLOAT_LYRIC_SHADOW_OFFSET_X, FLOAT_LYRIC_SHADOW_OFFSET_Y
        global FLOAT_LYRIC_SHADOW_OPACITY
        
        # 以1080P为基准动态调整字体大小
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_height = screen_geometry.height()
        base_height = 1080  # 1080P的高度
        import math
        scale_factor = math.sqrt(screen_height / base_height)
        max_scale = 1.5
        scale_factor = min(scale_factor, max_scale)
        adjusted_text_size = int(FLOAT_LYRIC_TEXT_SIZE * scale_factor)
        
        # 处理文本颜色和透明度
        if FLOAT_LYRIC_TEXT_COLOR.lower() == "white":
            # 白色文本，应用透明度
            r, g, b = 255, 255, 255
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "red":
            r, g, b = 255, 100, 100  # 降低红色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "blue":
            r, g, b = 100, 100, 255  # 降低蓝色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "green":
            r, g, b = 100, 255, 100  # 降低绿色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "yellow":
            r, g, b = 255, 255, 100  # 降低黄色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "purple":
            r, g, b = 200, 100, 200  # 降低紫色饱和度
        else:
            # 其他颜色，暂不支持透明度，使用默认白色
            r, g, b = 255, 255, 255
        
        # 更新样式
        style = """
            QLabel {
                font-size: %dpx;
                color: rgba(%d, %d, %d, %f);
                font-weight: %d;
                background-color: rgba(0, 0, 0, %f);
                border-radius: %dpx;
                padding: %dpx;
            }
        """
        self.lyric_label.setStyleSheet(style % (
            adjusted_text_size, r, g, b, FLOAT_LYRIC_TEXT_OPACITY,
            FLOAT_LYRIC_TEXT_WEIGHT, FLOAT_LYRIC_BACKGROUND_OPACITY,
            FLOAT_LYRIC_BORDER_RADIUS, FLOAT_LYRIC_PADDING
        ))
    
    def show_with_animation(self, parsed_lyric=None, current_time=None):
        """
        带入场动画显示窗口
        :param parsed_lyric: 解析后的歌词列表（可选）
        :param current_time: 当前播放时间（秒）（可选）
        """
        # 检查是否有隐藏动画在运行，如果有则先停止它
        if hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running:
            self.hide_animation.stop()
        
        # 检查是否已经有显示动画在运行，如果有则不重复创建
        if hasattr(self, 'show_animation') and self.show_animation and self.show_animation.state() == QAbstractAnimation.Running:
            return
        
        # 如果提供了歌词数据，先更新窗口的歌词
        if parsed_lyric and current_time is not None:
            self.update_lyric(parsed_lyric, current_time)
        else:
            # 否则使用窗口内部的歌词数据
            self.display_current_lyric()
        
        # 强制重绘窗口，确保文字已经渲染
        self.repaint()
        
        # 先设置窗口位置在屏幕下方外
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = screen_geometry.height() + 100  # 屏幕下方外
        self.move(x, y)
        
        # 强制处理所有待处理的事件，确保歌词完全渲染
        QApplication.processEvents()
        
        # 创建动画
        from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
        self.show_animation = QPropertyAnimation(self, b"pos")
        self.show_animation.setDuration(500)  # 增加动画持续时间
        self.show_animation.setEasingCurve(QEasingCurve.OutCubic)  # 缓动曲线
        
        # 目标位置：屏幕底部上方指定距离
        global FLOAT_LYRIC_BOTTOM_MARGIN
        target_y = screen_geometry.height() - self.height() - FLOAT_LYRIC_BOTTOM_MARGIN
        self.show_animation.setEndValue(QPoint(x, target_y))

        # 动画结束后回调
        def on_show_animation_finished():
            self.visible = True
        
        self.show_animation.finished.connect(on_show_animation_finished)
        
        # 显示窗口（但还不在动画位置）
        self.show()
        
        # 启动动画
        self.show_animation.start()
    
    def hide_with_animation(self):
        """
        带出场动画隐藏窗口
        """
        # 检查是否已经有隐藏动画在运行，如果有则不重复创建
        if hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running:
            return
        
        # 创建动画
        from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
        self.hide_animation = QPropertyAnimation(self, b"pos")
        self.hide_animation.setDuration(500)  # 增加动画持续时间
        self.hide_animation.setEasingCurve(QEasingCurve.InCubic)  # 缓动曲线
        
        # 目标位置：屏幕下方外
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        target_y = screen_geometry.height() + 100  # 屏幕下方外
        self.hide_animation.setEndValue(QPoint(self.x(), target_y))
        
        # 动画结束后隐藏窗口
        def on_hide_animation_finished():
            self.hide()
        
        self.hide_animation.finished.connect(on_hide_animation_finished)
        
        # 启动动画
        self.hide_animation.start()

# 读秒悬浮窗口类
class CountdownFloatWindow(QWidget):
    """
    桌面读秒悬浮窗口，用于显示退出倒计时
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hide()
        
        self.setWindowTitle("读秒悬浮窗口")
        
        # 设置窗口属性
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 导入悬浮歌词配置参数
        global FLOAT_LYRIC_HEIGHT
        
        # 动态计算窗口宽度：屏幕宽度的3/4
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.dynamic_width = int(screen_geometry.width() * 0.75)
        
        # 设置窗口大小，使用悬浮歌词的高度
        self.setFixedSize(self.dynamic_width, FLOAT_LYRIC_HEIGHT)
        
        # 初始化UI
        self.init_ui()
        
        # 初始化拖拽相关属性
        self.dragging = False
        self.drag_position = QPoint()
        
        # 初始化动画相关属性
        self.show_animation = None
        self.hide_animation = None
        
        # 初始状态为隐藏
        self.visible = False
        
        # 将窗口默认位置设置到屏幕之外
        x = (screen_geometry.width() - self.width()) // 2
        y = screen_geometry.height() + 100  # 屏幕下方外
        self.move(x, y)
        
        # 确保窗口保持隐藏状态
        self.hide()
    
    def init_ui(self):
        """
        初始化UI
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # 导入悬浮歌词配置参数
        global FLOAT_LYRIC_TEXT_SIZE, FLOAT_LYRIC_TEXT_COLOR, FLOAT_LYRIC_TEXT_WEIGHT
        global FLOAT_LYRIC_TEXT_OPACITY
        global FLOAT_LYRIC_BACKGROUND_OPACITY, FLOAT_LYRIC_BORDER_RADIUS, FLOAT_LYRIC_PADDING
        global FLOAT_LYRIC_SHADOW_BLUR_RADIUS, FLOAT_LYRIC_SHADOW_OFFSET_X, FLOAT_LYRIC_SHADOW_OFFSET_Y
        global FLOAT_LYRIC_SHADOW_OPACITY, FLOAT_LYRIC_HEIGHT, FLOAT_LYRIC_BOTTOM_MARGIN
        
        # 以1080P为基准动态调整字体大小
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_height = screen_geometry.height()
        base_height = 1080  # 1080P的高度
        import math
        scale_factor = math.sqrt(screen_height / base_height)
        max_scale = 1.5
        scale_factor = min(scale_factor, max_scale)
        adjusted_text_size = int(FLOAT_LYRIC_TEXT_SIZE * scale_factor)  # 使用悬浮歌词的字体大小
        
        # 处理文本颜色和透明度
        if FLOAT_LYRIC_TEXT_COLOR.lower() == "white":
            r, g, b = 255, 255, 255
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "red":
            r, g, b = 255, 100, 100  # 降低红色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "blue":
            r, g, b = 100, 100, 255  # 降低蓝色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "green":
            r, g, b = 100, 255, 100  # 降低绿色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "yellow":
            r, g, b = 255, 255, 100  # 降低黄色饱和度
        elif FLOAT_LYRIC_TEXT_COLOR.lower() == "purple":
            r, g, b = 200, 100, 200  # 降低紫色饱和度
        else:
            r, g, b = 255, 255, 255
        
        # 创建弹簧，将标签推到底部
        from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)
        
        # 创建读秒标签
        self.countdown_label = QLabel("程序将在5秒后自动退出")
        self.countdown_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.countdown_label.setWordWrap(True)  # 支持自动换行
        style = """
            QLabel {
                font-size: %dpx;
                color: rgba(%d, %d, %d, %f);
                font-weight: %d;
                background-color: rgba(0, 0, 0, %f);
                border-radius: %dpx;
                padding: %dpx;
            }
        """
        self.countdown_label.setStyleSheet(style % (
            adjusted_text_size, r, g, b, FLOAT_LYRIC_TEXT_OPACITY,
            FLOAT_LYRIC_TEXT_WEIGHT, FLOAT_LYRIC_BACKGROUND_OPACITY,
            FLOAT_LYRIC_BORDER_RADIUS, FLOAT_LYRIC_PADDING
        ))
        
        # 添加文本阴影效果
        from PyQt5.QtWidgets import QGraphicsDropShadowEffect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(FLOAT_LYRIC_SHADOW_BLUR_RADIUS)
        shadow.setOffset(FLOAT_LYRIC_SHADOW_OFFSET_X, FLOAT_LYRIC_SHADOW_OFFSET_Y)
        shadow.setColor(QColor(0, 0, 0, FLOAT_LYRIC_SHADOW_OPACITY))
        self.countdown_label.setGraphicsEffect(shadow)
        
        layout.addWidget(self.countdown_label)
        self.setLayout(layout)
        
        # 确保窗口保持隐藏状态
        self.hide()
    
    def update_countdown(self, seconds):
        """
        更新倒计时显示
        :param seconds: 剩余秒数
        """
        message = f"程序将在{seconds}秒后自动退出\n单击专辑图取消退出"
        self.countdown_label.setText(message)
    
    # 实现拖拽功能
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if self.dragging and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        self.dragging = False
    
    def show_with_animation(self):
        """
        带入场动画显示窗口
        """
        # 检查是否有隐藏动画在运行，如果有则先停止它
        if hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running:
            self.hide_animation.stop()
        
        # 检查是否已经有显示动画在运行，如果有则不重复创建
        if hasattr(self, 'show_animation') and self.show_animation and self.show_animation.state() == QAbstractAnimation.Running:
            return
        
        # 强制重绘窗口
        self.repaint()
        
        # 先设置窗口位置在屏幕下方外
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = screen_geometry.height() + 100  # 屏幕下方外
        self.move(x, y)
        
        # 强制处理所有待处理的事件
        QApplication.processEvents()
        
        # 创建动画
        from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
        self.show_animation = QPropertyAnimation(self, b"pos")
        self.show_animation.setDuration(500)
        self.show_animation.setEasingCurve(QEasingCurve.OutCubic)
        
        # 目标位置：屏幕底部上方指定距离，使用悬浮歌词的底部边距
        global FLOAT_LYRIC_BOTTOM_MARGIN
        target_y = screen_geometry.height() - self.height() - FLOAT_LYRIC_BOTTOM_MARGIN
        self.show_animation.setEndValue(QPoint(x, target_y))

        # 动画结束后回调
        def on_show_animation_finished():
            self.visible = True
        
        self.show_animation.finished.connect(on_show_animation_finished)
        
        # 显示窗口
        self.show()
        
        # 启动动画
        self.show_animation.start()
    
    def hide_with_animation(self):
        """
        带出场动画隐藏窗口
        """
        # 检查是否已经有隐藏动画在运行，如果有则不重复创建
        if hasattr(self, 'hide_animation') and self.hide_animation and self.hide_animation.state() == QAbstractAnimation.Running:
            return
        
        # 创建动画
        from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
        self.hide_animation = QPropertyAnimation(self, b"pos")
        self.hide_animation.setDuration(500)
        self.hide_animation.setEasingCurve(QEasingCurve.InCubic)
        
        # 目标位置：屏幕下方外
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        target_y = screen_geometry.height() + 100  # 屏幕下方外
        self.hide_animation.setEndValue(QPoint(self.x(), target_y))
        
        # 动画结束后隐藏窗口
        def on_hide_animation_finished():
            self.hide()
        
        self.hide_animation.finished.connect(on_hide_animation_finished)
        
        # 启动动画
        self.hide_animation.start()

# 整合ultimate_lyric_getter.py中的get_lyric函数
def get_lyric(artist_name, track_name, file_path=""):
    """
    根据歌手名和歌曲名获取歌词（优先内嵌，其次本地，最后联网）
    :param artist_name: 歌手名
    :param track_name: 歌曲名
    :param file_path: 音频文件路径（可选）
    :return: 获取到的歌词，如果没有获取到则返回空字符串
    """
    print(f"[歌词搜索过程] 开始搜索歌词：{artist_name} - {track_name}")
    print(f"[歌词搜索过程] 内嵌歌词开关: {'开启' if EMBEDDED_LYRIC_ENABLED == 1 else '关闭'}")
    print(f"[歌词搜索过程] 本地歌词开关: {'开启' if LOCAL_LYRIC_ENABLED == 1 else '关闭'}")
    print(f"[歌词搜索过程] 联网歌词开关: {'开启' if NETWORK_LYRIC_ENABLED == 1 else '关闭'}")
    
    # 1. 优先尝试从音频文件内嵌获取歌词（如果开关开启）
    if EMBEDDED_LYRIC_ENABLED == 1:
        print("[歌词搜索过程] 尝试从音频文件内嵌获取歌词")
        # 如果没有提供文件路径，尝试自动搜索
        if not file_path:
            print("[歌词搜索过程] 没有提供文件路径，尝试自动搜索音频文件")
            file_path = search_audio_file(artist_name, track_name)
            if file_path:
                print(f"[歌词搜索过程] 找到音频文件: {file_path}")
            else:
                print("[歌词搜索过程] 未找到音频文件")
        
        if file_path:
            embedded_lyric = get_embedded_lyric(file_path)
            if embedded_lyric:
                print("[歌词搜索过程] 成功获取音频文件内嵌歌词")
                return embedded_lyric
            else:
                print("[歌词搜索过程] 未找到内嵌歌词")
    else:
        print("[歌词搜索过程] 内嵌歌词开关关闭，跳过内嵌歌词获取")
    
    # 2. 尝试获取本地歌词
    if LOCAL_LYRIC_ENABLED == 1:
        print("[歌词搜索过程] 尝试从本地获取歌词")
        local_lyric = get_local_lyric(artist_name, track_name)
        if local_lyric:
            print("[歌词搜索过程] 成功获取本地歌词")
            return local_lyric
        else:
            print("[歌词搜索过程] 未找到本地歌词")
    else:
        print("[歌词搜索过程] 本地歌词开关关闭，跳过本地歌词获取")
    
    # 3. 如果本地歌词获取失败，尝试联网获取
    # 如果联网获取歌词开关关闭，直接返回空字符串
    if NETWORK_LYRIC_ENABLED == 0:
        print("[歌词搜索过程] 联网获取歌词已关闭，跳过联网歌词获取")
        return ""
    else:
        print("[歌词搜索过程] 尝试联网获取歌词")
        try:
            # 使用 MusicLyricDownloader 获取歌词
            downloader = MusicLyricDownloader()
            
            # 构建搜索关键词
            search_keyword = f"{artist_name} {track_name}"
            print(f"[歌词搜索过程] 搜索关键词: {search_keyword}")
            
            # 搜索歌曲
            results = []
            results.extend(downloader.search_netease(search_keyword))
            results.extend(downloader.search_qq(search_keyword))
            
            if results:
                print(f"[歌词搜索过程] 找到 {len(results)} 个搜索结果")
                
                # 过滤结果，排除Live、纯音乐等类型
                filtered_results = []
                for result in results:
                    title_lower = result['title'].lower()
                    # 排除包含以下关键词的结果
                    if any(keyword in title_lower for keyword in ['live', 'instrumental', '纯音乐', '伴奏', 'off vocal']):
                        continue
                    filtered_results.append(result)
                
                # 如果过滤后没有结果，使用原始结果
                if not filtered_results:
                    filtered_results = results
                
                # 显示全部候选歌词列表
                print("[歌词搜索过程] 候选歌词列表:")
                for i, result in enumerate(filtered_results):
                    print(f"[歌词搜索过程] 候选 {i+1}: {result['title']} - {result['artist']} ({result['source']})")
                
                # 按顺序尝试获取歌词
                for i, result in enumerate(filtered_results):
                    print(f"[歌词搜索过程] 选择第 {i+1} 个结果: {result['title']} - {result['artist']} ({result['source']})")
                    
                    # 获取歌词
                    if result['source'] == '网易云':
                        lyric = downloader.get_netease_lyric(result['id'])
                    else:
                        lyric = downloader.get_qq_lyric(result['mid'])
                    
                    if lyric and lyric != '暂无歌词':
                        print("[歌词搜索过程] 成功获取联网歌词")
                        return lyric
                    else:
                        print(f"[歌词搜索过程] 第 {i+1} 个结果未找到歌词，尝试下一个")
                
                print("[歌词搜索过程] 所有结果都未找到歌词")
            else:
                print("[歌词搜索过程] 联网搜索无结果")
        except Exception as e:
            # 发生错误时返回空字符串，不影响主程序运行
            print(f"[歌词搜索过程] 获取联网歌词时发生错误: {e}")
    
    print("[歌词搜索过程] 未找到任何歌词")
    return ""


class AudioCaptureThread(QThread):
    """音频捕获线程 - 用于真实音频可视化"""
    audio_data_signal = pyqtSignal(np.ndarray)  # 发送音频数据数组
    
    def __init__(self):
        super().__init__()
        self.is_running = False
        self.sample_rate = 44100  # 采样率
        self.chunk_size = 4096  # 每次捕获的音频数据大小，增大缓冲区以减少数据不连续警告
        self.device = None  # 默认设备
        self.is_capturing = False  # 标记是否正在捕获音频
        self.mic_session = None  # 麦克风会话
    
    def run(self):
        """运行音频捕获"""
        self.is_running = True
        self.is_capturing = True
        
        try:
            # 1. 屏蔽 soundcard 抛出的特定警告，避免刷屏
            import warnings
            import soundcard as sc
            warnings.filterwarnings("ignore", category=sc.SoundcardRuntimeWarning)
            
            # 2. 获取所有麦克风（包括回环设备）
            all_mics = sc.all_microphones(include_loopback=True)
            
            # 获取默认播放器的名称，用来做匹配
            default_speaker = sc.default_speaker()
            print(f"[音频捕获] 当前默认输出设备 (扬声器): {default_speaker.name}")

            target_mic = None

            # 3. 打印所有可选的录制设备，并寻找匹配项
            print("[音频捕获] 可用录制设备列表:")
            for i, m in enumerate(all_mics):
                print(f"[音频捕获] [{i}] {m.name}")
                # 匹配逻辑：名称里包含 'Loopback' 或者 包含扬声器的名称
                if "loopback" in m.name.lower() or default_speaker.name in m.name:
                    target_mic = m

            print("[音频捕获] " + "-" * 30)

            # 4. 如果没自动找到，选择最后一个设备（通常是 Loopback）
            if not target_mic:
                print("[音频捕获] 未自动识别到回环设备，使用最后一个设备")
                target_mic = all_mics[-1]
            else:
                print(f"[音频捕获] 已自动选择匹配设备: {target_mic.name}")

            # 5. 开始捕获
            print("[音频捕获] 开始捕获系统音频...")
            with target_mic.recorder(samplerate=self.sample_rate) as mic_session:
                self.mic_session = mic_session
                while self.is_running:
                    # 捕获数据
                    data = mic_session.record(numframes=self.chunk_size)
                    
                    # 处理音频数据
                    if data.size > 0:
                        # 转换为单声道
                        if data.shape[1] > 1:
                            data = np.mean(data, axis=1, keepdims=True)
                        # 发送音频数据
                        self.audio_data_signal.emit(data)
                    
                    # 短暂休眠，避免CPU占用过高
                    self.msleep(5)
        except Exception as e:
            print(f"[音频捕获] 捕获过程中出错: {e}")
        finally:
            # 确保会话被关闭
            self.mic_session = None
            self.is_capturing = False
            self.is_running = False
    
    def start_capture(self):
        """开始音频捕获"""
        if not self.is_capturing:
            print("[音频捕获] 开始音频捕获")
            self.is_capturing = True
            self.start()
    
    def stop_capture(self):
        """停止音频捕获"""
        if self.is_capturing:
            print("[音频捕获] 停止音频捕获")
            self.is_running = False
            # 设置一个较短的超时时间，避免阻塞
            self.wait(200)  # 等待最多200ms
            self.is_capturing = False
    
    def is_capture_running(self):
        """检查音频捕获是否正在进行"""
        return self.is_capturing


class MediaInfoThread(QThread):
    """媒体信息获取线程"""
    media_info_signal = pyqtSignal(str, object)  # 第二个参数可以是字节数组或None
    
    def run(self):
        """运行媒体信息获取"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        media_info, album_art_bytes = loop.run_until_complete(self.get_media_info())
        loop.close()
        self.media_info_signal.emit(media_info, album_art_bytes)
    
    async def get_album_art(self, media_properties):
        """获取专辑图字节数组"""
        album_art_bytes = None
        try:
            # 尝试获取缩略图
            if hasattr(media_properties, 'thumbnail'):
                thumbnail = media_properties.thumbnail
                
                if thumbnail is not None:
                    # 打开读取流
                    stream = await thumbnail.open_read_async()
                    # 获取流大小
                    size = stream.size
                    
                    if size > 0:
                        # 获取输入流
                        reader = stream.get_input_stream_at(0)
                        # 创建数据读取器
                        data_reader = DataReader(reader)
                        # 加载数据
                        await data_reader.load_async(size)
                        # 直接读取字节数组
                        album_art_bytes = bytearray(size)
                        data_reader.read_bytes(album_art_bytes)
        except Exception as e:
            pass
        return album_art_bytes
    
    async def get_media_info(self):
        """使用Windows系统媒体API获取当前媒体播放信息"""
        album_art_bytes = None
        try:
            # 获取媒体会话管理器
            manager = await MediaManager.request_async()
            
            # 获取所有会话
            sessions = manager.get_sessions()
            
            result = "=== 当前媒体播放信息 ===\n\n"
            
            # 初始化album_art_bytes为None，确保始终有返回值
            album_art_bytes = None
            
            # 过滤掉没有有效媒体信息的会话
            valid_sessions = []
            for session in sessions:
                try:
                    media_properties = await session.try_get_media_properties_async()
                    if media_properties:
                        title = getattr(media_properties, "title", "")
                        # 检查是否有有效标题或播放进度
                        timeline = session.get_timeline_properties()
                        has_valid_progress = False
                        if timeline and hasattr(timeline, 'position') and hasattr(timeline, 'end_time'):
                            if hasattr(timeline.position, 'total_seconds'):
                                position = timeline.position.total_seconds()
                                end_time = timeline.end_time.total_seconds()
                                has_valid_progress = end_time > 0
                        
                        # 如果有标题或有效进度，认为是有效会话
                        if title and title != "PotPlayer" or has_valid_progress:
                            valid_sessions.append(session)
                except Exception as e:
                    pass
            
            if valid_sessions:
                result += f"检测到 {len(valid_sessions)} 个有效媒体会话\n\n"
                
                # 只处理第一个有效会话，避免多个会话导致的混淆
                session = valid_sessions[0]
                try:
                    result += f"--- 会话 1 ---\n"
                    app_id = session.source_app_user_model_id
                    result += f"应用ID: {app_id}\n"
                    
                    # 获取播放信息
                    playback_info = session.get_playback_info()
                    
                    # 获取播放状态
                    status_value = playback_info.playback_status
                    
                    # 获取媒体属性
                    media_properties = await session.try_get_media_properties_async()
                    
                    # 获取播放位置
                    has_valid_playback = False
                    position = 0
                    end_time = 0
                    try:
                        timeline = session.get_timeline_properties()
                        if timeline and hasattr(timeline, 'position') and hasattr(timeline, 'end_time'):
                            if hasattr(timeline.position, 'total_seconds'):
                                position = timeline.position.total_seconds()
                                end_time = timeline.end_time.total_seconds()
                                has_valid_playback = end_time > 0
                    except Exception as e:
                        print(f"获取播放进度时出错: {type(e).__name__}: {e}")
                        pass
                    
                    # 状态映射 - 结合系统状态和实际播放情况
                    # 根据用户反馈，状态值5表示暂停状态
                    status_map = {
                        0: "停止播放",
                        1: "正在播放",
                        2: "暂停播放",
                        3: "正在打开",
                        4: "正在播放",
                        5: "暂停播放",  # 新增：状态值5表示暂停状态
                        6: "正在改变"   # 新增：处理其他可能的状态
                    }
                    
                    # 初始状态使用系统返回值
                    status_text = status_map.get(status_value, f"未知状态 ({status_value})")
                    
                    # 优化状态判断
                    if media_properties:
                        title = getattr(media_properties, "title", "")
                        # 如果标题为空或为"PotPlayer"且没有有效播放进度，认为已停止
                        if (not title or title == "PotPlayer") and not has_valid_playback:
                            status_text = "已停止"
                        # 如果有有效播放进度但状态显示正在播放，检查是否真的在播放
                        elif has_valid_playback and status_text == "正在播放":
                            # 如果进度为00:00/00:00，认为已停止
                            if end_time == 0:
                                status_text = "已停止"
                    else:
                        # 没有媒体属性，认为已停止
                        status_text = "已停止"
                    
                    result += f"状态: {status_text}\n"
                    
                    # 获取系统音量信息
                    volume_text = "无法获取"
                    try:
                        from pycaw.pycaw import AudioUtilities
                        
                        # 获取默认音频设备并直接访问EndpointVolume属性
                        default_device = AudioUtilities.GetSpeakers()
                        volume = default_device.EndpointVolume
                        
                        # 获取音量值（范围0.0到1.0）
                        current_volume = volume.GetMasterVolumeLevelScalar()
                        # 转换为百分比格式，使用四舍五入而不是截断
                        volume_percent = round(current_volume * 100)
                        volume_text = f"{volume_percent}%"
                    except Exception as e:
                        pass
                    result += f"系统音量: {volume_text}\n"
                    
                    # 移除应用音量信息获取
                    
                    if media_properties:
                        # 直接访问已知属性 - 移除专辑信息
                        title = getattr(media_properties, "title", "未知")
                        artist = getattr(media_properties, "artist", "未知")
                        
                        # 尝试获取文件路径
                        file_path = ""
                        try:
                            # 尝试不同的属性名获取文件路径
                            file_path = getattr(media_properties, "path", "")
                            if not file_path:
                                file_path = getattr(media_properties, "file_path", "")
                            if not file_path:
                                file_path = getattr(media_properties, "local_path", "")
                        except Exception as e:
                            pass
                        
                        # 输出关键媒体信息
                        result += f"歌曲: {title}\n"
                        result += f"歌手: {artist}\n"
                        if file_path:
                            result += f"文件路径: {file_path}\n"
                        
                        # 获取专辑图
                        try:
                            album_art_bytes = await self.get_album_art(media_properties)
                        except Exception as e:
                            album_art_bytes = None
                        
                        # 显示播放位置
                        if has_valid_playback:
                            pos_min, pos_sec = divmod(int(position), 60)
                            end_min, end_sec = divmod(int(end_time), 60)
                            result += f"进度: {pos_min:02d}:{pos_sec:02d} / {end_min:02d}:{end_sec:02d}\n"
                        else:
                            result += f"进度: 00:00 / 00:00\n"
                    else:
                        result += f"歌曲: 未知\n"
                        result += f"歌手: 未知\n"
                        result += f"专辑: 未知\n"
                        result += f"进度: 00:00 / 00:00\n"
                        # 没有媒体属性时，重置专辑图为None
                        album_art_bytes = None
                    
                    result += "\n"
                except Exception as e:
                    result += f"处理会话时出错: {type(e).__name__}\n\n"
            else:
                result += "没有检测到媒体会话\n"
                
            return result, album_art_bytes
        except Exception as e:
            error_msg = f"错误: {type(e).__name__}\n详细信息: {e}\n"
            return error_msg, None


class DynamicIslandWidget(QWidget):
    """灵动岛模式UI组件"""
    # 添加信号，用于在主线程中更新歌词
    update_lyric_signal = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        # 连接信号和槽
        self.update_lyric_signal.connect(self._update_lyric_display)
        # 初始化所有需要在init_ui中使用的属性
        # 歌曲名滚动相关属性
        self.song_scroll_offset = 0  # 滚动偏移量
        self.song_scroll_direction = 1  # 滚动方向：1向右，-1向左
        self.song_scroll_timer = QTimer(self)  # 滚动定时器
        self.song_scroll_interval = 50  # 滚动更新间隔（ms）
        self.song_scroll_speed = 1  # 每次滚动的像素数
        self.song_original_text = ""  # 原始完整歌曲名
        self.song_display_width = 0  # 歌曲名显示区域宽度
        self.song_text_width = 0  # 歌曲名文本总宽度
        self.song_scroll_needed = False  # 是否需要滚动
        self.song_scroll_pause_time = 2000  # 滚动到边界后的停顿时间（ms）
        self.song_scroll_state = 0  # 滚动状态：0-初始/停顿，1-滚动中
        
        # 歌词相关属性
        self.current_lyric = ""  # 当前歌词
        self.current_artist = ""  # 当前歌手名
        self.lyric_update_timer = QTimer(self)  # 歌词更新定时器
        self.lyric_update_interval = 200  # 缩短歌词更新间隔（ms），提高响应速度
        self.lyric_update_timer.setInterval(self.lyric_update_interval)
        self.lyric_update_timer.timeout.connect(self._update_lyric_by_progress)
        self.lyric_update_timer.start()  # 启动歌词更新定时器
        self.last_countdown_second = -1  # 上一次输出的倒计时秒数，用于避免重复输出
        
        # 悬浮歌词窗口相关属性
        self.float_lyric_window = None  # 悬浮歌词窗口实例
        self.float_lyric_window_visible = False  # 悬浮歌词窗口是否可见
        self.old_parsed_lyric = []  # 上一首歌曲的歌词，用于动画期间显示
        self.float_lyric_animating = False  # 标记悬浮歌词动画是否正在播放
        
        # 读秒悬浮窗口相关属性
        self.countdown_float_window = None  # 读秒悬浮窗口实例
        self.countdown_float_window_visible = False  # 读秒悬浮窗口是否可见
        
        # 专辑图旋转相关属性
        self.rotation_angle = 0  # 当前旋转角度
        self.target_rotation_angle = 0  # 目标旋转角度（仅在调整时间时使用）
        self.rotation_smoothness = 0.2  # 旋转平滑系数（0-1，值越大越平滑）
        self.is_adjusting_time = False  # 是否正在调整时间（需要平滑过渡）
        
        # 用于平滑过渡的额外属性
        self.last_progress_seconds = 0  # 上一次的进度秒数
        from PyQt5.QtCore import QDateTime
        self.last_rotation_update_time = QDateTime.currentMSecsSinceEpoch()  # 上一次更新旋转的时间（初始化为当前时间）
        self.estimated_total_seconds = 0  # 估计的总时长秒数
        
        # 添加平滑旋转定时器
        self.rotation_smooth_timer = QTimer(self)
        self.rotation_smooth_timer.setInterval(30)  # 33fps，提供流畅的视觉效果
        self.rotation_smooth_timer.timeout.connect(self.update_smooth_rotation)
        self.rotation_smooth_timer.start()  # 持续运行，实现平滑过渡
        
        # 保存上一次的专辑图数据，用于检测变化
        self.last_album_art_bytes = None
        # 保存原始专辑图数据，用于旋转绘制
        self.original_album_art = None
        
        # 保存当前歌曲名和歌手名，用于检测下一曲
        self.current_song = ""
        self.current_artist = ""
        # 主动隐藏标志 - 用于区分用户主动隐藏和自动隐藏
        self.actively_hidden = False
        
        # 歌词相关属性
        self.lyric_cache = {}  # 歌词缓存，格式：{"歌手-歌曲": "歌词"}
        self.parsed_lyric_cache = {}  # 解析后的歌词缓存，格式：{"歌手-歌曲": [(时间(秒), 歌词内容), ...]}
        self.lyric_fetch_count = {}  # 歌词获取次数，格式：{"歌手-歌曲": 次数}
        self.current_parsed_lyric = []  # 当前歌曲解析后的歌词
        self.lyric_timer = QTimer(self)  # 歌词获取延时定时器
        self.lyric_timer.setSingleShot(True)  # 只执行一次
        self.current_lyric_task = None  # 当前等待执行的歌词获取任务
        
        # 初始化音频可视化定时器
        self.visualization_timer = QTimer(self)
        self.visualization_timer.timeout.connect(self.update_visualization)
        self.visualization_timer.start(50)  # 每50ms更新一次
        
        # 保存播放状态
        self.is_playing = False
        # 保存停止状态
        self.is_stopped = True
        
        # 初始化音频数据相关变量
        self.audio_data = np.zeros(1024)  # 音频数据
        self.fft_data = np.zeros(5)  # FFT数据，用于5个柱状条
        
        # 初始化音频可视化样式索引
        global VISUALIZATION_STYLE
        self.visualization_style = VISUALIZATION_STYLE  # 3: 圆形频谱样式(第4个), 4: 波浪形样式(第5个), 5: 关闭
        
        # 初始化音频捕获线程，但不自动启动
        self.audio_thread = AudioCaptureThread()
        self.audio_thread.audio_data_signal.connect(self.process_audio_data)
        
        # 初始化动画对象
        self.init_animations()
        
        # 初始状态为隐藏
        self.hide()
        self.is_visible = False
        
        # 保存初始位置
        self.initial_y = 20
        self.offscreen_y = -100  # 画面外位置
        self.move(self.x(), self.offscreen_y)
        
        # 全屏应用检测定时器
        self.fullscreen_detection_timer = QTimer(self)
        self.fullscreen_detection_timer.timeout.connect(self.check_fullscreen_app)
        self.fullscreen_detection_timer.start(300)  # 每300毫秒检测一次，提高响应速度
        self.last_fullscreen_state = None  # 保存上一次的全屏检测结果
        
        # 退出程序倒计时相关
        self.exit_timer = QTimer(self)
        self.exit_countdown = 5
        self.exit_timer.timeout.connect(self.update_exit_countdown)
        
        # 双击检测相关
        self.last_click_time = 0
        self.click_count = 0
        
        # 调用init_ui初始化UI
        self.init_ui()
        
    def init_ui(self):
        """初始化灵动岛UI"""
        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 设置窗口透明度
        global DYNAMIC_ISLAND_OPACITY
        self.setWindowOpacity(DYNAMIC_ISLAND_OPACITY)
        
        # 设置固定大小，适合三段式布局 - 调整为350x65
        self.setFixedSize(350, 65)
        
        # 创建主布局 - 左中右三段式
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)  # 减小左中右三个部分之间的间距
        
        # 左侧：专辑图 - 创建一个自定义的圆形专辑图控件
        self.left_section = QWidget(self)
        self.left_section.setFixedSize(45, 45)
        
        # 创建一个空白的QPixmap作为初始专辑图
        initial_pixmap = QPixmap(45, 45)
        initial_pixmap.fill(Qt.transparent)
        painter = QPainter(initial_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        
        # 绘制初始的圆形背景
        painter.setBrush(QColor(51, 51, 51))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QRectF(0, 0, 45, 45))
        
        # 绘制音乐图标
        font = painter.font()
        font.setPointSize(20)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(QRectF(0, 0, 45, 45), Qt.AlignCenter, "🎵")
        painter.end()
        
        # 创建最终的专辑图标签
        self.album_art = QLabel(self.left_section)
        self.album_art.setGeometry(0, 0, 45, 45)
        self.album_art.setAlignment(Qt.AlignCenter)
        # 设置鼠标指针为手型，提示可点击
        self.album_art.setCursor(Qt.PointingHandCursor)
        # 添加点击事件处理
        self.album_art.mousePressEvent = self.on_album_art_clicked
        # 使用抗锯齿圆形样式
        self.album_art.setPixmap(initial_pixmap)
        
        # 应用高质量的圆形遮罩
        # 创建一个高质量的圆形遮罩
        mask_pixmap = QPixmap(45, 45)
        mask_pixmap.fill(Qt.transparent)
        mask_painter = QPainter(mask_pixmap)
        mask_painter.setRenderHint(QPainter.Antialiasing, True)
        mask_painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        
        # 绘制一个抗锯齿的白色圆形
        mask_painter.setBrush(QColor(255, 255, 255))
        mask_painter.setPen(Qt.NoPen)
        mask_painter.drawEllipse(QRectF(0.5, 0.5, 44, 44))  # 微调位置，避免锯齿
        mask_painter.end()
        
        # 应用遮罩
        self.album_art.setMask(mask_pixmap.createMaskFromColor(Qt.transparent))
        self.main_layout.addWidget(self.left_section)
        
        # 中间：使用绝对定位，让元素可以重叠显示
        self.middle_section = QWidget(self)
        self.middle_section.setFixedSize(180, 45)  # 设置固定大小，确保有足够空间显示所有元素
        
        # 1. 歌曲名 - 独立模块，向上移动以避开歌手名
        self.song_label = QLabel(self.middle_section)
        self.song_label.setStyleSheet("QLabel { color: rgba(255, 255, 255, 0.3); font-family: 'Microsoft YaHei UI', 'Segoe UI', sans-serif; font-size: 12px; font-weight: bold; background: transparent; letter-spacing: 0.3px; border: none; }")
        self.song_label.setText("- 歌曲 - ")
        self.song_label.setAlignment(Qt.AlignCenter)
        self.song_label.setFixedSize(180, 15)  # 固定高度，确保完整显示
        self.song_label.move(0, 0)  # 绝对定位，距离顶部0px，向上移动5px
        # 设置鼠标指针为手型，提示可双击
        self.song_label.setCursor(Qt.PointingHandCursor)
        # 添加双击事件处理
        self.song_label.mouseDoubleClickEvent = self.toggle_float_lyric_window
        
        # 2. 歌手名 - 独立模块，调整位置与歌曲名形成适当间距
        self.artist_label = QLabel(self.middle_section)
        self.artist_label.setStyleSheet("QLabel { color: rgba(255, 255, 255, 0.25); font-family: 'Microsoft YaHei UI', 'Segoe UI', sans-serif; font-size: 10px; font-weight: bold; background: transparent; letter-spacing: 0.2px; border: none; }")
        self.artist_label.setText("- 歌手 - ")
        self.artist_label.setAlignment(Qt.AlignCenter)
        self.artist_label.setFixedSize(180, 15)  # 固定高度，确保完整显示
        self.artist_label.move(0, 12)  # 绝对定位，距离顶部12px，与歌曲名保持3px间距
        # 设置鼠标指针为手型，提示可双击
        self.artist_label.setCursor(Qt.PointingHandCursor)
        # 添加双击事件处理
        self.artist_label.mouseDoubleClickEvent = self.toggle_float_lyric_window
        
        # 3. 播放控件 - 独立模块，允许与歌手名重叠
        # 上一曲按钮
        self.prev_button = QPushButton("◀◀", self.middle_section)
        self.prev_button.setStyleSheet(
            "QPushButton { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-size: 14px; font-weight: bold; outline: none; }"
            "QPushButton:hover { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:focus { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:pressed { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
        )
        self.prev_button.clicked.connect(self.prev_track)
        self.prev_button.setFixedSize(25, 25)
        self.prev_button.move(50, 25)  # 绝对定位，距离左侧50px，顶部25px
        
        # 播放/暂停按钮
        self.play_pause_button = QPushButton("▶", self.middle_section)
        self.play_pause_button.setStyleSheet(
            "QPushButton { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-size: 16px; font-weight: bold; outline: none; }"
            "QPushButton:hover { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:focus { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:pressed { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
        )
        self.play_pause_button.clicked.connect(self.play_pause)
        self.play_pause_button.setFixedSize(25, 25)
        self.play_pause_button.move(80, 25)  # 绝对定位，距离左侧80px，顶部25px
        
        # 下一曲按钮
        self.next_button = QPushButton("▶▶", self.middle_section)
        self.next_button.setStyleSheet(
            "QPushButton { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-size: 14px; font-weight: bold; outline: none; }"
            "QPushButton:hover { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:focus { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
            "QPushButton:pressed { color: rgba(255, 255, 255, 0.1); background: transparent; border: none; font-weight: bold; outline: none; }"
        )
        self.next_button.clicked.connect(self.next_track)
        self.next_button.setFixedSize(25, 25)
        self.next_button.move(110, 25)  # 绝对定位，距离左侧110px，顶部25px
        
        # 初始化滚动定时器
        self.song_scroll_timer.setInterval(self.song_scroll_interval)
        self.song_scroll_timer.timeout.connect(self.update_song_scroll)
        
        self.main_layout.addWidget(self.middle_section, 1)
        
        # 右侧：音频可视化
        self.right_section = QWidget(self)
        self.right_section.setFixedSize(55, 45)
        # 设置鼠标指针为手型，提示可点击
        self.right_section.setCursor(Qt.PointingHandCursor)
        # 添加点击事件处理
        self.right_section.mousePressEvent = self.toggle_visualization_style
        
        self.visualization_layout = QHBoxLayout(self.right_section)
        self.visualization_layout.setContentsMargins(8, 5, 8, 5)
        self.visualization_layout.setSpacing(2)  # 减小间距
        
        # 创建可视化条 - 5个，缩小宽度
        self.visualization_bars = []
        for i in range(5):
            bar = QWidget(self.right_section)
            bar.setFixedSize(6, 10)  # 缩小宽度为6像素
            bar.setStyleSheet("QWidget { background-color: #4CAF50; border-radius: 2px; }")
            self.visualization_bars.append(bar)
            self.visualization_layout.addWidget(bar)
        
        self.main_layout.addWidget(self.right_section)
    
    def init_animations(self):
        """初始化动画对象"""
        # 进场动画 - 从画面外移动到固定位置
        self.enter_animation = QPropertyAnimation(self, b"pos")
        self.enter_animation.setDuration(500)  # 动画持续时间500ms
        self.enter_animation.setEasingCurve(QEasingCurve.OutCubic)  # 缓动曲线
        
        # 出场动画 - 从固定位置移动到画面外
        self.exit_animation = QPropertyAnimation(self, b"pos")
        self.exit_animation.setDuration(500)  # 动画持续时间500ms
        self.exit_animation.setEasingCurve(QEasingCurve.InCubic)  # 缓动曲线
        self.exit_animation.finished.connect(self.on_exit_animation_finished)
    
    def show_with_animation(self):
        """带进场动画显示"""
        if not self.is_visible:
            self.is_visible = True
            
            # 设置动画起始和结束位置
            start_pos = self.pos()
            end_pos = QPoint(start_pos.x(), self.initial_y)
            
            # 停止可能正在运行的动画
            self.exit_animation.stop()
            
            # 设置进场动画
            self.enter_animation.setStartValue(QPoint(start_pos.x(), self.offscreen_y))
            self.enter_animation.setEndValue(end_pos)
            
            # 显示窗口并启动动画
            self.show()
            self.enter_animation.start()
    
    def hide_with_animation(self):
        """带出场动画隐藏"""
        if self.is_visible:
            self.is_visible = False
            
            # 设置动画起始和结束位置
            start_pos = self.pos()
            end_pos = QPoint(start_pos.x(), self.offscreen_y)
            
            # 停止可能正在运行的动画
            self.enter_animation.stop()
            
            # 设置出场动画
            self.exit_animation.setStartValue(start_pos)
            self.exit_animation.setEndValue(end_pos)
            
            # 启动动画
            self.exit_animation.start()
    
    def on_exit_animation_finished(self):
        """出场动画结束后调用"""
        # 动画结束后隐藏窗口
        self.hide()
    
    def is_fullscreen_or_maximized(self):
        """检查当前是否有全屏或最大化应用，并返回导致全屏的窗口信息"""
        try:
            # 获取当前焦点窗口
            foreground_hwnd = user32.GetForegroundWindow()
            
            if foreground_hwnd:
                # 获取焦点窗口的标题
                title = ctypes.create_string_buffer(255)
                user32.GetWindowTextA(foreground_hwnd, title, 255)
                window_title = title.value.decode('gbk', errors='ignore')
                
                # 先检查窗口标题是否为系统窗口
                if window_title not in ['Program Manager', '', 'File Explorer', 'Task Switching', 'Windows 输入体验'] and 'NVIDIA GeForce Overlay' not in window_title:
                    # 获取窗口进程名
                    process_id = ctypes.c_ulong()
                    user32.GetWindowThreadProcessId(foreground_hwnd, ctypes.byref(process_id))
                    h_process = ctypes.windll.kernel32.OpenProcess(0x400 | 0x10, False, process_id.value)
                    process_name = ""
                    if h_process:
                        exe_path = ctypes.create_string_buffer(255)
                        if ctypes.windll.psapi.GetModuleFileNameExA(h_process, None, exe_path, 255):
                            process_name = exe_path.value.decode('gbk', errors='ignore').split('\\')[-1]
                        ctypes.windll.kernel32.CloseHandle(h_process)
                    
                    # 检查进程名是否为触摸键盘应用
                    if process_name != 'TabTip.exe':
                        # 检查窗口是否最大化
                        style = user32.GetWindowLongA(foreground_hwnd, GWL_STYLE)
                        is_maximized = (style & WS_MAXIMIZE) != 0
                        
                        # 检查窗口是否全屏（占据整个屏幕）
                        rect = RECT()
                        user32.GetWindowRect(foreground_hwnd, ctypes.byref(rect))
                        
                        # 获取屏幕尺寸
                        screen_width = user32.GetSystemMetrics(0)  # SM_CXSCREEN
                        screen_height = user32.GetSystemMetrics(1)  # SM_CYSCREEN
                        
                        # 计算窗口尺寸
                        window_width = rect.right - rect.left
                        window_height = rect.bottom - rect.top
                        
                        # 检查是否全屏（考虑窗口边框，允许10像素误差）
                        is_fullscreen = (abs(window_width - screen_width) <= 10 and 
                                       abs(window_height - screen_height) <= 10)
                        
                        if is_maximized or is_fullscreen:
                            fullscreen_window_info = f"{window_title} ({process_name}) [{'全屏' if is_fullscreen else '最大化'}]"
                            return True, fullscreen_window_info
            
            # 检查焦点窗口是否是某个全屏程序的子窗口
            # 获取焦点窗口的父窗口
            parent_hwnd = user32.GetParent(foreground_hwnd)
            while parent_hwnd:
                # 获取父窗口标题
                title = ctypes.create_string_buffer(255)
                user32.GetWindowTextA(parent_hwnd, title, 255)
                window_title = title.value.decode('gbk', errors='ignore')
                
                # 排除系统窗口，如Program Manager（explorer.exe）
                if window_title in ['Program Manager']:
                    parent_hwnd = user32.GetParent(parent_hwnd)
                    continue
                
                # 检查父窗口是否全屏
                rect = RECT()
                user32.GetWindowRect(parent_hwnd, ctypes.byref(rect))
                
                # 获取屏幕尺寸
                screen_width = user32.GetSystemMetrics(0)  # SM_CXSCREEN
                screen_height = user32.GetSystemMetrics(1)  # SM_CYSCREEN
                
                # 计算窗口尺寸
                window_width = rect.right - rect.left
                window_height = rect.bottom - rect.top
                
                # 检查是否全屏（考虑窗口边框，允许10像素误差）
                is_fullscreen = (abs(window_width - screen_width) <= 10 and 
                               abs(window_height - screen_height) <= 10)
                
                if is_fullscreen:
                    # 获取父窗口进程名
                    process_id = ctypes.c_ulong()
                    user32.GetWindowThreadProcessId(parent_hwnd, ctypes.byref(process_id))
                    h_process = ctypes.windll.kernel32.OpenProcess(0x400 | 0x10, False, process_id.value)
                    process_name = ""
                    if h_process:
                        exe_path = ctypes.create_string_buffer(255)
                        if ctypes.windll.psapi.GetModuleFileNameExA(h_process, None, exe_path, 255):
                            process_name = exe_path.value.decode('gbk', errors='ignore').split('\\')[-1]
                        ctypes.windll.kernel32.CloseHandle(h_process)
                    
                    fullscreen_window_info = f"{window_title} ({process_name}) [全屏]"
                    return True, fullscreen_window_info
                
                # 继续获取上一级父窗口
                parent_hwnd = user32.GetParent(parent_hwnd)
            
            # 如果焦点窗口不是全屏或最大化，且不是全屏程序的子窗口，则返回False
            return False, ""
        except Exception as e:
            print(f"全屏检测错误: {e}")
        return False, ""
    
    def check_fullscreen_app(self):
        """检测是否有全屏或最大化应用，同时控制悬浮歌词的显示和隐藏"""
        # 调用新的检测方法
        has_fullscreen_app, fullscreen_window_info = self.is_fullscreen_or_maximized()
        
        # 只有当检测结果变化时才执行操作
        if self.last_fullscreen_state != has_fullscreen_app:
            if has_fullscreen_app:
                print(f"[全屏检测] 状态变化: 有全屏/最大化应用")
                print(f"[全屏检测] 导致全屏的应用: {fullscreen_window_info}")
                # 隐藏灵动岛
                if self.is_visible and not self.actively_hidden:
                    self.hide_with_animation()
                # 隐藏悬浮歌词
                if self.float_lyric_window_visible:
                    if self.float_lyric_window:
                        self.float_lyric_window.hide_with_animation()
                    self.float_lyric_window_visible = False
            else:
                print(f"[全屏检测] 状态变化: 无全屏/最大化应用")
                # 检查媒体是否在播放
                if self.is_playing and not self.is_visible and not self.actively_hidden:
                    self.show_with_animation()
                # 显示悬浮歌词（如果开启且不是主动隐藏状态，且正在播放）
                if FLOAT_LYRIC_ENABLED == 1 and not self.float_lyric_window_visible and self.current_parsed_lyric and not self.actively_hidden and self.is_playing:
                    # 检查当前时间段是否有歌词
                    current_seconds = self.last_progress_seconds
                    adjusted_seconds = current_seconds + LYRIC_OFFSET
                    
                    # 特殊处理：如果当前进度接近0秒，不显示任何歌词，避免切换歌曲时显示0.00秒的歌词
                    if adjusted_seconds >= 0.5:
                        # 找到当前时间对应的歌词
                        current_lyric = ""
                        next_lyric_time = None
                        
                        for i, (time, content) in enumerate(self.current_parsed_lyric):
                            if time <= adjusted_seconds:
                                if content:
                                    current_lyric = content
                            else:
                                # 找到下一句歌词的时间
                                next_lyric_time = time
                                break
                        
                        # 只有当当前有歌词或者下一句歌词即将开始时，才显示悬浮歌词窗口
                        # 下一句歌词即将开始的定义：当前时间距离下一句歌词的时间小于0.5秒
                        has_lyric = False
                        if current_lyric:
                            has_lyric = True
                        elif next_lyric_time and (next_lyric_time - adjusted_seconds) < 0.5:
                            has_lyric = True
                        else:
                            has_lyric = False
                        
                        # 只有当当前时间段有歌词时才显示悬浮歌词窗口
                        if has_lyric:
                            if not self.float_lyric_window:
                                self.float_lyric_window = LyricFloatWindow()
                                # 导入全局配置
                                global FLOAT_LYRIC_BOTTOM_MARGIN
                                # 居中显示在屏幕底部上方指定距离处
                                screen = QApplication.primaryScreen()
                                screen_geometry = screen.geometry()
                                x = (screen_geometry.width() - self.float_lyric_window.width()) // 2
                                # 将窗口位置设置到屏幕之外
                                y = screen_geometry.height() + 100  # 屏幕下方外
                                self.float_lyric_window.move(x, y)
                            # 先设置窗口可见标志，以便更新歌词
                            self.float_lyric_window_visible = True
                            # 显示窗口并播放动画，传递当前歌词数据和时间
                            self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)
            print(f"[全屏检测] 灵动岛当前状态: {'可见' if self.is_visible else '隐藏'}")
            print(f"[全屏检测] 媒体播放状态: {'播放' if self.is_playing else '停止'}")
            
            # 更新上一次的检测结果
            self.last_fullscreen_state = has_fullscreen_app

    def on_album_art_clicked(self, event):
        """专辑图点击事件处理"""
        from PyQt5.QtCore import QDateTime
        current_time = QDateTime.currentMSecsSinceEpoch()
        
        # 检测双击
        if current_time - self.last_click_time < 500:  # 500ms内的第二次点击视为双击
            self.click_count += 1
        else:
            self.click_count = 1
        
        self.last_click_time = current_time
        
        # 处理右双击
        if event.button() == Qt.RightButton and self.click_count == 2:
            self.on_album_art_right_double_clicked()
            self.click_count = 0  # 重置点击计数
        # 处理左单击
        elif event.button() == Qt.LeftButton and self.click_count == 1:
            # 检查是否正在退出倒计时
            if self.exit_timer.isActive():
                # 取消退出程序并临时隐藏
                self.exit_timer.stop()
                self.cancel_exit()
            else:
                # 临时隐藏加清除缓存
                self.temp_hide_and_clear_cache()
        # 右单击不响应
        elif event.button() == Qt.RightButton and self.click_count == 1:
            pass  # 右单击不响应
    
    def temp_hide_and_clear_cache(self):
        """临时隐藏加清除缓存"""
        if self.is_visible:
            # 设置主动隐藏标志
            self.actively_hidden = True
            # 隐藏整个灵动岛
            self.hide_with_animation()
            # 隐藏悬浮歌词（无论是否可见）
            if self.float_lyric_window:
                self.float_lyric_window.hide_with_animation()
                self.float_lyric_window_visible = False
            
            # 清理歌词缓存和解析后的歌词缓存
            self.lyric_cache.clear()
            self.parsed_lyric_cache.clear()
            
            # 清理专辑图相关缓存
            self.last_album_art_bytes = None
            self.original_album_art = None
            
            # 绘制默认音乐图标
            self.draw_rotated_album_art()
            
            print("[缓存清理] 点击专辑图，已清理歌词缓存、解析后的歌词缓存和专辑图缓存")
    
    def on_album_art_right_double_clicked(self):
        """专辑图右双击处理 - 关闭程序逻辑"""
        # 临时设置主动隐藏标志，防止悬浮歌词在播放状态下重新出现
        self.actively_hidden = True
        
        # 隐藏现有悬浮歌词
        if self.float_lyric_window and self.float_lyric_window_visible:
            self.float_lyric_window.hide_with_animation()
            self.float_lyric_window_visible = False
            
            # 延迟显示倒计时窗口，确保悬浮歌词隐藏动画完成
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(600, self.show_countdown_window)
        else:
            # 如果没有悬浮歌词或已隐藏，直接显示倒计时窗口
            self.show_countdown_window()
    
    def show_countdown_window(self):
        """显示倒计时窗口"""
        # 创建并显示读秒悬浮窗口
        if not self.countdown_float_window:
            self.countdown_float_window = CountdownFloatWindow()
        
        # 显示退出提示
        self.countdown_float_window_visible = True
        self.exit_countdown = 5
        self.update_exit_message()
        # 显示读秒窗口
        self.countdown_float_window.show_with_animation()
        
        # 启动倒计时
        self.exit_timer.start(1000)  # 每秒更新一次
        
        print("[退出提示] 程序将在5秒后自动退出，单击专辑图取消退出")
    
    def update_exit_message(self):
        """更新退出提示消息"""
        if self.countdown_float_window:
            self.countdown_float_window.update_countdown(self.exit_countdown)
    
    def update_exit_countdown(self):
        """更新退出倒计时"""
        self.exit_countdown -= 1
        if self.exit_countdown <= 0:
            self.exit_timer.stop()
            # 隐藏读秒窗口
            if self.countdown_float_window and self.countdown_float_window_visible:
                self.countdown_float_window.hide_with_animation()
                self.countdown_float_window_visible = False
            # 退出程序
            QApplication.quit()
        else:
            self.update_exit_message()
    
    def cancel_exit(self):
        """取消退出程序"""
        # 恢复主动隐藏标志，允许悬浮歌词在播放状态下重新出现
        self.actively_hidden = False
        
        # 隐藏悬浮歌词
        if self.float_lyric_window:
            self.float_lyric_window.hide_with_animation()
            self.float_lyric_window_visible = False
        
        # 隐藏读秒悬浮窗口
        if self.countdown_float_window and self.countdown_float_window_visible:
            self.countdown_float_window.hide_with_animation()
            self.countdown_float_window_visible = False
        
        print("[退出取消] 已取消退出程序")
    
    def toggle_float_lyric_window(self, event):
        """
        切换悬浮歌词窗口的显示状态
        """
        global FLOAT_LYRIC_ENABLED
        
        if FLOAT_LYRIC_ENABLED == 1:
            # 关闭悬浮歌词
            FLOAT_LYRIC_ENABLED = 0
            
            # 关闭悬浮歌词窗口
            if self.float_lyric_window:
                # 保存引用，以便在动画完成后清理
                float_lyric_window = self.float_lyric_window
                
                # 动画完成后清理窗口对象
                def on_hide_finished():
                    # 清理窗口对象
                    self.float_lyric_window = None
                    self.float_lyric_window_visible = False
                
                # 启动隐藏动画
                float_lyric_window.hide_with_animation()
                
                # 等待动画对象创建后再连接信号
                from PyQt5.QtCore import QTimer
                QTimer.singleShot(10, lambda: float_lyric_window.hide_animation.finished.connect(on_hide_finished) if float_lyric_window.hide_animation else on_hide_finished())
            
            # 直接修改代码文件中的FLOAT_LYRIC_ENABLED值，保存状态
            try:
                with open(__file__, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 使用正则表达式替换配置区的FLOAT_LYRIC_ENABLED的值，确保只匹配配置行
                import re
                # 只匹配以FLOAT_LYRIC_ENABLED开头的行，避免影响其他代码
                new_content = re.sub(r'^FLOAT_LYRIC_ENABLED\s*=\s*\d+', 'FLOAT_LYRIC_ENABLED = 0', content, flags=re.MULTILINE)
                with open(__file__, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已将代码中的FLOAT_LYRIC_ENABLED修改为0")
            except Exception as e:
                print(f"修改代码文件时发生错误：{e}")
            
            # 直接更新灵动岛显示状态：显示歌词（如果有）
            self._update_lyric_by_progress()
        else:
            # 打开悬浮歌词
            FLOAT_LYRIC_ENABLED = 1
            
            # 创建并显示悬浮歌词窗口
            if not self.float_lyric_window:
                self.float_lyric_window = LyricFloatWindow()
            # 导入全局配置
            global FLOAT_LYRIC_BOTTOM_MARGIN
            # 居中显示在屏幕底部上方指定距离处
            screen = QApplication.primaryScreen()
            screen_geometry = screen.geometry()
            x = (screen_geometry.width() - self.float_lyric_window.width()) // 2
            # 将窗口位置设置到屏幕之外
            y = screen_geometry.height() + 100  # 屏幕下方外
            self.float_lyric_window.move(x, y)
            
            # 先设置窗口可见标志
            self.float_lyric_window_visible = True
            
            # 显示窗口并播放动画，传递当前歌词数据和时间
            self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)
            
            # 直接修改代码文件中的FLOAT_LYRIC_ENABLED值，保存状态
            try:
                with open(__file__, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 使用正则表达式替换配置区的FLOAT_LYRIC_ENABLED的值，确保只匹配配置行
                import re
                # 只匹配以FLOAT_LYRIC_ENABLED开头的行，避免影响其他代码
                new_content = re.sub(r'^FLOAT_LYRIC_ENABLED\s*=\s*\d+', 'FLOAT_LYRIC_ENABLED = 1', content, flags=re.MULTILINE)
                with open(__file__, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已将代码中的FLOAT_LYRIC_ENABLED修改为1")
            except Exception as e:
                print(f"修改代码文件时发生错误：{e}")
            
            # 直接更新灵动岛显示状态：显示原歌手和歌曲名
            self.song_label.setText(self.current_song)
            self.artist_label.setText(self.current_artist)
            # 调整透明度
            self._set_song_label_opacity(0.3)
            
            # 立即更新悬浮歌词
            self.update_float_lyric()
    
    def update_float_lyric(self):
        """
        更新悬浮歌词窗口的歌词显示
        """
        # 当隐藏动画正在播放时，不更新歌词显示，这样文字会和窗口一起消失
        # 显示动画期间允许更新歌词，确保文字先写入窗口再播放动画
        # 即使窗口不可见，只要有窗口对象且没有隐藏动画，就更新歌词
        # 退出倒计时期间不更新歌词，只显示倒计时信息
        is_hiding_animating = hasattr(self.float_lyric_window, 'hide_animation') and self.float_lyric_window.hide_animation and self.float_lyric_window.hide_animation.state() == QAbstractAnimation.Running
        
        if self.float_lyric_window and not is_hiding_animating and not getattr(self, 'float_lyric_animating', False) and not self.exit_timer.isActive():
            current_seconds = self.last_progress_seconds
            # 使用当前解析后的歌词
            if self.current_parsed_lyric:
                self.float_lyric_window.update_lyric(self.current_parsed_lyric, current_seconds)
            else:
                pass
        else:
            if not self.float_lyric_window:
                pass
            elif getattr(self, 'float_lyric_animating', False):
                pass
            elif self.exit_timer.isActive():
                pass  # 退出倒计时期间不更新歌词
    
    def paintEvent(self, event):
        """绘制圆角胶囊形状"""
        painter = QPainter(self)
        # 添加抗锯齿和高质量渲染设置
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        
        # 绘制黑色半透明背景
        brush = QBrush(QColor(30, 30, 30, 230))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        
        # 绘制圆角矩形，调整圆角半径为35
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 35, 35)
    
    def process_audio_data(self, audio_data):
        """处理音频数据，实现5个频段的音频可视化"""
        try:
            # 只有在媒体正在播放时才处理音频数据
            if self.is_playing:
                # 保存音频数据
                self.audio_data = audio_data.flatten()
                
                # 检查并清理无效数据
                if np.isnan(self.audio_data).any() or np.isinf(self.audio_data).any():
                    # 替换无效值为0
                    self.audio_data = np.nan_to_num(self.audio_data)
                
                # 计算FFT (快速傅里叶变换)
                fft = np.fft.fft(self.audio_data)
                # 获取FFT的幅度
                fft_magnitude = np.abs(fft[:len(fft)//2])
                
                # 频段划分 - 5个频段
                n_bands = 5
                total_bins = len(fft_magnitude)
                
                # 使用线性频段划分，从较高频率开始，避免低频能量问题
                band_bins = [
                    int(total_bins * 0.2),     # 起始点：从20%频率开始，避免低频能量过高
                    int(total_bins * 0.35),    # 第1个频段结束点（35%）
                    int(total_bins * 0.5),     # 第2个频段结束点（50%）
                    int(total_bins * 0.65),    # 第3个频段结束点（65%）
                    int(total_bins * 0.85),    # 第4个频段结束点（85%）
                    total_bins                  # 最高频率
                ]
                
                # 计算每个频段的幅度，使用平均值
                self.fft_data = []
                for i in range(n_bands):
                    start = band_bins[i]
                    end = band_bins[i+1]
                    if start < end:
                        # 获取频段数据
                        band_values = fft_magnitude[start:end]
                        
                        # 计算平均值
                        band_magnitude = np.mean(band_values)
                        
                        # 对幅度值进行限制，使用75%分位数作为上限
                        band_magnitude = min(band_magnitude, np.percentile(band_values, 75))
                        
                        self.fft_data.append(band_magnitude)
                    else:
                        self.fft_data.append(0)
                
                # 优化归一化处理
                self.fft_data = np.array(self.fft_data)
                
                # 添加一个小的偏移量，避免log(0)错误
                epsilon = 1e-10
                
                # 使用对数缩放，压缩高能量值
                self.fft_data = np.log10(1 + self.fft_data)
                
                # 归一化到0-1范围
                min_val = np.min(self.fft_data)
                max_val = np.max(self.fft_data)
                if max_val > min_val:
                    # 使用线性归一化
                    normalized = (self.fft_data - min_val) / (max_val - min_val)
                    
                    # 对归一化后的数据进行压缩，平衡各频段能量
                    compression_factor = 0.4  # 压缩因子
                    self.fft_data = normalized ** compression_factor
                else:
                    self.fft_data = np.zeros(5)
                
                # 对FFT数据进行平滑处理，使可视化效果更流畅
                self.fft_data = np.clip(self.fft_data, 0, 1)  # 确保值在0-1范围内
            else:
                # 媒体停止时，重置FFT数据
                self.fft_data = np.zeros(5)
        except Exception as e:
            print(f"音频数据处理错误: {e}")
            self.fft_data = np.zeros(5)
    
    def update_visualization(self):
        """更新音频可视化动画 - 根据样式索引调用不同的样式方法"""
        # 避免在关闭音频可视化后频繁调用停止和启动麦克风捕获
        if self.visualization_style == 5:
            # 关闭音频可视化，隐藏所有可视化条
            # 重置FFT数据，避免使用旧的音频数据
            self.fft_data = np.zeros(5)
            # 隐藏所有可视化条
            for bar in self.visualization_bars:
                bar.setFixedSize(6, 0)
                bar.setStyleSheet("QWidget { background-color: transparent; border-radius: 2px; }")
            # 停止音频捕获（只在需要时）
            if self.audio_thread.is_capture_running():
                self.audio_thread.stop_capture()
        elif self.is_playing and (self.visualization_style == 3 or self.visualization_style == 4):
            # 媒体正在播放且音频可视化开启时，使用真实音频数据显示动态可视化效果
            if self.visualization_style == 3:
                self.visualization_circular()
                # 确保音频捕获线程在运行
                if not self.audio_thread.is_capture_running():
                    self.audio_thread.start_capture()
            elif self.visualization_style == 4:
                self.visualization_wave()
                # 确保音频捕获线程在运行
                if not self.audio_thread.is_capture_running():
                    self.audio_thread.start_capture()
        else:
            # 媒体暂停或停止，或音频可视化关闭时，完全隐藏可视化条
            # 重置FFT数据，避免使用旧的音频数据
            self.fft_data = np.zeros(5)
            # 隐藏所有可视化条
            for bar in self.visualization_bars:
                bar.setFixedSize(6, 0)
                bar.setStyleSheet("QWidget { background-color: transparent; border-radius: 2px; }")
            # 停止音频捕获（只在需要时）
            if self.audio_thread.is_capture_running():
                self.audio_thread.stop_capture()
    
    def visualization_classic(self):
        """经典样式 - 当前的实现"""
        for i, bar in enumerate(self.visualization_bars):
            # 根据FFT数据计算柱状条高度
            # 基础高度10，最大高度40
            height = int(10 + self.fft_data[i] * 30)
            height = max(10, min(40, height))
            
            bar.setFixedSize(8, height)
            
            # 根据高度调整颜色
            if height < 20:
                bar.setStyleSheet("QWidget { background-color: #4CAF50; border-radius: 2px; }")
            elif height < 30:
                bar.setStyleSheet("QWidget { background-color: #FFC107; border-radius: 2px; }")
            else:
                bar.setStyleSheet("QWidget { background-color: #FF5722; border-radius: 2px; }")
    
    def visualization_gradient(self):
        """渐变样式 - 使用渐变颜色"""
        colors = ["#4CAF50", "#2196F3", "#9C27B0", "#FF9800", "#FF5722"]
        for i, bar in enumerate(self.visualization_bars):
            # 根据FFT数据计算柱状条高度
            # 基础高度10，最大高度40
            height = int(10 + self.fft_data[i] * 30)
            height = max(10, min(40, height))
            
            bar.setFixedSize(8, height)
            
            # 使用渐变颜色，每个柱状条使用不同的颜色
            color = colors[i % len(colors)]
            bar.setStyleSheet(f"QWidget {{ background-color: {color}; border-radius: 2px; }}")
    
    def visualization_reverse(self):
        """反向样式 - 从底部向上显示"""
        for i, bar in enumerate(self.visualization_bars):
            # 根据FFT数据计算柱状条高度
            # 基础高度10，最大高度40
            height = int(10 + self.fft_data[i] * 30)
            height = max(10, min(40, height))
            
            # 计算反向高度（从底部向上）
            reverse_height = 40 - height + 10
            
            bar.setFixedSize(8, reverse_height)
            
            # 根据高度调整颜色
            if height < 20:
                bar.setStyleSheet("QWidget { background-color: #4CAF50; border-radius: 2px; }")
            elif height < 30:
                bar.setStyleSheet("QWidget { background-color: #FFC107; border-radius: 2px; }")
            else:
                bar.setStyleSheet("QWidget { background-color: #FF5722; border-radius: 2px; }")
    
    def visualization_circular(self):
        """圆形频谱样式 - 柱状条围绕中心点排列"""
        # 计算中心点
        center_x = 22  # 右侧区域宽度为55，中心点x坐标
        center_y = 22  # 右侧区域高度为45，中心点y坐标
        radius = 15  # 圆的半径
        
        # 根据FFT数据调整柱状条高度
        for i, bar in enumerate(self.visualization_bars):
            # 根据FFT数据计算柱状条高度
            height = int(10 + self.fft_data[i] * 20)
            height = max(10, min(30, height))
            
            # 设置柱状条大小
            bar.setFixedSize(6, height)
            
            # 使用渐变颜色
            colors = ["#4CAF50", "#2196F3", "#9C27B0", "#FF9800", "#FF5722"]
            color = colors[i % len(colors)]
            bar.setStyleSheet(f"QWidget {{ background-color: {color}; border-radius: 2px; }}")
    
    def visualization_wave(self):
        """波浪形样式 - 柱状条高度随时间呈现波浪状变化"""
        # 计算波浪效果
        time = self.visualization_timer.interval() * 0.001  # 时间因子
        for i, bar in enumerate(self.visualization_bars):
            # 根据FFT数据和波浪因子计算柱状条高度
            wave_factor = np.sin(i * 0.5 + time * 10)  # 波浪效果
            height = int(10 + (self.fft_data[i] + wave_factor * 0.2) * 25)
            height = max(10, min(40, height))
            
            # 设置柱状条大小
            bar.setFixedSize(6, height)
            
            # 使用蓝紫色调渐变
            color = f"#{int(100 + self.fft_data[i] * 155):02x}{int(100 + wave_factor * 50):02x}FF"
            bar.setStyleSheet(f"QWidget {{ background-color: {color}; border-radius: 2px; }}")
    
    def toggle_visualization_style(self, event):
        """音频可视化点击事件处理"""
        if event.button() == Qt.LeftButton:
            # 左单击：切换音频可视化状态
            # 循环切换样式：3(圆形频谱) -> 4(波浪形) -> 5(关闭)
            if self.visualization_style == 3:
                self.visualization_style = 4
            elif self.visualization_style == 4:
                self.visualization_style = 5
                # 立即停止音频捕获
                self.audio_thread.stop_capture()
            else:
                self.visualization_style = 3
            print(f"切换到音频可视化样式: {self.visualization_style}")
            
            # 保存配置到文件
            try:
                with open(__file__, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 使用正则表达式替换配置区的VISUALIZATION_STYLE的值，确保只匹配配置行
                import re
                # 只匹配以VISUALIZATION_STYLE开头的行，避免影响其他代码
                new_content = re.sub(r'^VISUALIZATION_STYLE\s*=\s*\d+', f'VISUALIZATION_STYLE = {self.visualization_style}', content, flags=re.MULTILINE)
                with open(__file__, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已将代码中的VISUALIZATION_STYLE修改为{self.visualization_style}")
            except Exception as e:
                print(f"修改代码文件时发生错误：{e}")
        elif event.button() == Qt.RightButton:
            # 右单击：切换悬浮歌词颜色
            # 声明全局变量
            global FLOAT_LYRIC_TEXT_COLOR
            # 颜色列表
            colors = ["white", "red", "blue", "green", "yellow", "purple"]
            # 获取当前颜色索引
            current_index = colors.index(FLOAT_LYRIC_TEXT_COLOR) if FLOAT_LYRIC_TEXT_COLOR in colors else 0
            # 切换到下一个颜色
            next_index = (current_index + 1) % len(colors)
            new_color = colors[next_index]
            
            # 更新全局配置
            FLOAT_LYRIC_TEXT_COLOR = new_color
            
            # 更新悬浮歌词窗口的颜色
            if self.float_lyric_window:
                self.float_lyric_window.update_lyric_style()
            
            # 保存配置到文件
            try:
                with open(__file__, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 使用正则表达式替换配置区的FLOAT_LYRIC_TEXT_COLOR的值，确保只匹配配置行
                import re
                # 只匹配以FLOAT_LYRIC_TEXT_COLOR开头的行，避免影响其他代码
                new_content = re.sub(r'^FLOAT_LYRIC_TEXT_COLOR\s*=\s*"[^"]*"', f'FLOAT_LYRIC_TEXT_COLOR = "{new_color}"', content, flags=re.MULTILINE)
                with open(__file__, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"已将代码中的FLOAT_LYRIC_TEXT_COLOR修改为{new_color}")
            except Exception as e:
                print(f"修改代码文件时发生错误：{e}")
            
            print(f"切换悬浮歌词颜色为: {new_color}")
    
    def update_rotation(self):
        """更新专辑图旋转角度并触发重绘"""
        # 更新旋转角度
        self.rotation_angle += self.rotation_speed
        # 确保角度在0-360度范围内
        if self.rotation_angle >= 360:
            self.rotation_angle -= 360
        # 触发专辑图重绘
        self.update()  # 调用paintEvent，触发整个窗口重绘
    
    def update_media_info(self, media_info):
        """更新媒体信息"""
        # 解析媒体信息
        lines = media_info.strip().split('\n')
        
        # 初始化播放状态为False，默认认为没有媒体在播放
        self.is_playing = False
        
        # 标记是否找到状态字段
        found_status = False
        
        # 初始化状态变量，默认值为"停止播放"
        status = "停止播放"
        
        # 添加进度信息检测
        has_valid_progress = False
        current_progress = ""
        total_duration = ""
        
        # 解析进度信息的辅助函数
        def parse_time(time_str):
            """将时间字符串（如"03:45"）转换为秒数"""
            try:
                minutes, seconds = map(int, time_str.split(':'))
                return minutes * 60 + seconds
            except:
                return 0
        
        # 初始化歌手名、歌曲名和文件路径
        artist_name = ""
        song_name = ""
        file_path = ""
        # 初始化新歌曲标志
        is_new_song = False
        # 检查是否有媒体会话
        has_media_session = "没有检测到媒体会话" not in media_info
        
        if has_media_session:
            for line in lines:
                line = line.strip()
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    key = key.strip()  # 移除键名前后的空格
                    if key == '歌曲':
                        song_name = value.strip()
                    elif key == '歌手':
                        artist_name = value.strip()
                    elif key == '状态':
                        # 更新播放状态
                        found_status = True
                        status = value.strip()
                    elif key == '文件路径':
                        file_path = value.strip()
                    elif key == '进度':
                        # 获取进度信息，用于判断是否真正在播放
                        progress = value.strip()
                        if '/' in progress:
                            current, total = progress.split('/', 1)
                            current_progress = current.strip()
                            total_duration = total.strip()
                            # 如果当前进度和总时长都不是00:00，说明有有效播放
                            if current_progress != "00:00" or total_duration != "00:00":
                                has_valid_progress = True
                            
                            # 将时间字符串转换为秒数
                            current_seconds = parse_time(current_progress)
                            total_seconds = parse_time(total_duration)
                            
                            from PyQt5.QtCore import QDateTime
                            
                            # 更新状态信息，确保后续旋转计算正确
                            self.last_progress_seconds = current_seconds
                            self.estimated_total_seconds = total_seconds
                            self.last_rotation_update_time = QDateTime.currentMSecsSinceEpoch()  # 更新为当前时间
                            
                            # 固定速度旋转模式，不需要基于进度计算旋转角度
                            # 确保不在调整时间状态，使用固定速度旋转
                            self.is_adjusting_time = False
                            
            # 优化歌曲名和歌手名的解析
            def optimize_song_info(artist, song):
                """
                优化歌曲名和歌手名的解析
                :param artist: 原始歌手名
                :param song: 原始歌曲名
                :return: (优化后的歌手名, 优化后的歌曲名)
                """
                import os
                import re
                
                # 1. 移除文件扩展名
                song = os.path.splitext(song)[0]
                
                # 2. 移除所有括号内容（包括括号本身）
                song = re.sub(r'\([^)]*\)', '', song)
                song = re.sub(r'\[[^\]]*\]', '', song)
                
                # 3. 移除帧率信息
                song = re.sub(r'\s*\d+fps\s*', '', song, flags=re.IGNORECASE)
                
                # 4. 移除多余空格
                song = ' '.join(song.split())
                
                # 5. 优先分割带空格的段落，处理"歌手 - 歌曲"格式
                if not artist and '-' in song:
                    # 寻找带空格的分割点，如"歌手名 - 歌曲名"（中间有空格）
                    space_dash_pattern = r'(.*?)\s+-\s+(.*)'
                    match = re.match(space_dash_pattern, song)
                    if match:
                        artist = match.group(1).strip()
                        song = match.group(2).strip()
                    else:
                        # 没有带空格的分割点，尝试普通分割
                        parts = song.split('-', 1)
                        if len(parts) == 2:
                            artist = parts[0].strip()
                            song = parts[1].strip()
                
                return artist, song
            
            # 保存原始歌曲名（包含视频后缀）
            song_name_original = song_name
            
            # 应用优化
            artist_name, song_name = optimize_song_info(artist_name, song_name)
            
            # 检测是否为新歌曲
            is_new_song = song_name != self.current_song or artist_name != self.current_artist
            
            # 只在信息发生变化时输出日志
            if is_new_song:
                try:
                    print(f"优化后的媒体信息：歌曲名='{song_name}', 歌手名='{artist_name}'")
                    print(f"解析到的媒体信息：歌曲名='{song_name}', 歌手名='{artist_name}'")
                except UnicodeEncodeError:
                    # 处理Unicode编码错误，使用replace模式
                    print("优化后的媒体信息：歌曲名='{}', 歌手名='{}".format(song_name.encode('utf-8', 'replace').decode('utf-8'), artist_name.encode('utf-8', 'replace').decode('utf-8')))
                    print("解析到的媒体信息：歌曲名='{}', 歌手名='{}".format(
                        song_name.encode('utf-8', 'replace').decode('utf-8'),
                        artist_name.encode('utf-8', 'replace').decode('utf-8')
                    ))
            
            # 更新歌词显示，但在新歌曲情况下延迟更新，确保消失动画正常播放
            if not is_new_song:
                # 不是新歌曲，正常更新歌词
                self._update_lyric_by_progress()
            else:
                # 是新歌曲，先标记动画正在播放，避免在更新歌词时清空文本
                if self.float_lyric_window_visible:
                    # 标记动画正在播放
                    self.float_lyric_animating = True
        
        # 判断当前状态是否为停止
        is_currently_stopped = False
        if status == '停止播放' or not found_status or "没有检测到媒体会话" in media_info:
            is_currently_stopped = True
        
        # 保存之前的播放状态，用于检测状态变化
        was_playing = self.is_playing
        
        # 综合判断播放状态：
        # 只有系统报告的状态为"正在播放"时，才视为正在播放
        # 暂停状态和停止状态都不启动音频捕获
        if status == '正在播放':
            self.is_playing = True
            # 更新播放/暂停按钮图标为暂停图标（使用更直观的符号）
            self.play_pause_button.setText("■")
            # 只有在音频可视化开启时才启动音频捕获
            if self.visualization_style in [3, 4]:
                self.audio_thread.start_capture()
            
            # 从暂停状态变为播放状态，显示悬浮歌词（如果无全屏应用）
            has_fullscreen, _ = self.is_fullscreen_or_maximized()
            if not was_playing and FLOAT_LYRIC_ENABLED == 1 and not self.float_lyric_window_visible and self.current_parsed_lyric and not self.actively_hidden and not has_fullscreen:
                # 检查当前时间段是否有歌词
                current_seconds = self.last_progress_seconds
                adjusted_seconds = current_seconds + LYRIC_OFFSET
                
                # 特殊处理：如果当前进度接近0秒，不显示任何歌词，避免切换歌曲时显示0.00秒的歌词
                if adjusted_seconds >= 0.5:
                    # 找到当前时间对应的歌词
                    current_lyric = ""
                    next_lyric_time = None
                    
                    for i, (time, content) in enumerate(self.current_parsed_lyric):
                        if time <= adjusted_seconds:
                            if content:
                                current_lyric = content
                        else:
                            # 找到下一句歌词的时间
                            next_lyric_time = time
                            break
                    
                    # 只有当当前有歌词或者下一句歌词即将开始时，才显示悬浮歌词窗口
                    # 下一句歌词即将开始的定义：当前时间距离下一句歌词的时间小于0.5秒
                    has_lyric = False
                    if current_lyric:
                        has_lyric = True
                    elif next_lyric_time and (next_lyric_time - adjusted_seconds) < 0.5:
                        has_lyric = True
                    else:
                        has_lyric = False
                    
                    # 只有当当前时间段有歌词时才显示悬浮歌词窗口
                    if has_lyric:
                        if not self.float_lyric_window:
                            self.float_lyric_window = LyricFloatWindow()
                            # 计算窗口位置
                            screen = QApplication.primaryScreen()
                            screen_geometry = screen.geometry()
                            x = (screen_geometry.width() - self.float_lyric_window.width()) // 2
                            # 将窗口位置设置到屏幕之外
                            y = screen_geometry.height() + 100  # 屏幕下方外
                            self.float_lyric_window.move(x, y)
                        self.float_lyric_window_visible = True
                        self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)
        else:
            self.is_playing = False
            # 更新播放/暂停按钮图标为播放图标
            self.play_pause_button.setText("▶")
            # 停止音频捕获
            self.audio_thread.stop_capture()
            
            # 暂停状态，隐藏悬浮歌词
            if self.float_lyric_window_visible:
                if self.float_lyric_window:
                    self.float_lyric_window.hide_with_animation()
                self.float_lyric_window_visible = False
        
        # 额外安全检查：确保暂停或停止状态下音频捕获被停止
        if status in ['暂停播放', '停止播放'] or not found_status or "没有检测到媒体会话" in media_info:
            self.is_playing = False
            self.audio_thread.stop_capture()
        
        # 处理动画逻辑
        if is_currently_stopped:
            # 停止状态 - 隐藏灵动岛和悬浮歌词，重置主动隐藏标志
            if self.is_visible:
                self.actively_hidden = False
                self.hide_with_animation()
            # 隐藏悬浮歌词
            if self.float_lyric_window_visible:
                if self.float_lyric_window:
                    self.float_lyric_window.hide_with_animation()
                self.float_lyric_window_visible = False
        else:
            # 播放或暂停状态 - 显示灵动岛
            if not self.is_visible and not self.actively_hidden:
                # 在显示之前检查是否有全屏或最大化应用
                has_fullscreen, _ = self.is_fullscreen_or_maximized()
                if not has_fullscreen:
                    self.show_with_animation()
        
        # 如果没有找到状态字段，检查是否有"没有检测到媒体会话"的信息
        if not found_status:
            if "没有检测到媒体会话" in media_info:
                # 没有检测到媒体会话，设置为停止状态
                self.is_playing = False
                self.play_pause_button.setText("▶")
        
        # 如果是新歌曲，更新当前歌曲名和歌手名
        if is_new_song:
            # 新歌曲开始，重置主动隐藏标志
            self.actively_hidden = False
            # 切换歌词后播放消失动画
            if self.float_lyric_window_visible:
                if self.float_lyric_window:
                    # 播放消失动画
                    self.float_lyric_window.hide_with_animation()
                    
                    # 动画结束后再重置歌词、进度秒数和窗口可见性
                    def on_animation_finished():
                        # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                        self.current_parsed_lyric = []
                        # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                        self.last_progress_seconds = 0.0
                        # 设置窗口可见性为 False
                        self.float_lyric_window_visible = False
                        # 标记动画结束
                        self.float_lyric_animating = False
                    
                    # 等待动画完成后再重置
                    QTimer.singleShot(500, on_animation_finished)
            else:
                # 标记动画结束
                self.float_lyric_animating = False
                # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                self.current_parsed_lyric = []
                # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                self.last_progress_seconds = 0.0
            
            # 新歌曲，更新当前歌曲名和歌手名
            self.current_song = song_name
            self.current_artist = artist_name
            # 重置倒计时秒数，确保新歌曲的倒计时日志能够正确显示
            self.last_countdown_second = -1
            
            # 重置专辑图相关属性
            self.rotation_angle = 0
            self.target_rotation_angle = 0
            # 清除原始专辑图，确保新歌曲重新获取专辑图
            self.original_album_art = None
            # 强制绘制默认音乐图标
            self.draw_rotated_album_art()
            
            # 1秒后更新文本
            def update_text_after_animation():
                # 检查悬浮歌词开关状态
                global FLOAT_LYRIC_ENABLED
                
                # 恢复默认透明度（30%）
                self._set_song_label_opacity(0.3)
                
                # 悬浮歌词开启，显示原歌手和歌曲名
                if FLOAT_LYRIC_ENABLED == 1:
                    # 显示原始歌手和歌曲名
                    display_text = song_name
                    # 保存原始显示文本
                    self.song_original_text = display_text
                    # 检查是否需要滚动
                    self.check_song_scroll_needed()
                    # 重置滚动状态
                    self.reset_song_scroll()
                    # 启动滚动（如果需要）
                    if self.song_scroll_needed:
                        # 先停顿2秒，然后开始滚动
                        QTimer.singleShot(2000, self.start_song_scroll)
                    else:
                        # 不需要滚动，直接显示
                        self.song_label.setText(display_text)
                    
                    # 更新歌手名显示为原始歌手名
                    self.artist_label.setText(artist_name)
                else:
                    # 悬浮歌词关闭，默认显示歌曲名
                    display_text = song_name
                    # 保存原始显示文本
                    self.song_original_text = display_text
                    # 检查是否需要滚动
                    self.check_song_scroll_needed()
                    # 重置滚动状态
                    self.reset_song_scroll()
                    # 启动滚动（如果需要）
                    if self.song_scroll_needed:
                        # 先停顿2秒，然后开始滚动
                        QTimer.singleShot(2000, self.start_song_scroll)
                    else:
                        # 不需要滚动，直接显示
                        self.song_label.setText(display_text)
                    
                    # 更新歌手名显示
                    self.artist_label.setText(artist_name)
            
            # 1秒后更新文本
            QTimer.singleShot(1000, update_text_after_animation)
            
            # 构建歌曲唯一标识
            song_key = f"{artist_name}-{song_name}"
            
            # 只有当artist_name或song_name不为空时，才尝试获取歌词
            if artist_name or song_name:
                # 检查是否已经在缓存中
                if song_key in self.lyric_cache:
                    lyric = self.lyric_cache[song_key]
                    if lyric:
                        self._update_lyric_display(lyric)
                else:
                    # 检查获取次数
                    fetch_count = self.lyric_fetch_count.get(song_key, 0)
                    if fetch_count < 3:
                        # 取消当前等待执行的歌词获取任务
                        if self.lyric_timer.isActive():
                            self.lyric_timer.stop()
                        
                        # 保存当前任务（包含文件路径和原始歌曲名）
                        # 传递原始的song_name用于视频文件检测
                        self.current_lyric_task = (artist_name, song_name, song_key, file_path, song_name_original)
                        
                        # 延时2秒后获取歌词
                        # 断开之前的连接，避免重复连接
                        try:
                            self.lyric_timer.timeout.disconnect(self._delayed_fetch_lyric)
                        except:
                            pass
                        self.lyric_timer.timeout.connect(self._delayed_fetch_lyric)
                        self.lyric_timer.start(2000)  # 2秒后执行
                        print(f"准备获取歌词：{artist_name} - {song_name}")
    
    def _delayed_fetch_lyric(self):
        """
        延时后执行的歌词获取任务
        """
        if self.current_lyric_task:
            # 解包任务参数，处理可能缺少文件路径和原始歌曲名的情况
            if len(self.current_lyric_task) == 5:
                artist_name, song_name, song_key, file_path, song_name_original = self.current_lyric_task
            elif len(self.current_lyric_task) == 4:
                artist_name, song_name, song_key, file_path = self.current_lyric_task
                song_name_original = song_name
            else:
                artist_name, song_name, song_key = self.current_lyric_task
                file_path = ""
                song_name_original = song_name
            self.current_lyric_task = None
            
            # 检查获取次数
            fetch_count = self.lyric_fetch_count.get(song_key, 0)
            if fetch_count >= 3:
                return
            
            # 增加获取次数
            self.lyric_fetch_count[song_key] = fetch_count + 1
            print(f"启动后台线程获取歌词：{artist_name} - {song_name}，第 {fetch_count + 1} 次尝试")
            
            # 启动后台线程获取歌词，传递文件路径和原始歌曲名
            threading.Thread(target=self._fetch_lyric_in_background, args=(artist_name, song_name, song_key, file_path, song_name_original), daemon=True).start()
    
    def _fetch_lyric_in_background(self, artist_name, song_name, song_key, file_path="", song_name_original=""):
        """
        后台线程获取歌词
        :param artist_name: 歌手名
        :param song_name: 歌曲名
        :param song_key: 歌曲唯一标识
        :param file_path: 音频文件路径（可选）
        :param song_name_original: 原始歌曲名（包含视频后缀）
        """
        try:
            # 检查是否是视频文件
            video_extensions = ['.mkv', '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm']
            
            print(f"[歌词搜索过程] 开始获取歌词: {artist_name} - {song_name}")
            print(f"[歌词搜索过程] 原始歌曲名: '{song_name_original}'")
            print(f"[歌词搜索过程] 视频文件歌词适配开关: {'开启' if VIDEO_LYRIC_ENABLED == 1 else '关闭'}")
            
            # 首先检查file_path是否是视频文件
            is_video = False
            if file_path:
                ext = os.path.splitext(file_path)[1].lower()
                is_video = ext in video_extensions
                print(f"[歌词搜索过程] 文件路径: '{file_path}', 扩展名: '{ext}', 是否视频文件: {is_video}")
            
            # 如果file_path不是视频文件，再检查原始歌曲名
            if not is_video and song_name_original:
                is_video = any(ext in song_name_original.lower() for ext in video_extensions)
                print(f"[歌词搜索过程] 原始歌曲名包含视频后缀: {is_video}")
            
            # 如果是视频文件且视频文件歌词适配开关关闭，则直接返回，完全不适配歌词
            if is_video and VIDEO_LYRIC_ENABLED == 0:
                print("[歌词搜索过程] 视频文件歌词适配开关关闭，忽略歌词适配")
                return
            
            # 检查是否有歌手信息，一般视频文件不含歌手信息
            if not artist_name and is_video:
                print("[歌词搜索过程] 视频文件且无歌手信息，忽略歌词适配")
                return
            
            # 获取歌词，传递文件路径
            print(f"[歌词搜索过程] 开始搜索歌词...")
            lyric = get_lyric(artist_name, song_name, file_path)
            
            # 将歌词保存到缓存中
            self.lyric_cache[song_key] = lyric
            
            # 如果获取到歌词，更新显示
            if lyric:
                print(f"[歌词] 成功获取歌词：{artist_name} - {song_name}")
                print(f"[歌词] 歌词长度: {len(lyric)}字符")
                # 使用信号-槽机制在主线程中更新UI
                self.update_lyric_signal.emit(lyric)
            else:
                print(f"[歌词] 未找到歌词：{artist_name} - {song_name}")
        except Exception as e:
            # 发生错误时不影响主程序运行
            print(f"[歌词] 获取歌词时出错: {e}")
            pass
    
    def _parse_lyric(self, lyric):
        """
        解析歌词，提取时间和歌词内容，支持双语字幕
        :param lyric: 原始歌词
        :return: 解析后的歌词列表，格式：[(时间(秒), 歌词内容), ...]
        """
        import re
        # 先按时间戳分组
        lyric_groups = {}
        lines = lyric.split('\n')
        print(f"[歌词] 开始解析歌词，共 {len(lines)} 行")
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # 查找时间标记，格式：[mm:ss.xx] 或 [mm:ss]
            # 使用(.*)匹配零个或多个字符，包括空字符串，以识别空白时间点
            match = re.match(r'\[(\d+):(\d+)(?:\.(\d+))?\](.*)', line)
            if match:
                minutes = int(match.group(1))
                seconds = int(match.group(2))
                milliseconds = int(match.group(3)) if match.group(3) else 0
                # 转换为总秒数，保留3位小数
                total_seconds = round(minutes * 60 + seconds + milliseconds / 1000, 3)
                content = match.group(4).strip()
                # 忽略所有0.0秒的歌词
                if total_seconds == 0.0:
                    print(f"[歌词] 忽略0:00歌词: '{content}'")
                    continue
                # 保留所有其他时间戳，包括空内容的，以识别空白时间
                if total_seconds in lyric_groups:
                    if content:  # 只有当内容不为空时才合并
                        lyric_groups[total_seconds] += ' / ' + content
                else:
                    # 即使内容为空，也要保留时间戳
                    lyric_groups[total_seconds] = content
                # 转换为分钟:秒:毫秒格式
                minutes_display = int(total_seconds // 60)
                seconds_display = int(total_seconds % 60)
                milliseconds_display = int((total_seconds % 1) * 1000)
                print(f"[歌词] 解析到时间戳: {minutes_display}:{seconds_display:02d}:{milliseconds_display:03d}, 内容: '{content}'")
        
        # 转换为列表并按时间排序
        parsed_lyric = [(time, content) for time, content in lyric_groups.items()]
        parsed_lyric.sort(key=lambda x: x[0])
        print(f"[歌词] 解析完成，共 {len(parsed_lyric)} 句歌词")
        if parsed_lyric:
            # 转换为分钟:秒:毫秒格式
            minutes_display = int(parsed_lyric[0][0] // 60)
            seconds_display = int(parsed_lyric[0][0] % 60)
            milliseconds_display = int((parsed_lyric[0][0] % 1) * 1000)
            print(f"[歌词] 第一句歌词时间: {minutes_display}:{seconds_display:02d}:{milliseconds_display:03d}, 内容: '{parsed_lyric[0][1]}'")
            if len(parsed_lyric) > 1:
                minutes_display = int(parsed_lyric[1][0] // 60)
                seconds_display = int(parsed_lyric[1][0] % 60)
                milliseconds_display = int((parsed_lyric[1][0] % 1) * 1000)
                print(f"[歌词] 第二句歌词时间: {minutes_display}:{seconds_display:02d}:{milliseconds_display:03d}, 内容: '{parsed_lyric[1][1]}'")
        return parsed_lyric
    
    def _get_current_lyric(self, parsed_lyric, current_seconds):
        """
        根据当前进度获取对应的歌词，识别并处理空白时间，支持歌词偏移
        空白时间持续小于3秒时，忽略空格，继续显示上一句歌词
        :param parsed_lyric: 解析后的歌词列表
        :param current_seconds: 当前进度（秒）
        :return: 当前进度对应的歌词，如果没有则返回空字符串
        """
        if not parsed_lyric:
            return ""
        
        # 应用歌词偏移，提前或延迟显示歌词
        adjusted_seconds = current_seconds + LYRIC_OFFSET
        
        # 特殊处理：如果当前进度接近0秒，不显示任何歌词，避免切换歌曲时显示0.00秒的歌词
        if adjusted_seconds < 0.5:
            return ""
        
        last_non_empty_lyric = ""  # 上一句非空白歌词
        
        # 遍历所有歌词，找到调整后时间对应的歌词
        for i, (time, content) in enumerate(parsed_lyric):
            # 检查调整后的时间是否在当前歌词的有效时间段内
            if time <= adjusted_seconds:
                # 记录非空白歌词
                if content:  # 如果当前歌词非空，更新上一句非空白歌词
                    last_non_empty_lyric = content
                
                # 检查是否有下一句歌词
                if i < len(parsed_lyric) - 1:
                    next_time = parsed_lyric[i+1][0]
                    
                    # 如果调整后的时间还没到下一句歌词
                    if adjusted_seconds < next_time:
                        # 计算空白时间长度（当前时间到下一句歌词的时间）
                        blank_duration = next_time - time
                        
                        # 如果当前是空白歌词，检查空白时长
                        if not content:
                            # 如果空白时长 < 3秒，使用上一句非空白歌词
                            if blank_duration < 3.0:
                                return last_non_empty_lyric
                            else:
                                # 空白时长 >= 3秒，返回空字符串
                                return ""
                        else:
                            # 当前不是空白歌词，直接返回当前歌词
                            return content
                else:
                    # 最后一句歌词，直接返回（如果是空白则返回上一句非空白歌词）
                    return content if content else last_non_empty_lyric
            else:
                # 还没到第一句歌词的时间
                break
        
        # 当前时间不在任何歌词的有效时间段内，返回空字符串
        return ""
    
    def _update_lyric_by_progress(self):
        """
        根据当前进度更新歌词显示
        """
        # 声明全局变量
        global FLOAT_LYRIC_ENABLED
        
        # 退出倒计时期间不更新歌词，只显示倒计时信息
        if self.exit_timer.isActive():
            return
        
        # 使用实时更新的进度秒数，避免依赖媒体信息获取的延迟
        # 从update_smooth_rotation方法中直接使用last_progress_seconds，该方法每30ms更新一次
        current_seconds = self.last_progress_seconds
        
        # 更新悬浮歌词窗口
        self.update_float_lyric()
        
        # 检查悬浮歌词开关状态 - 只要开关开启，无论窗口是否可见，都显示原歌手和歌曲名
        if FLOAT_LYRIC_ENABLED == 1:
            # 悬浮歌词开启，显示原歌手和歌曲名，不再高亮和显示歌词
            
            # 显示当前歌曲名
            display_text = self.current_song
            # 只有当动画不在播放时，才更新文本
            if display_text != self.song_original_text and not getattr(self, 'float_lyric_animating', False):
                self.song_original_text = display_text
                
                # 检查是否需要滚动
                self.check_song_scroll_needed()
                
                # 重置滚动状态
                self.reset_song_scroll()
                
                # 启动滚动（如果需要）
                if self.song_scroll_needed:
                    # 立即更新显示
                    self.update_song_display()
                    # 先停顿2秒，然后开始滚动
                    QTimer.singleShot(2000, self.start_song_scroll)
                else:
                    # 不需要滚动，直接显示
                    self.song_label.setText(display_text)
            
            # 更新歌手名显示为原歌手名
            if self.artist_label.text() != self.current_artist and not getattr(self, 'float_lyric_animating', False):
                self.artist_label.setText(self.current_artist)
            
            # 输出悬浮歌词倒计时日志
            if self.current_parsed_lyric and self.is_playing:
                # 计算调整后的时间
                adjusted_seconds = current_seconds + LYRIC_OFFSET
                
                # 特殊处理：如果当前进度接近0秒，不显示任何歌词，避免切换歌曲时显示0.00秒的歌词
                if adjusted_seconds >= 0.5:
                    # 找到当前时间对应的歌词
                    current_lyric = ""
                    next_lyric_time = None
                    
                    for i, (time, content) in enumerate(self.current_parsed_lyric):
                        if time <= adjusted_seconds:
                            if content:
                                current_lyric = content
                        else:
                            # 找到下一句歌词的时间
                            next_lyric_time = time
                            break
                    
                    # 只有当当前没有歌词且有下一句歌词时，才输出倒计时日志
                    if not current_lyric and next_lyric_time and not self.actively_hidden:
                        time_left = next_lyric_time - adjusted_seconds
                        # 只显示总秒数和最后倒计时3秒的信息
                        current_int_time = int(time_left)
                        # 只在整数秒变化时输出日志
                        if (time_left >= 10 and current_int_time % 5 == 0 and time_left < current_int_time + 1) or \
                           (time_left < 3 and time_left < current_int_time + 1):
                            # 只有当秒数变化时才输出日志，避免重复
                            if current_int_time != self.last_countdown_second:
                                print(f"[悬浮歌词] 距离下一句歌词还有 {current_int_time}秒")
                                self.last_countdown_second = current_int_time
            
            return
        
        # 悬浮歌词关闭，正常显示歌词
        
        # 获取当前进度对应的歌词
        current_lyric = ""
        if self.current_parsed_lyric:
            current_lyric = self._get_current_lyric(self.current_parsed_lyric, current_seconds)
        
        # 根据是否有歌词调整透明度（高亮显示）
        if current_lyric:
            # 有歌词，高亮显示（65%透明度）
            self._set_song_label_opacity(0.65)
        else:
            # 没有歌词，不高亮显示（30%透明度）
            self._set_song_label_opacity(0.3)
        
        # 检查歌曲原始文本是否与当前歌曲名匹配，不匹配则需要更新
        song_mismatch = self.song_original_text != self.current_song
        label_mismatch = self.song_label.text() != self.current_song and not current_lyric
        
        # 优化歌词显示：区分有歌词和空白时间
        if current_lyric:
            # 有歌词的情况下
            # 检查是否是双语歌词（包含 / 分隔符）
            if ' / ' in current_lyric:
                # 分割双语歌词
                parts = current_lyric.split(' / ', 1)
                if len(parts) == 2:
                    # 第一部分显示在歌曲名位置
                    song_lyric = parts[0].strip()
                    # 第二部分显示在歌手名位置
                    artist_lyric = parts[1].strip()
                    
                    # 更新歌曲名显示
                    display_text = song_lyric
                    if display_text != self.song_original_text:
                        self.song_original_text = display_text
                        
                        # 检查是否需要滚动
                        self.check_song_scroll_needed()
                        
                        # 重置滚动状态
                        self.reset_song_scroll()
                        
                        # 启动滚动（如果需要）
                        if self.song_scroll_needed:
                            # 立即更新显示
                            self.update_song_display()
                            # 先停顿2秒，然后开始滚动
                            QTimer.singleShot(2000, self.start_song_scroll)
                        else:
                            # 不需要滚动，直接显示
                            self.song_label.setText(display_text)
                    
                    # 更新歌手名显示（翻译部分）
                    self.artist_label.setText(artist_lyric)
                    return  # 双语歌词处理完成，直接返回
            else:
                # 非双语歌词，只显示在歌曲名位置
                display_text = current_lyric
                if display_text != self.song_original_text:
                    self.song_original_text = display_text
                    
                    # 检查是否需要滚动
                    self.check_song_scroll_needed()
                    
                    # 重置滚动状态
                    self.reset_song_scroll()
                    
                    # 启动滚动（如果需要）
                    if self.song_scroll_needed:
                        # 立即更新显示
                        self.update_song_display()
                        # 先停顿2秒，然后开始滚动
                        QTimer.singleShot(2000, self.start_song_scroll)
                    else:
                        # 不需要滚动，直接显示
                        self.song_label.setText(display_text)
                    
                    # 单语歌词时，清除歌手名栏的残留翻译
                    self.artist_label.setText("")
                    return  # 单语歌词处理完成，直接返回
        elif song_mismatch or label_mismatch:
            # 空白时间或没有歌词，且歌曲信息不匹配，显示当前歌曲信息
            # 显示当前歌曲名
            display_text = self.current_song
            self.song_original_text = display_text
            
            # 检查是否需要滚动
            self.check_song_scroll_needed()
            
            # 重置滚动状态
            self.reset_song_scroll()
            
            # 启动滚动（如果需要）
            if self.song_scroll_needed:
                # 立即更新显示
                self.update_song_display()
                # 先停顿2秒，然后开始滚动
                QTimer.singleShot(2000, self.start_song_scroll)
            else:
                # 不需要滚动，直接显示
                self.song_label.setText(display_text)
            
            # 更新歌手名显示为当前歌手名
            self.artist_label.setText(self.current_artist)
        elif self.song_original_text == self.current_song:
            # 还没显示过歌词，空白时间显示歌曲名和歌手名
            display_text = self.current_song
            if display_text != self.song_original_text:
                self.song_original_text = display_text
                
                # 检查是否需要滚动
                self.check_song_scroll_needed()
                
                # 重置滚动状态
                self.reset_song_scroll()
                
                # 启动滚动（如果需要）
                if self.song_scroll_needed:
                    # 立即更新显示
                    self.update_song_display()
                    # 先停顿2秒，然后开始滚动
                    QTimer.singleShot(2000, self.start_song_scroll)
                else:
                    # 不需要滚动，直接显示
                    self.song_label.setText(display_text)
                
                # 歌手名位置显示原始歌手名
                self.artist_label.setText(self.current_artist)
    
    def _set_song_label_opacity(self, opacity):
        """
        动态调整歌曲名和歌手名标签的透明度
        :param opacity: 透明度值，0.0-1.0
        """
        import re
        
        # 更新歌曲名标签透明度
        song_current_style = self.song_label.styleSheet()
        song_new_style = re.sub(r'color: rgba\(\d+,\s*\d+,\s*\d+,\s*\d*\.?\d+\);', 
                              f'color: rgba(255, 255, 255, {opacity});', 
                              song_current_style)
        self.song_label.setStyleSheet(song_new_style)
        
        # 更新歌手名标签透明度
        artist_current_style = self.artist_label.styleSheet()
        artist_new_style = re.sub(r'color: rgba\(\d+,\s*\d+,\s*\d+,\s*\d*\.?\d+\);', 
                                f'color: rgba(255, 255, 255, {opacity});', 
                                artist_current_style)
        self.artist_label.setStyleSheet(artist_new_style)
    
    def _update_lyric_display(self, lyric):
        """
        在主线程中更新歌词显示
        :param lyric: 获取到的歌词
        """
        # 声明全局变量
        global FLOAT_LYRIC_ENABLED
        
        # 构建歌曲唯一标识
        song_key = f"{self.current_artist}-{self.current_song}"
        
        # 检查解析后的歌词是否已经在缓存中
        if song_key not in self.parsed_lyric_cache:
            # 解析歌词
            parsed_lyric = self._parse_lyric(lyric)
            print(f"解析歌词完成：{self.current_artist} - {self.current_song}，共 {len(parsed_lyric)} 句")
            # 保存到缓存中
            self.parsed_lyric_cache[song_key] = parsed_lyric
        else:
            # 从缓存中获取解析后的歌词
            parsed_lyric = self.parsed_lyric_cache[song_key]
        
        # 更新当前歌曲解析后的歌词
        self.current_parsed_lyric = parsed_lyric
        
        # 调整透明度
        if FLOAT_LYRIC_ENABLED == 1:
            # 悬浮歌词开启，保持默认透明度（30%）
            self._set_song_label_opacity(0.3)
        else:
            # 悬浮歌词关闭
            if parsed_lyric:
                # 有歌词，高亮显示（65%透明度）
                self._set_song_label_opacity(0.65)
            else:
                # 无歌词，不高亮显示（30%透明度）
                self._set_song_label_opacity(0.3)
        
        # 检查是否正在播放悬浮歌词的隐藏动画
        is_float_lyric_hiding = False
        if self.float_lyric_window and self.float_lyric_window_visible:
            is_float_lyric_hiding = hasattr(self.float_lyric_window, 'hide_animation') and self.float_lyric_window.hide_animation and self.float_lyric_window.hide_animation.state() == QAbstractAnimation.Running
        
        # 如果没有正在播放隐藏动画，才更新歌词显示
        if not is_float_lyric_hiding:
            # 立即更新悬浮歌词窗口
            self.update_float_lyric()
            
            # 立即根据当前进度更新歌词显示
            self._update_lyric_by_progress()
        else:
            # 如果正在播放隐藏动画，延迟更新歌词显示，等待动画完成
            def delayed_update():
                self.update_float_lyric()
                self._update_lyric_by_progress()
            
            # 等待500毫秒（动画持续时间）后更新
            QTimer.singleShot(500, delayed_update)
        
        # 检查悬浮歌词开关状态，如果开启且窗口不可见，自动显示悬浮歌词窗口（非停止状态且非主动隐藏，且无全屏应用）
        has_fullscreen, _ = self.is_fullscreen_or_maximized()
        if FLOAT_LYRIC_ENABLED == 1 and not self.float_lyric_window_visible and parsed_lyric and self.is_playing and not self.actively_hidden and not has_fullscreen:
            # 检查当前时间段是否有歌词
            current_seconds = self.last_progress_seconds
            adjusted_seconds = current_seconds + LYRIC_OFFSET
            
            # 特殊处理：如果当前进度接近0秒，不显示任何歌词，避免切换歌曲时显示0.00秒的歌词
            if adjusted_seconds >= 0.5:
                # 检查当前时间段是否有歌词
                has_lyric = False
                last_non_empty_lyric = ""
                
                # 找到当前时间对应的歌词
                current_lyric = ""
                next_lyric_time = None
                
                for i, (time, content) in enumerate(parsed_lyric):
                    if time <= adjusted_seconds:
                        if content:
                            last_non_empty_lyric = content
                            current_lyric = content
                    else:
                        # 找到下一句歌词的时间
                        next_lyric_time = time
                        break
                
                # 只有当当前有歌词或者下一句歌词即将开始时，才显示悬浮歌词窗口
                # 下一句歌词即将开始的定义：当前时间距离下一句歌词的时间小于0.5秒
                if current_lyric:
                    has_lyric = True
                elif next_lyric_time and (next_lyric_time - adjusted_seconds) < 0.5:
                    has_lyric = True
                else:
                    has_lyric = False
                    if next_lyric_time:
                        pass
                    else:
                        pass
                
                # 只有当当前时间段有歌词时才显示悬浮歌词窗口
                if has_lyric:
                    if not self.float_lyric_window:
                        self.float_lyric_window = LyricFloatWindow()
                        # 导入全局配置
                        global FLOAT_LYRIC_BOTTOM_MARGIN
                        # 居中显示在屏幕底部上方指定距离处
                        screen = QApplication.primaryScreen()
                        screen_geometry = screen.geometry()
                        x = (screen_geometry.width() - self.float_lyric_window.width()) // 2
                        # 计算y坐标：屏幕高度 - 窗口高度 - 底部间距
                        y = screen_geometry.height() - self.float_lyric_window.height() - FLOAT_LYRIC_BOTTOM_MARGIN
                        self.float_lyric_window.move(x, y)
                        print(f"[悬浮歌词] 当前有歌词: '{current_lyric}'，显示悬浮歌词窗口")
                        print("[悬浮歌词] 显示悬浮歌词窗口并播放出现动画")
                        # 显示窗口并播放动画，传递当前歌词数据和时间
                        self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)  # 有动画显示
                        self.float_lyric_window_visible = True
                    elif not self.float_lyric_window_visible:
                        # 悬浮歌词窗口已存在但不可见，显示它并输出日志
                        print(f"[悬浮歌词] 当前有歌词: '{current_lyric}'，显示悬浮歌词窗口")
                        print("[悬浮歌词] 显示悬浮歌词窗口并播放出现动画")
                        # 显示窗口并播放动画，传递当前歌词数据和时间
                        self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)  # 有动画显示
                        self.float_lyric_window_visible = True
                    # 立即更新悬浮歌词
                    self.update_float_lyric()
        

    

    
    def update_album_art(self, album_art_bytes):
        """
        更新专辑图 - 使用高质量圆形处理
        """
        # 检查专辑图是否真正变化
        # 特别处理None和bytearray的比较情况
        is_album_art_changed = False
        if (album_art_bytes is None and self.last_album_art_bytes is not None) or \
           (album_art_bytes is not None and self.last_album_art_bytes is None) or \
           (album_art_bytes is not None and self.last_album_art_bytes is not None and album_art_bytes != self.last_album_art_bytes):
            is_album_art_changed = True
        
        # 更新缓存
        self.last_album_art_bytes = album_art_bytes
        
        if album_art_bytes:
            # 加载原始图片并保存
            self.original_album_art = QPixmap()
            self.original_album_art.loadFromData(album_art_bytes)
        else:
            # 清除原始专辑图
            self.original_album_art = None
        
        # 只有在专辑图真正变化时才重置旋转角度（如切换歌曲或专辑图变化）
        if is_album_art_changed:
            # 下一曲时，重置旋转角度和目标旋转角度为0（摆正）
            self.rotation_angle = 0
            self.target_rotation_angle = 0
        
        # 绘制旋转后的专辑图（无论专辑图是否变化，都重新绘制，确保默认图标显示）
        self.draw_rotated_album_art()
    
    def update_smooth_rotation(self):
        """平滑更新旋转角度"""
        from PyQt5.QtCore import QDateTime
        
        # 固定速度旋转模式，不需要基于进度计算初始旋转角度
        # 程序刚启动时也直接使用固定速度旋转
        if self.rotation_angle == 0:
            # 初始化旋转角度为0，开始固定速度旋转
            self.rotation_angle = 0
            self.is_adjusting_time = False
        
        # 如果正在调整时间，使用平滑过渡到目标旋转角度
        if self.is_adjusting_time:
            # 平滑过渡到目标角度
            if abs(self.rotation_angle - self.target_rotation_angle) < 0.1:
                # 角度差很小，直接设置为目标角度，避免无限接近
                self.rotation_angle = self.target_rotation_angle
                # 结束调整时间状态
                self.is_adjusting_time = False
            else:
                # 计算角度差，考虑360度环绕
                angle_diff = self.target_rotation_angle - self.rotation_angle
                if angle_diff > 180:
                    angle_diff -= 360
                elif angle_diff < -180:
                    angle_diff += 360
                
                # 平滑过渡到目标角度
                self.rotation_angle += angle_diff * self.rotation_smoothness
                
                # 确保角度在0-360度范围内
                self.rotation_angle %= 360
            
            # 更新专辑图显示
            self.draw_rotated_album_art()
        # 否则，正常播放时使用自己的计时器
        elif self.is_playing and self.estimated_total_seconds > 0:
            # 计算从上一次更新到现在的时间差（毫秒）
            current_time = QDateTime.currentMSecsSinceEpoch()
            time_diff_seconds = (current_time - self.last_rotation_update_time) / 1000
            
            # 使用固定速度旋转，每分钟旋转360度（6度/秒）
            rotation_speed = 12  # 度/秒
            rotation_increment = rotation_speed * time_diff_seconds
            
            # 更新旋转角度
            self.rotation_angle = (self.rotation_angle + rotation_increment) % 360
            
            # 更新最后旋转时间
            self.last_rotation_update_time = current_time
            
            # 更新专辑图显示
            self.draw_rotated_album_art()
    
    def draw_rotated_album_art(self):
        """根据当前旋转角度绘制专辑图"""
        # 创建一个高质量的圆形专辑图
        final_pixmap = QPixmap(45, 45)
        final_pixmap.fill(Qt.transparent)
        painter = QPainter(final_pixmap)
        
        # 设置最高质量的渲染提示
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        
        # 绘制圆形背景
        painter.setBrush(QColor(51, 51, 51))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(QRectF(0, 0, 45, 45))
        
        # 裁剪绘制区域为圆形
        circle_path = QPainterPath()
        circle_path.addEllipse(QRectF(0, 0, 45, 45))
        painter.setClipPath(circle_path)
        
        if self.original_album_art:
            # 保存当前坐标系
            painter.save()
            
            # 移动坐标系原点到圆心
            painter.translate(22.5, 22.5)  # 45/2 = 22.5
            
            # 旋转坐标系
            painter.rotate(self.rotation_angle)
            
            # 高质量缩放专辑图
            scaled_pixmap = self.original_album_art.scaled(
                45, 45, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            # 计算居中位置（相对于旋转后的坐标系）
            x = -scaled_pixmap.width() // 2
            y = -scaled_pixmap.height() // 2
            
            # 绘制专辑图
            painter.drawPixmap(x, y, scaled_pixmap)
            
            # 恢复坐标系
            painter.restore()
        else:
            # 绘制音乐图标 - 使用更明显的样式
            font = painter.font()
            font.setPointSize(24)
            painter.setFont(font)
            painter.setPen(QColor(200, 200, 200))  # 使用浅灰色，比纯白色更柔和但更明显
            painter.drawText(QRectF(0, 0, 45, 45), Qt.AlignCenter, "🎵")
        
        painter.end()
        
        # 更新专辑图
        self.album_art.setPixmap(final_pixmap)
        # 强制更新UI，确保专辑图立即变化
        self.album_art.update()
        self.update()
    
    def check_song_scroll_needed(self):
        """检查歌曲名是否需要滚动"""
        if not self.song_original_text:
            return False
        
        # 获取字体度量信息
        font = self.song_label.font()
        metrics = QFontMetrics(font)
        
        # 计算文本宽度
        self.song_text_width = metrics.width(self.song_original_text)
        self.song_display_width = self.song_label.width()
        
        # 判断是否需要滚动
        self.song_scroll_needed = self.song_text_width > self.song_display_width
        return self.song_scroll_needed
    
    def start_song_scroll(self):
        """开始歌曲名滚动"""
        if self.song_scroll_needed and not self.song_scroll_timer.isActive():
            self.song_scroll_timer.start()
    
    def stop_song_scroll(self):
        """停止歌曲名滚动"""
        if self.song_scroll_timer.isActive():
            self.song_scroll_timer.stop()
            self.reset_song_scroll()
    
    def reset_song_scroll(self):
        """重置歌曲名滚动状态"""
        self.song_scroll_offset = 0
        self.song_scroll_direction = 1
        self.song_scroll_state = 0
        self.update_song_display()
    
    def update_song_display(self):
        """更新歌曲名显示"""
        if not self.song_scroll_needed:
            # 不需要滚动，直接显示完整文本
            self.song_label.setText(self.song_original_text)
            return
        
        # 需要滚动，根据偏移量显示部分文本
        # 创建一个足够宽的QPixmap用于绘制文本
        pixmap = QPixmap(max(self.song_text_width, self.song_display_width), self.song_label.height())
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setFont(self.song_label.font())
        painter.setPen(QColor(255, 255, 255, 128))  # 与标签相同的颜色
        
        # 绘制文本（居中对齐）
        rect = QRectF(0, 0, pixmap.width(), pixmap.height())
        painter.drawText(rect, Qt.AlignCenter, self.song_original_text)
        painter.end()
        
        # 确保偏移量在有效范围内
        max_offset = max(0, self.song_text_width - self.song_display_width)
        self.song_scroll_offset = max(0, min(self.song_scroll_offset, max_offset))
        
        # 截取当前偏移量对应的部分
        clipped_pixmap = pixmap.copy(self.song_scroll_offset, 0, self.song_display_width, self.song_label.height())
        
        # 更新标签显示
        self.song_label.setPixmap(clipped_pixmap)
    
    def update_song_scroll(self):
        """更新歌曲名滚动"""
        if not self.song_scroll_needed:
            return
        
        # 根据滚动状态处理
        if self.song_scroll_state == 0:  # 初始/停顿状态
            # 开始滚动
            self.song_scroll_state = 1
            return
        
        # 更新滚动偏移量
        self.song_scroll_offset += self.song_scroll_direction * self.song_scroll_speed
        
        # 检查是否到达边界
        if self.song_scroll_direction == 1:  # 向右滚动
            if self.song_scroll_offset >= self.song_text_width - self.song_display_width:
                # 到达右边界，停顿后反向滚动
                self.song_scroll_offset = self.song_text_width - self.song_display_width
                self.song_scroll_state = 0
                self.song_scroll_direction = -1
                # 停顿后反向滚动
                QTimer.singleShot(self.song_scroll_pause_time, self.start_song_scroll)
                self.song_scroll_timer.stop()
        else:  # 向左滚动
            if self.song_scroll_offset <= 0:
                # 到达左边界，停顿后正向滚动
                self.song_scroll_offset = 0
                self.song_scroll_state = 0
                self.song_scroll_direction = 1
                # 停顿后正向滚动
                QTimer.singleShot(self.song_scroll_pause_time, self.start_song_scroll)
                self.song_scroll_timer.stop()
        
        # 更新显示
        self.update_song_display()
    
    def prev_track(self):
        """上一曲"""
        print("执行上一曲操作...")
        # 先触发悬浮歌词的隐藏动画
        if self.float_lyric_window_visible and self.float_lyric_window:
            # 标记动画正在播放
            self.float_lyric_animating = True
            # 播放消失动画
            self.float_lyric_window.hide_with_animation()
            
            # 动画结束后再重置歌词、进度秒数和窗口可见性
            def on_animation_finished():
                # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                self.current_parsed_lyric = []
                # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                self.last_progress_seconds = 0.0
                # 设置窗口可见性为 False
                self.float_lyric_window_visible = False
                # 标记动画结束
                self.float_lyric_animating = False
            
            # 等待动画完成后再重置
            QTimer.singleShot(500, on_animation_finished)
        
        # 执行上一曲操作
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                current_session.try_skip_previous_async()
                print("上一曲操作执行成功")
            except Exception as e:
                print(f"上一曲操作执行失败: {type(e).__name__}: {e}")
    
    def play_pause(self):
        """播放/暂停"""
        print("执行播放/暂停操作...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                current_session.try_toggle_play_pause_async()
                print("播放/暂停操作执行成功")
                
                # 保存之前的播放状态
                was_playing = self.is_playing
                
                # 立即切换播放状态并更新按钮图标，提高用户体验
                self.is_playing = not self.is_playing
                if self.is_playing:
                    # 播放状态，显示暂停图标
                    self.play_pause_button.setText("■")
                    # 只有在音频可视化开启时才启动音频捕获
                    if self.visualization_style in [3, 4]:
                        self.audio_thread.start_capture()
                    # 从暂停状态变为播放状态，显示悬浮歌词（如果无全屏应用）
                    has_fullscreen, _ = self.is_fullscreen_or_maximized()
                    if not was_playing and FLOAT_LYRIC_ENABLED == 1 and not self.float_lyric_window_visible and self.current_parsed_lyric and not self.actively_hidden and not has_fullscreen:
                        if not self.float_lyric_window:
                            self.float_lyric_window = LyricFloatWindow()
                            # 计算窗口位置
                            screen = QApplication.primaryScreen()
                            screen_geometry = screen.geometry()
                            x = (screen_geometry.width() - self.float_lyric_window.width()) // 2
                            # 将窗口位置设置到屏幕之外
                            y = screen_geometry.height() + 100  # 屏幕下方外
                            self.float_lyric_window.move(x, y)
                        self.float_lyric_window_visible = True
                        self.float_lyric_window.show_with_animation(self.current_parsed_lyric, self.last_progress_seconds)
                else:
                    # 暂停状态，显示播放图标
                    self.play_pause_button.setText("▶")
                    # 暂停时停止音频捕获和可视化
                    print("暂停播放，停止音频捕获和可视化")
                    self.audio_thread.stop_capture()
                    # 暂停状态，隐藏悬浮歌词
                    if self.float_lyric_window_visible:
                        if self.float_lyric_window:
                            self.float_lyric_window.hide_with_animation()
                        self.float_lyric_window_visible = False
            except Exception as e:
                print(f"播放/暂停操作执行失败: {type(e).__name__}: {e}")
    
    def next_track(self):
        """下一曲"""
        print("执行下一曲操作...")
        # 先触发悬浮歌词的隐藏动画
        if self.float_lyric_window_visible and self.float_lyric_window:
            # 标记动画正在播放
            self.float_lyric_animating = True
            # 播放消失动画
            self.float_lyric_window.hide_with_animation()
            
            # 动画结束后再重置歌词、进度秒数和窗口可见性
            def on_animation_finished():
                # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                self.current_parsed_lyric = []
                # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                self.last_progress_seconds = 0.0
                # 设置窗口可见性为 False
                self.float_lyric_window_visible = False
                # 标记动画结束
                self.float_lyric_animating = False
            
            # 等待动画完成后再重置
            QTimer.singleShot(500, on_animation_finished)
        
        # 执行下一曲操作
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                current_session.try_skip_next_async()
                print("下一曲操作执行成功")
            except Exception as e:
                print(f"下一曲操作执行失败: {type(e).__name__}: {e}")
    
    async def get_current_session(self):
        """获取当前媒体会话"""
        try:
            from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as MediaManager
            # 获取媒体会话管理器
            manager = await MediaManager.request_async()
            # 获取当前会话
            current_session = manager.get_current_session()
            return current_session
        except Exception as e:
            print(f"获取当前会话失败: {type(e).__name__}: {e}")
            return None
    
    def update_volume(self, volume_percent):
        """更新音量（兼容旧代码，三段式布局中不显示音量控制）"""
        pass


class MediaGUIFromCurrent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("媒体信息显示")
        self.setGeometry(100, 100, 500, 300)
        
        # 初始化UI
        self.init_ui()
        
        # 创建灵动岛组件
        self.dynamic_island = DynamicIslandWidget()
        # 居中显示在屏幕顶部
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        x = (screen_geometry.width() - self.dynamic_island.width()) // 2
        y = 20
        self.dynamic_island.move(x, self.dynamic_island.offscreen_y)  # 初始位置在画面外
        
        # 根据开关决定显示模式
        if DYNAMIC_ISLAND_ENABLED == 1:
            # 启用灵动岛模式，隐藏主窗口
            self.is_dynamic_island_mode = True
            # 不直接显示灵动岛，让它通过动画自行管理显示和隐藏
            self.hide()
        else:
            # 显示主窗口，隐藏灵动岛
            self.is_dynamic_island_mode = False
            self.dynamic_island.hide()
            self.show()
    
    # 移除toggle_mode方法，现在通过DYNAMIC_ISLAND_ENABLED变量控制模式
    
    def init_ui(self):
        """初始化主窗口UI"""
        # 设置主布局
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # 创建水平布局用于显示媒体信息和专辑图
        self.content_layout = QHBoxLayout()
        
        # 媒体信息布局 - 左侧
        self.info_layout = QVBoxLayout()
        
        # 创建媒体信息显示区域 - 固定标签+可变值
        self.info_group = QGroupBox("媒体信息")
        self.info_group_layout = QVBoxLayout()
        
        # 创建各个信息项的固定标签和可变值标签
        self.info_items = {}
        
        # 信息项定义 - 移除应用音量和专辑
        info_fields = [
            "应用ID", "状态", 
            "歌手", "歌曲", "进度"
        ]
        
        for field in info_fields:
            # 创建水平布局
            h_layout = QHBoxLayout()
            
            # 固定标签
            label = QLabel(f"{field}: ")
            label.setFixedWidth(80)
            label.setStyleSheet(
                """QLabel { 
                    font-weight: bold; 
                    font-family: 'Microsoft YaHei UI', 'Segoe UI', sans-serif; 
                    font-size: 9pt; 
                }"""
            )
            h_layout.addWidget(label)
            
            # 可变值标签
            value_label = QLabel("-")
            value_label.setStyleSheet(
                """QLabel { 
                    background-color: white; 
                    padding: 2px 5px; 
                    border-radius: 3px; 
                    font-family: 'Microsoft YaHei UI', 'Segoe UI', sans-serif; 
                    font-size: 9pt; 
                }"""
            )
            h_layout.addWidget(value_label)
            
            # 添加到布局
            self.info_group_layout.addLayout(h_layout)
            
            # 保存可变值标签引用
            self.info_items[field] = value_label
        
        # 设置信息组布局
        self.info_group.setLayout(self.info_group_layout)
        
        # 音量滑块布局
        self.volume_layout = QHBoxLayout()
        
        # 音量图标
        self.volume_icon = QLabel("🔊")
        # 设置鼠标指针为手型，提示可点击
        self.volume_icon.setCursor(Qt.PointingHandCursor)
        # 保存静音状态和静音前的音量值
        self.is_muted = False
        self.volume_before_mute = 50
        # 添加点击事件处理
        self.volume_icon.mousePressEvent = self.toggle_mute
        self.volume_layout.addWidget(self.volume_icon)
        
        # 音量滑块
        from PyQt5.QtWidgets import QSlider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)  # 默认值
        # 使用valueChanged信号，实时响应滑块变化
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        self.volume_layout.addWidget(self.volume_slider)
        
        # 音量值显示
        self.volume_value = QLabel("50%")
        self.volume_value.setFixedWidth(50)
        self.volume_layout.addWidget(self.volume_value)
        
        # 添加音量布局到信息布局
        self.info_layout.addWidget(self.info_group)
        self.info_layout.addLayout(self.volume_layout)
        self.content_layout.addLayout(self.info_layout, 1)
        
        # 初始化音量滑块值
        self.update_volume_slider()
        
        # 专辑图显示 - 右侧
        self.album_art_label = QLabel("专辑图")
        self.album_art_label.setAlignment(Qt.AlignCenter)
        self.album_art_label.setFixedSize(200, 200)
        self.album_art_label.setStyleSheet("border: 1px solid gray;")
        self.content_layout.addWidget(self.album_art_label)
        
        self.main_layout.addLayout(self.content_layout)
        
        # 多媒体控制按钮布局
        self.control_layout = QHBoxLayout()
        
        self.prev_button = QPushButton("上一曲")
        self.prev_button.clicked.connect(self.prev_track)
        self.control_layout.addWidget(self.prev_button)
        
        self.play_pause_button = QPushButton("播放/暂停")
        self.play_pause_button.clicked.connect(self.play_pause)
        self.control_layout.addWidget(self.play_pause_button)
        
        self.next_button = QPushButton("下一曲")
        self.next_button.clicked.connect(self.next_track)
        self.control_layout.addWidget(self.next_button)
        
        self.main_layout.addLayout(self.control_layout)
        
        # 创建媒体信息线程
        self.media_thread = None
        
        # 保存当前媒体会话，用于控制操作
        self.current_session = None
        
        # 添加定时器实现实时刷新
        from PyQt5.QtCore import QTimer
        self.refresh_timer = QTimer(self)
        self.refresh_timer.setInterval(500)  # 每500ms刷新一次，减少延迟
        self.refresh_timer.timeout.connect(self.refresh_media_info)
        self.refresh_timer.start()
        
        # 保存上一次的媒体信息，用于检测变化
        self.last_media_info = ""
        self.last_album_art_bytes = None
        self.last_song = ""
        self.last_artist = ""
        self.last_status = ""
        
        # 初始刷新
        self.refresh_media_info()
    
    def refresh_media_info(self):
        """刷新媒体信息"""
        # 不需要设置整个区域为"正在获取"，只在数据变化时更新
        
        # 创建并启动媒体信息获取线程
        self.media_thread = MediaInfoThread()
        self.media_thread.media_info_signal.connect(self.update_media_info)
        self.media_thread.start()
    
    def update_volume_slider(self):
        """更新音量滑块值 - 使用pycaw库的简单方式"""
        try:
            from pycaw.pycaw import AudioUtilities
            
            # 获取默认音频设备并直接访问EndpointVolume属性
            default_device = AudioUtilities.GetSpeakers()
            volume = default_device.EndpointVolume
            
            # 获取音量值（范围0.0到1.0）
            current_volume = volume.GetMasterVolumeLevelScalar()
            # 转换为0-100范围，使用四舍五入而不是截断
            volume_percent = round(current_volume * 100)
            
            # 更新UI
            self.volume_slider.setValue(volume_percent)
            self.volume_value.setText(f"{volume_percent}%")
            
            # 更新音量图标
            if volume_percent == 0:
                self.volume_icon.setText("🔇")
            elif volume_percent < 30:
                self.volume_icon.setText("🔈")
            elif volume_percent < 70:
                self.volume_icon.setText("🔉")
            else:
                self.volume_icon.setText("🔊")
        except Exception as e:
            print(f"更新音量滑块失败: {type(e).__name__}: {e}")
    
    def on_volume_changed(self):
        """处理音量滑块变化事件 - 使用pycaw库的简单方式"""
        try:
            from pycaw.pycaw import AudioUtilities
            
            # 获取滑块值
            volume_percent = self.volume_slider.value()
            # 转换为0-1范围
            volume_level = volume_percent / 100.0
            
            # 获取默认音频设备并直接访问EndpointVolume属性
            default_device = AudioUtilities.GetSpeakers()
            volume = default_device.EndpointVolume
            
            # 设置音量
            volume.SetMasterVolumeLevelScalar(volume_level, None)
            
            # 更新UI
            self.volume_value.setText(f"{volume_percent}%")
            
            # 更新静音状态
            if volume_percent > 0:
                self.is_muted = False
            
            # 更新音量图标
            if volume_percent == 0:
                self.volume_icon.setText("🔇")
            elif volume_percent < 30:
                self.volume_icon.setText("🔈")
            elif volume_percent < 70:
                self.volume_icon.setText("🔉")
            else:
                self.volume_icon.setText("🔊")
        except Exception as e:
            print(f"设置音量失败: {type(e).__name__}: {e}")
    
    def toggle_mute(self, event):
        """切换静音状态 - 一键静音/取消静音"""
        try:
            from pycaw.pycaw import AudioUtilities
            
            # 获取默认音频设备并直接访问EndpointVolume属性
            default_device = AudioUtilities.GetSpeakers()
            volume = default_device.EndpointVolume
            
            if self.is_muted:
                # 取消静音，恢复之前的音量
                volume.SetMasterVolumeLevelScalar(self.volume_before_mute / 100.0, None)
                # 更新UI
                self.volume_slider.setValue(self.volume_before_mute)
                self.volume_value.setText(f"{self.volume_before_mute}%")
                # 更新音量图标
                if self.volume_before_mute == 0:
                    self.volume_icon.setText("🔇")
                elif self.volume_before_mute < 30:
                    self.volume_icon.setText("🔈")
                elif self.volume_before_mute < 70:
                    self.volume_icon.setText("🔉")
                else:
                    self.volume_icon.setText("🔊")
                # 更新静音状态
                self.is_muted = False
            else:
                # 静音，保存当前音量
                self.volume_before_mute = self.volume_slider.value()
                # 设置音量为0
                volume.SetMasterVolumeLevelScalar(0.0, None)
                # 更新UI
                self.volume_slider.setValue(0)
                self.volume_value.setText("0%")
                self.volume_icon.setText("🔇")
                # 更新静音状态
                self.is_muted = True
        except Exception as e:
            print(f"切换静音状态失败: {type(e).__name__}: {e}")
    
    def update_media_info(self, media_info, album_art_bytes):
        """更新媒体信息显示并输出到控制台"""
        import sys
        import re
        
        # 解析媒体信息字符串，提取歌曲名、歌手名和状态
        info_dict = {}
        lines = media_info.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('---') or line.startswith('===') or line.startswith('检测到'):
                    continue
                
                # 查找分隔符
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    # 匹配中文开头，后面可以跟中文、英文或数字
                    match = re.match(r'([\u4e00-\u9fa5]+[\w\u4e00-\u9fa5]*)', key)
                    if match:
                        full_key = match.group(1)
                        info_dict[full_key] = value.strip()
        
        # 获取当前歌曲名、歌手名和状态
        current_song = info_dict.get('歌曲', '')
        current_artist = info_dict.get('歌手', '')
        current_status = info_dict.get('状态', '')
        
        # 检测歌曲或状态是否发生变化
        song_changed = current_song != self.last_song
        artist_changed = current_artist != self.last_artist
        status_changed = current_status != self.last_status
        
        # 只在歌曲或状态变化时输出日志
        if song_changed or artist_changed or status_changed:
            # 输出到控制台，使用更可靠的方式处理Unicode编码问题
            print("获取当前媒体信息...")
            print("=========================")
            try:
                # 尝试直接打印
                print(media_info)
            except UnicodeEncodeError:
                try:
                    # 尝试使用系统默认编码并替换无法编码的字符
                    print(media_info.encode(sys.stdout.encoding, 'replace').decode(sys.stdout.encoding))
                except Exception:
                    # 最后尝试使用UTF-8编码写入字节
                    sys.stdout.buffer.write((media_info + '\n').encode('utf-8', 'replace'))
            print("=========================")
            print("...")
            
            # 更新保存的歌曲名、歌手名和状态
            self.last_song = current_song
            self.last_artist = current_artist
            self.last_status = current_status
        
        # 检测媒体信息是否发生变化，只有变化时才更新UI，减少闪屏
        media_info_changed = media_info != self.last_media_info
        album_art_changed = album_art_bytes != self.last_album_art_bytes
        
        if media_info_changed:
            # 更新各个字段的值，只更新变化的字段
            for field, label in self.info_items.items():
                current_value = info_dict.get(field, "-")
                if label.text() != current_value:
                    label.setText(current_value)
            
            # 保存当前媒体信息
            self.last_media_info = media_info
        
        # 更新专辑图显示 - 总是更新，确保从有专辑图到无专辑图的过渡能正确处理
        if album_art_bytes:
            # 从字节数组创建QPixmap
            pixmap = QPixmap()
            pixmap.loadFromData(album_art_bytes)
            # 调整专辑图大小以适应标签
            pixmap = pixmap.scaled(self.album_art_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.album_art_label.setPixmap(pixmap)
            self.album_art_label.setText("")
        else:
            self.album_art_label.setText("暂无专辑图")
        # 更新缓存
        self.last_album_art_bytes = album_art_bytes
        
        # 移除自动更新音量滑块，避免覆盖用户手动调整
        # 音量滑块只在初始化和用户调整时更新
        
        # 更新灵动岛信息
        if self.is_dynamic_island_mode:
            self.dynamic_island.update_media_info(media_info)
            # 总是更新灵动岛的专辑图，确保从有专辑图到无专辑图的过渡能正确处理
            self.dynamic_island.update_album_art(album_art_bytes)
    
    async def get_current_session(self):
        """获取当前媒体会话"""
        try:
            # 获取媒体会话管理器
            manager = await MediaManager.request_async()
            # 获取当前会话
            current_session = manager.get_current_session()
            return current_session
        except Exception as e:
            print(f"获取当前会话失败: {type(e).__name__}: {e}")
            return None
    
    def prev_track(self):
        """上一曲"""
        print("执行上一曲操作...")
        # 先触发悬浮歌词的隐藏动画
        if hasattr(self, 'dynamic_island') and self.dynamic_island and self.dynamic_island.float_lyric_window_visible and self.dynamic_island.float_lyric_window:
            # 标记动画正在播放
            self.dynamic_island.float_lyric_animating = True
            # 播放消失动画
            self.dynamic_island.float_lyric_window.hide_with_animation()
            
            # 动画结束后再重置歌词、进度秒数和窗口可见性
            def on_animation_finished():
                # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                self.dynamic_island.current_parsed_lyric = []
                # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                self.dynamic_island.last_progress_seconds = 0.0
                # 设置窗口可见性为 False
                self.dynamic_island.float_lyric_window_visible = False
                # 标记动画结束
                self.dynamic_island.float_lyric_animating = False
            
            # 等待动画完成后再重置
            QTimer.singleShot(500, on_animation_finished)
        
        # 执行上一曲操作
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                current_session.try_skip_previous_async()
                print("上一曲操作执行成功")
            except Exception as e:
                print(f"上一曲操作执行失败: {type(e).__name__}: {e}")
        else:
            print("没有获取到当前媒体会话")
    
    def play_pause(self):
        """播放/暂停"""
        print("执行播放/暂停操作...")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                # 执行播放/暂停命令
                current_session.try_toggle_play_pause_async()
                print("播放/暂停操作执行成功")
            except Exception as e:
                print(f"播放/暂停操作执行失败: {type(e).__name__}: {e}")
        else:
            print("没有获取到当前媒体会话")
    
    def next_track(self):
        """下一曲"""
        print("执行下一曲操作...")
        # 先触发悬浮歌词的隐藏动画
        if hasattr(self, 'dynamic_island') and self.dynamic_island and self.dynamic_island.float_lyric_window_visible and self.dynamic_island.float_lyric_window:
            # 标记动画正在播放
            self.dynamic_island.float_lyric_animating = True
            # 播放消失动画
            self.dynamic_island.float_lyric_window.hide_with_animation()
            
            # 动画结束后再重置歌词、进度秒数和窗口可见性
            def on_animation_finished():
                # 重置当前解析后的歌词，避免显示上一首歌曲的歌词
                self.dynamic_island.current_parsed_lyric = []
                # 重置进度秒数，避免显示上一首歌曲0.00秒的歌词
                self.dynamic_island.last_progress_seconds = 0.0
                # 设置窗口可见性为 False
                self.dynamic_island.float_lyric_window_visible = False
                # 标记动画结束
                self.dynamic_island.float_lyric_animating = False
            
            # 等待动画完成后再重置
            QTimer.singleShot(500, on_animation_finished)
        
        # 执行下一曲操作
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        current_session = loop.run_until_complete(self.get_current_session())
        loop.close()
        
        if current_session:
            try:
                # 执行下一曲命令
                current_session.try_skip_next_async()
                print("下一曲操作执行成功")
            except Exception as e:
                print(f"下一曲操作执行失败: {type(e).__name__}: {e}")
        else:
            print("没有获取到当前媒体会话")
    
    def closeEvent(self, event):
        """关闭事件处理"""
        if self.media_thread and self.media_thread.isRunning():
            self.media_thread.quit()
            self.media_thread.wait()
        event.accept()


if __name__ == "__main__":
    print("正在启动媒体信息显示应用...")
    print(f"灵动岛模式: {'开启' if DYNAMIC_ISLAND_ENABLED == 1 else '关闭'}")
    
    # 如果设置了自定义歌词目录，删除默认的Lyrics文件夹
    if LYRIC_DIR:
        lyrics_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Lyrics")
        if os.path.exists(lyrics_dir):
            try:
                import shutil
                shutil.rmtree(lyrics_dir)
                print(f"已删除默认Lyrics文件夹: {lyrics_dir}")
            except Exception as e:
                print(f"删除默认Lyrics文件夹时出错: {e}")
        
        # 同时删除旧的LRC文件夹（如果存在）
        lrc_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LRC")
        if os.path.exists(lrc_dir):
            try:
                import shutil
                shutil.rmtree(lrc_dir)
                print(f"已删除旧的LRC文件夹: {lrc_dir}")
            except Exception as e:
                print(f"删除旧的LRC文件夹时出错: {e}")
    
    # 优化字体渲染 - 在创建QApplication之前设置高DPI属性
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 启用高DPI缩放
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # 使用高DPI像素图
    
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 设置默认字体为微软雅黑UI，大小9
    app.setFont(QFont("Microsoft YaHei UI", 9))  
    
    # 创建主窗口
    window = MediaGUIFromCurrent()
    # 不要调用window.show()，因为我们在初始化时已经通过DYNAMIC_ISLAND_ENABLED变量设置了显示模式
    print("应用已启动，正在显示GUI窗口...")
    sys.exit(app.exec_())