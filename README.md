
# 灵动岛 (MediaIsland) - 媒体信息显示工具

基于 Windows 系统媒体通知接口的媒体信息显示工具，为缺少悬浮歌词功能的播放器提供扩展支持。**开箱即用，零配置**。

## 🎯 核心特性

- 🔌 **Windows 原生媒体接口** - 基于 Windows 系统媒体通知接口获取媒体信息
- 📱 **通用兼容性** - 支持所有发送媒体通知的播放器和应用程序
- 🎵 **灵动岛模式** - 在屏幕顶部显示媒体信息，支持流畅动画效果
- 📝 **悬浮歌词** - 为无悬浮歌词功能的播放器提供歌词显示扩展
- 🎨 **音频可视化** - 显示音频频谱，支持圆形频谱和波浪形两种样式
- 🔄 **自动更新** - 实时获取并更新媒体信息
- 🎯 **响应式设计** - 自适应不同屏幕分辨率
- 🌐 **多源歌词** - 支持内嵌歌词、本地LRC文件和网易云/QQ音乐在线歌词
- 📂 **智能扫描** - 自动扫描音乐、视频、下载、桌面目录查找音频文件
- 🔧 **智能依赖管理** - 程序自动检测并安装所需依赖，无需手动配置

## 🚀 快速开始

### 一键启动

直接双击运行 `dynamic.py` 即可启动程序！

**无需额外配置** - 程序会：
- 🔍 **自动检测依赖环境** - 智能检查所需的 Python 库是否已安装
- 📦 **自动安装缺失依赖** - 如果检测到缺少依赖，会自动从清华镜像源下载并安装
- 🌐 **使用内置 Python 环境**（可选）- 项目自带完整 Python 环境（位于 `Python/` 目录）
- ⚙️ **自动配置环境变量** - 无需手动设置任何环境变量

### 两种使用方式

#### 方式一：使用内置 Python 环境（推荐）
直接运行 `dynamic.py`，使用项目自带的 Python 环境，开箱即用。

#### 方式二：使用独立 Python 文件
只需下载 `dynamic.py` 单个文件，在您的 Python 环境中运行，程序会：
- 自动检测您的 Python 环境
- 自动安装所有必要的依赖包（numpy、PyQt5、winsdk、pycaw、Pillow、requests、mutagen、sounddevice、soundcard）
- 使用清华镜像源加速下载，安装过程完全自动化

### 系统要求

- Windows 操作系统
- Python 3.7+（如使用独立文件方式）
- 无需预先安装任何依赖包（程序会自动处理）

## 🎮 操作指南

### 基本操作

| 操作 | 功能 |
|------|------|
| **左单击专辑图** | 取消退出倒计时 / 临时隐藏并清除缓存 |
| **右双击专辑图** | 触发退出倒计时（5秒） |
| **双击歌曲名/歌手名** | 切换悬浮歌词显示状态 |
| **点击音频可视化区域** | 切换音频可视化样式 |

### 悬浮歌词操作

- **右键点击** - 切换歌词颜色
- **拖拽移动** - 在非背景穿透模式下可拖拽移动窗口

## ⚙️ 配置说明

所有配置参数位于 `dynamic.py` 文件开头部分：

### 歌词配置

```python
EMBEDDED_LYRIC_ENABLED    = 1  # 内嵌歌词开关
LOCAL_LYRIC_ENABLED       = 1  # 本地歌词开关
AUTO_SCAN_ENABLED         = 1  # 自动扫描目录开关
NETWORK_LYRIC_ENABLED     = 1  # 联网获取歌词开关
LYRIC_OFFSET              = 1.0 # 歌词偏移时间（秒）
```

### 悬浮歌词配置

```python
FLOAT_LYRIC_ENABLED           = 1      # 悬浮歌词开关
FLOAT_LYRIC_TEXT_COLOR        = "green" # 歌词颜色
FLOAT_LYRIC_TEXT_SIZE         = 40     # 歌词字体大小
FLOAT_LYRIC_BACKGROUND_OPACITY = 0.0    # 背景透明度
FLOAT_LYRIC_DISPLAY_MODE      = 1      # 显示模式（0=单行，1=双行）
FLOAT_LYRIC_BOTTOM_MARGIN     = 40     # 屏幕下方间距
FLOAT_LYRIC_BACKGROUND_PENETRATION = 1 # 背景穿透（0=不锁定，1=锁定）
```

### 灵动岛配置

```python
DYNAMIC_ISLAND_ENABLED = 1   # 灵动岛模式开关
DYNAMIC_ISLAND_OPACITY = 0.9 # 灵动岛透明度
```

### 音频可视化配置

```python
VISUALIZATION_STYLE = 3 # 可视化样式（3=圆形频谱，4=波浪形，5=关闭）
```

## 📁 支持格式

### 音频格式

- MP3（支持 ID3 标签）
- FLAC
- OGG
- MP4 / M4A
- WAV
- WMA

### 视频格式

- MKV
- MP4
- AVI
- MOV
- WMV
- FLV
- WebM

### 歌词格式

- 内嵌歌词（USLT、COMM 标签）
- 本地 LRC 文件
- 在线歌词（网易云音乐、QQ 音乐）

## 🛠️ 技术栈

- **开发语言**：Python 3.x
- **GUI 框架**：PyQt5
- **音频处理**：pycaw、sounddevice、soundcard
- **媒体元数据**：mutagen
- **网络请求**：requests
- **数值计算**：numpy
- **图像处理**：Pillow
- **系统交互**：winsdk

## 📂 项目结构

```
灵动岛/
├── dynamic.py      # 主程序文件
└── Python/         # 内置 Python 环境（可选）
    ├── Lib/        # Python 标准库和第三方库
    ├── Scripts/    # Python 脚本
    └── ...
```

## 🤝 常见问题

### Q: 需要手动安装依赖吗？
A: 不需要！程序启动时会自动检测所需的 Python 库，如果缺少会自动从清华镜像源安装，完全无需手动配置。

### Q: 只下载 dynamic.py 单个文件可以运行吗？
A: 可以！只要您的电脑上安装了 Python 3.7+，只需下载 `dynamic.py` 单个文件即可运行，程序会自动检测并安装所有必需的依赖包。

### Q: 依赖安装很慢怎么办？
A: 程序已配置使用清华镜像源（pypi.tuna.tsinghua.edu.cn），通常下载速度很快。如果遇到网络问题，请检查网络连接或稍后重试。

### Q: 悬浮歌词不显示？
A: 检查 `FLOAT_LYRIC_ENABLED` 是否设置为 1，确保音乐正在播放且有歌词。

### Q: 音频可视化不显示？
A: 检查 `VISUALIZATION_STYLE` 是否设置为 3 或 4，确保有音频输出。

### Q: 灵动岛不显示？
A: 检查 `DYNAMIC_ISLAND_ENABLED` 是否设置为 1，确保有媒体会话正在播放。

### Q: 如何自定义歌词目录？
A: 修改 `LYRIC_DIR` 配置项，设置为您的歌词文件夹路径。

## 📄 许可证

本项目采用 MIT 许可证。

## 🎉 致谢

感谢所有为本项目做出贡献的开发者！

---

**享受您的音乐体验！** 🎵
