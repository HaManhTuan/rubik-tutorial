#!/usr/bin/env python3
"""Vẽ sơ đồ Rubik cho rubic.md (PNG, tiếng Việt)."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

C = {
    "W": (247, 247, 247),
    "Y": (245, 208, 0),
    "R": (212, 43, 59),
    "O": (255, 122, 20),
    "B": (26, 111, 219),
    "G": (18, 160, 90),
    "X": (214, 214, 214),
    "K": (38, 38, 38),
    "BG": (255, 248, 236),
    "INK": (43, 33, 24),
    "MUTED": (122, 106, 88),
    "PINK": (225, 29, 72),
}


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_REG
    return ImageFont.truetype(path, size)


def canvas(w, h):
    img = Image.new("RGB", (w, h), C["BG"])
    return img, ImageDraw.Draw(img)


def text(draw, xy, s, size=18, fill=C["INK"], bold=False, anchor="lt"):
    draw.text(xy, s, font=font(size, bold), fill=fill, anchor=anchor)


def rounded(draw, box, fill, outline=C["K"], width=3, radius=12):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def face_3x3(draw, ox, oy, s, gap, grid, highlight=None):
    step = s + gap
    pad = gap
    rounded(
        draw,
        (ox - pad, oy - pad, ox + 3 * s + 4 * gap - pad, oy + 3 * s + 4 * gap - pad),
        C["K"],
        outline=C["K"],
        width=0,
        radius=18,
    )
    for r in range(3):
        for c in range(3):
            x = ox + c * step
            y = oy + r * step
            col = C[grid[r][c]]
            rounded(draw, (x, y, x + s, y + s), col, radius=8)
            if highlight and (r, c) in highlight:
                draw.rounded_rectangle(
                    (x - 4, y - 4, x + s + 4, y + s + 4),
                    radius=10,
                    outline=C["PINK"],
                    width=4,
                )


def proj(ox, oy, s, x, y, z):
    ux, uy = 0.86 * s, 0.50 * s
    sx = ox + (x - z) * ux
    sy = oy - y * s + (x + z) * uy
    return (sx, sy)


def quad(draw, pts, fill):
    draw.polygon(pts, fill=fill, outline=C["K"], width=2)


def iso_cube(draw, ox, oy, s, U, F, R):
    """U/F/R: 3x3, U row0 = sau, F row0 = tầng trên, R col0 = phía trước."""

    def P(x, y, z):
        return proj(ox, oy, s, x, y, z)

    for r in range(3):
        for c in range(3):
            x0, z0 = c, r
            quad(
                draw,
                [P(x0, 3, z0), P(x0 + 1, 3, z0), P(x0 + 1, 3, z0 + 1), P(x0, 3, z0 + 1)],
                C[U[r][c]],
            )
    for c in range(2, -1, -1):
        for r in range(3):
            y1, y0 = 3 - r, 2 - r
            z1, z0 = 3 - c, 2 - c
            quad(
                draw,
                [P(3, y1, z1), P(3, y1, z0), P(3, y0, z0), P(3, y0, z1)],
                C[R[r][c]],
            )
    for r in range(3):
        for c in range(3):
            y1, y0 = 3 - r, 2 - r
            quad(
                draw,
                [P(c, y1, 3), P(c + 1, y1, 3), P(c + 1, y0, 3), P(c, y0, 3)],
                C[F[r][c]],
            )


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    print("wrote", name)


# --- 01 opposite colors + hold ---
img, d = canvas(980, 390)
text(d, (24, 18), "Màu đối diện — cầm khối như thế này", 22, bold=True)
pairs = [
    (70, "Trắng", "W", "Vàng", "Y"),
    (280, "Đỏ", "R", "Cam", "O"),
    (490, "Xanh biển", "B", "Xanh lá", "G"),
]
for x, a, ca, b, cb in pairs:
    text(d, (x + 44, 62), a, 16, anchor="mm", bold=True)
    rounded(d, (x, 78, x + 88, 166), C[ca], radius=16)
    d.line((x + 44, 176, x + 44, 214), fill=C["MUTED"], width=3)
    text(d, (x + 44, 196), "đối", 13, C["MUTED"], anchor="mm")
    rounded(d, (x, 222, x + 88, 310), C[cb], radius=16)
    text(d, (x + 44, 332), b, 16, anchor="mm", bold=True)
iso_cube(
    d,
    820,
    210,
    26,
    [["Y"] * 3] * 3,
    [["G"] * 3, ["G"] * 3, ["W"] * 3],
    [["R"] * 3, ["R"] * 3, ["W"] * 3],
)
text(d, (790, 360), "Vàng trần · Trắng đáy", 15, C["MUTED"], anchor="mm")
save(img, "01-mau-doi-dien.png")

# --- 02 notation ---
img, d = canvas(900, 400)
text(d, (24, 18), "Các mặt khi cầm: Vàng trên, nhìn mặt trước", 22, bold=True)
face_3x3(d, 378, 90, 44, 8, [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "X"]])
text(d, (458, 72), "U  trần", 16, anchor="mm", bold=True)
text(d, (210, 190), "L  trái", 16, C["G"], anchor="mm", bold=True)
text(d, (710, 190), "R  phải", 16, C["B"], anchor="mm", bold=True)
text(d, (458, 292), "F  trước", 16, C["R"], anchor="mm", bold=True)
text(d, (458, 360), "Bạn đang đứng nhìn mặt F", 15, C["MUTED"], anchor="mm")
save(img, "02-ky-hieu-mat.png")

# --- 03 daisy ---
img, d = canvas(820, 400)
text(d, (24, 18), "Hoa cúc: 4 cạnh trắng ngửa quanh nhụy vàng", 22, bold=True)
face_3x3(d, 70, 80, 50, 9, [["X", "W", "X"], ["W", "Y", "W"], ["X", "W", "X"]])
text(d, (164, 310), "Đúng — trắng ngửa lên trần", 15, anchor="mm", bold=True)
# wrong: top-view without white on right edge, plus a white SIDE flap
face_3x3(
    d,
    470,
    80,
    50,
    9,
    [["X", "W", "X"], ["W", "Y", "X"], ["X", "W", "X"]],
    highlight={(1, 2)},
)
sx, sy, ss = 470 + 2 * 59, 80 + 59, 50
rounded(d, (sx + ss + 8, sy, sx + ss + 28, sy + ss), C["W"], radius=6)
text(d, (564, 310), "Sai — trắng nằm hông (ô khoanh)", 15, anchor="mm", bold=True)
text(d, (70, 350), "Góc xám = chưa cần quan tâm", 14, C["MUTED"])
save(img, "03-hoa-cuc.png")

# --- 04 white cross ---
img, d = canvas(860, 380)
text(d, (24, 18), "Dấu cộng trắng ở đáy, màu hông khớp tâm", 22, bold=True)
text(d, (40, 70), "1. Canh màu phụ của cánh cúc với tâm", 16)
text(d, (40, 98), "2. Xoay đúng mặt đó 180°  (F2 / R2 / L2)", 16)
iso_cube(
    d,
    280,
    210,
    30,
    [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "X"]],
    [["X", "X", "X"], ["X", "G", "X"], ["X", "G", "X"]],
    [["X", "X", "X"], ["X", "R", "X"], ["X", "R", "X"]],
)
text(d, (280, 352), "Nhìn nghiêng", 14, C["MUTED"], anchor="mm")
face_3x3(d, 620, 110, 42, 8, [["X", "W", "X"], ["W", "W", "W"], ["X", "W", "X"]])
text(d, (698, 320), "Nhìn đáy: dấu cộng trắng", 14, C["MUTED"], anchor="mm")
save(img, "04-dau-cong-trang.png")

# --- 05 corner ---
img, d = canvas(900, 380)
text(d, (24, 18), "Góc trắng: đặt trước–phải rồi đánh R U R' U'", 22, bold=True)
iso_cube(
    d,
    220,
    200,
    30,
    [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "W"]],
    [["X", "X", "G"], ["X", "G", "X"], ["W", "W", "W"]],
    [["W", "X", "X"], ["X", "R", "X"], ["W", "W", "W"]],
)
text(d, (480, 110), "Viên góc trắng nằm đây", 18, C["PINK"], bold=True)
text(d, (480, 142), "(góc trên - trước - phải)", 16, C["MUTED"])
text(d, (480, 190), "Kẹp giữa 2 tâm trùng 2 màu phụ,", 16)
text(d, (480, 220), "rồi lặp tay phải 1–5 lần.", 16)
save(img, "05-goc-trang.png")

# --- 06 layer 2 T ---
img, d = canvas(900, 380)
text(d, (24, 18), "Tầng 2: chữ T rồi nhìn màu trên đỉnh", 22, bold=True)
face_3x3(d, 70, 118, 42, 8, [["X", "G", "X"], ["X", "G", "X"], ["W", "W", "W"]])
cap = (70 + 50, 68, 70 + 50 + 42, 110)
rounded(d, cap, C["R"], radius=8)
text(d, (210, 88), "màu đỉnh", 13, C["PINK"], anchor="mm", bold=True)
text(d, (148, 350), "Chữ T mặt trước (khớp tâm)", 14, C["MUTED"], anchor="mm")
text(d, (380, 100), "Màu đỉnh trùng tâm PHẢI:", 17, bold=True)
text(d, (380, 132), "U R U' R' U' F' U F", 20, C["B"], bold=True)
text(d, (380, 186), "Màu đỉnh trùng tâm TRÁI:", 17, bold=True)
text(d, (380, 218), "U' L' U L U F U' F'", 20, C["G"], bold=True)
text(d, (380, 280), "Viên cạnh trên trần không được có màu vàng.", 15, C["MUTED"])
save(img, "06-tang-2-chu-t.png")

# --- 07 yellow cross ---
img, d = canvas(980, 360)
text(d, (24, 18), "Dấu cộng vàng — chỉ nhìn 4 cạnh, bỏ qua góc", 22, bold=True)
cases = [
    (36, [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "X"]], "Chấm", "công thức ×1"),
    (270, [["X", "Y", "X"], ["Y", "Y", "X"], ["X", "X", "X"]], "Chữ L  9h–12h", "công thức ×1"),
    (504, [["X", "X", "X"], ["Y", "Y", "Y"], ["X", "X", "X"]], "Thẳng ngang", "công thức ×1"),
    (738, [["X", "Y", "X"], ["Y", "Y", "Y"], ["X", "Y", "X"]], "Đã có cộng", "bỏ qua"),
]
for x, g, title, note in cases:
    face_3x3(d, x, 70, 40, 7, g)
    text(d, (x + 70, 268), title, 15, anchor="mm", bold=True)
    text(d, (x + 70, 292), note, 13, C["MUTED"], anchor="mm")
text(d, (24, 326), "Công thức:  F R U R' U' F'     ·     L phải ở 9h (trái) và 12h (sau)", 14, C["MUTED"])
save(img, "07-cong-vang.png")

# --- 08 sune fish ---
img, d = canvas(920, 370)
text(d, (24, 18), "Sune: đầu cá = góc vàng ở dưới–trái trần", 22, bold=True)
face_3x3(
    d,
    70,
    70,
    50,
    9,
    [["X", "Y", "X"], ["Y", "Y", "Y"], ["Y", "Y", "X"]],
    highlight={(2, 0)},
)
text(d, (164, 320), "Nhìn trần · khoanh đỏ = đầu cá", 14, C["MUTED"], anchor="mm")
text(d, (420, 90), "1 góc vàng trên trần: đưa góc đó", 16)
text(d, (420, 118), "về trước–trái (ô khoanh), rồi", 16)
text(d, (420, 154), "R U R' U R U2 R'", 20, C["PINK"], bold=True)
text(d, (420, 206), "2 góc: góc chưa xong ở trước–trái,", 16)
text(d, (420, 234), "vàng nhìn về phía mình.", 16)
text(d, (420, 276), "0 góc: vàng trên hông, trước–trái,", 16)
text(d, (420, 304), "nhìn sang trái.", 16)
save(img, "08-sune-ca.png")

# --- 09 headlights ---
img, d = canvas(860, 340)
text(d, (24, 18), "Mắt kính: 2 góc cùng màu trên 1 mặt hông", 22, bold=True)

def side_bar(draw, x, y, cols):
    rounded(draw, (x - 12, y - 12, x + 3 * 56 + 8, y + 64), C["K"], width=0, radius=14)
    labels = ["góc", "cạnh", "góc"]
    for i, col in enumerate(cols):
        rounded(draw, (x + i * 56, y, x + i * 56 + 48, y + 48), C[col], radius=8)
        text(draw, (x + i * 56 + 24, y + 68), labels[i], 13, C["MUTED"], anchor="mm")

side_bar(d, 70, 90, ["R", "G", "R"])
text(d, (154, 200), "Có mắt kính  (Đỏ–xanh–Đỏ)", 15, anchor="mm", bold=True)
side_bar(d, 470, 90, ["R", "G", "O"])
text(d, (554, 200), "Chưa có  (hai góc khác màu)", 15, anchor="mm", bold=True)
text(d, (24, 250), "Canh mắt kính với tâm, rồi xoay CẢ KHỐI để mặt đó sang TRÁI", 16, bold=True)
text(d, (24, 282), "(không xoay tầng 3). Cạnh tầng 3 sẽ bị xáo — chưa cần lo.", 15, C["MUTED"])
save(img, "09-mat-kinh.png")

# --- 10 T-perm hold ---
img, d = canvas(920, 400)
text(d, (24, 18), "T-perm: mặt mắt kính (đã khớp tâm) bên TAY TRÁI", 22, bold=True)
iso_cube(
    d,
    280,
    210,
    28,
    [["Y"] * 3] * 3,
    [["O", "X", "G"], ["X", "O", "X"], ["W", "W", "W"]],
    [["G", "X", "B"], ["X", "B", "X"], ["W", "W", "W"]],
)
rounded(d, (40, 100, 128, 290), C["K"], width=0, radius=14)
rounded(d, (52, 112, 116, 164), C["R"], radius=8)
rounded(d, (52, 174, 116, 226), C["X"], radius=8)
rounded(d, (52, 236, 116, 288), C["R"], radius=8)
text(d, (84, 86), "tay trái", 15, C["PINK"], anchor="mm", bold=True)
text(d, (84, 312), "mắt kính", 14, C["MUTED"], anchor="mm")
text(d, (520, 120), "R U R' U' R' F R2", 18, bold=True)
text(d, (520, 152), "U' R' U' R U R' F'", 18, bold=True)
text(d, (520, 210), "Xoay cả khối, không xoay tầng 3.", 15, C["MUTED"])
save(img, "10-tperm-cam.png")

# --- 11 U-perm hold ---
img, d = canvas(940, 390)
text(d, (24, 18), "U-perm: mặt / cạnh đã đúng đưa ra PHÍA SAU", 22, bold=True)
iso_cube(
    d,
    240,
    210,
    28,
    [["Y"] * 3] * 3,
    [["O", "G", "R"], ["X", "O", "X"], ["W", "W", "W"]],
    [["R", "O", "G"], ["X", "R", "X"], ["W", "W", "W"]],
)
# back face hint: a bar behind
rounded(d, (40, 100, 128, 290), C["K"], width=0, radius=14)
rounded(d, (52, 112, 116, 164), C["G"], radius=8)
rounded(d, (52, 174, 116, 226), C["G"], radius=8)
rounded(d, (52, 236, 116, 288), C["G"], radius=8)
text(d, (84, 86), "mặt sau", 15, C["PINK"], anchor="mm", bold=True)
text(d, (84, 312), "FULL màu", 14, C["MUTED"], anchor="mm")
text(d, (500, 100), "Tìm 1 mặt hông FULL màu", 17, bold=True)
text(d, (500, 130), "(2 góc + cạnh giữa khớp tâm)", 16, C["MUTED"])
text(d, (500, 172), "Xoay cả khối, mặt đó ra SAU", 17, C["PINK"], bold=True)
text(d, (500, 214), "R U' R U R U R U' R' U' R2", 17, bold=True)
text(d, (500, 260), "Chưa xong: giữ cạnh đúng ở sau,", 15, C["MUTED"])
text(d, (500, 286), "đánh thêm 1 lần.", 15, C["MUTED"])
save(img, "11-uperm-cam.png")

# --- 12 solved ---
img, d = canvas(720, 380)
text(d, (24, 18), "Xong — 6 mặt một màu", 22, bold=True)
iso_cube(
    d,
    360,
    200,
    34,
    [["Y"] * 3 for _ in range(3)],
    [["G"] * 3 for _ in range(3)],
    [["R"] * 3 for _ in range(3)],
)
save(img, "12-xong.png")

# --- 13 daisy 4 places ---
img, d = canvas(980, 420)
text(d, (24, 16), "Hoa cúc: 4 chỗ viên cạnh trắng hay gặp", 22, bold=True)

def mini_front(draw, x, y, grid, title, note, flap=None, hl=None):
    face_3x3(draw, x, y, 32, 6, grid, highlight=hl)
    text(draw, (x + 56, y + 132), title, 14, anchor="mm", bold=True)
    text(draw, (x + 56, y + 154), note, 12, C["MUTED"], anchor="mm")
    if flap:
        fx, fy, col = flap
        rounded(draw, (fx, fy, fx + 16, fy + 32), C[col], radius=5)

mini_front(
    d, 40, 70,
    [["X", "W", "X"], ["W", "Y", "W"], ["X", "W", "X"]],
    "Đã đúng", "bỏ qua, đừng đụng",
)
mini_front(
    d, 270, 70,
    [["X", "X", "X"], ["X", "G", "X"], ["X", "W", "X"]],
    "Đáy, trắng nhìn hông", "xoay mặt đó 1 nấc",
    hl={(2, 1)},
)
mini_front(
    d, 500, 70,
    [["X", "X", "X"], ["X", "G", "W"], ["X", "X", "X"]],
    "Tầng giữa, trắng nhìn mình", "cầm trước-phải, đánh R",
    hl={(1, 2)},
)
mini_front(
    d, 730, 70,
    [["X", "X", "X"], ["X", "G", "X"], ["X", "X", "X"]],
    "Tầng giữa, trắng nhìn phải", "cầm trước-phải, đánh F'",
    flap=(730 + 2 * 38 + 32 + 6, 70 + 38, "W"),
    hl={(1, 2)},
)
text(d, (24, 360), "Trước khi xoay: nếu cánh cúc đã đúng đang nằm đúng chỗ mặt đó, xoay U đưa cánh đó sang chỗ khác.", 15, C["MUTED"])
text(d, (24, 388), "Đáy + trắng nhìn xuống: không thấy trắng ở hông — xoay mặt đó 2 nấc (180°).", 15, C["MUTED"])
save(img, "13-hoa-cuc-4-cho.png")

# --- 14 white corner 3 orientations ---
img, d = canvas(980, 380)
text(d, (24, 16), "Góc trắng trên trần: 3 hướng — cứ lặp R U R' U'", 22, bold=True)
iso_cube(
    d, 160, 200, 24,
    [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "W"]],
    [["X", "X", "G"], ["X", "G", "X"], ["W", "W", "W"]],
    [["R", "X", "X"], ["X", "R", "X"], ["W", "W", "W"]],
)
text(d, (160, 330), "Trắng ngửa lên", 14, anchor="mm", bold=True)
iso_cube(
    d, 490, 200, 24,
    [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "G"]],
    [["X", "X", "W"], ["X", "G", "X"], ["W", "W", "W"]],
    [["R", "X", "X"], ["X", "R", "X"], ["W", "W", "W"]],
)
text(d, (490, 330), "Trắng nhìn về mình", 14, anchor="mm", bold=True)
iso_cube(
    d, 820, 200, 24,
    [["X", "X", "X"], ["X", "Y", "X"], ["X", "X", "R"]],
    [["X", "X", "G"], ["X", "G", "X"], ["W", "W", "W"]],
    [["W", "X", "X"], ["X", "R", "X"], ["W", "W", "W"]],
)
text(d, (820, 330), "Trắng nhìn sang phải", 14, anchor="mm", bold=True)
text(d, (24, 358), "Cả 3 hướng: giữ viên ở trước-phải, đánh tay phải đến khi trắng chui xuống đáy.", 15, C["MUTED"])
save(img, "14-goc-trang-3-huong.png")

# --- 15 yellow vertical line ---
img, d = canvas(820, 340)
text(d, (24, 16), "Đường thẳng vàng dọc: xoay U thành ngang trước", 22, bold=True)
face_3x3(d, 70, 70, 40, 7, [["X", "Y", "X"], ["X", "Y", "X"], ["X", "Y", "X"]])
text(d, (134, 268), "Thẳng dọc  (12h-6h)", 15, anchor="mm", bold=True)
text(d, (134, 292), "chưa đánh — xoay U", 13, C["PINK"], anchor="mm")
text(d, (330, 165), "xoay U", 16, C["PINK"], anchor="mm", bold=True)
face_3x3(d, 470, 70, 40, 7, [["X", "X", "X"], ["Y", "Y", "Y"], ["X", "X", "X"]])
text(d, (534, 268), "Thẳng ngang", 15, anchor="mm", bold=True)
text(d, (534, 292), "rồi đánh F R U R' U' F'", 13, C["MUTED"], anchor="mm")
save(img, "15-cong-vang-doc.png")

# --- 16 sune 0 and 2 ---
img, d = canvas(980, 420)
text(d, (24, 16), "Sune: cách cầm khi 0 góc hoặc 2 góc vàng trên trần", 22, bold=True)
face_3x3(
    d, 80, 70, 42, 8,
    [["X", "Y", "X"], ["Y", "Y", "Y"], ["X", "Y", "X"]],
    highlight={(2, 0)},
)
rounded(d, (80 - 24, 70 + 2 * 50, 80 - 6, 70 + 2 * 50 + 42), C["Y"], radius=6)
text(d, (155, 300), "0 góc vàng trên trần", 16, anchor="mm", bold=True)
text(d, (155, 328), "Vàng trên hông góc dưới-trái,", 14, C["MUTED"], anchor="mm")
text(d, (155, 350), "nhìn sang trái, rồi Sune.", 14, C["MUTED"], anchor="mm")
face_3x3(
    d, 560, 70, 42, 8,
    [["X", "Y", "Y"], ["Y", "Y", "Y"], ["X", "Y", "Y"]],
    highlight={(2, 0)},
)
text(d, (635, 300), "2 góc vàng trên trần", 16, anchor="mm", bold=True)
text(d, (635, 328), "Góc chưa xong ở dưới-trái;", 14, C["MUTED"], anchor="mm")
text(d, (635, 350), "vàng nhìn về mình, rồi Sune.", 14, C["MUTED"], anchor="mm")
text(d, (24, 388), "Cả hai: đánh 1 lần, nhìn lại trần, canh hình mới rồi đánh tiếp (thường ra con cá).", 15, C["MUTED"])
save(img, "16-sune-0-va-2.png")

# --- 17 four headlights ---
img, d = canvas(900, 440)
text(d, (24, 16), "4 mặt đều mắt kính: CHỈ xoay tầng 3, không T-perm", 22, bold=True)
face_3x3(d, 360, 120, 36, 7, [["Y"] * 3] * 3)

def bar_h(draw, x, y, cols):
    rounded(draw, (x - 6, y - 6, x + 3 * 34 + 4, y + 34), C["K"], width=0, radius=8)
    for i, col in enumerate(cols):
        rounded(draw, (x + i * 34, y, x + i * 34 + 28, y + 28), C[col], radius=5)

bar_h(d, 368, 78, ["B", "X", "B"])
text(d, (430, 70), "sau", 12, C["MUTED"], anchor="mm")
bar_h(d, 368, 280, ["G", "X", "G"])
text(d, (430, 328), "trước", 12, C["MUTED"], anchor="mm")
rounded(d, (300, 114, 340, 260), C["K"], width=0, radius=8)
rounded(d, (306, 120, 334, 148), C["O"], radius=5)
rounded(d, (306, 166, 334, 194), C["X"], radius=5)
rounded(d, (306, 212, 334, 240), C["O"], radius=5)
text(d, (286, 190), "trái", 12, C["MUTED"], anchor="mm")
rounded(d, (530, 114, 570, 260), C["K"], width=0, radius=8)
rounded(d, (536, 120, 564, 148), C["R"], radius=5)
rounded(d, (536, 166, 564, 194), C["X"], radius=5)
rounded(d, (536, 212, 564, 240), C["R"], radius=5)
text(d, (610, 190), "phải", 12, C["MUTED"], anchor="mm")
text(d, (24, 360), "Góc đã đúng chỗ với nhau. Xoay U / U' đến khi mỗi cặp khớp tâm.", 15, C["PINK"], bold=True)
text(d, (24, 392), "Đánh T-perm lúc này sẽ phá. Chỉ T-perm khi có đúng 1 cặp mắt kính.", 15, C["MUTED"])
save(img, "17-bon-mat-kinh.png")

# --- 18 AUF ---
img, d = canvas(860, 360)
text(d, (24, 16), "Gần xong nhưng lệch 1 nấc: chỉ xoay tầng trên", 22, bold=True)
iso_cube(
    d, 200, 200, 28,
    [["Y"] * 3 for _ in range(3)],
    [["R", "R", "R"], ["G", "G", "G"], ["G", "G", "G"]],
    [["G", "G", "G"], ["R", "R", "R"], ["R", "R", "R"]],
)
text(d, (200, 330), "Tầng 3 lệch tâm", 14, C["PINK"], anchor="mm", bold=True)
iso_cube(
    d, 620, 200, 28,
    [["Y"] * 3 for _ in range(3)],
    [["G"] * 3 for _ in range(3)],
    [["R"] * 3 for _ in range(3)],
)
text(d, (620, 330), "Xoay U cho khớp", 14, anchor="mm", bold=True)
save(img, "18-lech-tang-u.png")

print("done")
