from datetime import date, timedelta
import streamlit as st

# ==============================================================================
# 1. Page Configuration & Custom CSS (Earth Tone & Google Fonts)
# ==============================================================================
st.set_page_config(
    page_title="BookShare - เช่าและซื้อขายหนังสือ",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&family=Mali:wght@400;600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Kanit', sans-serif;
        color: #3D312A;
    }

    .stApp {
        background-color: #F5EFE6;
    }

    h1, h2, h3, .brand-logo {
        font-family: 'Mali', cursive !important;
        color: #6B4F4F !important;
    }

    .book-card {
        background-color: #FFFFFF;
        border: 1px solid #E8D8C4;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(61, 49, 42, 0.05);
    }

    .badge-available {
        background-color: #A3B18A;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-rented {
        background-color: #E26D5C;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-sale {
        background-color: #BC6C25;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    .stButton>button {
        background-color: #6B4F4F !important;
        color: #F5EFE6 !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 500 !important;
    }
    .stButton>button:hover {
        background-color: #BC6C25 !important;
        color: #FFFFFF !important;
    }

    .hero-banner {
        background-color: #E8D8C4;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        margin-bottom: 20px;
        border: 2px dashed #A3B18A;
    }

    .cart-box {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #E8D8C4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. Session State Initialization
# ==============================================================================
if 'user' not in st.session_state:
    st.session_state.user = {
        'logged_in': False,
        'name': '',
        'phone': '',
        'address': ''
    }

if 'cart_buy' not in st.session_state:
    st.session_state.cart_buy = []
if 'cart_rent' not in st.session_state:
    st.session_state.cart_rent = []

if 'my_books' not in st.session_state:
    st.session_state.my_books = [
        {
            'title': 'เจ้าชายน้อย (The Little Prince)',
            'category': 'วรรณกรรม',
            'condition': '95% สภาพสะสม',
            'type': 'ทั้งขายและเช่า',
            'price_buy': 250,
            'price_rent': 15,
            'status': '🟢 พร้อมให้ยืม',
        }
    ]

# ข้อมูลหนังสือจำลอง
MOCK_BOOKS = [
    {
        'id': 1,
        'title': 'Atomic Habits เพราะชีวิตดีได้กว่าที่เป็น',
        'author': 'James Clear',
        'buy_price': 285,
        'rent_price': 15,
        'status': 'available',
        'desc': 'หนังสือการเปลี่ยนแปลงนิสัยโดยเริ่มต้นจากสิ่งเล็กๆ ที่จะส่งผลกระทบอันยิ่งใหญ่ต่อชีวิต',
        'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400',
    },
    {
        'id': 2,
        'title': 'The Psychology of Money',
        'author': 'Morgan Housel',
        'buy_price': 290,
        'rent_price': 20,
        'status': 'rented',
        'desc': 'ข้อคิดเรื่องเงิน อิสรภาพ และโชคลาภ ผ่านมุมมองทางจิตวิทยาและการตัดสินใจของมนุษย์',
        'img': 'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=400',
    },
    {
        'id': 3,
        'title': 'เจ้าชายน้อย (The Little Prince)',
        'author': 'Antoine de Saint-Exupéry',
        'buy_price': 220,
        'rent_price': 0,
        'status': 'sale_only',
        'desc': 'วรรณกรรมคลาสสิกระดับโลกสะท้อนมุมมองชีวิต ความรัก และมิตรภาพอันบริสุทธิ์',
        'img': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400',
    },
    {
        'id': 4,
        'title': 'คิดแบบย่อยสลาย ความคิดสร้างสรรค์',
        'author': 'ผู้เขียนอิสระ',
        'buy_price': 310,
        'rent_price': 18,
        'status': 'available',
        'desc': 'คู่มือปลดล็อกไอเดียและการคิดนอกกรอบเพื่อการสร้างสรรค์ผลงานในยุคดิจิทัล',
        'img': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400',
    },
]

# ==============================================================================
# 3. Dialog Modals (Pop-ups)
# ==============================================================================

# 3.1 Pop-up เข้าสู่ระบบ / ลงทะเบียน
@st.dialog("🔐 เข้าสู่ระบบ / ลงทะเบียน")
def login_dialog():
    st.write("กรุณากรอกข้อมูลเพื่อเข้าสู่ระบบ BookShare")
    name = st.text_input("ชื่อ-นามสกุล", value=st.session_state.user['name'])
    phone = st.text_input("เบอร์โทรศัพท์", value=st.session_state.user['phone'])
    
    if st.button("ตกลง / เข้าสู่ระบบ", use_container_width=True):
        if name and phone:
            st.session_state.user['logged_in'] = True
            st.session_state.user['name'] = name
            st.session_state.user['phone'] = phone
            st.success(f"ยินดีต้อนรับคุณ {name}!")
            st.rerun()
        else:
            st.error("กรุณากรอกชื่อและเบอร์โทรศัพท์ให้ครบถ้วน")

# 3.2 Pop-up ดูรายละเอียดหนังสือ และกดใส่ตะกร้า
@st.dialog("📖 รายละเอียดหนังสือ")
def book_detail_dialog(book):
    st.image(book['img'], use_column_width=True)
    st.subheader(book['title'])
    st.write(f"**ผู้แต่ง:** {book['author']}")
    st.caption(book['desc'])
    st.markdown("---")

    col_b, col_r = st.columns(2)
    
    # ซื้อขาด
    with col_b:
        st.write(f"💵 **ราคาซื้อขาด:** ฿{book['buy_price']}")
        if st.button("🛒 ใส่ตะกร้า (ซื้อ)", key=f"dlg_buy_{book['id']}", use_container_width=True):
            st.session_state.cart_buy.append(book)
            st.toast(f"เพิ่ม '{book['title']}' ลงในตะกร้าซื้อเรียบร้อย!", icon="🛒")
            st.rerun()

    # ยืมอ่าน
    with col_r:
        if book['status'] != 'sale_only':
            st.write(f"🗓️ **ค่ายืม:** ฿{book['rent_price']}/วัน")
            today = date.today()
            start = st.date_input('วันเริ่มยืม', today, key=f"dlg_s_{book['id']}")
            end = st.date_input('วันคืนหนังสือ', today + timedelta(days=7), key=f"dlg_e_{book['id']}")
            
            rent_days = (end - start).days
            if rent_days > 0:
                total_rent = rent_days * book['rent_price']
                st.info(f"เช่า {rent_days} วัน | ราคารวม ฿{total_rent}")
                if st.button("📦 ใส่ตะกร้า (เช่า)", key=f"dlg_rent_{book['id']}", use_container_width=True):
                    rent_item = book.copy()
                    rent_item['rent_days'] = rent_days
                    rent_item['total_rent'] = total_rent
                    rent_item['return_date'] = str(end)
                    st.session_state.cart_rent.append(rent_item)
                    st.toast(f"เพิ่ม '{book['title']}' ลงในตะกร้าเช่าเรียบร้อย!", icon="📖")
                    st.rerun()
            else:
                st.warning("วันคืนต้องอยู่หลังวันเริ่มยืม")
        else:
            st.caption("🚫 หนังสือเล่มนี้สำหรับขายเท่านั้น")

# ==============================================================================
# 4. Sidebar Navigation
# ==============================================================================
st.sidebar.markdown("<h1 class='brand-logo'>📚 BookShare</h1>", unsafe_allow_html=True)

# สถานะเข้าสู่ระบบที่ Sidebar
if st.session_state.user['logged_in']:
    st.sidebar.success(f"👤 ผู้ใช้: **{st.session_state.user['name']}**")
    if st.sidebar.button("ออกจากระบบ"):
        st.session_state.user['logged_in'] = False
        st.rerun()
else:
    if st.sidebar.button("🔑 เข้าสู่ระบบ / ลงทะเบียน", use_container_width=True):
        login_dialog()

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "เมนูการใช้งาน",
    [
        '🏠 หน้าแรก (Explore)',
        '🛒 ตะกร้าสินค้า (Cart)',
        '💳 ชำระเงิน (Checkout)',
        '🏪 บัญชีผู้ขาย (Seller Center)'
    ]
)

