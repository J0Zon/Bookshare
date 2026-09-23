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

# Custom CSS กำหนด Earth Tone Palette และฟอนต์ Kanit/Mali
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&family=Mali:wght@400;600&display=swap');

    /* Color Palette Variables
       Primary: #F5EFE6 (เบจ/ครีม)
       Secondary: #E8D8C4 / #A3B18A (น้ำตาลอ่อน/เขียวมัสตาร์ด)
       Accent: #6B4F4F / #BC6C25 (น้ำตาลเข้ม/ส้มอิฐ)
       Text: #3D312A (น้ำตาลไหม้)
    */

    html, body, [class*="css"]  {
        font-family: 'Kanit', sans-serif;
        color: #3D312A;
    }

    /* Main Background */
    .stApp {
        background-color: #F5EFE6;
    }

    /* Typography */
    h1, h2, h3, .brand-logo {
        font-family: 'Mali', cursive !important;
        color: #6B4F4F !important;
    }

    /* Custom Cards */
    .book-card {
        background-color: #FFFFFF;
        border: 1px solid #E8D8C4;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(61, 49, 42, 0.05);
        transition: transform 0.2s;
    }
    .book-card:hover {
        transform: translateY(-4px);
    }

    /* Status Badges */
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

    /* Buttons Override */
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

    /* Banner Styling */
    .hero-banner {
        background-color: #E8D8C4;
        border-radius: 16px;
        padding: 28px;
        text-align: center;
        margin-bottom: 25px;
        border: 2px dashed #A3B18A;
    }

    /* Cart Tabs & Items */
    .cart-box {
        background-color: #E8D8C4;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. Session State Initialization (Mock Data & State Management)
# ==============================================================================
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

# ข้อมูลหนังสือจำลองสำหรับหน้าแรก
MOCK_BOOKS = [
    {
        'id': 1,
        'title': 'Atomic Habits เพราะชีวิตดีได้กว่าที่เป็น',
        'author': 'James Clear',
        'buy_price': 285,
        'rent_price': 15,
        'status': 'available',
        'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400',
    },
    {
        'id': 2,
        'title': 'The Psychology of Money',
        'author': 'Morgan Housel',
        'buy_price': 290,
        'rent_price': 20,
        'status': 'rented',
        'img': 'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=400',
    },
    {
        'id': 3,
        'title': 'เจ้าชายน้อย (The Little Prince)',
        'author': 'Antoine de Saint-Exupéry',
        'buy_price': 220,
        'rent_price': 0,
        'status': 'sale_only',
        'img': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400',
    },
    {
        'id': 4,
        'title': 'คิดแบบย่อยสลาย ความคิดสร้างสรรค์',
        'author': 'ผู้เขียนอิสระ',
        'buy_price': 310,
        'rent_price': 18,
        'status': 'available',
        'img': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400',
    },
]

# ==============================================================================
# 3. Sidebar Navigation & Global Header
# ==============================================================================
st.sidebar.markdown(
    "<h1 class='brand-logo'>📚 BookShare</h1>", unsafe_allow_html=True
)
st.sidebar.caption("ชุมชนแบ่งปันและเช่าหนังสือออนไลน์")

# Navigation Menu
menu = st.sidebar.radio(
    'เมนูหลัก',
    [
        '🏠 หน้าแรก (Home)',
        '🛒 ตะกร้าสินค้า (Cart)',
        '💳 ชำระเงิน (Checkout)',
        '🏪 บัญชีผู้ขาย (Seller Dashboard)',
    ],
)

st.sidebar.markdown('---')
st.sidebar.write('🛍️ **สรุปตะกร้าของคุณ**')
st.sidebar.write(f'• ซื้อขาด: **{len(st.session_state.cart_buy)}** เล่ม')
st.sidebar.write(f'• เช่าอ่าน: **{len(st.session_state.cart_rent)}** เล่ม')

# ==============================================================================
# 4. Page Routing & View Logic
# ==============================================================================

# ------------------------------------------------------------------------------
# PAGE 1: HOME PAGE
# ------------------------------------------------------------------------------
if menu == '🏠 หน้าแรก (Home)':
    # Header & Search Bar
    col_logo, col_search, col_user = st.columns([2, 4, 2])
    with col_search:
        search_query = st.text_input(
            '🔍 ค้นหาหนังสือ...', placeholder='พิมพ์ชื่อหนังสือ หรือผู้แต่ง...'
        )
    with col_user:
        st.write('')
        st.button('👤 โปรไฟล์ / ลงชื่อเข้าใช้')

    # Banner Section
    st.markdown(
        """
        <div class="hero-banner">
            <h2 style="margin:0; color:#6B4F4F;">📖 โปรโมชันต้อนรับสัปดาห์การอ่าน!</h2>
            <p style="margin:8px 0 0 0; color:#3D312A;">ยืมหนังสือครบ 3 เล่ม ฟรีค่ายืมเล่มที่ 4 | ส่งฟรีทั่วไทยเมื่อซื้อครบ 500 บาท</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Filter Bar
    categories = ['ทั้งหมด', 'วรรณกรรม', 'จิตวิทยา/พัฒนาตนเอง', 'ธุรกิจ/การเงิน', 'นิยาย']
    st.selectbox('🏷️ หมวดหมู่หนังสือ', categories)

    st.subheader('📚 รายการหนังสือทั้งหมด')

    # Book Grid Display (2x2 Grid)
    cols = st.columns(2)
    for index, book in enumerate(MOCK_BOOKS):
        col_idx = index % 2
        with cols[col_idx]:
            # Badge Handling
            if book['status'] == 'available':
                badge_html = "<span class='badge-available'>🟢 พร้อมให้ยืม</span>"
            elif book['status'] == 'rented':
                badge_html = "<span class='badge-rented'>🔴 ถูกยืมอยู่</span>"
            else:
                badge_html = (
                    "<span class='badge-sale'>🏷️ สำหรับขายเท่านั้น</span>"
                )

            st.markdown(
                f"""
                <div class="book-card">
                    <div style="display:flex; gap:15px;">
                        <img src="{book['img']}" style="width:100px; height:140px; object-fit:cover; border-radius:8px;">
                        <div>
                            {badge_html}
                            <h4 style="margin:8px 0 4px 0; color:#3D312A;">{book['title']}</h4>
                            <p style="margin:0; font-size:14px; color:#6B4F4F;">ผู้แต่ง: {book['author']}</p>
                            <p style="margin:8px 0 0 0; font-size:14px;">
                                💵 <b>ราคาซื้อ:</b> ฿{book['buy_price']} | 
                                🗓️ <b>ค่ายืม:</b> ฿{book['rent_price']}/วัน
                            </p>
                        </div>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Interactive Detail & Pop-up Modal Options
            with st.expander(f"📖 รายละเอียด & สั่งซื้อ: {book['title']}"):
                opt_col1, opt_col2 = st.columns(2)

                # Option A: Buy
                with opt_col1:
                    st.write(f"**ซื้อขาด:** ฿{book['buy_price']}")
                    if st.button(
                        f"🛒 เพิ่มในตะกร้าซื้อ", key=f"buy_{book['id']}"
                    ):
                        st.session_state.cart_buy.append(book)
                        st.success('เพิ่มในตะกร้าซื้อสำเร็จ!')

                # Option B: Rent with Date Picker Pop-up Simulation
                with opt_col2:
                    if book['status'] != 'sale_only':
                        st.write(f"**ยืมอ่าน:** ฿{book['rent_price']}/วัน")

                        # Date Range Selector
                        today = date.today()
                        start_date = st.date_input(
                            'วันเริ่มยืม', today, key=f"start_{book['id']}"
                        )
                        end_date = st.date_input(
                            'วันกำหนดคืน',
                            today + timedelta(days=7),
                            key=f"end_{book['id']}",
                        )

                        rent_days = (end_date - start_date).days
                        if rent_days > 0:
                            total_rent = rent_days * book['rent_price']
                            st.info(
                                f'จำนวน {rent_days} วัน | ราคารวม: ฿{total_rent}'
                            )

                            if st.button(
                                f"📦 ยืมเล่มนี้", key=f"rent_{book['id']}"
                            ):
                                rent_item = book.copy()
                                rent_item['rent_days'] = rent_days
                                rent_item['total_rent'] = total_rent
                                rent_item['return_date'] = str(end_date)
                                st.session_state.cart_rent.append(rent_item)
                                st.success('เพิ่มในตะกร้ายืมสำเร็จ!')
                        else:
                            st.warning('วันกำหนดคืนต้องอยู่หลังวันเริ่มยืม')
                    else:
                        st.caption('เล่มนี้ไม่เปิดให้เช่า')

# ------------------------------------------------------------------------------
# PAGE 2: CART PAGE
# ------------------------------------------------------------------------------
elif menu == '🛒 ตะกร้าสินค้า (Cart)':
    st.title('🛒 ตะกร้าสินค้าของคุณ')

    tab_buy, tab_rent = st.tabs(
        [
            f"🛍️ รายการสั่งซื้อ ({len(st.session_state.cart_buy)})",
            f"📖 รายการยืม ({len(st.session_state.cart_rent)})",
        ]
    )

    with tab_buy:
        if not st.session_state.cart_buy:
            st.write('ไม่มีรายการหนังสือที่เลือกซื้อ')
        else:
            total_buy = 0
            for item in st.session_state.cart_buy:
                st.markdown(
                    f"""
                    <div class="cart-box">
                        <b>{item['title']}</b> - ฿{item['buy_price']}
                    </div>
                """,
                    unsafe_allow_html=True,
                )
                total_buy += item['buy_price']
            st.write(f'### ราคารวมซื้อหนังสือ: **฿{total_buy}**')

    with tab_rent:
        if not st.session_state.cart_rent:
            st.write('ไม่มีรายการหนังสือที่เลือกรวมยืม')
        else:
            total_rent = 0
            for item in st.session_state.cart_rent:
                st.markdown(
                    f"""
                    <div class="cart-box">
                        <b>{item['title']}</b><br>
                        ระยะเวลา: {item['rent_days']} วัน | กำหนดคืน: <span style="color:#BC6C25;"><b>{item['return_date']}</b></span><br>
                        ค่ายืมรวม: ฿{item['total_rent']}
                    </div>
                """,
                    unsafe_allow_html=True,
                )
                total_rent += item['total_rent']
            st.write(f'### ราคารวมค่ายืมหนังสือ: **฿{total_rent}**')

# ------------------------------------------------------------------------------
# PAGE 3: CHECKOUT PAGE
# ------------------------------------------------------------------------------
elif menu == '💳 ชำระเงิน (Checkout)':
    st.title('💳 ชำระเงินและจัดส่ง')

    col_form, col_summary = st.columns([5, 4])

    with col_form:
        st.subheader('📦 ฟอร์มข้อมูลจัดส่ง')
        with st.form('shipping_form'):
            name = st.text_input('ชื่อ-นามสกุล', value='สมชาย รักการอ่าน')
            phone = st.text_input('เบอร์โทรศัพท์', value='081-234-5678')
            address = st.text_area(
                'ที่อยู่จัดส่ง',
                value='123/45 ถนนมิตรภาพ อ.เมือง จ.พิษณุโลก 65000',
            )
            st.checkbox('บันทึกที่อยู่อัตโนมัติสำหรับการสั่งซื้อครั้งถัดไป', value=True)

            st.subheader('💵 วิธีการชำระเงิน')
            payment_method = st.radio(
                'เลือกช่องทางชำระเงิน',
                ['PromptPay QR Code', 'โอนผ่านธนาคาร', 'บัตรเครดิต/เดบิต'],
            )

            submit = st.form_submit_button('ยืนยันการสั่งซื้อ')

        if submit:
            st.balloons()
            st.success(
                '🎉 ทำรายการสั่งซื้อเรียบร้อย! ระบบกำลังดำเนินการจัดส่ง'
            )

    with col_summary:
        st.subheader('📋 สรุปรายการคำสั่งซื้อ')

        buy_total = sum(item['buy_price'] for item in st.session_state.cart_buy)
        rent_total = sum(
            item['total_rent'] for item in st.session_state.cart_rent
        )
        shipping_fee = 50 if (buy_total + rent_total) > 0 else 0
        insurance_fee = 100 if len(st.session_state.cart_rent) > 0 else 0

        st.write(f'• ยอดซื้อหนังสือ: ฿{buy_total}')
        st.write(f'• ยอดค่ายืมหนังสือ: ฿{rent_total}')
        st.write(f'• ค่าจัดส่ง: ฿{shipping_fee}')
        st.write(f'• ค่าประกันหนังสือ (คืนได้เมื่อส่งคืนหนังสือ): ฿{insurance_fee}')
        st.markdown('---')
        grand_total = buy_total + rent_total + shipping_fee + insurance_fee
        st.write(f'### ยอดชำระสุทธิ: <span style="color:#BC6C25;">฿{grand_total}</span>', unsafe_allow_html=True)

        if payment_method == 'PromptPay QR Code':
            st.image(
                'https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=BookSharePromptPay',
                caption='สแกน QR Code เพื่อชำระเงิน',
            )

# ------------------------------------------------------------------------------
# PAGE 4: SELLER DASHBOARD
# ------------------------------------------------------------------------------
elif menu == '🏪 บัญชีผู้ขาย (Seller Dashboard)':
    st.title('🏪 Marketplace Dashboard สำหรับผู้ขาย')

    # Seller Register Banner
    st.success(
        '✅ คุณได้รับการยืนยันตัวตนเป็นผู้ขาย/ผู้ให้เช่าเรียบร้อยแล้ว (Seller Verified)'
    )

    tab_add, tab_stock = st.tabs(
        ['➕ ลงขาย/ให้เช่าหนังสือใหม่', '📦 จัดการสต็อกและสถานะ']
    )

    with tab_add:
        st.subheader('📝 ฟอร์มลงทะเบียนหนังสือใหม่')
        with st.form('add_book_form'):
            b_title = st.text_input('ชื่อเรื่อง')
            b_cat = st.selectbox(
                'หมวดหมู่',
                [
                    'วรรณกรรม',
                    'จิตวิทยา/พัฒนาตนเอง',
                    'ธุรกิจ/การเงิน',
                    'นิยาย',
                    'ความรู้ทั่วไป',
                ],
            )
            b_cond = st.text_input(
                'สภาพหนังสือ', placeholder='เช่น 90% สภาพดี มีรอยไฮไลท์เล็กน้อย'
            )
            b_type = st.radio(
                'ตั้งค่าประเภทการลงรายการ',
                ['ขายอย่างเดียว', 'ให้เช่าอย่างเดียว', 'ได้ทั้งขายและเช่า'],
            )

            col_p1, col_p2 = st.columns(2)
            with col_p1:
                b_price_buy = st.number_input('ราคาขายขาด (บาท)', min_value=0, value=200)
            with col_p2:
                b_price_rent = st.number_input('ราคาเช่า (บาท/วัน)', min_value=0, value=15)

            b_cover = st.file_uploader(
                'อัปโหลดรูปภาพปกและสภาพหนังสือภายใน', type=['jpg', 'png']
            )

            btn_save = st.form_submit_button('บันทึกและลงรายการหนังสือ')

        if btn_save:
            new_entry = {
                'title': b_title,
                'category': b_cat,
                'condition': b_cond,
                'type': b_type,
                'price_buy': b_price_buy,
                'price_rent': b_price_rent,
                'status': '🟢 พร้อมให้ยืม',
            }
            st.session_state.my_books.append(new_entry)
            st.success(f"ลงขายหนังสือ '{b_title}' เรียบร้อยแล้ว!")

    with tab_stock:
        st.subheader('📦 รายการหนังสือที่คุณลงขาย/ให้เช่า')

        for idx, book_item in enumerate(st.session_state.my_books):
            with st.container():
                st.markdown(
                    f"""
                    <div class="cart-box">
                        <h4>{book_item['title']}</h4>
                        <p>หมวดหมู่: {book_item['category']} | สภาพ: {book_item['condition']} | ประเภท: {book_item['type']}</p>
                        <p>ราคาขาย: ฿{book_item['price_buy']} | ค่ายืม: ฿{book_item['price_rent']}/วัน</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                # Delivery Tracking Status Update
                status_option = st.selectbox(
                    f"อัปเดตสถานะการจัดส่ง/คืนหนังสือ (ID: {idx+1})",
                    [
                        '🟢 พร้อมให้ยืม',
                        '🚚 กำลังจัดส่งให้ผู้เช่า',
                        '📖 อยู่ระหว่างการเช่า (ติดตามคืน)',
                        '📦 ได้รับหนังสือคืนแล้ว',
                    ],
                    key=f"status_{idx}",
                )
                st.caption(f'สถานะปัจจุบัน: {status_option}')
                st.markdown('---')