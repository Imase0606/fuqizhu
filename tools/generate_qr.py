from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont


URL = "https://imase0606.github.io/fuqizhu/"
OUT_DIR = Path("output/qr")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=18,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="#201b1c", back_color="#fffaf6").convert("RGB")
qr_path = OUT_DIR / "fuqizhu-github-pages-qr.png"
qr_img.save(qr_path)

canvas_w, canvas_h = 1080, 1480
canvas = Image.new("RGB", (canvas_w, canvas_h), "#fffaf6")
draw = ImageDraw.Draw(canvas)

draw.rounded_rectangle((70, 70, 1010, 1410), radius=34, fill="#ffffff", outline="#eadbd4", width=4)
draw.text((canvas_w // 2, 150), "同岁同行，一起长大", fill="#201b1c", font=font(56, True), anchor="mm")
draw.text((canvas_w // 2, 220), "泡泡玛特20周年 HTML5 互动作品", fill="#6f6669", font=font(30), anchor="mm")

qr_size = 760
qr_resized = qr_img.resize((qr_size, qr_size), Image.Resampling.NEAREST)
qr_x = (canvas_w - qr_size) // 2
canvas.paste(qr_resized, (qr_x, 320))

draw.rounded_rectangle((180, 1120, 900, 1208), radius=16, fill="#ff5f88")
draw.text((canvas_w // 2, 1164), "微信扫码打开 H5 作品", fill="#ffffff", font=font(36, True), anchor="mm")
draw.text((canvas_w // 2, 1278), URL, fill="#201b1c", font=font(28), anchor="mm")
draw.text((canvas_w // 2, 1342), "建议使用微信或手机浏览器扫码查看", fill="#6f6669", font=font(26), anchor="mm")

poster_path = OUT_DIR / "fuqizhu-github-pages-qr-poster.png"
canvas.save(poster_path)

print(qr_path)
print(poster_path)