st.sidebar.markdown('---')
st.sidebar.write('🛒 **สรุปตะกร้าปัจจุบัน**')
st.sidebar.write(f'• ซื้อขาด: **{len(st.session_state.cart_buy)}** เล่ม')
st.sidebar.write(f'• เช่าอ่าน: **{len(st.session_state.cart_rent)}** เล่ม')

# ==============================================================================
# 5. Page Routing Logic
# ==============================================================================

# ------------------------------------------------------------------------------
# PAGE 1: HOME PAGE
# ------------------------------------------------------------------------------
if menu == '🏠 หน้าแรก (Explore)':
    col_search, col_btn = st.columns([4, 1])
    with col_search:
        st.text_input('🔍 ค้นหาหนังสือ...', placeholder='พิมพ์ชื่อหนังสือ หรือผู้แต่ง...')
    with col_btn:
        st.write("")
        if st.button("🛒 ดูตะกร้า", use_container_width=True):
            st.switch_page # ใช้ Navigation จำลองได้

    st.markdown(
        """
        <div class="hero-banner">
            <h2 style="margin:0; color:#6B4F4F;">📖 สัปดาห์แห่งการอ่าน แบ่งปันความรู้!</h2>
            <p style="margin:6px 0 0 0; color:#3D312A;">ยืมหนังสือประหยัดกว่า 80% หรือลงขายหนังสือมือสองของคุณได้ง่ายๆ ที่นี่</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader('📚 รายการหนังสือแนะนำ')

    cols = st.columns(2)
    for index, book in enumerate(MOCK_BOOKS):
        col_idx = index % 2
        with cols[col_idx]:
            if book['status'] == 'available':
                badge_html = "<span class='badge-available'>🟢 พร้อมให้ยืม</span>"
            elif book['status'] == 'rented':
                badge_html = "<span class='badge-rented'>🔴 ถูกยืมอยู่</span>"
            else:
                badge_html = "<span class='badge-sale'>🏷️ สำหรับขายเท่านั้น</span>"

            st.markdown(
                f"""
                <div class="book-card">
                    <div style="display:flex; gap:15px;">
                        <img src="{book['img']}" style="width:90px; height:130px; object-fit:cover; border-radius:8px;">
                        <div>
                            {badge_html}
                            <h4 style="margin:6px 0 2px 0; color:#3D312A;">{book['title']}</h4>
                            <p style="margin:0; font-size:13px; color:#6B4F4F;">ผู้แต่ง: {book['author']}</p>
                            <p style="margin:6px 0 0 0; font-size:13px;">
                                💵 ขาย: ฿{book['buy_price']} | 🗓️ เช่า: ฿{book['rent_price']}/วัน
                            </p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # ปุ่มเปิด Pop-up รายละเอียด
            if st.button(f"🔍 ดูรายละเอียด & สั่งซื้อ", key=f"btn_detail_{book['id']}"):
                book_detail_dialog(book)

# ------------------------------------------------------------------------------
# PAGE 2: CART PAGE
# ------------------------------------------------------------------------------
elif menu == '🛒 ตะกร้าสินค้า (Cart)':
    st.title('🛒 ตะกร้าสินค้าของคุณ')

    tab_buy, tab_rent = st.tabs([
        f"🛍️ ซื้อขาด ({len(st.session_state.cart_buy)})",
        f"📖 เช่าอ่าน ({len(st.session_state.cart_rent)})"
    ])

    total_all = 0

    with tab_buy:
        if not st.session_state.cart_buy:
            st.info('ไม่มีรายการหนังสือที่เลือกซื้อ')
        else:
            for idx, item in enumerate(st.session_state.cart_buy):
                col_info, col_del = st.columns([5, 1])
                with col_info:
                    st.markdown(f"""
                        <div class="cart-box">
                            <b>{item['title']}</b> - ราคา: ฿{item['buy_price']}
                        </div>
                    """, unsafe_allow_html=True)
                with col_del:
                    if st.button("❌ ลบ", key=f"del_buy_{idx}"):
                        st.session_state.cart_buy.pop(idx)
                        st.rerun()
                total_all += item['buy_price']

    with tab_rent:
        if not st.session_state.cart_rent:
            st.info('ไม่มีรายการหนังสือที่เลือกเช่า')
        else:
            for idx, item in enumerate(st.session_state.cart_rent):
                col_info, col_del = st.columns([5, 1])
                with col_info:
                    st.markdown(f"""
                        <div class="cart-box">
                            <b>{item['title']}</b><br>
                            ระยะเวลาเช่า: {item['rent_days']} วัน (คืนวันที่: {item['return_date']})<br>
                            <b>ค่ายืมรวม: ฿{item['total_rent']}</b>
                        </div>
                    """, unsafe_allow_html=True)
                with col_del:
                    if st.button("❌ ลบ", key=f"del_rent_{idx}"):
                        st.session_state.cart_rent.pop(idx)
                        st.rerun()
                total_all += item['total_rent']

    st.markdown("---")
    st.write(f"### ราคารวมสินค้าทั้งหมด: :green[฿{total_all}]")

# ------------------------------------------------------------------------------
# PAGE 3: CHECKOUT PAGE
# ------------------------------------------------------------------------------
elif menu == '💳 ชำระเงิน (Checkout)':
    st.title('💳 ชำระเงินและระบุที่อยู่จัดส่ง')

    has_items = len(st.session_state.cart_buy) > 0 or len(st.session_state.cart_rent) > 0

    if not has_items:
        st.warning("⚠️ ตะกร้าสินค้าของคุณยังว่างเปล่า กรุณาเลือกหนังสือเข้าตะกร้าก่อนดำเนินการชำระเงิน")
    else:
        col_form, col_summary = st.columns([5, 4])

        with col_form:
            st.subheader('📦 1. กรอกที่อยู่สำหรับจัดส่ง')
            with st.form('address_form'):
                fullname = st.text_input('ชื่อ-นามสกุล ผู้รับ', value=st.session_state.user['name'])
                phone = st.text_input('เบอร์โทรศัพท์ติดต่อ', value=st.session_state.user['phone'])
                address = st.text_area('ที่อยู่จัดส่งอย่างละเอียด', value=st.session_state.user['address'], placeholder="บ้านเลขที่, ถนน, แขวง/ตำบล, เขต/อำเภอ, จังหวัด, รหัสไปรษณีย์")
                
                save_address = st.form_submit_button('บันทึกที่อยู่จัดส่ง')
                if save_address:
                    st.session_state.user['name'] = fullname
                    st.session_state.user['phone'] = phone
                    st.session_state.user['address'] = address
                    st.success("บันทึกข้อมูลที่อยู่เรียบร้อยแล้ว!")

            st.subheader('💳 2. ช่องทางการชำระเงิน')
            payment_method = st.radio(
                'เลือกวิธีชำระเงิน',
                ['PromptPay QR Code', 'โอนเงินผ่านธนาคาร', 'บัตรเครดิต / เดบิต']
            )

        with col_summary:
            st.subheader('📋 สรุปรายการคำสั่งซื้อ')
            buy_total = sum(item['buy_price'] for item in st.session_state.cart_buy)
            rent_total = sum(item['total_rent'] for item in st.session_state.cart_rent)
            shipping_fee = 50 if has_items else 0
            insurance_fee = 100 if len(st.session_state.cart_rent) > 0 else 0

            st.write(f"• ยอดซื้อขาด: ฿{buy_total}")
            st.write(f"• ยอดค่ายืมอ่าน: ฿{rent_total}")
            st.write(f"• ค่าจัดส่ง: ฿{shipping_fee}")
            st.write(f"• ค่าประกันหนังสือ (ได้คืนเมื่อส่งคืนหนังสือ): ฿{insurance_fee}")
            st.markdown("---")
            grand_total = buy_total + rent_total + shipping_fee + insurance_fee
            st.markdown(f"### ยอดชำระสุทธิ: :orange[฿{grand_total}]")

            if payment_method == 'PromptPay QR Code':
                st.image(
                    'https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=BookSharePromptPay',
                    caption='สแกน QR Code เพื่อชำระเงิน'
                )

            st.markdown("---")
            # ตรวจสอบการกรอกที่อยู่ก่อนยอมให้กดชำระเงิน
            if not st.session_state.user['address']:
                st.error("🚨 กรุณากรอกและบันทึก 'ที่อยู่จัดส่ง' ด้านซ้ายก่อนทำการชำระเงิน")
                st.button("ยืนยันและชำระเงิน", disabled=True, use_container_width=True)
            else:
                if st.button("✅ ยืนยันการชำระเงิน", use_container_width=True):
                    st.balloons()
                    st.success("🎉 ชำระเงินเรียบร้อยแล้ว! ระบบกำลังเตรียมจัดส่งสินค้าไปตามที่อยู่ของคุณ")
                    # ล้างตะกร้าหลังชำระเงินสำเร็จ
                    st.session_state.cart_buy = []
                    st.session_state.cart_rent = []

# ------------------------------------------------------------------------------
# PAGE 4: SELLER DASHBOARD
# ------------------------------------------------------------------------------
elif menu == '🏪 บัญชีผู้ขาย (Seller Center)':
    st.title('🏪 บัญชีผู้ขาย / ผู้ให้เช่า')

    if not st.session_state.user['logged_in']:
        st.warning("🔒 กรุณาล็อกอินเข้าสู่ระบบก่อนใช้งานหน้าผู้ขาย")
        if st.button("เข้าสู่ระบบตอนนี้"):
            login_dialog()
    else:
        st.success(f"สวัสดีผู้ขาย: คุณ **{st.session_state.user['name']}** (Verified Seller)")

        tab_add, tab_stock = st.tabs(['➕ ลงขาย/ให้เช่าหนังสือใหม่', '📦 หนังสือของคุณ'])

        with tab_add:
            with st.form('add_book_form'):
                b_title = st.text_input('ชื่อเรื่องหนังสือ')
                b_cat = st.selectbox('หมวดหมู่', ['วรรณกรรม', 'จิตวิทยา/พัฒนาตนเอง', 'ธุรกิจ/การเงิน', 'นิยาย'])
                b_cond = st.text_input('สภาพหนังสือ', placeholder='เช่น 95% สภาพสะสม')
                b_type = st.radio('ประเภทการลงรายการ', ['ขายอย่างเดียว', 'ให้เช่าอย่างเดียว', 'ได้ทั้งขายและเช่า'])

                col1, col2 = st.columns(2)
                with col1:
                    b_buy = st.number_input('ราคาขายขาด (บาท)', min_value=0, value=200)
                with col2:
                    b_rent = st.number_input('ราคาเช่า (บาท/วัน)', min_value=0, value=15)

                btn_add = st.form_submit_button('บันทึกและลงขายทันที')

            if btn_add:
                if b_title:
                    st.session_state.my_books.append({
                        'title': b_title,
                        'category': b_cat,
                        'condition': b_cond,
                        'type': b_type,
                        'price_buy': b_buy,
                        'price_rent': b_rent,
                        'status': '🟢 พร้อมให้ยืม'
                    })
                    st.success(f"ลงขายหนังสือเรื่อง '{b_title}' เรียบร้อยแล้ว!")
                else:
                    st.error("กรุณาระบุชื่อเรื่องหนังสือ")

        with tab_stock:
            for idx, book in enumerate(st.session_state.my_books):
                st.markdown(f"""
                    <div class="cart-box">
                        <h4>{book['title']}</h4>
                        <p>หมวดหมู่: {book['category']} | สภาพ: {book['condition']}</p>
                        <p>ราคาขาย: ฿{book['price_buy']} | ค่ายืม: ฿{book['price_rent']}/วัน</p>
                    </div>
                """, unsafe_allow_html=True)