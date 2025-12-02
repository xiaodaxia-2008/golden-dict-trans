# GoldenDict 集成 `translate.py`

[English](./README_En.md) | **中文**

本指南解释了如何将 `translate.py` 脚本集成到 GoldenDict 中，使您能够根据语言检测在中文和英文之间自动翻译选定的文本。

## 脚本功能

`translate.py` 脚本执行以下操作：
-   **语言检测**：自动检测输入文本的语言。
-   **条件翻译**：
    -   如果检测到的语言是**中文**，则将文本翻译为**英文**。
    -   如果检测到的语言**不是中文**（例如，英文、西班牙语等），则将文本翻译为**中文**。
-   **GoldenDict 优化输出**：生成专为 GoldenDict 显示面板设计的干净 HTML 输出。

## 先决条件

在集成之前，请确保您已具备以下条件：

- 安装 [uv](https://docs.astral.sh/uv/#installation)

## 设置

1.  **保存脚本**：确保 `translate.py` 已保存到您系统上的永久位置（例如，`C:\Users\YourUser\Scripts\translate.py` 或 `/home/youruser/scripts/translate.py`）。

2.  **配置 GoldenDict**：
    *   打开 GoldenDict。
    *   转到 `编辑 -> 词典 -> 程序` 选项卡。
    *   点击 `添加程序`。
    *   **类型**：选择 `Html`。
    *   **命令行**：这至关重要。输入以下命令，将 `"path/to/translate.py"` 替换为您的 `translate.py` 文件的实际绝对路径。`uv` 将在临时虚拟环境中自动管理脚本的依赖项。
        ```
        uv run "path/to/translate.py" "$GDSEARCH$"
        ```
        **示例 (Windows)**：
        `uv run "C:\Users\YourUser\Scripts\translate.py" "$GDSEARCH$"`
        **示例 (Linux/macOS)**：
        `uv run "/home/youruser/scripts/translate.py" "$GDSEARCH$"`
        **重要提示**：`$GDSEARCH$` 变量是 GoldenDict 中选定文本的占位符。如果文本可能包含空格，请确保将其用双引号括起来。
    *   **名称**：给它一个描述性名称，例如“使用 uv 自动翻译”。
    *   **图标 (可选)**：您可以为您的程序选择一个图标。
    *   点击 `确定` 保存程序词典。

## GoldenDict 中的用法

像使用普通词典一样使用它。
