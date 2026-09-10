# Hướng dẫn giải Rubik 3x3 cho bạn nhỏ (từ A đến Z)

Chào mừng bạn nhỏ đến với thế giới Rubik! Giải Rubik giống xếp hình: làm đúng từng bước, không cần nhớ quá nhiều một lúc.

Tài liệu này dùng **phương pháp từng tầng** (beginner method). Có **hai bộ phép thuật dùng rất nhiều**, nhưng tầng 3 còn vài công thức nữa — đừng lo, mỗi công thức sẽ được giải thích khi tới bước đó.

---

## Quy ước màu sắc và tâm khối

### 1. Màu đối diện (Rubik chuẩn)

- **Trắng** đối **Vàng** — thường giữ **Trắng ở Đáy**, **Vàng ở Trần**.
- **Đỏ** đối **Cam**.
- **Xanh biển** đối **Xanh lá**.

Nếu Rubik nhà bạn **trắng không đối vàng** thì đây là khối non-standard. Hãy dùng khối chuẩn, nếu không các bước dưới sẽ lệch màu.

![Màu đối diện và cách cầm khối](rubic-assets/01-mau-doi-dien.png)

### 2. Tâm không bao giờ đổi chỗ

Sáu ô **tâm** ở giữa mỗi mặt là “nhà” của màu đó. Tâm trắng mãi là mặt trắng, tâm đỏ mãi là mặt đỏ. Mình chỉ xếp **cạnh** và **góc** cho khớp với tâm.

### 3. Chú giải ký hiệu (đọc trước khi xoay)

Nhìn khối, mặt vàng (trần) hướng lên:

| Ký hiệu | Nghĩa |
|---|---|
| `R` | Mặt **phải** xoay 90° thuận (cạnh trước-phải đi **lên**) |
| `R'` | Mặt phải xoay 90° ngược (cạnh trước-phải đi **xuống**) |
| `L` | Mặt **trái** xoay 90° thuận (cạnh trước-trái đi **xuống**) |
| `L'` | Mặt trái xoay 90° ngược (cạnh trước-trái đi **lên**) |
| `U` | Tầng **trên** xoay 90° thuận (nhìn từ trước: tầng trên đi **sang trái**) |
| `U'` | Tầng trên xoay 90° ngược (tầng trên đi **sang phải**) |
| `F` | Mặt **trước** (đang nhìn) xoay 90° thuận |
| `F'` | Mặt trước xoay 90° ngược |
| `B` | Mặt **sau** xoay 90° thuận |
| `B'` | Mặt sau xoay 90° ngược |
| `X2` | Xoay mặt đó **2 nấc = 180°** (ví dụ `F2`, `R2`, `L2`, `B2`, `U2`) |

Dấu `'` đọc là “phẩy” = xoay ngược lại.

![Các mặt U L R F khi cầm khối](rubic-assets/02-ky-hieu-mat.png)

---

## Hai bộ phép thuật dùng nhiều nhất

### Tay phải — `R U R' U'`

1. `R`: tay phải xoay **lên**
2. `U`: ngón trỏ phải đẩy tầng trên **sang trái**
3. `R'`: tay phải xoay **xuống**
4. `U'`: ngón trỏ trái đẩy tầng trên **sang phải**

### Tay trái — `L' U' L U`

1. `L'`: tay trái xoay **lên**
2. `U'`: ngón trỏ trái đẩy tầng trên **sang phải**
3. `L`: tay trái xoay **xuống**
4. `U`: ngón trỏ phải đẩy tầng trên **sang trái**

---

## Bước 1 — Tầng 1: bông hoa cúc và dấu cộng trắng

Giữ **Vàng ở trần**.

### 1.1. Làm bông hoa cúc

Mục tiêu: 4 viên **cạnh trắng** vây quanh nhụy vàng, và **ô trắng phải ngửa lên trần** (không được trắng nằm hông).

![Hoa cúc đúng và sai](rubic-assets/03-hoa-cuc.png)

Góc chưa cần quan tâm.

Cách đưa từng viên cạnh trắng lên:

**Cánh đã đúng** (trắng ngửa trên trần, vây quanh vàng): bỏ qua. Đừng xoay mặt sẽ đá cánh này.

1. **Trắng ở đáy, trắng nhìn xuống**  
   Không thấy trắng ở hông. Xoay đúng mặt đó **2 nấc (180°)** → trắng lên trần.

2. **Trắng ở đáy, trắng nhìn ra hông**  
   Xoay mặt hông đó **1 nấc** cho ô trắng ngửa lên trần.  
   Nếu cánh cúc đã đúng đang nằm ngay chỗ mặt đó, xoay `U` đưa cánh đúng sang chỗ khác **trước**.

