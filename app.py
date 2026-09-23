from datetime import date, timedelta
import streamlit as st

# ==============================================================================
# 1. Page Configuration & Comprehensive Earth Tone CSS
# ==============================================================================
st.set_page_config(
    page_title="BookShare - ร้านหนังสือ & เช่ายืมออนไลน์",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&family=Mali:wght@400;500;600;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Kanit', sans-serif !important;
        background-color: #F8F3EC !important;
        color: #382B24 !important;
    }

    h1, h2, h3, .font-cute {
        font-family: 'Mali', cursive !important;
        color: #4A3528 !important;
    }

    /* Remove default Streamlit top margin/padding */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1240px !important;
    }

    /* Custom Header bar */
    .bs-header {
        background-color: #F8F3EC;
        border-bottom: 1px solid #E8DDD0;
        padding: 12px 0 16px 0;
        margin-bottom: 20px;
    }

    .brand-title {
        font-family: 'Mali', cursive !important;
        font-size: 24px;
        font-weight: 700;
        color: #4A3528;
        line-height: 1.1;
    }
    .brand-sub {
        font-size: 11px;
        color: #8D7B68;
    }

    /* Badges */
    .badge-available {
        background-color: #588157;
        color: #FFFFFF;
        padding: 3px 9px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-rented {
        background-color: #D9534F;
        color: #FFFFFF;
        padding: 3px 9px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-sale {
        background-color: #BC6C25;
        color: #FFFFFF;
        padding: 3px 9px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-condition {
        background-color: #F5EFE6;
        color: #6B4F4F;
        border: 1px solid #E2D4C5;
        padding: 2px 7px;
        border-radius: 6px;
        font-size: 10px;
        font-weight: 500;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #F3E9DD 0%, #EFE1D1 100%);
        border-radius: 24px;
        padding: 36px 36px;
        border: 1px solid #E5D7C7;
        margin-bottom: 30px;
        position: relative;
    }
    .hero-badge {
        display: inline-block;
        background-color: #DCE8DA;
        color: #385E38;
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 12px;
    }
    .hero-h1 {
        font-family: 'Mali', cursive !important;
        font-size: 34px;
        font-weight: 700;
        color: #4A3528;
        line-height: 1.25;
        margin-bottom: 12px;
    }
    .hero-desc {
        font-size: 14px;
        color: #6C5E53;
        line-height: 1.6;
        margin-bottom: 20px;
        max-width: 580px;
    }
    .hero-stat-card {
        background-color: #FFFFFF;
        border: 1px solid #E8DDD0;
        border-radius: 14px;
        padding: 10px 16px;
        box-shadow: 0 2px 8px rgba(61,46,36,0.03);
    }

    /* Category Pill */
    .cat-pill {
        display: inline-block;
        padding: 7px 16px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 500;
        margin-right: 6px;
        margin-bottom: 8px;
        text-decoration: none;
        transition: all 0.2s;
    }
    .cat-pill-active {
        background-color: #4A3528;
        color: #FFFFFF !important;
    }
    .cat-pill-inactive {
        background-color: #FFFFFF;
        color: #6C5E53 !important;
        border: 1px solid #E8DDD0;
    }

    /* Book Cards */
    .card-book {
        background-color: #FFFFFF;
        border: 1px solid #EADBCE;
        border-radius: 18px;
        padding: 14px;
        margin-bottom: 16px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        box-shadow: 0 4px 14px rgba(61,46,36,0.04);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }
    .card-book:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(61,46,36,0.08);
        border-color: #D4BFA9;
    }

    .book-cover-img {
        width: 100%;
        aspect-ratio: 3/4;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    /* Detail Page Styling */
    .detail-container {
        background-color: #FFFFFF;
        border: 1px solid #E8DDD0;
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 24px;
        box-shadow: 0 6px 20px rgba(61,46,36,0.04);
    }
    .seller-card {
        background-color: #F8F3EC;
        border: 1px solid #EADBCE;
        border-radius: 14px;
        padding: 14px 18px;
        margin-top: 16px;
    }
    .check-box-cert {
        background-color: #FAF6F0;
        border: 1px solid #EADBCE;
        border-radius: 14px;
        padding: 14px 18px;
        margin-top: 14px;
    }

    /* Rental vs Buy Choice Card */
    .choice-card-active {
        border: 2px solid #588157;
        background-color: #FAFDFC;
        border-radius: 14px;
        padding: 14px;
    }
    .choice-card-inactive {
        border: 1px solid #EADBCE;
        background-color: #FFFFFF;
        border-radius: 14px;
        padding: 14px;
    }

    /* Cart & Checkout Styling */
    .cart-section-title {
        font-family: 'Mali', cursive !important;
        font-size: 18px;
        font-weight: 700;
        color: #4A3528;
    }
    .cart-item-card {
        background-color: #FFFFFF;
        border: 1px solid #EADBCE;
        border-radius: 16px;
        padding: 14px 18px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(61,46,36,0.03);
    }
    .summary-card {
        background-color: #FFFFFF;
        border: 1px solid #EADBCE;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 4px 18px rgba(61,46,36,0.05);
    }

    /* Buttons */
    .stButton>button {
        background-color: #4A3528 !important;
        color: #FAF5EF !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 8px 18px !important;
        font-family: 'Kanit', sans-serif !important;
        transition: all 0.2s !important;
    }
    .stButton>button:hover {
        background-color: #BC6C25 !important;
        color: #FFFFFF !important;
    }

    /* Secondary outline button style for preview */
    .btn-secondary>button {
        background-color: #FFFFFF !important;
        color: #4A3528 !important;
        border: 1px solid #C8B9A9 !important;
    }
    .btn-secondary>button:hover {
        background-color: #F3E9DD !important;
        color: #382B24 !important;
    }

    /* Top cart buttons styling */
    .btn-cart-rent>button {
        background-color: #E2ECE0 !important;
        color: #2F5930 !important;
        border: 1px solid #C0DAC0 !important;
        border-radius: 999px !important;
        font-size: 13px !important;
    }
    .btn-cart-buy>button {
        background-color: #FAEEE1 !important;
        color: #9C5212 !important;
        border: 1px solid #EAC8A8 !important;
        border-radius: 999px !important;
        font-size: 13px !important;
    }

    /* Input styling */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        border-radius: 10px !important;
        border: 1px solid #DACABD !important;
        background-color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. Complete Mock Data (8 Books matching the provided Mockup Images)
# ==============================================================================
MOCK_BOOKS = [
    {
        'id': 1,
        'title': 'Atomic Habits (ฉบับแปลไทย)',
        'full_title': 'Atomic Habits: เพราะชีวิตดีได้กว่าที่เป็น',
        'author': 'James Clear (แปลโดย ประภากาศ บริบูรณ์พาณิชย์)',
        'category': 'จิตวิทยา & พัฒนาตนเอง',
        'isbn': '978-616-287-343-0',
        'status': 'available',
        'status_text': '🟢 พร้อมให้ยืม',
        'condition': 'สภาพ 95%',
        'condition_full': 'สภาพดีเยี่ยม 95%',
        'buy_price': 280,
        'original_price': 330,
        'rent_price': 7,
        'deposit': 150,
        'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80',
        'desc': 'หนังสือระดับโลกที่จะเปลี่ยนความคิดและพฤติกรรมทีละ 1% เพื่อสร้างผลลัพธ์มหาศาล เหมาะอย่างยิ่งสำหรับผู้ที่ต้องการปลดล็อกศักยภาพในทุกๆ วัน',
        'seller_name': 'ร้านคุณมัสยิดนักอ่าน',
        'seller_rating': 4.9,
        'seller_count': 142,
        'thumbnails': [
            'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=300&q=80',
            'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=300&q=80',
            'https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 2,
        'title': 'ปาฏิหาริย์ร้านชำของคุณนามิยะ',
        'full_title': 'ปาฏิหาริย์ร้านชำของคุณนามิยะ (Miracles of the Namiya General Store)',
        'author': 'ฮิงาชิโนะ เคโงะ',
        'category': 'วรรณกรรม & นิยายแปล',
        'isbn': '978-616-18-2234-7',
        'status': 'rented',
        'status_text': '🔴 ถูกยืมอยู่ (รอคิว 2 คน)',
        'available_date': 'ว่าง 28 ต.ค.',
        'condition': 'สภาพ 92%',
        'condition_full': 'สภาพดี 92%',
        'buy_price': 245,
        'original_price': 295,
        'rent_price': 6,
        'deposit': 120,
        'img': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80',
        'desc': 'เมื่อหัวขโมยสามคนหลบหนีไปซ่อนตัวในร้านชำร้างแห่งหนึ่ง แต่กลับได้รับจดหมายขอคำปรึกษาจากคนในอดีต เรื่องราวอบอุ่นหัวใจและชะตากรรมที่ร้อยเรียงจึงเริ่มต้นขึ้น',
        'seller_name': 'ร้านวรรณกรรมอุ่นใจ',
        'seller_rating': 4.9,
        'seller_count': 98,
        'thumbnails': [
            'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=300&q=80',
            'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 3,
        'title': 'The Psychology of Money',
        'full_title': 'The Psychology of Money: จิตวิทยาว่าด้วยเงิน',
        'author': 'Morgan Housel',
        'category': 'ธุรกิจ & การลงทุน',
        'isbn': '978-616-8187-25-8',
        'status': 'sale_only',
        'status_text': '🏷️ สำหรับขายเท่านั้น',
        'condition': 'สภาพ 98% เหมือนใหม่',
        'condition_full': 'สภาพ 98% เหมือนใหม่ (เกือบมือหนึ่ง)',
        'buy_price': 230,
        'original_price': 290,
        'rent_price': 0,
        'deposit': 0,
        'img': 'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?auto=format&fit=crop&w=600&q=80',
        'desc': 'ข้อคิดเรื่องเงิน อิสรภาพ และโชคลาภ ผ่าน 19 เรื่องสั้นที่สะท้อนว่าทัศนคติเกี่ยวกับเงินมีความสำคัญและส่งผลต่อชีวิตมากกว่าความรู้ทางคณิตศาสตร์',
        'seller_name': 'ร้าน Wealth Books',
        'seller_rating': 5.0,
        'seller_count': 215,
        'thumbnails': [
            'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 4,
        'title': 'คิดแบบยิว ทำแบบญี่ปุ่น',
        'full_title': 'คิดแบบยิว ทำแบบญี่ปุ่น (Jewish Mind Japanese Execution)',
        'author': 'ฮอนดะ เคน',
        'category': 'ธุรกิจ & การลงทุน',
        'isbn': '978-616-287-112-2',
        'status': 'available',
        'status_text': '🟢 พร้อมให้ยืม',
        'condition': 'สภาพ 90%',
        'condition_full': 'สภาพ 90% ไร้รอยยับ',
        'buy_price': 190,
        'original_price': 250,
        'rent_price': 5,
        'deposit': 100,
        'img': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=600&q=80',
        'desc': 'บทเรียนชีวิตและธุรกิจจากมหาเศรษฐีชาวยิว ถ่ายทอดผ่านมุมมองและวัฒนธรรมความมุ่งมั่นสไตล์คนญี่ปุ่น นำไปประยุกต์ใช้เพื่อความมั่งคั่งที่ยั่งยืน',
        'seller_name': 'BookHouse สยาม',
        'seller_rating': 4.8,
        'seller_count': 87,
        'thumbnails': [
            'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 5,
        'title': 'กล้าที่จะถูกเกลียด',
        'full_title': 'กล้าที่จะถูกเกลียด (The Courage to Be Disliked)',
        'author': 'อิจิโร คิชิมิ และ ฟุมิทาเกะ โคกะ',
        'category': 'จิตวิทยา & พัฒนาตนเอง',
        'isbn': '978-616-287-142-9',
        'status': 'available',
        'status_text': '🟢 พร้อมให้ยืม',
        'condition': 'สภาพ 96%',
        'condition_full': 'สภาพ 96% สะอาด',
        'buy_price': 220,
        'original_price': 260,
        'rent_price': 6,
        'deposit': 120,
        'img': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80',
        'desc': 'จิตวิทยาแบบแอดเลอร์ที่จะช่วยปลดปล่อยคุณจากความคาดหวังของผู้อื่น และค้นพบความสุขที่แท้จริงในชีวิตด้วยการยอมรับและเป็นตัวของตัวเอง',
        'seller_name': 'ร้านสุขใจอ่าน',
        'seller_rating': 4.9,
        'seller_count': 164,
        'thumbnails': [
            'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 6,
        'title': 'เมื่อแมวที่บ้านผันตัวมาเป็นนักพยากรณ์',
        'full_title': 'เมื่อแมวที่บ้านผันตัวมาเป็นนักพยากรณ์',
        'author': 'โมจิซึกิ ไม',
        'category': 'วรรณกรรม & นิยายแปล',
        'isbn': '978-616-18-4900-9',
        'status': 'rented',
        'status_text': '🔴 ถูกยืมอยู่',
        'available_date': 'ว่าง 31 ต.ค.',
        'condition': 'สภาพ 94%',
        'condition_full': 'สภาพ 94% ดูแลอย่างดี',
        'buy_price': 210,
        'original_price': 250,
        'rent_price': 5,
        'deposit': 110,
        'img': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=600&q=80',
        'desc': 'เรื่องราวของร้านน้ำชาจันทร์เพ็ญที่มีแมวตัวโตคอยชงชาและเสิร์ฟคำพยากรณ์ฮีลใจให้แก่ผู้คนที่กำลังสับสนและตามหาความหมายในชีวิต',
        'seller_name': 'Cat & Tea Books',
        'seller_rating': 4.8,
        'seller_count': 73,
        'thumbnails': [
            'https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 7,
        'title': 'สูญสิ้นความเป็นคน (ปกแข็ง สะสม)',
        'full_title': 'สูญสิ้นความเป็นคน (No Longer Human) ฉบับปกแข็งสะสม',
        'author': 'ดะไซ โอซามุ',
        'category': 'วรรณกรรมคลาสสิก',
        'isbn': '978-616-563-021-4',
        'status': 'sale_only',
        'status_text': '🏷️ สำหรับขายเท่านั้น',
        'condition': 'สภาพ 99% สะสม',
        'condition_full': 'สภาพ 99% ฉบับสะสมพรีเมียม',
        'buy_price': 450,
        'original_price': 550,
        'rent_price': 0,
        'deposit': 0,
        'img': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=600&q=80',
        'desc': 'วรรณกรรมชิ้นเอกที่สะท้อนถึงความแปลกแยก ความเจ็บปวด และความจริงใจอย่างสุดโต่งของมนุษย์ ฉบับปกแข็งพรีเมียม หายาก รวมค่าจัดส่งแล้ว',
        'seller_name': 'Vintage Rare Books',
        'seller_rating': 5.0,
        'seller_count': 45,
        'thumbnails': [
            'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=300&q=80',
        ]
    },
    {
        'id': 8,
        'title': 'โตเกียวไม่มีขา',
        'full_title': 'โตเกียวไม่มีขา (Tokyo No Feet)',
        'author': 'นิ้วกลม',
        'category': 'หนังสือภาพ & ไลฟ์สไตล์',
        'isbn': '978-974-02-1234-5',
        'status': 'available',
        'status_text': '🟢 พร้อมให้ยืม',
        'condition': 'สภาพ 93%',
        'condition_full': 'สภาพ 93% สมบูรณ์',
        'buy_price': 210,
        'original_price': 260,
        'rent_price': 6,
        'deposit': 120,
        'img': 'https://images.unsplash.com/photo-1476275466078-4007374efbbe?auto=format&fit=crop&w=600&q=80',
        'desc': 'บันทึกการเดินทางในโตเกียวที่เต็มไปด้วยความละเมียดละไม มุมมองสดใหม่ และแรงบันดาลใจที่ทำให้เราอยากก้าวออกไปสำรวจความงดงามของโลกกว้าง',
        'seller_name': 'RoundFinger Reader',
        'seller_rating': 4.9,
        'seller_count': 110,
        'thumbnails': [
            'https://images.unsplash.com/photo-1476275466078-4007374efbbe?auto=format&fit=crop&w=300&q=80',
        ]
    },
]

# ==============================================================================
# 3. Session State Initialization
# ==============================================================================
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'home'  # 'home', 'detail', 'cart', 'seller', 'order_success'

if 'selected_book_id' not in st.session_state:
    st.session_state.selected_book_id = 1

if 'active_category' not in st.session_state:
    st.session_state.active_category = 'ทั้งหมด'

if 'search_query' not in st.session_state:
    st.session_state.search_query = ''

# User Authentication State (Default: Logged in as คุณมีนา as in mockup, but fully toggleable)
if 'user' not in st.session_state:
    st.session_state.user = {
        'logged_in': True,
        'name': 'คุณมีนา',
        'phone': '081-234-5678',
        'address': '123/45 ถนนมิตรภาพ แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110',
        'tier': 'ผู้อ่านระดับ 2 (เช่าอยู่ 2 เล่ม)',
    }

# Cart State pre-populated with exact items from Image 4 (Cart Mockup)
if 'cart_initialized' not in st.session_state:
    st.session_state.cart_initialized = True
    # Section A: Rental Items (2 items from mockup)
    st.session_state.cart_rent = [
        {
            'id': 1,
            'title': 'Atomic Habits: เพราะชีวิตดีได้กว่าที่เป็น',
            'author': 'James Clear',
            'condition': 'สภาพ 95%',
            'rent_days': 10,
            'start_date': '15/10/2024',
            'return_date': '25 ต.ค. 2024',
            'rate_per_day': 7,
            'total_rent': 70,
            'deposit': 150,
            'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=200&q=80',
        },
        {
            'id': 2,
            'title': 'ปาฏิหาริย์ร้านชำของคุณนามิยะ',
            'author': 'ฮิงาชิโนะ เคโงะ',
            'condition': 'สภาพ 92%',
            'rent_days': 7,
            'start_date': '15/10/2024',
            'return_date': '22 ต.ค. 2024',
            'rate_per_day': 6,
            'total_rent': 42,
            'deposit': 120,
            'img': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=200&q=80',
        }
    ]
    # Section B: Purchase Items (1 item from mockup)
    st.session_state.cart_buy = [
        {
            'id': 3,
            'title': 'The Psychology of Money: จิตวิทยาว่าด้วยเงิน',
            'author': 'Morgan Housel',
            'condition': 'สภาพ 98% (เกือบมือหนึ่ง)',
            'buy_price': 230,
            'original_price': 290,
            'tag': 'ซื้อขาดมือสอง จัดส่งทันที',
            'img': 'https://images.unsplash.com/photo-1592496431122-2349e0fbc666?auto=format&fit=crop&w=200&q=80',
        }
    ]

if 'cart_rent' not in st.session_state:
    st.session_state.cart_rent = []
if 'cart_buy' not in st.session_state:
    st.session_state.cart_buy = []

if 'promo_code' not in st.session_state:
    st.session_state.promo_code = 'WELCOMEREAD'

if 'last_order' not in st.session_state:
    st.session_state.last_order = None

# Custom Seller Inventory
if 'my_books' not in st.session_state:
    st.session_state.my_books = [
        {
            'title': 'เจ้าชายน้อย (The Little Prince)',
            'category': 'วรรณกรรม & นิยายแปล',
            'condition': '95% สภาพสะสม',
            'type': 'ทั้งขายและเช่า',
            'price_buy': 250,
            'price_rent': 15,
            'status': '🟢 พร้อมให้ยืม',
        }
    ]

# Helper to find book by ID
def get_book_by_id(book_id):
    for b in MOCK_BOOKS:
        if b['id'] == book_id:
            return b
    return MOCK_BOOKS[0]

# ==============================================================================
# 4. Modals (Dialogs)
# ==============================================================================
@st.dialog("🔑 เข้าสู่ระบบ / สมัครสมาชิก BookShare")
def login_dialog():
    st.markdown(
        """
        <div style="text-align:center; margin-bottom:15px;">
            <h3 style="margin:0; color:#4A3528;">ยินดีต้อนรับสู่นักอ่าน BookShare</h3>
            <p style="font-size:12px; color:#8D7B68; margin-top:4px;">เข้าสู่ระบบเพื่อเช่ายืม สั่งซื้อ และสะสมแต้มการอ่าน</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    name = st.text_input("ชื่อ-นามสกุล", value=st.session_state.user.get('name', 'คุณมีนา'))
    phone = st.text_input("เบอร์โทรศัพท์ติดต่อ", value=st.session_state.user.get('phone', '081-234-5678'))
    address = st.text_area("ที่อยู่สำหรับจัดส่งหนังสือ", value=st.session_state.user.get('address', ''), placeholder="บ้านเลขที่, ซอย, ถนน, แขวง/ตำบล, เขต/อำเภอ, จังหวัด, รหัสไปรษณีย์")

    if st.button("ยืนยันเข้าสู่ระบบ", use_container_width=True):
        if name and phone:
            st.session_state.user['logged_in'] = True
            st.session_state.user['name'] = name
            st.session_state.user['phone'] = phone
            st.session_state.user['address'] = address
            st.session_state.user['tier'] = 'ผู้อ่านระดับ 2 (เช่าอยู่ 2 เล่ม)'
            st.success(f"ยินดีต้อนรับ {name} เข้าสู่ระบบเรียบร้อยแล้ว!")
            st.rerun()
        else:
            st.error("กรุณากรอกชื่อและเบอร์โทรศัพท์ให้ครบถ้วน")

@st.dialog("ℹ️ วิธีการยืม - คืนหนังสือ")
def how_it_works_dialog():
    st.markdown(
        """
        <div style="font-size:14px; line-height:1.7; color:#382B24;">
            <h3 style="color:#4A3528; margin-bottom:10px;">📖 3 ขั้นตอนง่ายๆ ในการเช่ายืมหนังสือ</h3>
            <ol style="padding-left:20px; margin-bottom:15px;">
                <li><b>เลือกหนังสือและระยะเวลายืม:</b> เลือกวันเริ่มและวันคืน (สูงสุด 30 วัน) ชำระค่ายืมและค่ามัดจำ</li>
                <li><b>รอรับหนังสือที่บ้าน:</b> จัดส่งด่วนถึงหน้าบ้าน หนังสือผ่านการตรวจสภาพและอบฆ่าเชื้อ UV ปลอดภัย 100%</li>
                <li><b>ส่งคืนง่าย & รับเงินมัดจำคืนทันที:</b> เมื่อครบกำหนด ส่งคืนผ่านไปรษณีย์ไทยหรือ Flash Express เมื่อผู้ให้เช่าตรวจรับ ระบบจะโอนเงินมัดจำคืนเข้า PromptPay ของคุณภายใน 24 ชม.!</li>
            </ol>
            <div style="background-color:#EAF2E8; border:1px solid #C0DAC0; border-radius:12px; padding:12px; font-size:12px; color:#2F5930;">
                🌱 <b>โครงการอ่านหนังสือยั่งยืน:</b> หนังสือ 1 เล่มที่ถูกยืมอ่าน ช่วยลดขยะกระดาษและลดการปล่อยคาร์บอนสู่สิ่งแวดล้อม
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# 5. Top Header Navigation (Identical to UX/UI Screenshot 1 & 2)
# ==============================================================================
rent_count = len(st.session_state.cart_rent)
buy_count = len(st.session_state.cart_buy)

col_logo, col_nav, col_cart_r, col_cart_b, col_user = st.columns([3.2, 3.8, 1.4, 1.4, 2.2])

with col_logo:
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:8px; cursor:pointer;" onclick="window.location.reload();">
            <span style="font-size:32px;">📚</span>
            <div>
                <span class="brand-title">BookShare</span><br>
                <span class="brand-sub">ร้านหนังสือ &amp; เช่ายืมออนไลน์</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_nav:
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        if st.button("หน้าแรก", key="nav_home", use_container_width=True):
            st.session_state.current_view = 'home'
            st.rerun()
    with n2:
        if st.button("สำรวจหนังสือ", key="nav_explore", use_container_width=True):
            st.session_state.current_view = 'home'
            st.rerun()
    with n3:
        if st.button("วิธีการยืม-คืน", key="nav_how", use_container_width=True):
            how_it_works_dialog()
    with n4:
        if st.button("สำหรับผู้ขาย", key="nav_seller", use_container_width=True):
            st.session_state.current_view = 'seller'
            st.rerun()

with col_cart_r:
    st.markdown("<div class='btn-cart-rent'>", unsafe_allow_html=True)
    if st.button(f"📖 ยืม {rent_count}", key="header_cart_rent", use_container_width=True):
        st.session_state.current_view = 'cart'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with col_cart_b:
    st.markdown("<div class='btn-cart-buy'>", unsafe_allow_html=True)
    if st.button(f"🛍️ ซื้อ {buy_count}", key="header_cart_buy", use_container_width=True):
        st.session_state.current_view = 'cart'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with col_user:
    if st.session_state.user['logged_in']:
        u_col_avatar, u_col_info = st.columns([1, 2.5])
        with u_col_avatar:
            st.markdown(
                """
                <div style="width:38px; height:38px; border-radius:50%; background-color:#E8DDD0; display:flex; align-items:center; justify-content:center; font-weight:700; color:#4A3528; border:1px solid #D5C5B5;">
                    M
                </div>
                """,
                unsafe_allow_html=True
            )
        with u_col_info:
            st.markdown(
                f"""
                <div style="line-height:1.2; font-size:12px;">
                    <b>{st.session_state.user['name']}</b><br>
                    <span style="font-size:10px; color:#588157;">● {st.session_state.user['tier']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        if st.button("🔑 เข้าสู่ระบบ", key="btn_header_login", use_container_width=True):
            login_dialog()

st.markdown("<hr style='border:0; border-top:1px solid #EADBCE; margin:8px 0 20px 0;'>", unsafe_allow_html=True)

# ==============================================================================
# 6. VIEW 1: HOME PAGE (Explore & Catalog - Images 1 & 2)
# ==============================================================================
if st.session_state.current_view == 'home':

    # Search bar & Quick action
    col_search, col_cart_jump = st.columns([4, 1.2])
    with col_search:
        search_kw = st.text_input(
            "ค้นหา",
            value=st.session_state.search_query,
            placeholder="🔍 ค้นหาชื่อหนังสือ, ผู้แต่ง, หรือหมวดหมู่...",
            label_visibility="collapsed"
        )
        st.session_state.search_query = search_kw
    with col_cart_jump:
        if st.button("👜 ไปที่ตะกร้าสินค้า", use_container_width=True):
            st.session_state.current_view = 'cart'
            st.rerun()

    # Hero Banner
    col_hero_text, col_hero_card = st.columns([1.8, 1.2])
    with col_hero_text:
        st.markdown(
            """
            <div class="hero-container">
                <span class="hero-badge">🌱 ชุมชนนักอ่านและการแบ่งปันหนังสือยั่งยืน</span>
                <div class="hero-h1">
                    ส่งต่อเรื่องราวดีๆ <br>
                    <u>อ่านเพลินไม่ต้องซื้อขาด</u> <br>
                    หรือสร้างรายได้จากตู้หนังสือ
                </div>
                <div class="hero-desc">
                    เช่ายืมเริ่มต้นเพียง <b>฿5 /วัน</b> ดื่มด่ำวรรณกรรมชิ้นโปรดแบบสบายกระเป๋า พร้อมส่งฟรีถึงประตูบ้านเมื่อเช่าครบ 3 เล่มขึ้นไป
                </div>
                <div style="display:flex; gap:12px; margin-bottom:20px;">
                    <a href="#book-catalog" style="text-decoration:none;">
                        <div style="background-color:#4A3528; color:#FAF5EF; padding:10px 22px; border-radius:12px; font-weight:600; font-size:14px; display:inline-block;">
                            📖 สำรวจหนังสือทั้งหมด
                        </div>
                    </a>
                    <a href="#seller" style="text-decoration:none;">
                        <div style="background-color:#FFFFFF; color:#4A3528; border:1px solid #C8B9A9; padding:10px 22px; border-radius:12px; font-weight:600; font-size:14px; display:inline-block;">
                            🏪 เริ่มเปิดร้านให้เช่า/ขาย
                        </div>
                    </a>
                </div>
                <div style="display:flex; gap:12px; flex-wrap:wrap;">
                    <div class="hero-stat-card">
                        <b style="font-size:18px; color:#4A3528;">12,500+</b><br>
                        <span style="font-size:11px; color:#8D7B68;">หนังสือพร้อมส่ง</span>
                    </div>
                    <div class="hero-stat-card">
                        <b style="font-size:18px; color:#4A3528;">3,200+</b><br>
                        <span style="font-size:11px; color:#8D7B68;">ผู้แบ่งปันในระบบ</span>
                    </div>
                    <div class="hero-stat-card">
                        <b style="font-size:18px; color:#4A3528;">4.9 ★</b><br>
                        <span style="font-size:11px; color:#8D7B68;">ความพึงพอใจ 99%</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_hero_card:
        st.markdown(
            """
            <div style="background-color:#FFFFFF; border:1px solid #E8DDD0; border-radius:24px; padding:16px; box-shadow:0 6px 20px rgba(61,46,36,0.05); text-align:center;">
                <div style="position:relative; border-radius:16px; overflow:hidden; margin-bottom:12px;">
                    <img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80" style="width:100%; height:220px; object-fit:cover;">
                    <div style="position:absolute; top:10px; left:10px; background-color:rgba(255,255,255,0.92); padding:4px 10px; border-radius:999px; font-size:11px; font-weight:600; color:#2F5930;">
                        🚚 ส่งฟรีเมื่อยืม 3 เล่มขึ้นไป
                    </div>
                    <div style="position:absolute; bottom:10px; right:10px; background-color:#BC6C25; color:#FFFFFF; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:600;">
                        ประหยัด 85%
                    </div>
                </div>
                <div style="background-color:#FAF5EF; border-radius:14px; padding:12px; text-align:left; border:1px solid #EADBCE;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span style="font-size:20px;">♻️</span>
                        <div style="font-size:11px; color:#4A3528; line-height:1.4;">
                            <b>หมุนเวียนแล้ว 48,000+ ครั้ง</b><br>
                            ลดการตัดต้นไม้กว่า 960 ต้น ในชุมชนนักอ่าน BookShare
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Category Section
    st.markdown("<div id='book-catalog'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:10px; margin-bottom:12px;">
            <div>
                <h3 style="margin:0; font-size:20px; color:#4A3528;">หมวดหมู่ยอดนิยม</h3>
                <span style="font-size:12px; color:#8D7B68;">เลือกตามความสนใจของคุณ</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    categories = [
        "ทั้งหมด",
        "วรรณกรรม & นิยายแปล",
        "จิตวิทยา & พัฒนาตนเอง",
        "ธุรกิจ & การลงทุน",
        "หนังสือภาพ & ไลฟ์สไตล์",
        "วรรณกรรมคลาสสิก",
    ]

    cat_cols = st.columns(len(categories))
    for i, c in enumerate(categories):
        with cat_cols[i]:
            is_active = (st.session_state.active_category == c)
            btn_label = f"✓ {c}" if is_active else c
            if st.button(btn_label, key=f"cat_btn_{i}", use_container_width=True):
                st.session_state.active_category = c
                st.rerun()

    st.markdown("<div style='margin-bottom:16px;'></div>", unsafe_allow_html=True)

    # Filter books based on search & category
    filtered_books = []
    for b in MOCK_BOOKS:
        # Check category
        if st.session_state.active_category != "ทั้งหมด" and b['category'] != st.session_state.active_category:
            continue
        # Check search
        if st.session_state.search_query:
            query = st.session_state.search_query.lower()
            if query not in b['title'].lower() and query not in b['author'].lower() and query not in b['category'].lower():
                continue
        filtered_books.append(b)

    # Section title & sort option
    col_sec_title, col_sort = st.columns([3, 1])
    with col_sec_title:
        st.markdown(
            f"""
            <div style="margin-bottom:16px;">
                <span style="font-size:12px; color:#BC6C25; font-weight:600;">คัดสรรพิเศษสำหรับคุณ</span>
                <h3 style="margin:2px 0 0 0; font-size:22px; color:#4A3528;">หนังสือแนะนำ &amp; มาใหม่ล่าสุด ({len(filtered_books)} เล่ม)</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_sort:
        sort_by = st.selectbox("เรียงตาม", ["ยอดนิยมสูงสุด", "ราคาเช่า: ต่ำ-สูง", "ราคาซื้อ: ต่ำ-สูง"], label_visibility="collapsed")

    if sort_by == "ราคาเช่า: ต่ำ-สูง":
        filtered_books = sorted(filtered_books, key=lambda x: x['rent_price'])
    elif sort_by == "ราคาซื้อ: ต่ำ-สูง":
        filtered_books = sorted(filtered_books, key=lambda x: x['buy_price'])

    # Book Grid (4 Columns as in Image 2)
    grid_cols = st.columns(4)
    for idx, book in enumerate(filtered_books):
        col_pos = idx % 4
        with grid_cols[col_pos]:
            # Badge html
            if book['status'] == 'available':
                badge_html = "<span class='badge-available'>🟢 พร้อมให้ยืม</span>"
            elif book['status'] == 'rented':
                badge_html = f"<span class='badge-rented'>🔴 ถูกยืมอยู่</span>"
            else:
                badge_html = "<span class='badge-sale'>🏷️ สำหรับขายเท่านั้น</span>"

            condition_html = f"<span class='badge-condition'>{book['condition']}</span>"

            # Pricing label
            if book['status'] == 'sale_only':
                price_html = f"""
                <div>
                    <span style="font-size:11px; color:#8D7B68; text-decoration:line-through;">฿{book['original_price']}</span><br>
                    <b style="font-size:16px; color:#BC6C25;">฿{book['buy_price']}</b>
                </div>
                """
            elif book['status'] == 'rented':
                avail_note = book.get('available_date', 'รอส่งคืน')
                price_html = f"""
                <div>
                    <span style="font-size:11px; color:#8D7B68;">ยืม ฿{book['rent_price']}/วัน</span><br>
                    <b style="font-size:13px; color:#D9534F;">{avail_note}</b> | <span style="font-size:12px; color:#4A3528;">ซื้อ ฿{book['buy_price']}</span>
                </div>
                """
            else:
                price_html = f"""
                <div>
                    <span style="font-size:11px; color:#8D7B68;">ยืมเพียง</span><br>
                    <b style="font-size:15px; color:#4A3528;">฿{book['rent_price']}</b> <span style="font-size:11px; color:#8D7B68;">/วัน</span> | <span style="font-size:12px; color:#4A3528;">ซื้อ ฿{book['buy_price']}</span>
                </div>
                """

            st.markdown(
                f"""
                <div class="card-book">
                    <div>
                        <div style="position:relative;">
                            <img src="{book['img']}" class="book-cover-img" alt="{book['title']}">
                            <div style="position:absolute; top:8px; left:8px;">{badge_html}</div>
                            <div style="position:absolute; bottom:14px; right:8px;">{condition_html}</div>
                        </div>
                        <div style="font-size:11px; color:#8D7B68; margin-bottom:2px;">{book['category']}</div>
                        <h4 style="margin:0 0 4px 0; font-size:14px; font-weight:600; color:#382B24; line-height:1.3; height:38px; overflow:hidden; text-overflow:ellipsis; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;">
                            {book['title']}
                        </h4>
                        <div style="font-size:11px; color:#6C5E53; margin-bottom:10px; height:18px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">
                            {book['author']}
                        </div>
                    </div>
                    <div style="border-top:1px solid #EADBCE; padding-top:10px; margin-top:8px; display:flex; justify-content:space-between; align-items:center;">
                        {price_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Button to view details
            btn_caption = "🔍 ดูรายละเอียด & สั่งซื้อ"
            if book['status'] == 'rented':
                btn_caption = "🔍 ดูข้อมูล & จองคิว"
            elif book['status'] == 'sale_only':
                btn_caption = "🛒 ดูรายละเอียด & ซื้อ"

            if st.button(btn_caption, key=f"btn_book_open_{book['id']}", use_container_width=True):
                st.session_state.selected_book_id = book['id']
                st.session_state.current_view = 'detail'
                st.rerun()

            st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)


# ==============================================================================
# 7. VIEW 2: BOOK DETAIL PAGE (Image 3)
# ==============================================================================
elif st.session_state.current_view == 'detail':
    book = get_book_by_id(st.session_state.selected_book_id)

    # Breadcrumb & Back button
    b_col1, b_col2 = st.columns([1.5, 8.5])
    with b_col1:
        if st.button("← กลับหน้าสำรวจ", key="back_to_catalog"):
            st.session_state.current_view = 'home'
            st.rerun()
    with b_col2:
        st.markdown(
            f"""
            <div style="font-size:13px; color:#8D7B68; padding-top:6px;">
                หน้าแรก / หมวด{book['category']} / <b style="color:#4A3528;">{book['title']}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-bottom:16px;'></div>", unsafe_allow_html=True)

    # Detail Container (Left: Images + Seller, Right: Info + Rental/Buy Options)
    col_left, col_right = st.columns([4.2, 5.8], gap="large")

    with col_left:
        # Big Cover
        st.markdown(
            f"""
            <div style="position:relative; background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:20px; overflow:hidden; padding:16px; text-align:center; box-shadow:0 4px 18px rgba(61,46,36,0.04);">
                <img src="{book['img']}" style="width:100%; max-height:420px; object-fit:contain; border-radius:14px;">
                <div style="position:absolute; top:24px; left:24px; background-color:#588157; color:#FFFFFF; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:600;">
                    ● {book['condition_full']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Thumbnails Gallery
        t_cols = st.columns(3)
        for t_idx, thumb_url in enumerate(book.get('thumbnails', [book['img']])):
            if t_idx < 3:
                with t_cols[t_idx]:
                    st.image(thumb_url, use_container_width=True)

        # Seller Card Box
        st.markdown(
            f"""
            <div class="seller-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div style="display:flex; align-items:center; gap:10px;">
                        <div style="width:40px; height:40px; border-radius:50%; background-color:#E8DDD0; display:flex; align-items:center; justify-content:center; font-size:18px;">
                            👤
                        </div>
                        <div>
                            <b style="font-size:14px; color:#4A3528;">{book['seller_name']}</b><br>
                            <span style="font-size:12px; color:#BC6C25;">★ {book['seller_rating']}</span>
                            <span style="font-size:11px; color:#8D7B68;">(ส่งต่อแล้ว {book['seller_count']} เล่ม)</span>
                        </div>
                    </div>
                    <div style="background-color:#FFFFFF; border:1px solid #DACABD; padding:5px 12px; border-radius:8px; font-size:12px; font-weight:600; color:#4A3528;">
                        ดูตู้หนังสือ
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Book Quality Inspection Checklist
        st.markdown(
            """
            <div class="check-box-cert">
                <b style="font-size:13px; color:#4A3528; display:block; margin-bottom:8px;">การตรวจรับรองสภาพหนังสือโดย BookShare</b>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:12px; color:#588157;">
                    <div>✔ ไม่มีรอยขีดเขียน/ไฮไลท์</div>
                    <div>✔ สันปกตรง ไม่งอ</div>
                    <div>✔ กระดาษถนอมสายตา</div>
                    <div>✔ ผ่านการอบฆ่าเชื้อ UV</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_right:
        # Categories & ISBN
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
                <span style="background-color:#F5EFE6; color:#6B4F4F; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:600;">{book['category']}</span>
                <span style="background-color:#EAF2E8; color:#2F5930; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:600;">พร้อมเช่า &amp; ซื้อ</span>
                <span style="font-size:11px; color:#8D7B68; margin-left:auto;">ISBN: {book['isbn']}</span>
            </div>
            <h2 style="margin:0 0 6px 0; font-size:26px; color:#4A3528; line-height:1.2;">
                {book['full_title']}
            </h2>
            <div style="font-size:13px; color:#6C5E53; margin-bottom:12px;">
                {book['author']}
            </div>
            <p style="font-size:13px; color:#4A3528; line-height:1.6; background-color:#FAF6F0; padding:12px 16px; border-radius:12px; border:1px solid #EADBCE;">
                {book['desc']}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<b style='font-size:14px; color:#4A3528; display:block; margin:16px 0 8px 0;'>เลือกรูปแบบที่ต้องการ:</b>", unsafe_allow_html=True)

        # Dual Option Selector: Rent vs Buy
        default_order_mode = 'rent' if book['status'] != 'sale_only' else 'buy'
        order_mode = st.radio(
            "รูปแบบการสั่งซื้อ",
            options=['rent', 'buy'] if book['status'] != 'sale_only' else ['buy'],
            format_func=lambda x: f"📖 ยืมอ่านประหยัด (฿{book['rent_price']}/วัน + มัดจำ ฿{book['deposit']})" if x == 'rent' else f"🛍️ ซื้อขาดมือสอง (฿{book['buy_price']} จากปกติ ฿{book['original_price']})",
            key=f"order_mode_radio_{book['id']}",
            horizontal=False
        )

        # IF RENT SELECTED
        if order_mode == 'rent':
            st.markdown(
                """
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:16px; padding:18px; margin-top:10px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                        <b style="font-size:14px; color:#2F5930;">🗓️ กำหนดระยะเวลายืมหนังสือ</b>
                        <span style="background-color:#EAF2E8; color:#2F5930; padding:2px 8px; border-radius:999px; font-size:11px; font-weight:600;">ยืมได้สูงสุด 30 วัน</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Quick days chips
            st.caption("เลือกด่วน:")
            q_cols = st.columns(4)
            if 'quick_days_selected' not in st.session_state:
                st.session_state.quick_days_selected = 10

            with q_cols[0]:
                if st.button("7 วัน", key="btn_days_7", use_container_width=True):
                    st.session_state.quick_days_selected = 7
                    st.rerun()
            with q_cols[1]:
                if st.button("10 วัน (แนะนำ)", key="btn_days_10", use_container_width=True):
                    st.session_state.quick_days_selected = 10
                    st.rerun()
            with q_cols[2]:
                if st.button("14 วัน", key="btn_days_14", use_container_width=True):
                    st.session_state.quick_days_selected = 14
                    st.rerun()
            with q_cols[3]:
                if st.button("21 วัน", key="btn_days_21", use_container_width=True):
                    st.session_state.quick_days_selected = 21
                    st.rerun()

            today = date.today()
            col_date_start, col_date_end = st.columns(2)
            with col_date_start:
                start_date_val = st.date_input("วันเริ่มยืม (Start Date)", today, key="rent_start_input")
            with col_date_end:
                suggested_end = start_date_val + timedelta(days=st.session_state.quick_days_selected)
                end_date_val = st.date_input("วันกำหนดคืน (Return Date)", suggested_end, key="rent_end_input")

            # Duration and price calculation
            calc_days = (end_date_val - start_date_val).days
            if calc_days <= 0:
                st.warning("⚠️ วันกำหนดคืนต้องอยู่หลังจากวันเริ่มยืมอย่างน้อย 1 วัน")
                calc_days = 1
            elif calc_days > 30:
                st.error("🚨 สามารถยืมได้สูงสุดไม่เกิน 30 วันต่อรอบคำสั่งซื้อ")
                calc_days = 30

            rental_cost = calc_days * book['rent_price']
            deposit_cost = book['deposit']
            total_rent_round = rental_cost + deposit_cost

            st.markdown(
                f"""
                <div style="background-color:#F5EFE6; border:1px solid #E2D4C5; border-radius:14px; padding:14px 18px; margin:14px 0; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:15px; color:#4A3528;">{calc_days} วัน × ฿{book['rent_price']}/วัน = <span style="color:#BC6C25;">฿{rental_cost}</span></b><br>
                        <span style="font-size:12px; color:#6C5E53;">+ ค่ามัดจำหนังสือ ฿{deposit_cost} (ได้รับคืนอัตโนมัติเมื่อคืนหนังสือ)</span>
                    </div>
                    <div style="text-align:right;">
                        <span style="font-size:11px; color:#8D7B68;">รวมชำระรอบนี้</span><br>
                        <b style="font-size:22px; color:#4A3528;">฿{total_rent_round}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Action Buttons for Rent
            act_col1, act_col2 = st.columns(2)
            with act_col1:
                if st.button("🛒 เพิ่มลงตะกร้ายืม", key="add_to_cart_rent_btn", use_container_width=True):
                    rent_item = {
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'rent_days': calc_days,
                        'start_date': start_date_val.strftime("%d/%m/%Y"),
                        'return_date': end_date_val.strftime("%d %b %Y"),
                        'rate_per_day': book['rent_price'],
                        'total_rent': rental_cost,
                        'deposit': deposit_cost,
                        'img': book['img'],
                    }
                    st.session_state.cart_rent.append(rent_item)
                    st.toast(f"เพิ่ม '{book['title']}' ลงในหมวดเช่ายืมแล้ว!", icon="📖")
                    st.rerun()

            with act_col2:
                if st.button(f"📖 ยืมทันที (฿{total_rent_round})", key="buy_now_rent_btn", use_container_width=True):
                    rent_item = {
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'rent_days': calc_days,
                        'start_date': start_date_val.strftime("%d/%m/%Y"),
                        'return_date': end_date_val.strftime("%d %b %Y"),
                        'rate_per_day': book['rent_price'],
                        'total_rent': rental_cost,
                        'deposit': deposit_cost,
                        'img': book['img'],
                    }
                    st.session_state.cart_rent.append(rent_item)
                    st.session_state.current_view = 'cart'
                    st.rerun()

        # IF BUY SELECTED
        else:
            st.markdown(
                f"""
                <div style="background-color:#FAF5EF; border:1px solid #E8DDD0; border-radius:16px; padding:18px; margin-top:10px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span style="font-size:12px; color:#BC6C25; font-weight:600;">ซื้อขาดเป็นเจ้าของถาวร</span>
                            <h3 style="margin:4px 0 0 0; color:#4A3528; font-size:24px;">฿{book['buy_price']}</h3>
                            <span style="font-size:12px; color:#8D7B68; text-decoration:line-through;">ราคาปก ฿{book['original_price']}</span>
                            <span style="font-size:12px; color:#588157; margin-left:6px; font-weight:600;">ประหยัด ฿{book['original_price'] - book['buy_price']}</span>
                        </div>
                        <div style="text-align:right; font-size:12px; color:#6C5E53;">
                            สภาพสะสม {book['condition']}<br>
                            ไม่ต้องส่งคืน จัดส่งทันที
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Action Buttons for Buy
            act_col1, act_col2 = st.columns(2)
            with act_col1:
                if st.button("🛒 เพิ่มลงตะกร้าซื้อ", key="add_to_cart_buy_btn", use_container_width=True):
                    buy_item = {
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'buy_price': book['buy_price'],
                        'original_price': book['original_price'],
                        'tag': 'ซื้อขาดมือสอง จัดส่งทันที',
                        'img': book['img'],
                    }
                    st.session_state.cart_buy.append(buy_item)
                    st.toast(f"เพิ่ม '{book['title']}' ลงในหมวดซื้อขาดแล้ว!", icon="🛍️")
                    st.rerun()

            with act_col2:
                if st.button(f"🛍️ สั่งซื้อทันที (฿{book['buy_price']})", key="buy_now_direct_btn", use_container_width=True):
                    buy_item = {
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'buy_price': book['buy_price'],
                        'original_price': book['original_price'],
                        'tag': 'ซื้อขาดมือสอง จัดส่งทันที',
                        'img': book['img'],
                    }
                    st.session_state.cart_buy.append(buy_item)
                    st.session_state.current_view = 'cart'
                    st.rerun()

        # Guarantee Badges
        st.markdown(
            """
            <div style="display:flex; justify-content:space-between; margin-top:24px; padding-top:16px; border-top:1px solid #EADBCE; text-align:center; font-size:12px; color:#6C5E53;">
                <div>🚚 ส่งด่วนถึงหน้าบ้าน</div>
                <div>↩️ คืนง่ายผ่านไปรษณีย์/ขนส่ง</div>
                <div>🛡️ คุ้มครองเงินมัดจำ 100%</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# 8. VIEW 3: CART & UNIFIED CHECKOUT (Image 4 - Separated Sections & Single Pay)
# ==============================================================================
elif st.session_state.current_view == 'cart':
    total_items = len(st.session_state.cart_rent) + len(st.session_state.cart_buy)

    # Cart Header
    col_cart_h1, col_cart_h2 = st.columns([3, 1])
    with col_cart_h1:
        st.markdown(
            """
            <div style="margin-bottom:16px;">
                <h2 style="margin:0; font-size:28px; color:#4A3528;">👜 ตะกร้าของคุณ</h2>
                <span style="font-size:13px; color:#8D7B68;">แยกสัดส่วนการชำระเงินระหว่าง หนังสือเช่ายืม และ หนังสือสั่งซื้อขาด</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_cart_h2:
        st.markdown(
            f"""
            <div style="text-align:right; padding-top:8px;">
                <span style="background-color:#E8DDD0; color:#4A3528; padding:6px 14px; border-radius:999px; font-size:13px; font-weight:600;">
                    {total_items} รายการในตะกร้า
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    if total_items == 0:
        st.info("🛒 ตะกร้าสินค้าของคุณยังว่างเปล่า เริ่มต้นเลือกหนังสือเพื่อยืมหรือซื้อได้เลย!")
        if st.button("← กลับไปสำรวจหนังสือ", key="empty_cart_back"):
            st.session_state.current_view = 'home'
            st.rerun()
    else:
        # Two Columns Layout: Left = Cart Items (A & B), Right = Summary & Mandatory Address/Auth
        cart_left, cart_right = st.columns([5.8, 4.2], gap="large")

        # ==========================================
        # LEFT: SECTIONS A & B
        # ==========================================
        with cart_left:
            # SECTION A: RENTAL ITEMS
            st.markdown(
                f"""
                <div style="background-color:#EAF2E8; border:1px solid #C0DAC0; border-radius:16px; padding:12px 18px; margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:16px; color:#2F5930;">📖 A) รายการที่จะเช่ายืม (Rental Items)</b><br>
                        <span style="font-size:12px; color:#4E704E;">ยืมอ่านตามกำหนด คืนสะดวก พร้อมรับมัดจำคืนเต็มจำนวน</span>
                    </div>
                    <span style="background-color:#588157; color:#FFFFFF; padding:2px 10px; border-radius:999px; font-size:11px; font-weight:600;">
                        {len(st.session_state.cart_rent)} เล่ม
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            total_rent_fee = 0
            total_deposit_fee = 0

            if not st.session_state.cart_rent:
                st.caption("ไม่มีรายการหนังสือในหมวดเช่ายืม")
            else:
                for idx, r_item in enumerate(st.session_state.cart_rent):
                    total_rent_fee += r_item['total_rent']
                    total_deposit_fee += r_item['deposit']

                    c_img, c_info, c_price, c_del = st.columns([1.2, 4.2, 1.8, 0.8])
                    with c_img:
                        st.image(r_item['img'], width=65)
                    with c_info:
                        st.markdown(
                            f"""
                            <b style="font-size:14px; color:#4A3528;">{r_item['title']}</b><br>
                            <span style="font-size:12px; color:#8D7B68;">{r_item['author']} • {r_item['condition']}</span><br>
                            <span style="font-size:11px; background-color:#FAF5EF; border:1px solid #EADBCE; padding:2px 6px; border-radius:6px; color:#6C5E53;">
                                ระยะเวลา: {r_item['rent_days']} วัน | กำหนดคืน: {r_item['return_date']}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_price:
                        st.markdown(
                            f"""
                            <div style="text-align:right;">
                                <b style="font-size:16px; color:#4A3528;">฿{r_item['total_rent']}</b><br>
                                <span style="font-size:11px; color:#8D7B68;">(มัดจำ ฿{r_item['deposit']})</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_del:
                        if st.button("🗑️", key=f"del_rent_{idx}", help="ลบรายการนี้"):
                            st.session_state.cart_rent.pop(idx)
                            st.rerun()

                    st.markdown("<hr style='border:0; border-top:1px dashed #E8DDD0; margin:8px 0;'>", unsafe_allow_html=True)

                st.markdown(
                    f"""
                    <div style="text-align:right; font-size:13px; color:#4A3528; padding:4px 0 16px 0;">
                        รวมค่าเช่ายืมหมวด A: <b style="font-size:16px; color:#2F5930;">฿{total_rent_fee}</b> 
                        <span style="font-size:12px; color:#8D7B68;">(มัดจำสะสม ฿{total_deposit_fee})</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)

            # SECTION B: PURCHASE ITEMS
            st.markdown(
                f"""
                <div style="background-color:#FAEEE1; border:1px solid #EAC8A8; border-radius:16px; padding:12px 18px; margin-bottom:14px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:16px; color:#9C5212;">🛍️ B) รายการที่จะซื้อขาด (Purchase Items)</b><br>
                        <span style="font-size:12px; color:#854711;">หนังสือมือสองคัดเกรด เป็นเจ้าของถาวร ไม่ต้องส่งคืน</span>
                    </div>
                    <span style="background-color:#BC6C25; color:#FFFFFF; padding:2px 10px; border-radius:999px; font-size:11px; font-weight:600;">
                        {len(st.session_state.cart_buy)} เล่ม
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

            total_buy_fee = 0

            if not st.session_state.cart_buy:
                st.caption("ไม่มีรายการหนังสือในหมวดซื้อขาด")
            else:
                for idx, b_item in enumerate(st.session_state.cart_buy):
                    total_buy_fee += b_item['buy_price']

                    c_img, c_info, c_price, c_del = st.columns([1.2, 4.2, 1.8, 0.8])
                    with c_img:
                        st.image(b_item['img'], width=65)
                    with c_info:
                        st.markdown(
                            f"""
                            <b style="font-size:14px; color:#4A3528;">{b_item['title']}</b><br>
                            <span style="font-size:12px; color:#8D7B68;">{b_item['author']} • {b_item['condition']}</span><br>
                            <span style="font-size:11px; background-color:#FAEEE1; color:#9C5212; padding:2px 6px; border-radius:6px;">
                                {b_item.get('tag', 'ซื้อขาดมือสอง จัดส่งทันที')}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_price:
                        orig = b_item.get('original_price', b_item['buy_price'])
                        st.markdown(
                            f"""
                            <div style="text-align:right;">
                                <b style="font-size:16px; color:#BC6C25;">฿{b_item['buy_price']}</b><br>
                                <span style="font-size:11px; color:#8D7B68; text-decoration:line-through;">฿{orig}</span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_del:
                        if st.button("🗑️", key=f"del_buy_{idx}", help="ลบรายการนี้"):
                            st.session_state.cart_buy.pop(idx)
                            st.rerun()

                    st.markdown("<hr style='border:0; border-top:1px dashed #E8DDD0; margin:8px 0;'>", unsafe_allow_html=True)

                st.markdown(
                    f"""
                    <div style="text-align:right; font-size:13px; color:#4A3528; padding:4px 0 16px 0;">
                        รวมค่าซื้อขาดหมวด B: <b style="font-size:16px; color:#BC6C25;">฿{total_buy_fee}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ==========================================
        # RIGHT: SUMMARY, ADDRESS & CHECKOUT
        # ==========================================
        with cart_right:
            st.markdown(
                """
                <div style="background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:20px; padding:20px; box-shadow:0 4px 18px rgba(61,46,36,0.05); margin-bottom:16px;">
                    <h3 style="margin:0 0 14px 0; font-size:18px; color:#4A3528; display:flex; justify-content:space-between; align-items:center;">
                        <span>สรุปยอดคำสั่งซื้อ</span>
                        <span style="font-size:20px;">🧾</span>
                    </h3>
                """,
                unsafe_allow_html=True
            )

            # Calculation
            shipping_cost = 45 if total_items > 0 else 0
            if len(st.session_state.cart_rent) >= 3:
                shipping_cost = 0  # Promo: Free shipping for 3+ rental books

            discount = 30 if st.session_state.promo_code.upper() == 'WELCOMEREAD' else 0
            grand_total = total_rent_fee + total_buy_fee + total_deposit_fee + shipping_cost - discount
            if grand_total < 0:
                grand_total = 0

            st.markdown(
                f"""
                <div style="font-size:13px; color:#6C5E53; line-height:2.0;">
                    <div style="display:flex; justify-content:space-between;">
                        <span>ค่าเช่ายืมรวม ({len(st.session_state.cart_rent)} เล่ม)</span>
                        <b style="color:#4A3528;">฿{total_rent_fee}</b>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>ค่าซื้อขาดรวม ({len(st.session_state.cart_buy)} เล่ม)</span>
                        <b style="color:#4A3528;">฿{total_buy_fee}</b>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>ค่ามัดจำรวม ℹ️</span>
                        <b style="color:#4A3528;">฿{total_deposit_fee}</b>
                    </div>
                    <div style="display:flex; justify-content:space-between;">
                        <span>ค่าบริการจัดส่งพัสดุ</span>
                        <b style="color:#4A3528;">{"ฟรี (โปร 3 เล่ม)" if shipping_cost == 0 and len(st.session_state.cart_rent) >= 3 else f"฿{shipping_cost}"}</b>
                    </div>
                    <div style="display:flex; justify-content:space-between; color:#588157;">
                        <span>โค้ดส่วนลดนักอ่านใหม่ ({st.session_state.promo_code})</span>
                        <b>-฿{discount}</b>
                    </div>
                </div>
                <hr style="border:0; border-top:1px solid #EADBCE; margin:12px 0;">
                <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:6px;">
                    <span style="font-size:15px; font-weight:700; color:#4A3528;">ยอดชำระทั้งหมด</span>
                    <span style="font-size:26px; font-weight:700; color:#4A3528;">฿{grand_total}</span>
                </div>
                <div style="font-size:11px; color:#8D7B68; margin-bottom:14px;">
                    * ยอดนี้รวมเงินมัดจำที่จะได้รับคืน ฿{total_deposit_fee} เมื่อส่งคืนหนังสือครบ
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Promo Code Input
            with st.expander("🏷️ มีโค้ดส่วนลดหรือไม่?"):
                code_in = st.text_input("กรอกโค้ดส่วนลด", value=st.session_state.promo_code)
                if st.button("ใช้โค้ด", key="btn_apply_code"):
                    st.session_state.promo_code = code_in.strip()
                    st.rerun()

            # MANDATORY CHECKOUT SECTION: Authentication & Shipping Address
            st.markdown(
                """
                <div style="background-color:#FAF5EF; border:1px solid #E8DDD0; border-radius:18px; padding:16px; margin-bottom:16px;">
                    <b style="font-size:14px; color:#4A3528; display:block; margin-bottom:8px;">📦 ข้อมูลสำหรับจัดส่ง &amp; สมาชิก (บังคับ)</b>
                """,
                unsafe_allow_html=True
            )

            # Check 1: User Logged in
            if not st.session_state.user['logged_in']:
                st.error("🚨 **กรุณาเข้าสู่ระบบบัญชีก่อน จึงจะสามารถสั่งซื้อได้**")
                if st.button("🔑 เข้าสู่ระบบ / ลงทะเบียน ตอนนี้", key="btn_cart_must_login", use_container_width=True):
                    login_dialog()
            else:
                st.success(f"✓ บัญชีผู้สั่งซื้อ: **{st.session_state.user['name']}** ({st.session_state.user['phone']})")

                # Check 2: Mandatory Address Form
                addr_input = st.text_area(
                    "ที่อยู่สำหรับจัดส่งพัสดุ * (บังคับ)",
                    value=st.session_state.user.get('address', ''),
                    placeholder="ระบุ บ้านเลขที่, ซอย, ถนน, แขวง/ตำบล, เขต/อำเภอ, จังหวัด, รหัสไปรษณีย์ ให้ครบถ้วน",
                    height=85,
                    help="จำเป็นต้องระบุที่อยู่เพื่อให้ผู้ให้เช่าและผู้ขายจัดส่งหนังสือถึงบ้านคุณได้อย่างถูกต้อง"
                )
                st.session_state.user['address'] = addr_input.strip()

                # Payment method selector
                pay_method = st.radio(
                    "ช่องทางชำระเงิน",
                    ["พร้อมเพย์ QR (PromptPay)", "บัตรเครดิต/เดบิต", "BookShare Wallet"],
                    horizontal=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

            # Verification for Checkout button
            can_checkout = True
            error_msgs = []

            if not st.session_state.user['logged_in']:
                can_checkout = False
                error_msgs.append("กรุณาเข้าสู่ระบบก่อนทำรายการ")

            if not st.session_state.user.get('address') or len(st.session_state.user.get('address', '').strip()) < 10:
                can_checkout = False
                error_msgs.append("กรุณากรอกที่อยู่จัดส่งอย่างละเอียด (ข้อมูลบังคับ)")

            if not can_checkout:
                for err in error_msgs:
                    st.caption(f"⚠️ {err}")
                st.button("🔒 กรุณาเข้าสู่ระบบและกรอกที่อยู่เพื่อชำระเงิน", disabled=True, use_container_width=True)
            else:
                # UNIFIED CHECKOUT BUTTON (ชำระเงินทีเดียว)
                if st.button(f"ดำเนินการชำระเงิน (Checkout ฿{grand_total}) ➔", key="btn_do_checkout", use_container_width=True):
                    # Save order record
                    st.session_state.last_order = {
                        'order_id': f"BS-{date.today().strftime('%Y%m%d')}-0992",
                        'user': st.session_state.user.copy(),
                        'rent_items': st.session_state.cart_rent.copy(),
                        'buy_items': st.session_state.cart_buy.copy(),
                        'total_rent': total_rent_fee,
                        'total_buy': total_buy_fee,
                        'total_deposit': total_deposit_fee,
                        'shipping': shipping_cost,
                        'discount': discount,
                        'grand_total': grand_total,
                        'payment_method': pay_method,
                    }
                    # Clear carts
                    st.session_state.cart_rent = []
                    st.session_state.cart_buy = []
                    st.session_state.current_view = 'order_success'
                    st.rerun()

            # Deposit guarantee callout (Matching Mockup Image 4)
            st.markdown(
                f"""
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:14px; padding:12px; margin-top:14px; font-size:11px; color:#2F5930; line-height:1.5;">
                    <b>🛡️ การันตีคืนมัดจำฉับไว:</b><br>
                    ระบบจะโอนเงินมัดจำ ฿{total_deposit_fee} กลับเข้าบัญชีพร้อมเพย์ของคุณภายใน 24 ชม. หลังจากผู้ให้เช่าตรวจสอบสภาพหนังสือเรียบร้อย
                </div>
                <div style="background-color:#FAF5EF; border:1px solid #EADBCE; border-radius:14px; padding:12px; margin-top:10px; font-size:11px; color:#4A3528; line-height:1.5;">
                    <b>🌱 การอ่านของคุณช่วยลดขยะกระดาษ!</b><br>
                    การเช่า {len(st.session_state.cart_rent)} เล่มในคำสั่งซื้อนี้ช่วยลดการปล่อยคาร์บอน -1.4 kg สู่สิ่งแวดล้อม
                </div>
                <div style="text-align:center; font-size:11px; color:#8D7B68; margin-top:12px;">
                    รองรับ: พร้อมเพย์ QR • บัตรเครดิต/เดบิต • BookShare Wallet
                </div>
                """,
                unsafe_allow_html=True
            )


# ==============================================================================
# 9. VIEW 4: ORDER SUCCESS / PAYMENT COMPLETED
# ==============================================================================
elif st.session_state.current_view == 'order_success':
    order = st.session_state.last_order
    st.balloons()

    st.markdown(
        """
        <div style="text-align:center; max-width:680px; margin:0 auto; padding:30px 20px; background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:24px; box-shadow:0 8px 24px rgba(61,46,36,0.06);">
            <span style="font-size:54px;">🎉</span>
            <h2 style="color:#4A3528; margin:10px 0 6px 0;">สั่งซื้อและชำระเงินสำเร็จเรียบร้อย!</h2>
            <p style="font-size:14px; color:#6C5E53;">ขอบคุณที่ร่วมเป็นส่วนหนึ่งของสังคมการอ่านและแบ่งปันที่ยั่งยืน</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if order:
        col_rec1, col_rec2 = st.columns([1, 1], gap="medium")
        with col_rec1:
            st.markdown(
                f"""
                <div style="background-color:#FAF5EF; border:1px solid #EADBCE; border-radius:16px; padding:18px; margin-top:16px;">
                    <b style="font-size:15px; color:#4A3528;">รายละเอียดคำสั่งซื้อ: {order['order_id']}</b><br>
                    <div style="font-size:13px; color:#6C5E53; margin-top:10px; line-height:1.7;">
                        <b>ผู้รับ:</b> {order['user']['name']} ({order['user']['phone']})<br>
                        <b>ที่อยู่จัดส่ง:</b> {order['user']['address']}<br>
                        <b>วิธีชำระเงิน:</b> {order['payment_method']}<br>
                        <b>ยอดชำระสุทธิ:</b> <span style="font-size:16px; color:#BC6C25; font-weight:700;">฿{order['grand_total']}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col_rec2:
            st.markdown(
                f"""
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:16px; padding:18px; margin-top:16px; text-align:center;">
                    <b style="font-size:15px; color:#2F5930;">สแกนชำระเงินผ่าน PromptPay QR</b><br>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=BookShare-{order['order_id']}" style="margin:10px 0; border-radius:8px;">
                    <div style="font-size:11px; color:#588157;">
                        ยอดเงิน ฿{order['grand_total']} (รวมค่ามัดจำคืน ฿{order['total_deposit']})
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:20px; text-align:center;'>", unsafe_allow_html=True)
    if st.button("← กลับสู่หน้าหลักเพื่อสำรวจหนังสือต่อ", key="btn_order_success_home"):
        st.session_state.current_view = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 10. VIEW 5: SELLER CENTER (สำหรับผู้ขาย/ผู้ให้เช่า)
# ==============================================================================
elif st.session_state.current_view == 'seller':
    st.markdown(
        """
        <div style="margin-bottom:20px;">
            <h2 style="margin:0; font-size:28px; color:#4A3528;">🏪 มุมผู้ขาย &amp; เจ้าของตู้หนังสือ</h2>
            <span style="font-size:13px; color:#8D7B68;">เปลี่ยนหนังสือที่อ่านแล้วบนชั้นให้กลายเป็นรายได้ พร้อมส่งต่อคุณค่าสู่นักอ่านคนถัดไป</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    tab_add_b, tab_list_b = st.tabs(["➕ ลงทะเบียนหนังสือเล่มใหม่", "📚 ตู้หนังสือของฉัน"])

    with tab_add_b:
        with st.form("seller_add_form"):
            b_title = st.text_input("ชื่อหนังสือ", placeholder="เช่น เซเปียนส์ ประวัติศาสตร์มนุษยชาติ")
            b_author = st.text_input("ชื่อผู้แต่ง / ผู้แปล", placeholder="เช่น ยูวัล โนอาห์ แฮรารี")
            b_cat = st.selectbox("หมวดหมู่หนังสือ", ["จิตวิทยา & พัฒนาตนเอง", "วรรณกรรม & นิยายแปล", "ธุรกิจ & การลงทุน", "หนังสือภาพ & ไลฟ์สไตล์", "วรรณกรรมคลาสสิก"])
            b_cond = st.selectbox("สภาพหนังสือ", ["สภาพ 98% เหมือนใหม่", "สภาพ 95% ดีเยี่ยม", "สภาพ 90% ดี", "สภาพ 85% มีตำหนิเล็กน้อย"])
            b_type = st.radio("รูปแบบที่ต้องการลงรายการ", ["ให้เช่ายืม & ซื้อขาดได้", "ให้เช่ายืมอย่างเดียว", "ขายขาดอย่างเดียว"], horizontal=True)

            col_p1, col_p2 = st.columns(2)
            with col_p1:
                b_rent = st.number_input("ค่ายืมต่อวัน (บาท)", min_value=1, value=6)
            with col_p2:
                b_buy = st.number_input("ราคาขายขาด (บาท)", min_value=10, value=220)

            b_desc = st.text_area("คำอธิบายหรือความประทับใจเกี่ยวกับเล่มนี้", placeholder="แนะนำหนังสือสั้นๆ เพื่อให้นักอ่านคนอื่นสนใจ...")

            btn_submit_book = st.form_submit_button("บันทึกและเปิดให้ยืม/ขายทันที")

        if btn_submit_book:
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
                st.success(f"ลงทะเบียนหนังสือ '{b_title}' ในร้านค้าของคุณเรียบร้อยแล้ว!")
            else:
                st.error("กรุณาระบุชื่อหนังสือ")

    with tab_list_b:
        st.markdown(f"<b>รายการหนังสือในตู้ของคุณ ({len(st.session_state.my_books)} เล่ม):</b>", unsafe_allow_html=True)
        for idx, bk in enumerate(st.session_state.my_books):
            st.markdown(
                f"""
                <div style="background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:14px; padding:14px 18px; margin-bottom:10px;">
                    <b style="font-size:15px; color:#4A3528;">{bk['title']}</b><br>
                    <span style="font-size:12px; color:#8D7B68;">หมวดหมู่: {bk['category']} | {bk['condition']}</span><br>
                    <span style="font-size:12px; color:#BC6C25;">ขาย: ฿{bk['price_buy']} | ค่ายืม: ฿{bk['price_rent']}/วัน | สถานะ: {bk['status']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    if st.button("← กลับสู่หน้าหลัก", key="btn_seller_back"):
        st.session_state.current_view = 'home'
        st.rerun()

# ==============================================================================
# 11. Footer (Earth Tone & Warm Branding)
# ==============================================================================
st.markdown(
    """
    <div style="margin-top:60px; padding:30px 10px; border-top:1px solid #EADBCE; text-align:center; font-size:12px; color:#8D7B68;">
        <div style="font-family:'Mali', cursive; font-size:16px; font-weight:700; color:#4A3528; margin-bottom:4px;">
            BookShare - ร้านหนังสือ &amp; เช่ายืมออนไลน์
        </div>
        <div>
            พื้นที่ส่งต่อเรื่องราวและคุณค่าของหนังสืออย่างยั่งยืน ทั้งการเช่ายืมและส่งต่อหนังสือมือสองในชุมชนนักอ่าน
        </div>
        <div style="margin-top:10px; display:flex; justify-content:center; gap:16px;">
            <a href="#" style="color:#6C5E53; text-decoration:none;">เกี่ยวกับ BookShare</a>
            <a href="#" style="color:#6C5E53; text-decoration:none;">ข้อกำหนดการยืมและประกันหนังสือ</a>
            <a href="#" style="color:#6C5E53; text-decoration:none;">ความปลอดภัยและการจัดส่ง</a>
            <a href="#" style="color:#6C5E53; text-decoration:none;">ติดต่อทีมงาน</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)