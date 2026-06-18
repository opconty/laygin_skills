#!/usr/bin/env python3
"""
图像水印工具 - 为图片添加透明水印

用法:
    python watermark.py -i image.jpg -w watermark.png -p bottom-right -o output.jpg
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps


def add_watermark(image_path, watermark_path, position, output_path, opacity=0.5, margin=20, scale=1.0):
    """
    为图像添加水印
    
    Args:
        image_path: 原图路径
        watermark_path: 水印图路径
        position: 水印位置 (top-left, top-right, bottom-left, bottom-right, center)
        output_path: 输出路径
        opacity: 透明度 0-1
        margin: 边距像素
        scale: 水印缩放比例
    """
    # 加载图像
    try:
        base_image = Image.open(image_path).convert("RGBA")
    except Exception as e:
        print(f"错误：无法打开原图 '{image_path}': {e}")
        sys.exit(1)
    
    try:
        watermark = Image.open(watermark_path).convert("RGBA")
    except Exception as e:
        print(f"错误：无法打开水印图 '{watermark_path}': {e}")
        sys.exit(1)
    
    # 缩放水印
    if scale != 1.0:
        new_width = int(watermark.width * scale)
        new_height = int(watermark.height * scale)
        watermark = watermark.resize((new_width, new_height), Image.LANCZOS)
    
    # 调整透明度
    if opacity < 1.0:
        # 获取水印的 alpha 通道
        r, g, b, a = watermark.split()
        # 调整透明度
        a = a.point(lambda x: int(x * opacity))
        watermark = Image.merge("RGBA", (r, g, b, a))
    
    # 计算位置
    position = position.lower().replace("-", "").replace("_", "")
    
    if position == "center":
        x = (base_image.width - watermark.width) // 2
        y = (base_image.height - watermark.height) // 2
    elif position in ("topleft", "topleft"):
        x = margin
        y = margin
    elif position in ("topright", "topright"):
        x = base_image.width - watermark.width - margin
        y = margin
    elif position in ("bottomleft", "bottomleft"):
        x = margin
        y = base_image.height - watermark.height - margin
    elif position in ("bottomright", "bottomright"):
        x = base_image.width - watermark.width - margin
        y = base_image.height - watermark.height - margin
    else:
        print(f"错误：未知位置 '{position}'")
        print("支持的位置：top-left, top-right, bottom-left, bottom-right, center")
        sys.exit(1)
    
    # 创建透明图层并粘贴水印
    layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    layer.paste(watermark, (x, y))
    
    # 合成图像
    result = Image.alpha_composite(base_image, layer)
    
    # 转换为 RGB 保存为 JPEG 或保留 RGBA 保存为 PNG
    _, ext = Path(output_path).suffix.lower(), Path(output_path).suffix.lower()
    if ext == ".jpg" or ext == ".jpeg":
        result = result.convert("RGB")
        result.save(output_path, "JPEG", quality=95)
    elif ext == ".png":
        result.save(output_path, "PNG")
    else:
        # 根据输出扩展名自动选择格式
        if ext in (".jpg", ".jpeg"):
            result = result.convert("RGB")
            result.save(output_path, "JPEG", quality=95)
        else:
            result.save(output_path)
    
    print(f"水印添加成功！")
    print(f"  原图：{image_path}")
    print(f"  水印图：{watermark_path}")
    print(f"  位置：{position}")
    print(f"  透明度：{opacity}")
    print(f"  输出：{output_path}")


def main():
    parser = argparse.ArgumentParser(description="图像水印工具")
    parser.add_argument("-i", "--image", required=True, help="原图路径")
    parser.add_argument("-w", "--watermark", required=True, help="水印图路径")
    parser.add_argument(
        "-p", "--position",
        required=True,
        choices=["top-left", "top-right", "bottom-left", "bottom-right", "center"],
        help="水印位置"
    )
    parser.add_argument("-o", "--output", default=None, help="输出路径（默认：原图路径_watermark.扩展名）")
    parser.add_argument("--opacity", type=float, default=0.5, help="透明度 0-1（默认：0.5）")
    parser.add_argument("--margin", type=int, default=20, help="边距像素（默认：20）")
    parser.add_argument("--scale", type=float, default=1.0, help="水印缩放比例（默认：1.0）")
    
    args = parser.parse_args()
    
    # 检查文件是否存在
    if not Path(args.image).exists():
        print(f"错误：原图不存在 '{args.image}'")
        sys.exit(1)
    
    if not Path(args.watermark).exists():
        print(f"错误：水印图不存在 '{args.watermark}'")
        sys.exit(1)
    
    # 生成默认输出路径
    if args.output is None:
        original_path = Path(args.image)
        args.output = str(original_path.parent / f"{original_path.stem}_watermark{original_path.suffix}")
    
    add_watermark(
        image_path=args.image,
        watermark_path=args.watermark,
        position=args.position,
        output_path=args.output,
        opacity=args.opacity,
        margin=args.margin,
        scale=args.scale
    )


if __name__ == "__main__":
    main()