3. **Trắng ở tầng giữa**  
   Đặt viên ở vị trí **trước–phải**:
   - Trắng **nhìn về mình** → đánh `R`
   - Trắng **nhìn sang phải** → đánh `F'`  
   Nếu nấc đó đá cánh cúc đã đúng, xoay `U` trước.

4. **Viên đã ở trần nhưng trắng nhìn ra hông (bị lật)**  
   - Xoay tầng trên đưa viên đó ra **mặt trước**.  
   - Kiểm tra góc trên-phải của trần **chưa có cánh cúc**.  
   - Đánh `F` rồi `R` — trắng sẽ ngửa lên.

![Bốn chỗ viên cạnh trắng](rubic-assets/13-hoa-cuc-4-cho.png)

Làm đủ 4 cánh. Hoa cúc xong khi nhìn trần thấy 4 ô trắng quanh tâm vàng.

### 1.2. Biến hoa cúc thành dấu cộng trắng ở đáy

1. Nhìn **màu phụ** (màu hông) của một cánh cúc.
2. Xoay tầng trên (`U` / `U'`) đến khi màu phụ **khớp tâm cùng màu**.
3. Xoay **đúng mặt khớp đó 2 nấc (180°)** để lật viên xuống đáy.  
   Mặt khớp bên trái thì `L2`, bên phải thì `R2`, phía trước thì `F2`, phía sau thì `B2` — không phải lúc nào cũng `F2`.
4. Làm lần lượt 4 viên. Kết quả: **dấu cộng trắng ở đáy**, và màu hông của 4 cạnh trắng cũng khớp tâm.

![Dấu cộng trắng ở đáy](rubic-assets/04-dau-cong-trang.png)

Nếu một cánh đã xuống đáy rồi, đừng xoay mặt đó nữa — chỉ xoay tầng trên để canh cánh tiếp theo.

---

## Bước 2 — Hoàn thành tầng 1 và tầng 2

Từ đây đến hết: **Trắng ở đáy, Vàng ở trần**.

### 2.1. Đưa 4 góc trắng về đúng chỗ (xong tầng 1)

**Góc đã đúng** (trắng kín đáy, hai màu hông khớp tâm): bỏ qua, đừng lấy lên.

Tìm viên **góc có màu trắng** đang ở tầng 3 (trần):

1. Xoay tầng 3 sao cho viên góc nằm **giữa 2 tâm** trùng với 2 màu phụ của viên đó.
2. Đặt viên góc ở vị trí **trước — bên phải** (góc trên-trước-phải).
3. Đánh tay phải `R U R' U'` **1 đến 5 lần**, đến khi trắng chui xuống đáy đúng chỗ.

Trắng có thể ngửa lên, nhìn về mình, hoặc nhìn sang phải — **cả 3 hướng đều lặp công thức đó**, không cần nhớ thêm.

![Ba hướng góc trắng trên trần](rubic-assets/14-goc-trang-3-huong.png)

![Đặt góc trắng ở trước-phải](rubic-assets/05-goc-trang.png)

Lặp với 3 góc còn lại.

**Góc trắng đã nằm đáy nhưng sai chỗ / sai hướng**

1. Xoay cả khối (không xoay tầng) để viên sai nằm ở góc **dưới-trước-phải**.
2. Đánh `R U R' U'` **1 lần** để lấy viên lên trần.
3. Làm lại như góc đang ở tầng 3.

Tầng 1 xong khi cả mặt trắng kín và 4 mặt hông tầng dưới khớp tâm.

### 2.2. Giải tầng 2 (4 viên cạnh giữa)

**Cạnh giữa đã đúng** (khớp cả hai tâm hai bên): bỏ qua.

Tìm viên **cạnh ở tầng 3 không có màu vàng**.

1. Xoay tầng 3 cho màu **trước mặt** khớp tâm → nhìn từ trước ra hình **chữ T**.
2. Nhìn màu trên đỉnh viên cạnh: trùng tâm **bên phải** hay **bên trái**?

![Chữ T tầng 2](rubic-assets/06-tang-2-chu-t.png)

**Đưa viên sang phải**

```
U R U' R' U' F' U F
```

**Đưa viên sang trái**

```
U' L' U L U F U' F'
```

Lặp đến khi 4 cạnh giữa đúng chỗ.

**Cạnh đã nằm tầng 2 nhưng sai chỗ hoặc bị lật**

1. **Xoay cả khối** để khe sai nằm ở **trước–phải** (khe giữa mặt trước và mặt phải).
2. Đánh **công thức sang phải** một lần — không cần chữ T đúng. Viên hỏng sẽ bị đẩy lên trần.
3. Lắp lại viên đó như cạnh đang ở tầng 3.

