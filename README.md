# 📚 BookShare - แพลตฟอร์มเช่าและซื้อขายหนังสือ

**BookShare** เป็นเว็บแอปพลิเคชันสำหรับการเช่า ยืม และซื้อขายหนังสือมือสอง พร้อมดีไซน์โทนสี Earth Tone มินิมอล ใช้งานง่าย

---

## ✨ ฟีเจอร์หลัก (Features)

- 🔍 **ค้นหาและเลือกดูหนังสือ**: ค้นหาตามชื่อหนังสือ ผู้แต่ง หรือหมวดหมู่
- 📖 **ระบบเช่ายืม & ซื้อหนังสือ**: เลือกระยะเวลาเช่า คำนวณราคาอัตโนมัติ หรือเลือกซื้อขาด
- 🛒 **ตะกร้าสินค้า & ชำระเงิน**: จัดการรายการหนังสือ สรุปยอด และขั้นตอนการชำระเงิน
- 📦 **ระบบลงรายการหนังสือสำหรับผู้ให้เช่า/ผู้ขาย**: เพิ่มหนังสือใหม่ กำหนดราคา และติดตามสถานะการจัดส่ง/คืน

---

## 🛠️ โครงสร้างโปรเจกต์ (Project Structure)

```text
Project/
├── app.py              # แอปพลิเคชันหลัก พัฒนาด้วย Streamlit
├── index.html          # ดีไซน์ต้นแบบ (HTML + Tailwind CSS)
├── p.hdml              # ไฟล์ต้นฉบับ HTML mockup
├── requirements.txt    # รายการแพ็กเกจ Python ที่จำเป็น
├── .gitignore          # ไฟล์ละเว้นสำหรับการ commit Git
└── README.md           # เอกสารแนะนำโปรเจกต์
```

---

## 🚀 วิธีการติดตั้งและเริ่มใช้งาน (Getting Started)

### 1. โคลนคลังข้อมูล (Clone Repository)
```bash
git clone <URL_ของ_Repository>
cd Project
```

### 2. ติดตั้ง Dependencies
แนะนำให้สร้าง Virtual Environment ก่อน:
```bash
python -m venv venv
# สำหรับ Windows:
.\venv\Scripts\activate
# สำหรับ macOS/Linux:
source venv/bin/activate
```

ติดตั้งแพ็กเกจ:
```bash
pip install -r requirements.txt
```

### 3. รันแอปพลิเคชัน
```bash
streamlit run app.py
```
เบราว์เซอร์จะเปิดหน้าเว็บที่ `http://localhost:8501` โดยอัตโนมัติ
