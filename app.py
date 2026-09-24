from datetime import date, timedelta
import streamlit as st

# ==============================================================================
# 1. Page Configuration & Custom Styling (Earth Tone Minimal)
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

    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1240px !important;
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
        background-color: #FFFFFF;
        color: #4A3528;
        border: 1px solid #EADBCE;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 10px;
        font-weight: 600;
    }

    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #F3E9DD 0%, #EFE1D1 100%);
        border-radius: 24px;
        padding: 32px 36px;
        border: 1px solid #E5D7C7;
        margin-bottom: 24px;
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

    /* Book Cards */
    .card-book {
        background-color: #FFFFFF;
        border: 1px solid #EADBCE;
        border-radius: 18px;
        padding: 14px;
        margin-bottom: 12px;
        box-shadow: 0 4px 14px rgba(61,46,36,0.04);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .book-cover-img {
        width: 100%;
        aspect-ratio: 3/4;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #4A3528 !important;
        color: #FAF5EF !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 8px 16px !important;
        font-family: 'Kanit', sans-serif !important;
        transition: all 0.2s !important;
    }
    .stButton>button:hover {
        background-color: #BC6C25 !important;
        color: #FFFFFF !important;
    }

    .btn-cart-rent>button {
        background-color: #EAF2E8 !important;
        color: #2F5930 !important;
        border: 1px solid #C0DAC0 !important;
        border-radius: 999px !important;
        font-size: 13px !important;
        font-weight: 700 !important;
    }
    .btn-cart-buy>button {
        background-color: #FAEEE1 !important;
        color: #9C5212 !important;
        border: 1px solid #EAC8A8 !important;
        border-radius: 999px !important;
        font-size: 13px !important;
        font-weight: 700 !important;
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        border-radius: 10px !important;
        border: 1px solid #DACABD !important;
        background-color: #FFFFFF !important;
    }

    /* Seller Center Specific Styling */
    .seller-header-card {
        background-color: #FFFFFF;
        border: 1px solid #EADBCE;
        border-radius: 20px;
        padding: 20px 24px;
        box-shadow: 0 4px 14px rgba(61,46,36,0.04);
        margin-bottom: 20px;
    }
    .listing-type-card {
        border: 1px solid #EADBCE;
        border-radius: 14px;
        padding: 14px;
        background-color: #FFFFFF;
        text-align: center;
        transition: all 0.2s;
    }
    .pricing-box-container {
        background-color: #FAF5EF;
        border: 1px solid #EADBCE;
        border-radius: 16px;
        padding: 16px;
        margin-top: 14px;
    }
    .dropzone-container {
        border: 2px dashed #D5C5B5;
        background-color: #FAF5EF;
        border-radius: 16px;
        padding: 28px 16px;
        text-align: center;
        margin-bottom: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. Complete 8 Books Mock Data for Storefront
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
        'desc': 'เมื่อหัวขโมยสามคนหลบหนีไปซ่อนตัวในร้านชำร้างแห่งหนึ่ง แต่กลับได้รับจดหมายขอคำปรึกษาจากคนในอดีต เรื่องราวอบอุ่นหัวใจจึงเริ่มต้นขึ้น',
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
        'seller_name': 'Wealth Books',
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
        'condition_full': 'สภาพ 90% สมบูรณ์',
        'buy_price': 190,
        'original_price': 250,
        'rent_price': 5,
        'deposit': 100,
        'img': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=600&q=80',
        'desc': 'บทเรียนชีวิตและธุรกิจจากมหาเศรษฐีชาวยิว ถ่ายทอดผ่านความมุ่งมั่นสไตล์คนญี่ปุ่น นำไปประยุกต์ใช้เพื่อความมั่งคั่งที่ยั่งยืน',
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
        'desc': 'จิตวิทยาแบบแอดเลอร์ที่จะช่วยปลดปล่อยคุณจากความคาดหวังของผู้อื่น และค้นพบความสุขที่แท้จริงในชีวิต',
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
        'desc': 'เรื่องราวของร้านน้ำชาจันทร์เพ็ญที่มีแมวตัวโตคอยชงชาและเสิร์ฟคำพยากรณ์ฮีลใจให้แก่ผู้คน',
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
        'full_title': 'สูญสิ้นความเป็นคน (No Longer Human) ปกแข็งสะสม',
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
        'desc': 'บันทึกการเดินทางในโตเกียวที่เต็มไปด้วยความละเมียดละไม มุมมองสดใหม่ และแรงบันดาลใจที่ทำให้เราอยากก้าวออกไปสำรวจโลก',
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
    st.session_state.current_view = 'home'  # 'home', 'detail', 'cart', 'order_success', 'seller'

if 'seller_subview' not in st.session_state:
    st.session_state.seller_subview = 'add_book'  # 'add_book' or 'shelf'

if 'selected_book_id' not in st.session_state:
    st.session_state.selected_book_id = 1

if 'active_category' not in st.session_state:
    st.session_state.active_category = 'ทั้งหมด'

if 'search_query' not in st.session_state:
    st.session_state.search_query = ''

# User Authentication State
if 'user' not in st.session_state:
    st.session_state.user = {
        'logged_in': True,
        'name': 'คุณมีนา',
        'phone': '081-234-5678',
        'address': '123/45 ถนนมิตรภาพ แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110',
        'tier': 'ผู้อ่านระดับ 2 (เช่าอยู่ 2 เล่ม)',
    }

# Cart State matching Image 4
if 'cart_initialized' not in st.session_state:
    st.session_state.cart_initialized = True
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

if 'rental_days_choice' not in st.session_state:
    st.session_state.rental_days_choice = 10

if 'last_order' not in st.session_state:
    st.session_state.last_order = None

# Meena's Bookshelf Data (Matching Image 2)
if 'meena_books' not in st.session_state:
    st.session_state.meena_books = [
        {
            'id': 101,
            'title': 'เพราะชีวิตดีได้กว่าที่เป็น (Atomic Habits)',
            'author': 'James Clear • แปลโดย ประพาส ปานพุ่ม',
            'isbn': '978-616-18-2898-1',
            'condition': 'สภาพ 95%',
            'type_badge': '● เช่า & ขาย',
            'price_structure': 'เช่า ฿7/วัน (฿42/สัปดาห์)<br>มัดจำ ฿200 • ขาย ฿230',
            'status': '🟢 ว่าง พร้อมให้เช่า/ซื้อ',
            'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=150&q=80'
        },
        {
            'id': 102,
            'title': 'ถ้าแมวตัวนั้นหายไปจากโลกนี้',
            'author': 'เกนกิ คาวามูระ • สภาพ 95% เนี๊ยบ',
            'isbn': '978-616-79-9742-1',
            'condition': 'สภาพ 95%',
            'type_badge': '🔁 เช่ายืมอย่างเดียว',
            'price_structure': 'เช่า ฿5/วัน (฿30/สัปดาห์)<br>มัดจำ ฿150',
            'status': '🟢 ว่าง พร้อมให้เช่า/ซื้อ',
            'img': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=150&q=80'
        },
        {
            'id': 103,
            'title': 'The Kinfolk Home: Interior Spaces',
            'author': 'Nathan Williams • ปกแข็งสภาพ 98%',
            'isbn': '978-157-96-5665-2',
            'condition': 'สภาพ 98%',
            'type_badge': '🏷️ ขายอย่างเดียว',
            'price_structure': '฿1,150 <span style="text-decoration:line-through; color:#8D7B68; font-size:11px;">฿1,650</span><br>มัดจำคืนคลัง ฿300',
            'status': '🟢 ว่าง พร้อมให้เช่า/ซื้อ',
            'img': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=150&q=80'
        }
    ]

def get_book(book_id):
    for b in MOCK_BOOKS:
        if b['id'] == book_id:
            return b
    return MOCK_BOOKS[0]

# ==============================================================================
# 4. Modals (Dialogs)
# ==============================================================================
@st.dialog("🔑 เข้าสู่ระบบ / สมัครสมาชิก")
def login_dialog():
    st.write("กรุณากรอกข้อมูลเพื่อเข้าสู่ระบบ BookShare")
    u_name = st.text_input("ชื่อ-นามสกุล", value=st.session_state.user.get('name', 'คุณมีนา'))
    u_phone = st.text_input("เบอร์โทรศัพท์", value=st.session_state.user.get('phone', '081-234-5678'))
    u_addr = st.text_area("ที่อยู่จัดส่ง", value=st.session_state.user.get('address', ''))

    if st.button("ตกลง / เข้าสู่ระบบ", use_container_width=True):
        if u_name and u_phone:
            st.session_state.user['logged_in'] = True
            st.session_state.user['name'] = u_name
            st.session_state.user['phone'] = u_phone
            st.session_state.user['address'] = u_addr
            st.success(f"ยินดีต้อนรับ {u_name} เข้าสู่ระบบแล้ว!")
            st.rerun()
        else:
            st.error("กรุณากรอกชื่อและเบอร์โทรศัพท์")

@st.dialog("📖 วิธีการยืม - คืนหนังสือ")
def how_it_works_dialog():
    st.markdown(
        """
        <div style="font-size:13px; line-height:1.7;">
            <b>1. เลือกหนังสือและระยะเวลา:</b> เลือกวันเริ่มและวันคืน (สูงสุด 30 วัน) ชำระค่ายืมและมัดจำ<br>
            <b>2. จัดส่งถึงบ้าน:</b> หนังสือผ่านการทำความสะอาดและอบฆ่าเชื้อ UV พร้อมส่งมอบ<br>
            <b>3. ส่งคืนสะดวก & รับมัดจำคืนทันที:</b> ส่งคืนผ่านไปรษณีย์/ขนส่ง เมื่อผู้ให้เช่าตรวจรับ เงินมัดจำจะโอนคืนอัตโนมัติเข้า PromptPay ภายใน 24 ชม.
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# 5. Top Header Navigation (Matching Images 1, 2, 3, 4)
# ==============================================================================
c_logo, c_nav, c_rent_btn, c_buy_btn, c_user = st.columns([3.2, 3.8, 1.4, 1.4, 2.2])

with c_logo:
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:8px;">
            <span style="font-size:32px;">📚</span>
            <div>
                <span class="font-cute" style="font-size:24px; font-weight:700; color:#4A3528; line-height:1.1;">BookShare</span><br>
                <span style="font-size:11px; color:#8D7B68;">ร้านหนังสือ &amp; เช่ายืมออนไลน์</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c_nav:
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        if st.button("หน้าแรก", key="nav_h", use_container_width=True):
            st.session_state.current_view = 'home'
            st.rerun()
    with n2:
        if st.button("สำรวจหนังสือ", key="nav_e", use_container_width=True):
            st.session_state.current_view = 'home'
            st.rerun()
    with n3:
        if st.button("วิธียืม-คืน", key="nav_hw", use_container_width=True):
            how_it_works_dialog()
    with n4:
        if st.button("สำหรับผู้ขาย", key="nav_s", use_container_width=True):
            st.session_state.current_view = 'seller'
            st.session_state.seller_subview = 'add_book'
            st.rerun()

with c_rent_btn:
    st.markdown("<div class='btn-cart-rent'>", unsafe_allow_html=True)
    if st.button(f"📖 ยืม {len(st.session_state.cart_rent)}", key="btn_top_rent", use_container_width=True):
        st.session_state.current_view = 'cart'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with c_buy_btn:
    st.markdown("<div class='btn-cart-buy'>", unsafe_allow_html=True)
    if st.button(f"🛍️ ซื้อ {len(st.session_state.cart_buy)}", key="btn_top_buy", use_container_width=True):
        st.session_state.current_view = 'cart'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with c_user:
    if st.session_state.user['logged_in']:
        u_col_av, u_col_nm = st.columns([1, 2.5])
        with u_col_av:
            st.markdown(
                """
                <div style="width:36px; height:36px; border-radius:50%; background-color:#E8DDD0; display:flex; align-items:center; justify-content:center; font-weight:700; color:#4A3528; border:1px solid #D5C5B5;">
                    M
                </div>
                """,
                unsafe_allow_html=True
            )
        with u_col_nm:
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
        if st.button("🔑 เข้าสู่ระบบ", key="btn_top_login", use_container_width=True):
            login_dialog()

st.markdown("<hr style='border:0; border-top:1px solid #EADBCE; margin:8px 0 20px 0;'>", unsafe_allow_html=True)

# ==============================================================================
# 6. VIEW 1: HOME PAGE (Images 1 & 2)
# ==============================================================================
if st.session_state.current_view == 'home':
    # Search bar & Quick action
    col_srch, col_to_cart = st.columns([4, 1.2])
    with col_srch:
        st.session_state.search_query = st.text_input(
            "ค้นหา",
            value=st.session_state.search_query,
            placeholder="🔍 ค้นหาชื่อหนังสือ, ผู้แต่ง, หรือหมวดหมู่...",
            label_visibility="collapsed"
        )
    with col_to_cart:
        if st.button("👜 ไปที่ตะกร้าสินค้า", use_container_width=True):
            st.session_state.current_view = 'cart'
            st.rerun()

    # Hero Banner
    col_ht, col_hc = st.columns([1.8, 1.2])
    with col_ht:
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

    with col_hc:
        st.markdown(
            """
            <div style="background-color:#FFFFFF; border:1px solid #E8DDD0; border-radius:24px; padding:16px; box-shadow:0 6px 20px rgba(61,46,36,0.05); text-align:center;">
                <div style="position:relative; border-radius:16px; overflow:hidden; margin-bottom:12px;">
                    <img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80" style="width:100%; height:200px; object-fit:cover;">
                    <div style="position:absolute; top:10px; left:10px; background-color:rgba(255,255,255,0.92); padding:4px 10px; border-radius:999px; font-size:11px; font-weight:600; color:#2F5930;">
                        🚚 ส่งฟรีเมื่อยืม 3 เล่มขึ้นไป
                    </div>
                    <div style="position:absolute; bottom:10px; right:10px; background-color:#BC6C25; color:#FFFFFF; padding:3px 10px; border-radius:999px; font-size:11px; font-weight:600;">
                        ประหยัด 85%
                    </div>
                </div>
                <div style="background-color:#FAF5EF; border-radius:14px; padding:12px; text-align:left; border:1px solid #EADBCE; display:flex; align-items:center; gap:8px;">
                    <span style="font-size:20px;">♻️</span>
                    <div style="font-size:11px; color:#4A3528; line-height:1.4;">
                        <b>หมุนเวียนแล้ว 48,000+ ครั้ง</b><br>
                        ลดการตัดต้นไม้กว่า 960 ต้น ในชุมชนนักอ่าน BookShare
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Categories
    st.markdown("<h3 style='margin:10px 0 6px 0; font-size:20px; color:#4A3528;'>หมวดหมู่ยอดนิยม</h3>", unsafe_allow_html=True)
    cats = ["ทั้งหมด", "วรรณกรรม & นิยายแปล", "จิตวิทยา & พัฒนาตนเอง", "ธุรกิจ & การลงทุน", "หนังสือภาพ & ไลฟ์สไตล์", "วรรณกรรมคลาสสิก"]
    c_cols = st.columns(len(cats))
    for i, c in enumerate(cats):
        with c_cols[i]:
            lbl = f"✓ {c}" if st.session_state.active_category == c else c
            if st.button(lbl, key=f"cat_sel_{i}", use_container_width=True):
                st.session_state.active_category = c
                st.rerun()

    # Filter books
    f_books = []
    for b in MOCK_BOOKS:
        if st.session_state.active_category != "ทั้งหมด" and b['category'] != st.session_state.active_category:
            continue
        if st.session_state.search_query:
            q = st.session_state.search_query.lower()
            if q not in b['title'].lower() and q not in b['author'].lower() and q not in b['category'].lower():
                continue
        f_books.append(b)

    st.markdown(f"<div style='margin:16px 0 10px 0;'><b style='font-size:18px; color:#4A3528;'>หนังสือแนะนำ &amp; มาใหม่ล่าสุด ({len(f_books)} เล่ม)</b></div>", unsafe_allow_html=True)

    # 4 Columns Book Grid
    grid_cols = st.columns(4)
    for idx, book in enumerate(f_books):
        col_pos = idx % 4
        with grid_cols[col_pos]:
            if book['status'] == 'available':
                badge_html = "<span class='badge-available'>🟢 พร้อมให้ยืม</span>"
            elif book['status'] == 'rented':
                badge_html = "<span class='badge-rented'>🔴 ถูกยืมอยู่</span>"
            else:
                badge_html = "<span class='badge-sale'>🏷️ สำหรับขายเท่านั้น</span>"

            if book['status'] == 'sale_only':
                price_html = f"<div><span style='font-size:10px; color:#8D7B68; text-decoration:line-through;'>฿{book['original_price']}</span><br><b style='font-size:15px; color:#BC6C25;'>฿{book['buy_price']}</b></div>"
            elif book['status'] == 'rented':
                price_html = f"<div><span style='font-size:10px; color:#8D7B68;'>ยืม ฿{book['rent_price']}/วัน</span><br><b style='font-size:12px; color:#D9534F;'>{book.get('available_date', 'รอคืน')}</b> | <span style='font-size:11px; font-weight:600;'>฿{book['buy_price']}</span></div>"
            else:
                price_html = f"<div><span style='font-size:10px; color:#8D7B68;'>ยืมเพียง ฿{book['rent_price']}/วัน</span><br><b style='font-size:14px; color:#4A3528;'>ซื้อ ฿{book['buy_price']}</b></div>"

            st.markdown(
                f"""
                <div class="card-book">
                    <div style="position:relative;">
                        <img src="{book['img']}" class="book-cover-img" alt="{book['title']}">
                        <div style="position:absolute; top:6px; left:6px;">{badge_html}</div>
                        <div style="position:absolute; bottom:14px; right:6px;"><span class='badge-condition'>{book['condition']}</span></div>
                    </div>
                    <div style="font-size:11px; color:#8D7B68;">{book['category']}</div>
                    <h4 style="margin:2px 0 4px 0; font-size:13px; font-weight:700; color:#382B24; height:36px; overflow:hidden; line-height:1.3;">
                        {book['title']}
                    </h4>
                    <div style="font-size:11px; color:#6C5E53; margin-bottom:8px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                        {book['author']}
                    </div>
                    <div style="border-top:1px solid #EADBCE; padding-top:8px; margin-top:4px;">
                        {price_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            btn_txt = "🔍 ดูรายละเอียด & สั่งซื้อ"
            if book['status'] == 'rented':
                btn_txt = "🔍 ดูข้อมูล & จองคิว"
            elif book['status'] == 'sale_only':
                btn_txt = "🛒 ดูรายละเอียด & ซื้อ"

            if st.button(btn_txt, key=f"btn_bk_{book['id']}", use_container_width=True):
                st.session_state.selected_book_id = book['id']
                st.session_state.current_view = 'detail'
                st.rerun()

            st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)


# ==============================================================================
# 7. VIEW 2: BOOK DETAIL PAGE (Image 3)
# ==============================================================================
elif st.session_state.current_view == 'detail':
    book = get_book(st.session_state.selected_book_id)

    b1, b2 = st.columns([1.5, 8.5])
    with b1:
        if st.button("← กลับหน้าสำรวจ", key="back_home_btn"):
            st.session_state.current_view = 'home'
            st.rerun()
    with b2:
        st.markdown(f"<div style='font-size:13px; color:#8D7B68; padding-top:6px;'>หน้าแรก / หมวด{book['category']} / <b style='color:#4A3528;'>{book['title']}</b></div>", unsafe_allow_html=True)

    col_l, col_r = st.columns([4.2, 5.8], gap="large")

    with col_l:
        st.markdown(
            f"""
            <div style="position:relative; background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:20px; overflow:hidden; padding:16px; text-align:center; box-shadow:0 4px 18px rgba(61,46,36,0.04);">
                <img src="{book['img']}" style="width:100%; max-height:400px; object-fit:contain; border-radius:14px;">
                <div style="position:absolute; top:20px; left:20px; background-color:#588157; color:#FFFFFF; padding:4px 12px; border-radius:999px; font-size:12px; font-weight:600;">
                    ● {book['condition_full']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        t_cols = st.columns(3)
        for t_idx, thumb_url in enumerate(book.get('thumbnails', [book['img']])):
            if t_idx < 3:
                with t_cols[t_idx]:
                    st.image(thumb_url, use_container_width=True)

        st.markdown(
            f"""
            <div style="background-color:#FAF5EF; border:1px solid #EADBCE; border-radius:14px; padding:14px; margin-top:14px; display:flex; justify-content:space-between; align-items:center;">
                <div style="display:flex; align-items:center; gap:10px;">
                    <div style="width:38px; height:38px; border-radius:50%; background-color:#E8DDD0; display:flex; align-items:center; justify-content:center;">👤</div>
                    <div>
                        <b style="font-size:13px; color:#4A3528;">{book['seller_name']}</b><br>
                        <span style="font-size:11px; color:#BC6C25;">★ {book['seller_rating']}</span> <span style="font-size:10px; color:#8D7B68;">(ส่งต่อแล้ว {book['seller_count']} เล่ม)</span>
                    </div>
                </div>
                <span style="background-color:#FFFFFF; border:1px solid #DACABD; padding:4px 10px; border-radius:8px; font-size:11px; font-weight:600;">ดูตู้หนังสือ</span>
            </div>
            <div style="background-color:#FAF6F0; border:1px solid #EADBCE; border-radius:14px; padding:12px 16px; margin-top:10px; font-size:11px; color:#588157;">
                <b style="color:#4A3528; display:block; margin-bottom:6px;">การตรวจรับรองสภาพหนังสือโดย BookShare</b>
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:4px;">
                    <div>✔ ไม่มีรอยขีดเขียน/ไฮไลท์</div>
                    <div>✔ สันปกตรง ไม่งอ</div>
                    <div>✔ กระดาษถนอมสายตา</div>
                    <div>✔ ผ่านการอบฆ่าเชื้อ UV</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_r:
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
                <span style="background-color:#F5EFE6; color:#6B4F4F; padding:2px 8px; border-radius:999px; font-size:11px; font-weight:600;">{book['category']}</span>
                <span style="background-color:#EAF2E8; color:#2F5930; padding:2px 8px; border-radius:999px; font-size:11px; font-weight:600;">พร้อมเช่า &amp; ซื้อ</span>
                <span style="font-size:11px; color:#8D7B68; margin-left:auto;">ISBN: {book['isbn']}</span>
            </div>
            <h2 style="margin:0 0 4px 0; font-size:24px; color:#4A3528; line-height:1.2;">{book['full_title']}</h2>
            <div style="font-size:12px; color:#6C5E53; margin-bottom:10px;">{book['author']}</div>
            <p style="font-size:12px; color:#4A3528; line-height:1.6; background-color:#FAF6F0; padding:10px 14px; border-radius:12px; border:1px solid #EADBCE;">
                {book['desc']}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<b style='font-size:13px; color:#4A3528; display:block; margin:12px 0 6px 0;'>เลือกรูปแบบที่ต้องการ:</b>", unsafe_allow_html=True)

        mode_options = ['rent', 'buy'] if book['status'] != 'sale_only' else ['buy']
        mode_choice = st.radio(
            "เลือกรูปแบบ",
            options=mode_options,
            format_func=lambda x: f"📖 ยืมอ่านประหยัด (฿{book['rent_price']}/วัน + มัดจำ ฿{book['deposit']})" if x == 'rent' else f"🛍️ ซื้อขาดมือสอง (฿{book['buy_price']} จาก ฿{book['original_price']})",
            key=f"mode_choice_{book['id']}"
        )

        if mode_choice == 'rent':
            st.markdown(
                """
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:14px; padding:14px; margin-top:8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <b style="font-size:13px; color:#2F5930;">🗓️ กำหนดระยะเวลายืมหนังสือ</b>
                        <span style="background-color:#EAF2E8; color:#2F5930; padding:2px 8px; border-radius:999px; font-size:10px; font-weight:600;">สูงสุด 30 วัน</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption("เลือกด่วน:")
            q1, q2, q3, q4 = st.columns(4)
            with q1:
                if st.button("7 วัน", key="q_7", use_container_width=True):
                    st.session_state.rental_days_choice = 7
                    st.rerun()
            with q2:
                if st.button("10 วัน (แนะนำ)", key="q_10", use_container_width=True):
                    st.session_state.rental_days_choice = 10
                    st.rerun()
            with q3:
                if st.button("14 วัน", key="q_14", use_container_width=True):
                    st.session_state.rental_days_choice = 14
                    st.rerun()
            with q4:
                if st.button("21 วัน", key="q_21", use_container_width=True):
                    st.session_state.rental_days_choice = 21
                    st.rerun()

            today_val = date.today()
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                start_d = st.date_input("วันเริ่มยืม", today_val, key="dt_start")
            with col_d2:
                suggested_end = start_d + timedelta(days=st.session_state.rental_days_choice)
                end_d = st.date_input("วันกำหนดคืน", suggested_end, key="dt_end")

            calc_days = max(1, min(30, (end_d - start_d).days))
            rent_fee = calc_days * book['rent_price']
            dep_fee = book['deposit']
            round_total = rent_fee + dep_fee

            st.markdown(
                f"""
                <div style="background-color:#F5EFE6; border:1px solid #E2D4C5; border-radius:12px; padding:12px 16px; margin:12px 0; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:14px; color:#4A3528;">{calc_days} วัน × ฿{book['rent_price']}/วัน = <span style="color:#BC6C25;">฿{rent_fee}</span></b><br>
                        <span style="font-size:11px; color:#6C5E53;">+ ค่ามัดจำหนังสือ ฿{dep_fee} (ได้รับคืนอัตโนมัติเมื่อคืนหนังสือ)</span>
                    </div>
                    <div style="text-align:right;">
                        <span style="font-size:10px; color:#8D7B68;">รวมชำระรอบนี้</span><br>
                        <b style="font-size:20px; color:#4A3528;">฿{round_total}</b>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            a1, a2 = st.columns(2)
            with a1:
                if st.button("🛒 เพิ่มลงตะกร้ายืม", key="add_r_btn", use_container_width=True):
                    st.session_state.cart_rent.append({
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'rent_days': calc_days,
                        'start_date': start_d.strftime("%d/%m/%Y"),
                        'return_date': end_d.strftime("%d %b %Y"),
                        'rate_per_day': book['rent_price'],
                        'total_rent': rent_fee,
                        'deposit': dep_fee,
                        'img': book['img'],
                    })
                    st.toast(f"เพิ่ม '{book['title']}' ลงในตะกร้ายืมแล้ว!", icon="📖")
                    st.rerun()

            with a2:
                if st.button(f"📖 ยืมทันที (฿{round_total})", key="now_r_btn", use_container_width=True):
                    st.session_state.cart_rent.append({
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'rent_days': calc_days,
                        'start_date': start_d.strftime("%d/%m/%Y"),
                        'return_date': end_d.strftime("%d %b %Y"),
                        'rate_per_day': book['rent_price'],
                        'total_rent': rent_fee,
                        'deposit': dep_fee,
                        'img': book['img'],
                    })
                    st.session_state.current_view = 'cart'
                    st.rerun()

        else:
            st.markdown(
                f"""
                <div style="background-color:#FAF5EF; border:1px solid #E8DDD0; border-radius:14px; padding:16px; margin-top:8px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-size:11px; color:#BC6C25; font-weight:600;">ซื้อขาดเป็นเจ้าของถาวร</span>
                        <h3 style="margin:2px 0 0 0; color:#4A3528; font-size:22px;">฿{book['buy_price']}</h3>
                        <span style="font-size:11px; color:#8D7B68; text-decoration:line-through;">฿{book['original_price']}</span>
                        <span style="font-size:11px; color:#588157; margin-left:6px; font-weight:600;">ประหยัด ฿{book['original_price'] - book['buy_price']}</span>
                    </div>
                    <div style="text-align:right; font-size:11px; color:#6C5E53;">
                        สภาพสะสม {book['condition']}<br>เป็นเจ้าของทันที ไม่ต้องส่งคืน
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            a1, a2 = st.columns(2)
            with a1:
                if st.button("🛒 เพิ่มลงตะกร้าซื้อ", key="add_b_btn", use_container_width=True):
                    st.session_state.cart_buy.append({
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'buy_price': book['buy_price'],
                        'original_price': book['original_price'],
                        'tag': 'ซื้อขาดมือสอง จัดส่งทันที',
                        'img': book['img'],
                    })
                    st.toast(f"เพิ่ม '{book['title']}' ลงในตะกร้าซื้อแล้ว!", icon="🛍️")
                    st.rerun()

            with a2:
                if st.button(f"🛍️ ซื้อทันที (฿{book['buy_price']})", key="now_b_btn", use_container_width=True):
                    st.session_state.cart_buy.append({
                        'id': book['id'],
                        'title': book['full_title'],
                        'author': book['author'],
                        'condition': book['condition'],
                        'buy_price': book['buy_price'],
                        'original_price': book['original_price'],
                        'tag': 'ซื้อขาดมือสอง จัดส่งทันที',
                        'img': book['img'],
                    })
                    st.session_state.current_view = 'cart'
                    st.rerun()

        st.markdown(
            """
            <div style="display:flex; justify-content:space-between; margin-top:20px; padding-top:12px; border-top:1px solid #EADBCE; text-align:center; font-size:11px; color:#6C5E53;">
                <div>🚚 ส่งด่วนถึงหน้าบ้าน</div>
                <div>↩️ คืนง่ายผ่านไปรษณีย์/ขนส่ง</div>
                <div>🛡️ คุ้มครองเงินมัดจำ 100%</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# 8. VIEW 3: CART & UNIFIED CHECKOUT (Image 4)
# ==============================================================================
elif st.session_state.current_view == 'cart':
    tot_cnt = len(st.session_state.cart_rent) + len(st.session_state.cart_buy)

    ch1, ch2 = st.columns([3, 1])
    with ch1:
        st.markdown(
            """
            <div>
                <h2 style="margin:0; font-size:26px; color:#4A3528;">👜 ตะกร้าของคุณ</h2>
                <span style="font-size:12px; color:#8D7B68;">แยกสัดส่วนการชำระเงินระหว่าง หนังสือเช่ายืม และ หนังสือสั่งซื้อขาด</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    with ch2:
        st.markdown(f"<div style='text-align:right;'><span style='background-color:#E8DDD0; color:#4A3528; padding:5px 12px; border-radius:999px; font-size:12px; font-weight:600;'>{tot_cnt} รายการในตะกร้า</span></div>", unsafe_allow_html=True)

    if tot_cnt == 0:
        st.info("🛒 ตะกร้าสินค้ายังว่างเปล่า เริ่มต้นเลือกดูหนังสือเพื่อเช่ายืมหรือซื้อได้เลย!")
        if st.button("← กลับไปเลือกหนังสือ", key="btn_empty_back"):
            st.session_state.current_view = 'home'
            st.rerun()
    else:
        cart_left, cart_right = st.columns([5.8, 4.2], gap="large")

        with cart_left:
            # Section A: Rental
            st.markdown(
                f"""
                <div style="background-color:#EAF2E8; border:1px solid #C0DAC0; border-radius:14px; padding:12px 16px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:15px; color:#2F5930;">📖 A) รายการที่จะเช่ายืม (Rental Items)</b><br>
                        <span style="font-size:11px; color:#4E704E;">ยืมอ่านตามกำหนด คืนสะดวก พร้อมรับมัดจำคืน</span>
                    </div>
                    <span style="background-color:#588157; color:#FFFFFF; padding:2px 8px; border-radius:999px; font-size:11px; font-weight:600;">{len(st.session_state.cart_rent)} เล่ม</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            sum_rent_f = 0
            sum_dep_f = 0

            if not st.session_state.cart_rent:
                st.caption("ไม่มีรายการหนังสือในหมวดเช่ายืม")
            else:
                for idx, r in enumerate(st.session_state.cart_rent):
                    sum_rent_f += r['total_rent']
                    sum_dep_f += r['deposit']

                    c_i, c_tx, c_pr, c_d = st.columns([1.2, 4.2, 1.8, 0.8])
                    with c_i:
                        st.image(r['img'], width=60)
                    with c_tx:
                        st.markdown(
                            f"""
                            <b style="font-size:13px; color:#4A3528;">{r['title']}</b><br>
                            <span style="font-size:11px; color:#8D7B68;">{r['author']} • {r['condition']}</span><br>
                            <span style="font-size:10px; background-color:#FAF5EF; border:1px solid #EADBCE; padding:2px 6px; border-radius:6px; color:#6C5E53;">
                                ระยะเวลา: {r['rent_days']} วัน | กำหนดคืน: {r['return_date']}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_pr:
                        st.markdown(f"<div style='text-align:right;'><b style='font-size:15px; color:#4A3528;'>฿{r['total_rent']}</b><br><span style='font-size:10px; color:#8D7B68;'>(มัดจำ ฿{r['deposit']})</span></div>", unsafe_allow_html=True)
                    with c_d:
                        if st.button("🗑️", key=f"del_r_{idx}"):
                            st.session_state.cart_rent.pop(idx)
                            st.rerun()

                    st.markdown("<hr style='border:0; border-top:1px dashed #E8DDD0; margin:6px 0;'>", unsafe_allow_html=True)

                st.markdown(f"<div style='text-align:right; font-size:13px; padding-bottom:12px;'>รวมค่าเช่ายืมหมวด A: <b style='color:#2F5930; font-size:16px;'>฿{sum_rent_f}</b> <span style='font-size:11px; color:#8D7B68;'>(มัดจำสะสม ฿{sum_dep_f})</span></div>", unsafe_allow_html=True)

            # Section B: Purchase
            st.markdown(
                f"""
                <div style="background-color:#FAEEE1; border:1px solid #EAC8A8; border-radius:14px; padding:12px 16px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <b style="font-size:15px; color:#9C5212;">🛍️ B) รายการที่จะซื้อขาด (Purchase Items)</b><br>
                        <span style="font-size:11px; color:#854711;">หนังสือมือสองคัดเกรด เป็นเจ้าของถาวร ไม่ต้องส่งคืน</span>
                    </div>
                    <span style="background-color:#BC6C25; color:#FFFFFF; padding:2px 8px; border-radius:999px; font-size:11px; font-weight:600;">{len(st.session_state.cart_buy)} เล่ม</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            sum_buy_f = 0
            if not st.session_state.cart_buy:
                st.caption("ไม่มีรายการหนังสือในหมวดซื้อขาด")
            else:
                for idx, b in enumerate(st.session_state.cart_buy):
                    sum_buy_f += b['buy_price']

                    c_i, c_tx, c_pr, c_d = st.columns([1.2, 4.2, 1.8, 0.8])
                    with c_i:
                        st.image(b['img'], width=60)
                    with c_tx:
                        st.markdown(
                            f"""
                            <b style="font-size:13px; color:#4A3528;">{b['title']}</b><br>
                            <span style="font-size:11px; color:#8D7B68;">{b['author']} • {b['condition']}</span><br>
                            <span style="font-size:10px; background-color:#FAEEE1; color:#9C5212; padding:2px 6px; border-radius:6px;">{b.get('tag', 'ซื้อขาดมือสอง จัดส่งทันที')}</span>
                            """,
                            unsafe_allow_html=True
                        )
                    with c_pr:
                        orig = b.get('original_price', b['buy_price'])
                        st.markdown(f"<div style='text-align:right;'><b style='font-size:15px; color:#BC6C25;'>฿{b['buy_price']}</b><br><span style='font-size:10px; color:#8D7B68; text-decoration:line-through;'>฿{orig}</span></div>", unsafe_allow_html=True)
                    with c_d:
                        if st.button("🗑️", key=f"del_b_{idx}"):
                            st.session_state.cart_buy.pop(idx)
                            st.rerun()

                    st.markdown("<hr style='border:0; border-top:1px dashed #E8DDD0; margin:6px 0;'>", unsafe_allow_html=True)

                st.markdown(f"<div style='text-align:right; font-size:13px; padding-bottom:12px;'>รวมค่าซื้อขาดหมวด B: <b style='color:#BC6C25; font-size:16px;'>฿{sum_buy_f}</b></div>", unsafe_allow_html=True)

        with cart_right:
            shipping = 45 if tot_cnt > 0 else 0
            if len(st.session_state.cart_rent) >= 3:
                shipping = 0

            discount = 30 if st.session_state.promo_code.upper() == 'WELCOMEREAD' else 0
            grand_total = max(0, sum_rent_f + sum_buy_f + sum_dep_f + shipping - discount)

            st.markdown(
                f"""
                <div style="background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:20px; padding:20px; box-shadow:0 4px 18px rgba(61,46,36,0.05); margin-bottom:14px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; border-bottom:1px solid #EADBCE; padding-bottom:8px;">
                        <b style="font-size:16px; color:#4A3528;">สรุปยอดคำสั่งซื้อ</b>
                        <span style="font-size:18px;">🧾</span>
                    </div>
                    <div style="font-size:13px; color:#6C5E53; line-height:1.9;">
                        <div style="display:flex; justify-content:space-between;">
                            <span>ค่าเช่ายืมรวม ({len(st.session_state.cart_rent)} เล่ม)</span>
                            <b style="color:#4A3528;">฿{sum_rent_f}</b>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span>ค่าซื้อขาดรวม ({len(st.session_state.cart_buy)} เล่ม)</span>
                            <b style="color:#4A3528;">฿{sum_buy_f}</b>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span>ค่ามัดจำรวม ℹ️</span>
                            <b style="color:#4A3528;">฿{sum_dep_f}</b>
                        </div>
                        <div style="display:flex; justify-content:space-between;">
                            <span>ค่าบริการจัดส่งพัสดุ</span>
                            <b style="color:#4A3528;">{"ฟรี (โปรยืม 3 เล่ม)" if shipping == 0 and len(st.session_state.cart_rent) >= 3 else f"฿{shipping}"}</b>
                        </div>
                        <div style="display:flex; justify-content:space-between; color:#588157;">
                            <span>โค้ดส่วนลดนักอ่านใหม่ ({st.session_state.promo_code})</span>
                            <b>-฿{discount}</b>
                        </div>
                    </div>
                    <hr style="border:0; border-top:1px solid #EADBCE; margin:10px 0;">
                    <div style="display:flex; justify-content:space-between; align-items:baseline;">
                        <span style="font-size:15px; font-weight:700; color:#4A3528;">ยอดชำระทั้งหมด</span>
                        <span style="font-size:26px; font-weight:700; color:#4A3528;">฿{grand_total}</span>
                    </div>
                    <div style="font-size:11px; color:#8D7B68; margin-top:2px;">
                        * ยอดนี้รวมเงินมัดจำที่จะได้รับคืน ฿{sum_dep_f} เมื่อส่งคืนหนังสือครบ
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Mandatory Auth & Address Block
            st.markdown(
                """
                <div style="background-color:#FAF5EF; border:1px solid #E8DDD0; border-radius:16px; padding:16px; margin-bottom:14px;">
                    <b style="font-size:13px; color:#4A3528; display:block; margin-bottom:8px;">📦 ข้อมูลการจัดส่ง &amp; สมาชิก (ข้อมูลบังคับ)</b>
                """,
                unsafe_allow_html=True
            )

            # Check 1: Auth
            if not st.session_state.user['logged_in']:
                st.error("🚨 **ต้องล็อกอินเข้าสู่ระบบบัญชีก่อน ถึงจะสามารถสั่งซื้อได้**")
                if st.button("🔑 เข้าสู่ระบบ / ลงทะเบียน", key="btn_must_login_now", use_container_width=True):
                    login_dialog()
            else:
                st.success(f"✓ บัญชี: **{st.session_state.user['name']}** ({st.session_state.user['phone']})")

                # Check 2: Mandatory Address
                addr_val = st.text_area(
                    "ที่อยู่จัดส่งพัสดุ * (บังคับ)",
                    value=st.session_state.user.get('address', ''),
                    placeholder="บ้านเลขที่, ถนน, แขวง/ตำบล, เขต/อำเภอ, จังหวัด, รหัสไปรษณีย์...",
                    height=80
                )
                st.session_state.user['address'] = addr_val.strip()

            st.markdown("</div>", unsafe_allow_html=True)

            can_checkout = True
            if not st.session_state.user['logged_in']:
                can_checkout = False
            if not st.session_state.user.get('address') or len(st.session_state.user.get('address', '').strip()) < 10:
                can_checkout = False

            if not can_checkout:
                st.caption("⚠️ ต้องเข้าสู่ระบบและระบุที่อยู่จัดส่งให้ครบถ้วนก่อนดำเนินการชำระเงิน")
                st.button("🔒 กรุณาเข้าสู่ระบบและระบุที่อยู่เพื่อชำระเงิน", disabled=True, use_container_width=True)
            else:
                if st.button(f"ดำเนินการชำระเงิน (Checkout ฿{grand_total}) ➔", key="btn_checkout_final", use_container_width=True):
                    st.session_state.last_order = {
                        'order_id': f"BS-{date.today().strftime('%Y%m%d')}-0992",
                        'user': st.session_state.user.copy(),
                        'rent_items': st.session_state.cart_rent.copy(),
                        'buy_items': st.session_state.cart_buy.copy(),
                        'grand_total': grand_total,
                        'deposit': sum_dep_f
                    }
                    st.session_state.cart_rent = []
                    st.session_state.cart_buy = []
                    st.session_state.current_view = 'order_success'
                    st.rerun()

            st.markdown(
                f"""
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:12px; padding:10px 14px; margin-top:12px; font-size:11px; color:#2F5930;">
                    <b>🛡️ การันตีคืนมัดจำฉับไว:</b><br>
                    ระบบจะโอนเงินมัดจำ ฿{sum_dep_f} กลับเข้าบัญชีพร้อมเพย์ของคุณภายใน 24 ชม. หลังจากผู้ให้เช่าตรวจรับหนังสือ
                </div>
                <div style="background-color:#FAF5EF; border:1px solid #EADBCE; border-radius:12px; padding:10px 14px; margin-top:8px; font-size:11px; color:#4A3528;">
                    <b>🌱 การอ่านของคุณช่วยลดขยะกระดาษ!</b><br>
                    การเช่าหนังสือในคำสั่งซื้อนี้ช่วยลดการปล่อยคาร์บอน -1.4 kg สู่สิ่งแวดล้อม
                </div>
                """,
                unsafe_allow_html=True
            )


# ==============================================================================
# 9. VIEW 4: ORDER SUCCESS
# ==============================================================================
elif st.session_state.current_view == 'order_success':
    st.balloons()
    ord_info = st.session_state.last_order
    st.markdown(
        """
        <div style="text-align:center; max-width:640px; margin:0 auto; padding:30px; background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:24px; box-shadow:0 8px 24px rgba(61,46,36,0.06);">
            <span style="font-size:50px;">🎉</span>
            <h2 style="color:#4A3528; margin:8px 0;">สั่งซื้อและชำระเงินสำเร็จเรียบร้อย!</h2>
            <p style="font-size:13px; color:#6C5E53;">ขอบคุณที่ร่วมแบ่งปันการอ่านกับ BookShare ระบบกำลังจัดเตรียมส่งมอบหนังสือถึงบ้านคุณ</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if ord_info:
        c1, c2 = st.columns([1, 1], gap="medium")
        with c1:
            st.markdown(
                f"""
                <div style="background-color:#FAF5EF; border:1px solid #EADBCE; border-radius:16px; padding:16px; margin-top:14px; font-size:12px; line-height:1.8;">
                    <b>รหัสคำสั่งซื้อ:</b> {ord_info['order_id']}<br>
                    <b>ผู้รับ:</b> {ord_info['user']['name']} ({ord_info['user']['phone']})<br>
                    <b>ที่อยู่จัดส่ง:</b> {ord_info['user']['address']}<br>
                    <b>ยอดชำระสุทธิ:</b> <b style="font-size:16px; color:#BC6C25;">฿{ord_info['grand_total']}</b>
                </div>
                """,
                unsafe_allow_html=True
            )
        with c2:
            st.markdown(
                f"""
                <div style="background-color:#FAFDFC; border:1px solid #C0DAC0; border-radius:16px; padding:16px; margin-top:14px; text-align:center;">
                    <b style="font-size:13px; color:#2F5930;">สแกนชำระผ่าน PromptPay QR</b><br>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data=BookShare-{ord_info['order_id']}" style="margin:8px 0; border-radius:8px;">
                    <div style="font-size:11px; color:#588157;">ยอดรวม ฿{ord_info['grand_total']} (มัดจำคืน ฿{ord_info['deposit']})</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
    if st.button("← กลับสู่หน้าหลักเพื่อสำรวจหนังสือต่อ", key="btn_succ_home"):
        st.session_state.current_view = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# 10. VIEW 5: SELLER CENTER & ADD BOOK (Overhauled per Images 1 & 2)
# ==============================================================================
elif st.session_state.current_view == 'seller':

    # --------------------------------------------------------------------------
    # SUBVIEW A: ADD NEW BOOK FORM (Exact layout of Image 1)
    # --------------------------------------------------------------------------
    if st.session_state.seller_subview == 'add_book':
        
        # Header banner
        col_hdr_l, col_hdr_r = st.columns([8, 3])
        with col_hdr_l:
            st.markdown(
                """
                <div style="display:flex; align-items:center; gap:12px; margin-bottom:18px;">
                    <div style="background-color:#4A3528; color:#FAF5EF; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:22px;">
                        📄
                    </div>
                    <div>
                        <h2 style="margin:0; font-size:22px; color:#4A3528;">ลงทะเบียนหนังสือใหม่เข้าสู่ระบบ (Add New Book)</h2>
                        <span style="font-size:12px; color:#8D7B68;">กรอกข้อมูลให้ครบถ้วนเพื่อเพิ่มโอกาสให้นักอ่านค้นพบหนังสือและไว้วางใจในการเช่าหรือซื้อ</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_hdr_r:
            st.markdown(
                """
                <div style="text-align:right; padding-top:6px;">
                    <span style="background-color:#EAF2E8; color:#2F5930; border:1px solid #C0DAC0; padding:6px 14px; border-radius:999px; font-size:11px; font-weight:600;">
                        🛡️ มีระบบคุ้มครองประกันมัดจำ BookShare
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Main 2 Columns Form Layout (White Card Container)
        st.markdown("<div style='background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:24px; padding:24px; box-shadow:0 6px 20px rgba(61,46,36,0.04);'>", unsafe_allow_html=True)
        col_form_left, col_form_right = st.columns([4.2, 5.8], gap="large")

        # LEFT COLUMN: Photos & Condition
        with col_form_left:
            st.markdown("<b style='font-size:13px; color:#382B24;'>รูปถ่ายปกและสภาพหนังสือ * <span style='font-size:11px; color:#8D7B68; font-weight:normal;'>(อย่างน้อย 2 ภาพ)</span></b>", unsafe_allow_html=True)
            
            # Dropzone simulation
            st.markdown(
                """
                <div class="dropzone-container">
                    <div style="font-size:32px; margin-bottom:4px;">🖼️</div>
                    <b style="font-size:13px; color:#4A3528;">คลิกเพื่ออัปโหลด หรือลากวางไฟล์ที่นี่</b><br>
                    <span style="font-size:11px; color:#8D7B68;">แนะนำ: ถ่ายปกหน้า, ปกหลัง, สันหนังสือ และรอยขีดเขียน (ถ้ามี)</span><br>
                    <span style="font-size:10px; color:#A4907C; margin-top:4px; display:inline-block;">รองรับ JPG, PNG, WEBP • ไม่เกิน 10MB/รูป</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Upload preview thumbnails row
            p1, p2, p3 = st.columns(3)
            with p1:
                st.markdown(
                    """
                    <div style="position:relative; border-radius:12px; overflow:hidden; border:1px solid #EADBCE; aspect-ratio:3/4;">
                        <img src="https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit:cover;">
                        <div style="position:absolute; top:4px; left:4px; background-color:rgba(74,53,40,0.85); color:#FFFFFF; font-size:9px; padding:2px 6px; border-radius:4px; font-weight:600;">
                            รูปปกหลัก
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with p2:
                st.markdown(
                    """
                    <div style="position:relative; border-radius:12px; overflow:hidden; border:1px solid #EADBCE; aspect-ratio:3/4;">
                        <img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=300&q=80" style="width:100%; height:100%; object-fit:cover;">
                        <div style="position:absolute; top:4px; left:4px; background-color:rgba(74,53,40,0.85); color:#FFFFFF; font-size:9px; padding:2px 6px; border-radius:4px; font-weight:600;">
                            สันกระดาษ
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with p3:
                st.markdown(
                    """
                    <div style="border:1px dashed #D5C5B5; border-radius:12px; aspect-ratio:3/4; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#8D7B68; background-color:#FAF5EF; cursor:pointer;">
                        <span style="font-size:20px; font-weight:bold;">+</span>
                        <span style="font-size:11px;">เพิ่มรูป</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("<div style='margin-bottom:16px;'></div>", unsafe_allow_html=True)

            # Condition Evaluation Slider
            col_cond_t, col_cond_b = st.columns([2.5, 1.8])
            with col_cond_t:
                st.markdown("<b style='font-size:13px; color:#382B24;'>ประเมินสภาพหนังสือ (Condition) *</b>", unsafe_allow_html=True)
            with col_cond_b:
                st.markdown("<div style='text-align:right;'><span style='background-color:#EAF2E8; color:#2F5930; font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px;'>95% ดีเยี่ยม (เหมือนใหม่)</span></div>", unsafe_allow_html=True)

            condition_val = st.select_slider(
                "สภาพหนังสือ",
                options=["70% เก่าเก็บ/มีรอย", "85% ปานกลาง", "95% ดีมาก", "100% มือหนึ่ง"],
                value="95% ดีมาก",
                label_visibility="collapsed"
            )

            st.markdown("<span style='font-size:11px; color:#6C5E53;'>หมายเหตุสภาพเพิ่มเติม:</span>", unsafe_allow_html=True)
            cond_note = st.text_area(
                "หมายเหตุ",
                value="เช่น ห่อปกพลาสติกแล้ว ไม่มีรอยไฮไลท์ สันกระดาษสะอาด ไม่มีหน้าพับ...",
                height=70,
                label_visibility="collapsed"
            )

        # RIGHT COLUMN: Book Details & Pricing
        with col_form_right:
            b_title_input = st.text_input("ชื่อหนังสือ (Book Title) *", value="สุขุม ละเมียด ละไม (Wabi Sabi)")
            
            c_auth, c_isbn = st.columns([1, 1])
            with c_auth:
                b_author_input = st.text_input("ผู้แต่ง (Author) *", value="Beth Kempton")
            with c_isbn:
                b_isbn_input = st.text_input("เลข ISBN (13 หลัก)", value="978-616-04-4521-9", help="ดึงข้อมูลอัตโนมัติจากฐานข้อมูล")

            c_pub, c_cat = st.columns([1, 1])
            with c_pub:
                b_pub_input = st.text_input("สำนักพิมพ์ (Publisher)", value="BookMaker Publishing")
            with c_cat:
                b_cat_input = st.selectbox("หมวดหมู่หนังสือ *", ["พัฒนาตนเอง / จิตวิทยา", "วรรณกรรม & นิยายแปล", "ธุรกิจ & การลงทุน", "หนังสือภาพ & ไลฟ์สไตล์", "วรรณกรรมคลาสสิก"])

            st.markdown("<b style='font-size:13px; color:#382B24; display:block; margin:14px 0 6px 0;'>ประเภทการลงรายการ (Listing Option) *</b>", unsafe_allow_html=True)
            listing_mode = st.radio(
                "ประเภทการลงรายการ",
                options=["ให้เช่าอย่างเดียว", "ขายอย่างเดียว", "ได้ทั้งเช่าและขาย ★"],
                index=2,
                horizontal=True,
                label_visibility="collapsed"
            )

            # Pricing Box (Exact layout of Image 1)
            st.markdown(
                """
                <div class="pricing-box-container">
                    <b style="font-size:13px; color:#4A3528; display:flex; align-items:center; gap:6px; margin-bottom:10px;">
                        <span>💳</span> กำหนดราคาและหลักประกันความเสียหาย
                    </b>
                </div>
                """,
                unsafe_allow_html=True
            )

            p_col1, p_col2, p_col3 = st.columns(3)
            with p_col1:
                price_sale = st.number_input("ราคาขายส่งต่อ (฿)", min_value=0, value=240, step=10)
                st.caption("เทียบราคาปก ฿320 (ลด 25%)")
            with p_col2:
                price_rent = st.number_input("ค่าเช่าต่อวัน (฿/วัน)", min_value=0, value=6, step=1)
                st.caption("หรือ ฿35 / สัปดาห์")
            with p_col3:
                price_deposit = st.number_input("ค่ามัดจำประกันหนังสือ (฿)", min_value=0, value=150, step=10)
                st.caption("คืนผู้เช่าเมื่อตรวจรับเล่ม")

            st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

            # Action Buttons Row
            b_act_l, b_act_r = st.columns([1, 2])
            with b_act_l:
                if st.button("ล้างข้อมูล", key="btn_clear_form", use_container_width=True):
                    st.rerun()
            with b_act_r:
                if st.button("💾 บันทึกและขึ้นแสดงบนระบบทันที", key="btn_submit_add_book", use_container_width=True):
                    # Add new book into Meena's shelf
                    new_item = {
                        'id': len(st.session_state.meena_books) + 101,
                        'title': b_title_input,
                        'author': f"{b_author_input} • แปลภาษาไทย",
                        'isbn': b_isbn_input,
                        'condition': condition_val.split()[0],
                        'type_badge': f"● {listing_mode}",
                        'price_structure': f"เช่า ฿{price_rent}/วัน • ขาย ฿{price_sale}<br>มัดจำ ฿{price_deposit} (จากราคาปก ฿320)",
                        'status': '🟢 ว่าง พร้อมให้เช่า/ซื้อ',
                        'img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=150&q=80'
                    }
                    st.session_state.meena_books.append(new_item)
                    st.toast(f"บันทึกหนังสือ '{b_title_input}' ขึ้นร้านค้าเรียบร้อยแล้ว!", icon="🎉")
                    st.session_state.seller_subview = 'shelf'
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # SUBVIEW B: SELLER'S SHELF & INVENTORY TABLE (Exact layout of Image 2)
    # --------------------------------------------------------------------------
    elif st.session_state.seller_subview == 'shelf':
        
        # Store Profile Banner
        col_sb_l, col_sb_r = st.columns([8, 3.5])
        with col_sb_l:
            st.markdown(
                """
                <div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">
                    <img src="https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=120&q=80" style="width:58px; height:58px; border-radius:14px; object-fit:cover; border:1px solid #EADBCE;">
                    <div>
                        <div style="display:flex; align-items:center; gap:8px;">
                            <h2 style="margin:0; font-size:22px; color:#4A3528;">ร้านหนังสือของมีนา (Meena's Shelf)</h2>
                            <span style="background-color:#EAF2E8; color:#2F5930; font-size:11px; font-weight:700; padding:2px 8px; border-radius:999px;">
                                ผู้ให้เช่าระดับพรีเมียม ★ 4.9
                            </span>
                        </div>
                        <span style="font-size:12px; color:#8D7B68;">ศูนย์จัดการหนังสือ ส่งต่อความรู้ และติดตามรายการหนังสือของคุณแบบเรียลไทม์</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_sb_r:
            st.markdown("<div style='padding-top:8px;'>", unsafe_allow_html=True)
            if st.button("➕ ลงขาย/ให้เช่าหนังสือใหม่", key="btn_goto_add_book", use_container_width=True):
                st.session_state.seller_subview = 'add_book'
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        # Inventory Table Container (Note: Per user's instruction, income, currently rented, and shipping cards are omitted)
        st.markdown(
            f"""
            <div style="background-color:#FFFFFF; border:1px solid #EADBCE; border-radius:24px; padding:24px; box-shadow:0 6px 20px rgba(61,46,36,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px; border-bottom:1px solid #EADBCE; padding-bottom:14px;">
                    <div>
                        <h3 style="margin:0; font-size:18px; color:#4A3528;">จัดการสต็อกและสถานะการเช่ายืม</h3>
                        <span style="font-size:12px; color:#8D7B68;">ติดตามรายการหนังสือของคุณ และตรวจสอบความพร้อมในการให้บริการ ({len(st.session_state.meena_books)} เล่ม)</span>
                    </div>
                    <span style="background-color:#FAF5EF; border:1px solid #EADBCE; padding:5px 12px; border-radius:999px; font-size:12px; color:#4A3528; font-weight:600;">
                        หนังสือทั้งหมดในคลัง: {len(st.session_state.meena_books)} เล่ม
                    </span>
                </div>
            """,
            unsafe_allow_html=True
        )

        # Table Header Row
        th1, th2, th3, th4, th5 = st.columns([3.8, 1.8, 2.4, 2.2, 1.8])
        with th1:
            st.markdown("<b style='font-size:12px; color:#8D7B68;'>ข้อมูลหนังสือ</b>", unsafe_allow_html=True)
        with th2:
            st.markdown("<b style='font-size:12px; color:#8D7B68;'>รูปแบบรายการ</b>", unsafe_allow_html=True)
        with th3:
            st.markdown("<b style='font-size:12px; color:#8D7B68;'>โครงสร้างราคา</b>", unsafe_allow_html=True)
        with th4:
            st.markdown("<b style='font-size:12px; color:#8D7B68;'>สถานะปัจจุบัน</b>", unsafe_allow_html=True)
        with th5:
            st.markdown("<b style='font-size:12px; color:#8D7B68;'>การจัดการ</b>", unsafe_allow_html=True)

        st.markdown("<hr style='border:0; border-top:1px solid #EADBCE; margin:6px 0 14px 0;'>", unsafe_allow_html=True)

        # Render Shelf Books
        for s_idx, sb in enumerate(st.session_state.meena_books):
            r1, r2, r3, r4, r5 = st.columns([3.8, 1.8, 2.4, 2.2, 1.8])
            with r1:
                c_img, c_info = st.columns([1, 3.2])
                with c_img:
                    st.image(sb['img'], width=50)
                with c_info:
                    st.markdown(
                        f"""
                        <b style="font-size:13px; color:#4A3528;">{sb['title']}</b><br>
                        <span style="font-size:11px; color:#8D7B68;">{sb['author']}</span><br>
                        <span style="font-size:10px; color:#A4907C;">ISBN: {sb['isbn']}</span>
                        """,
                        unsafe_allow_html=True
                    )
            with r2:
                badge_bg = "#EAF2E8" if "เช่า & ขาย" in sb['type_badge'] else ("#FAEEE1" if "ขาย" in sb['type_badge'] else "#FAF5EF")
                badge_fg = "#2F5930" if "เช่า & ขาย" in sb['type_badge'] else ("#9C5212" if "ขาย" in sb['type_badge'] else "#4A3528")
                st.markdown(
                    f"""
                    <span style="background-color:{badge_bg}; color:{badge_fg}; font-size:11px; font-weight:700; padding:3px 10px; border-radius:999px;">
                        {sb['type_badge']}
                    </span>
                    """,
                    unsafe_allow_html=True
                )
            with r3:
                st.markdown(f"<div style='font-size:12px; color:#4A3528; line-height:1.5;'>{sb['price_structure']}</div>", unsafe_allow_html=True)
            with r4:
                st.markdown(f"<span style='background-color:#EAF2E8; color:#2F5930; font-size:11px; font-weight:600; padding:3px 8px; border-radius:6px;'>{sb['status']}</span>", unsafe_allow_html=True)
            with r5:
                act_c1, act_c2 = st.columns(2)
                with act_c1:
                    if st.button("✏️", key=f"edit_sb_{sb['id']}", help="แก้ไขข้อมูล"):
                        st.toast(f"แก้ไขข้อมูล {sb['title']}")
                with act_c2:
                    if st.button("🗑️", key=f"del_sb_{sb['id']}", help="ลบเล่มนี้"):
                        st.session_state.meena_books.pop(s_idx)
                        st.rerun()

            st.markdown("<hr style='border:0; border-top:1px dashed #E8DDD0; margin:10px 0;'>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:20px; text-align:center;'>", unsafe_allow_html=True)
    if st.button("← กลับสู่หน้าหลัก", key="btn_seller_back_to_home"):
        st.session_state.current_view = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 11. Footer
# ==============================================================================
st.markdown(
    """
    <div style="margin-top:60px; padding:24px 10px; border-top:1px solid #EADBCE; text-align:center; font-size:12px; color:#8D7B68;">
        <div style="font-family:'Mali', cursive; font-size:15px; font-weight:700; color:#4A3528; margin-bottom:4px;">
            BookShare - ร้านหนังสือ &amp; เช่ายืมออนไลน์
        </div>
        <div>พื้นที่ส่งต่อเรื่องราวและคุณค่าของหนังสืออย่างยั่งยืน ในชุมชนนักอ่าน</div>
    </div>
    """,
    unsafe_allow_html=True
)