Nếu trên trần toàn cạnh có vàng thì chắc đang có viên tầng 2 bị kẹt — dùng mẹo trên để lấy ra.

---

## Bước 3 — Tầng 3: mặt vàng và 4 mặt hông

Vẫn **Vàng ở trần, Trắng ở đáy**. Chỉ xoay tầng 3 và các công thức dưới — đừng lật cả khối.

### 3.1. Làm dấu cộng vàng trên trần

Chỉ nhìn **4 viên cạnh** mặt vàng (bỏ qua góc). Có 4 dạng:

| Nhìn trần (cạnh vàng) | Cách cầm | Làm gì |
|---|---|---|
| Đã có dấu cộng | — | **Bỏ qua**, sang 3.2 |
| Chấm (chưa có cạnh vàng) | Cầm mặt nào cũng được | Công thức 1 lần → ra chữ L |
| Chữ L (hai cạnh kề, **9 giờ và 12 giờ**: trái và sau) | Giữ L đúng 9h–12h | Công thức 1 lần → ra đường thẳng |
| Đường thẳng **nằm ngang** | Giữ đường thẳng ngang | Công thức 1 lần → ra dấu cộng |
| Đường thẳng **dọc** (12h–6h) | Xoay `U` thành ngang trước | Rồi công thức 1 lần |

![Bốn dạng dấu cộng vàng](rubic-assets/07-cong-vang.png)

![Thẳng vàng dọc phải xoay thành ngang](rubic-assets/15-cong-vang-doc.png)

**Công thức** (mặt trước = mặt đang nhìn):

```
F + (tay phải 1 lần: R U R' U') + F'
```

Tức là: `F R U R' U' F'`

Chữ L **không** phải chữ V. Nếu L đang ở góc khác, xoay tầng trên cho L về 9h–12h rồi mới đánh. Đường thẳng đang **dọc** thì xoay `U` thành **ngang** rồi mới đánh — đừng đánh khi đang dọc.

### 3.2. Phủ kín mặt vàng (Sune)

Mục tiêu: 4 góc cũng vàng ngửa lên trần. Công thức:

```
R U R' U R U2 R'
```

(`U2` = tầng trên xoay 2 nấc.)

Đếm số góc đã có vàng trên trần:

**1 góc vàng trên trần (hình con cá)**  
Xoay tầng 3 đưa góc vàng đó về **góc dưới-trái của mặt trần** (góc trước-trái). Đánh Sune 1 lần.

![Hình con cá Sune](rubic-assets/08-sune-ca.png)

**2 góc vàng trên trần**  
Xoay tầng 3 đưa **một góc chưa xong** vào góc dưới-trái, sao cho ô vàng của góc đó **nhìn về phía mình**. Đánh Sune — thường ra hình cá, rồi làm như trên.

**0 góc vàng trên trần**  
Xoay tầng 3 sao cho một ô vàng nằm **trên hông**, ở góc dưới-trái, **nhìn sang trái**. Đánh Sune — rồi làm tiếp theo hình mới.

![Cách cầm Sune khi 0 góc hoặc 2 góc](rubic-assets/16-sune-0-va-2.png)

**4 góc đã vàng**  
Bỏ qua, sang 3.3.

Có thể phải Sune vài lần. Mỗi lần xong, **nhìn lại trần và cầm lại cho đúng** rồi mới đánh tiếp. Đừng đánh liên tục khi chưa canh hình.

### 3.3. Đổi 4 góc tầng 3 (tìm “mắt kính”)

Mặt vàng đã kín. Giờ xếp **góc** đúng chỗ (màu hông khớp). Cạnh tầng 3 **sẽ bị xáo** — bình thường, chưa cần lo.

**Mắt kính** = trên **cùng một mặt hông**, 2 ô **góc** hai bên **cùng màu** với nhau, ví dụ `ĐỎ — (cạnh xanh) — ĐỎ`. Ô giữa là **cạnh**, không phải tâm.

![Mắt kính có và chưa có](rubic-assets/09-mat-kinh.png)

**Đã có 1 cặp mắt kính**

1. Xoay **chỉ tầng 3** đến khi 2 góc mắt kính khớp **tâm cùng màu**.
2. **Xoay cả khối** (không xoay tầng 3 nữa) để mặt mắt kính nằm **bên tay trái**.
3. Đánh **1 lần** T-perm:

![Cách cầm T-perm: mắt kính bên trái](rubic-assets/10-tperm-cam.png)

```
R U R' U' R' F R2 U' R' U' R U R' F'
```

**Chưa có mắt kính nào**

1. Cầm mặt nào hướng về mình cũng được.
2. Đánh T-perm **1 lần**.
3. Xoay tầng 3 — sẽ xuất hiện 1 cặp mắt kính.
4. Làm lại như trường hợp đã có mắt kính.

**4 góc đã đúng chỗ** (mỗi mặt hông: 2 ô góc khớp tâm): bỏ qua, sang 3.4.

**4 mặt đều có mắt kính** (mỗi hông 2 góc cùng màu với nhau): góc đã đúng permutation. **Chỉ xoay tầng 3** (`U` / `U'`) cho khớp tâm. **Không đánh T-perm** — đánh sẽ phá.

![Bốn mặt đều mắt kính — không T-perm](rubic-assets/17-bon-mat-kinh.png)

### 3.4. Đổi 4 viên cạnh — bước cuối

Góc đã đúng. Chỉ còn xoay vòng **3 hoặc 4 viên cạnh** tầng 3.

Nhìn 4 mặt hông, tìm **một mặt đã full màu** (2 góc + 1 cạnh giữa cùng màu, khớp tâm). Vì góc đã đúng, điều này cũng chính là **một cạnh tầng 3 đã đúng chỗ**.

**Đã có 1 mặt / 1 cạnh đúng**

1. **Xoay cả khối** đưa mặt full đó ra **phía sau** (không phải bên trái).
2. Đánh U-perm:

![Cách cầm U-perm: mặt full phía sau](rubic-assets/11-uperm-cam.png)

```
R U' R U R U R U' R' U' R2
```

3. Nếu chưa xong: giữ cạnh đúng ở **phía sau**, đánh **thêm 1 lần nữa**.

**Chưa có mặt nào full**

1. Cầm mặt nào cũng được, đánh U-perm **1 lần**.
2. Sẽ xuất hiện 1 cạnh / 1 mặt đúng → đưa ra **phía sau** → đánh U-perm thêm 1 lần (nếu cần thì 2 lần).

**4 cạnh đã đúng**: khối xong, không đánh nữa.

**Sáu mặt gần xong nhưng tầng trên lệch 1 nấc so với tâm:** chỉ xoay `U` / `U'` / `U2` cho khớp. Không đánh thêm T-perm hay U-perm.

![Lệch tầng trên — chỉ xoay U](rubic-assets/18-lech-tang-u.png)

Xong khi 6 mặt đều một màu. Chúc bạn nhỏ hoàn thành khối Rubik!

![Khối Rubik đã xong](rubic-assets/12-xong.png)

---

## Khi bị kẹt — kiểm tra nhanh

1. Tâm 6 mặt còn đúng quy ước trắng đối vàng chưa?
2. Hoa cúc: 4 ô trắng **có ngửa lên trần** không, hay trắng đang nằm hông? Cánh đã đúng thì đừng đụng.
3. Dấu cộng trắng: màu hông cạnh trắng đã khớp tâm chưa? (Chỉ trắng ở đáy thì chưa đủ.)
4. Góc trắng “biến mất”: chúng đang cắm sai dưới đáy — lấy lên bằng `R U R' U'` rồi lắp lại. Góc đã đúng thì bỏ qua.
5. Tầng 2 không còn viên không-vàng trên trần: có viên đang kẹt sai slot tầng 2 — đưa khe sai ra trước-phải, đánh công thức sang phải để đẩy lên.
6. Chữ L vàng: đã cầm đúng **9h và 12h** chưa? Thẳng **dọc** thì xoay `U` thành ngang trước.
7. Sune: mỗi lần đánh xong phải **canh lại hình**, không spam khi cầm sai.
8. Mắt kính: **4 mặt đều mắt kính** thì chỉ xoay tầng 3, không T-perm. Một cặp: đưa sang trái bằng **xoay cả khối**.
9. Bước cuối: mặt full phải ở **phía sau**, không phải bên trái.
10. Gần xong, chỉ lệch tâm: xoay `U`, đừng đánh công thức dài.

---

## Bảng công thức (để ôn)

| Bước | Công thức |
|---|---|
| Góc tầng 1 / lấy góc kẹt lên | `R U R' U'` |
| Cạnh tầng 2 sang phải | `U R U' R' U' F' U F` |
| Cạnh tầng 2 sang trái | `U' L' U L U F U' F'` |
| Dấu cộng vàng | `F R U R' U' F'` |
| Phủ vàng (Sune) | `R U R' U R U2 R'` |
| Đổi góc (T-perm, mắt kính bên trái) | `R U R' U' R' F R2 U' R' U' R U R' F'` |
| Đổi cạnh (U-perm, cạnh đúng phía sau) | `R U' R U R U R U' R' U' R2` |
