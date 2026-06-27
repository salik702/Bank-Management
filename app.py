# app.py - Bank Management System with Advanced UI (No External Dependencies)
import streamlit as st
import json
import random
import string
from pathlib import Path
import pandas as pd
from datetime import datetime
import base64

# Page Configuration
st.set_page_config(
    page_title="🏦 World Bank Management System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium UI
def load_css():
    st.markdown("""
    <style>
        /* Remove default padding and margins */
        .main > div {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
        }
        
        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        
        .stApp {
            margin-top: 0px !important;
            padding-top: 0px !important;
        }
        
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            margin-bottom: 1rem;
        }
        
        .glass-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.4);
            border-color: rgba(255, 255, 255, 0.2);
        }
        
        .premium-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem 2rem;
            border-radius: 20px;
            color: white;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
            margin-bottom: 1.5rem;
        }
        
        .premium-header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }
        
        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .premium-title {
            font-size: 2.2rem;
            font-weight: 700;
            background: linear-gradient(135deg, #fff 0%, #e0e0ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            z-index: 1;
        }
        
        .premium-subtitle {
            font-size: 1rem;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }
        
        .metric-premium {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 1rem 1.2rem;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            margin-bottom: 0.5rem;
        }
        
        .metric-premium::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        }
        
        .metric-premium:hover {
            transform: scale(1.02);
            border-color: rgba(102, 126, 234, 0.5);
        }
        
        .metric-premium .label {
            color: #aaa;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .metric-premium .value {
            color: white;
            font-size: 1.8rem;
            font-weight: 700;
            margin-top: 0.3rem;
        }
        
        .metric-premium .icon {
            position: absolute;
            right: 1rem;
            top: 1rem;
            font-size: 1.8rem;
            opacity: 0.2;
        }
        
        .account-premium {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 1.5rem 2rem;
            color: white;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
            margin-bottom: 1rem;
        }
        
        .account-premium::after {
            content: '● ● ● ● ● ● ● ● ● ● ● ●';
            position: absolute;
            bottom: 0;
            right: 0;
            font-size: 1.2rem;
            opacity: 0.1;
            letter-spacing: 10px;
            transform: rotate(-10deg);
        }
        
        .account-number-display {
            font-size: 1.2rem;
            font-weight: 600;
            letter-spacing: 3px;
            background: rgba(255, 255, 255, 0.15);
            padding: 0.3rem 1.2rem;
            border-radius: 50px;
            display: inline-block;
            backdrop-filter: blur(5px);
        }
        
        .balance-display {
            font-size: 2.8rem;
            font-weight: 700;
            margin: 0.5rem 0;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            width: 100%;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(102, 126, 234, 0.5);
        }
        
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            background: rgba(255, 255, 255, 0.05);
            border: 2px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 0.6rem 1rem;
            color: white;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
            background: rgba(255, 255, 255, 0.08);
        }
        
        .stTextInput > div > div > input::placeholder {
            color: rgba(255, 255, 255, 0.4);
        }
        
        .css-1d391kg {
            background: rgba(15, 12, 41, 0.95);
            backdrop-filter: blur(10px);
        }
        
        .premium-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            margin: 1rem 0;
        }
        
        .status-badge {
            display: inline-block;
            padding: 0.2rem 0.8rem;
            border-radius: 50px;
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .status-badge.active {
            background: rgba(56, 239, 125, 0.2);
            color: #38ef7d;
            border: 1px solid rgba(56, 239, 125, 0.3);
        }
        
        ::-webkit-scrollbar {
            width: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
        }
        
        .stAlert {
            border-radius: 12px;
            border: none;
            backdrop-filter: blur(10px);
            padding: 0.8rem;
            margin-bottom: 0.5rem;
        }
        
        .stSuccess {
            background: rgba(56, 239, 125, 0.1);
            border: 1px solid rgba(56, 239, 125, 0.2);
            color: #38ef7d;
        }
        
        .stError {
            background: rgba(245, 87, 108, 0.1);
            border: 1px solid rgba(245, 87, 108, 0.2);
            color: #f5576c;
        }
        
        .stWarning {
            background: rgba(255, 193, 7, 0.1);
            border: 1px solid rgba(255, 193, 7, 0.2);
            color: #ffc107;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .css-1d391kg .css-1v3fvcr {
            padding-top: 0.5rem;
        }
        
        .premium-footer {
            text-align: center;
            padding: 0.8rem;
            color: rgba(255, 255, 255, 0.2);
            font-size: 0.8rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            margin-top: 1rem;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .fade-in-up {
            animation: fadeInUp 0.5s ease;
        }
        
        .row-widget.stColumns {
            margin-top: 0px !important;
            margin-bottom: 0px !important;
        }
        
        .element-container {
            margin-bottom: 0.3rem !important;
        }
        
        .stMetric {
            background: rgba(255,255,255,0.03);
            border-radius: 10px;
            padding: 0.5rem;
            border: 1px solid rgba(255,255,255,0.05);
        }
        
        .stMetric label {
            color: rgba(255,255,255,0.5) !important;
            font-size: 0.7rem !important;
        }
        
        .stMetric div {
            color: white !important;
            font-size: 1.2rem !important;
        }
        
        /* Sidebar menu styling */
        .sidebar-menu-item {
            padding: 0.5rem 1rem;
            margin: 0.2rem 0;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            color: rgba(255,255,255,0.7);
            font-size: 14px;
        }
        
        .sidebar-menu-item:hover {
            background: rgba(102, 126, 234, 0.1);
            color: white;
        }
        
        .sidebar-menu-item.active {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# ============================================================================
# BANK CLASS
# ============================================================================
class Bank:
    database = "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                loaded_data = json.loads(fs.read())
                if isinstance(loaded_data, list):
                    data = loaded_data
                else:
                    data = []
        else:
            with open(database, 'w') as fs:
                json.dump([], fs)
            data = []
    except Exception as err:
        print(f"⚠️ Error loading data: {err}")
        data = []

    @classmethod
    def __update(cls):
        try:
            with open(cls.database, 'w') as fs:
                json.dump(cls.data, fs, indent=4)
            return True
        except Exception as err:
            print(f"⚠️ Error saving data: {err}")
            return False

    @classmethod
    def __generate_account_number(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        account_id = alpha + num + spchar
        random.shuffle(account_id)
        return "".join(account_id)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18:
            return False, "❌ Age must be 18 or above!"
        
        if len(str(pin)) != 4:
            return False, "❌ PIN must be exactly 4 digits!"
        
        for user in cls.data:
            if user.get("email") == email:
                return False, "❌ Email already registered!"
        
        account_no = cls.__generate_account_number()
        
        new_account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": account_no,
            "balance": 0,
        }
        
        cls.data.append(new_account)
        cls.__update()
        
        return True, f"✅ Account created successfully! Your Account Number: {account_no}"

    @classmethod
    def find_user(cls, account_no, pin):
        for user in cls.data:
            if user.get("accountNo.") == account_no and user.get("pin") == pin:
                return user
        return None

    @classmethod
    def deposit_money(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        
        if not user:
            return False, "❌ Invalid account number or PIN!"
        
        if amount > 10000:
            return False, "❌ Maximum deposit is $10,000!"
        
        if amount <= 0:
            return False, "❌ Amount must be greater than 0!"
        
        user["balance"] += amount
        cls.__update()
        
        return True, f"✅ ${amount:,.2f} deposited successfully! New Balance: ${user['balance']:,.2f}"

    @classmethod
    def withdraw_money(cls, account_no, pin, amount):
        user = cls.find_user(account_no, pin)
        
        if not user:
            return False, "❌ Invalid account number or PIN!"
        
        if user["balance"] < amount:
            return False, f"❌ Insufficient balance! Current balance: ${user['balance']:,.2f}"
        
        if amount <= 0:
            return False, "❌ Amount must be greater than 0!"
        
        user["balance"] -= amount
        cls.__update()
        
        return True, f"✅ ${amount:,.2f} withdrawn successfully! New Balance: ${user['balance']:,.2f}"

    @classmethod
    def get_user_details(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        
        if not user:
            return None, "❌ Invalid account number or PIN!"
        
        return user, None

    @classmethod
    def update_details(cls, account_no, pin, name=None, email=None, new_pin=None):
        user = cls.find_user(account_no, pin)
        
        if not user:
            return False, "❌ Invalid account number or PIN!"
        
        if name:
            user["name"] = name
        if email:
            for u in cls.data:
                if u.get("email") == email and u.get("accountNo.") != account_no:
                    return False, "❌ Email already registered with another account!"
            user["email"] = email
        if new_pin:
            if len(str(new_pin)) != 4:
                return False, "❌ PIN must be exactly 4 digits!"
            user["pin"] = new_pin
        
        cls.__update()
        return True, "✅ Account details updated successfully!"

    @classmethod
    def delete_account(cls, account_no, pin):
        user = cls.find_user(account_no, pin)
        
        if not user:
            return False, "❌ Invalid account number or PIN!"
        
        cls.data.remove(user)
        cls.__update()
        
        return True, "✅ Account deleted successfully!"

    @classmethod
    def get_all_accounts(cls):
        return cls.data

    @classmethod
    def get_total_balance(cls):
        return sum(user.get("balance", 0) for user in cls.data)

    @classmethod
    def get_total_accounts(cls):
        return len(cls.data)

    @classmethod
    def get_average_balance(cls):
        if not cls.data:
            return 0
        return cls.get_total_balance() / len(cls.data)

    @classmethod
    def get_all_account_numbers(cls):
        return [user.get("accountNo.", "") for user in cls.data]


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'account_no' not in st.session_state:
    st.session_state.account_no = None
if 'pin' not in st.session_state:
    st.session_state.pin = None
if 'user_data' not in st.session_state:
    st.session_state.user_data = None
if 'debug_mode' not in st.session_state:
    st.session_state.debug_mode = False
if 'page' not in st.session_state:
    st.session_state.page = "Login"

bank = Bank()

# ============================================================================
# MAIN APP
# ============================================================================
def main():
    # Sidebar with custom navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0;">
            <div style="font-size: 3rem;">🏦</div>
            <h3 style="color: white; margin: 0.2rem 0;">World Bank</h3>
            <p style="color: rgba(255,255,255,0.4); font-size: 0.7rem;">Premium Banking</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
        
        # Navigation buttons
        if not st.session_state.logged_in:
            if st.button("🔐 Login", use_container_width=True, key="nav_login"):
                st.session_state.page = "Login"
                st.rerun()
            if st.button("📝 Create Account", use_container_width=True, key="nav_create"):
                st.session_state.page = "Create Account"
                st.rerun()
        else:
            if st.button("📊 Dashboard", use_container_width=True, key="nav_dashboard"):
                st.session_state.page = "Dashboard"
                st.rerun()
            if st.button("💰 Deposit", use_container_width=True, key="nav_deposit"):
                st.session_state.page = "Deposit"
                st.rerun()
            if st.button("💳 Withdraw", use_container_width=True, key="nav_withdraw"):
                st.session_state.page = "Withdraw"
                st.rerun()
            if st.button("👤 My Details", use_container_width=True, key="nav_details"):
                st.session_state.page = "My Details"
                st.rerun()
            if st.button("✏️ Update", use_container_width=True, key="nav_update"):
                st.session_state.page = "Update"
                st.rerun()
            if st.button("🗑️ Delete", use_container_width=True, key="nav_delete"):
                st.session_state.page = "Delete"
                st.rerun()
            if st.button("🚪 Logout", use_container_width=True, key="nav_logout"):
                st.session_state.page = "Logout"
                st.rerun()
        
        st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
        
        # Quick Stats
        st.markdown("""
        <div style="color: rgba(255,255,255,0.4); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.3rem;">
            📊 Quick Stats
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accounts", bank.get_total_accounts())
        with col2:
            st.metric("Total", f"${bank.get_total_balance():,.0f}")
        
        if st.session_state.logged_in:
            st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
            st.session_state.debug_mode = st.checkbox("🔧 Debug", value=st.session_state.debug_mode)
    
    # Main Content
    if not st.session_state.logged_in:
        if st.session_state.page == "Login":
            login_page()
        elif st.session_state.page == "Create Account":
            create_account_page()
        else:
            login_page()  # Default to login
    else:
        if st.session_state.page == "Dashboard":
            dashboard_page()
        elif st.session_state.page == "Deposit":
            deposit_page()
        elif st.session_state.page == "Withdraw":
            withdraw_page()
        elif st.session_state.page == "My Details":
            my_details_page()
        elif st.session_state.page == "Update":
            update_details_page()
        elif st.session_state.page == "Delete":
            delete_account_page()
        elif st.session_state.page == "Logout":
            logout()
        else:
            dashboard_page()  # Default to dashboard

# ============================================================================
# PAGE FUNCTIONS (Same as before - keeping them short for space)
# ============================================================================

def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="premium-header fade-in-up" style="text-align: center;">
            <h1 class="premium-title">🔐 Welcome Back</h1>
            <p class="premium-subtitle">Login to your premium account</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        account_no = st.text_input("📋 Account Number", placeholder="Enter your account number")
        pin = st.text_input("🔑 PIN", type="password", placeholder="Enter your 4-digit PIN", max_chars=4)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔐 Login", use_container_width=True):
                if account_no and pin:
                    try:
                        pin_int = int(pin)
                        user_data, error = bank.get_user_details(account_no, pin_int)
                        if user_data:
                            st.session_state.logged_in = True
                            st.session_state.account_no = account_no
                            st.session_state.pin = pin_int
                            st.session_state.user_data = user_data
                            st.session_state.page = "Dashboard"
                            st.success("✅ Login successful!")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error(error)
                            if st.session_state.debug_mode:
                                st.markdown(f"""
                                <div style="background: rgba(255,0,0,0.1); padding: 0.8rem; border-radius: 10px; margin-top: 0.5rem;">
                                    <p style="color: #ff6b6b; font-size: 0.75rem;">
                                        🔍 Debug: Account: {account_no} | PIN: {pin_int} | Users: {len(bank.data)}
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)
                    except ValueError:
                        st.error("❌ PIN must be a number!")
                else:
                    st.warning("⚠️ Please fill in all fields!")
        
        with col2:
            if st.button("🔄 Reset", use_container_width=True):
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def create_account_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="premium-header fade-in-up" style="text-align: center;">
            <h1 class="premium-title">📝 Create Account</h1>
            <p class="premium-subtitle">Join World Bank today</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        name = st.text_input("👤 Full Name", placeholder="Enter your full name")
        age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1, value=18)
        email = st.text_input("📧 Email", placeholder="Enter your email address")
        pin = st.text_input("🔑 Create PIN (4 digits)", type="password", placeholder="Enter 4-digit PIN", max_chars=4)
        confirm_pin = st.text_input("🔑 Confirm PIN", type="password", placeholder="Re-enter your PIN", max_chars=4)
        
        if st.button("🚀 Create Account", use_container_width=True):
            if name and email and pin and confirm_pin:
                if len(pin) != 4:
                    st.error("❌ PIN must be exactly 4 digits!")
                elif pin != confirm_pin:
                    st.error("❌ PINs do not match!")
                else:
                    try:
                        pin_int = int(pin)
                        success, message = bank.create_account(name, age, email, pin_int)
                        if success:
                            st.success(f"✅ {message}")
                            st.balloons()
                            st.info("📌 Please note down your account number for future logins!")
                            user_data = bank.find_user(message.split(":")[-1].strip(), pin_int)
                            if user_data:
                                st.markdown(f"""
                                <div style="background: rgba(102, 126, 234, 0.1); padding: 0.8rem; border-radius: 10px; margin-top: 0.8rem;">
                                    <p style="color: white; margin: 0; font-size: 0.9rem;">
                                        <strong>📋 Account Details:</strong><br>
                                        Name: {user_data.get('name')}<br>
                                        Account: {user_data.get('accountNo.')}
                                    </p>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.error(f"❌ {message}")
                    except ValueError:
                        st.error("❌ PIN must be a number!")
            else:
                st.warning("⚠️ Please fill in all fields!")
        
        st.markdown('</div>', unsafe_allow_html=True)

def dashboard_page():
    user_data = st.session_state.user_data
    
    st.markdown(f"""
    <div class="premium-header fade-in-up">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 class="premium-title">👋 Welcome, {user_data.get('name', 'User')}!</h1>
                <p class="premium-subtitle">Account: {user_data.get('accountNo.', 'N/A')}</p>
            </div>
            <div>
                <span class="status-badge active">● Active</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-premium fade-in-up">
            <div class="icon">💰</div>
            <div class="label">Balance</div>
            <div class="value">${user_data.get('balance', 0):,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-premium fade-in-up">
            <div class="icon">👤</div>
            <div class="label">Holder</div>
            <div class="value" style="font-size: 1.3rem;">{user_data.get('name', 'N/A')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-premium fade-in-up">
            <div class="icon">📧</div>
            <div class="label">Email</div>
            <div class="value" style="font-size: 1rem;">{user_data.get('email', 'N/A')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-premium fade-in-up">
            <div class="icon">🎂</div>
            <div class="label">Age</div>
            <div class="value">{user_data.get('age', 0)} yrs</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="account-premium fade-in-up">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="opacity: 0.7; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px;">
                    🏦 Savings Account
                </div>
                <div class="account-number-display">
                    🔑 {user_data.get('accountNo.', 'N/A')}
                </div>
            </div>
            <div style="text-align: right;">
                <div style="opacity: 0.7; font-size: 0.7rem;">Available Balance</div>
                <div class="balance-display">${user_data.get('balance', 0):,.2f}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h4 style="color: white; margin-bottom: 0.5rem;">⚡ Quick Actions</h4>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💰 Deposit", use_container_width=True):
            st.session_state.page = "Deposit"
            st.rerun()
    
    with col2:
        if st.button("💳 Withdraw", use_container_width=True):
            st.session_state.page = "Withdraw"
            st.rerun()
    
    with col3:
        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = "My Details"
            st.rerun()

def deposit_page():
    st.markdown("""
    <div class="premium-header fade-in-up">
        <h1 class="premium-title">💰 Deposit Money</h1>
        <p class="premium-subtitle">Add funds to your account</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        account_no = st.text_input("📋 Account Number", value=st.session_state.account_no, disabled=True)
        pin = st.text_input("🔑 PIN", type="password", placeholder="Enter your PIN", max_chars=4)
        amount = st.number_input("💰 Amount to Deposit", min_value=1, max_value=10000, step=100, value=100)
        
        if st.button("💳 Deposit Now", use_container_width=True):
            if pin and amount:
                try:
                    pin_int = int(pin)
                    success, message = bank.deposit_money(account_no, pin_int, amount)
                    if success:
                        st.success(f"✅ {message}")
                        user_data, _ = bank.get_user_details(account_no, pin_int)
                        if user_data:
                            st.session_state.user_data = user_data
                        st.balloons()
                    else:
                        st.error(f"❌ {message}")
                except ValueError:
                    st.error("❌ PIN must be a number!")
            else:
                st.warning("⚠️ Please enter your PIN!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card fade-in-up" style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));">
            <h4 style="color: white; margin-bottom: 0.5rem;">📌 Guidelines</h4>
            <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Minimum: $1
                </div>
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Maximum: $10,000
                </div>
                <div style="padding: 0.3rem 0;">
                    ✅ Instant processing
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def withdraw_page():
    st.markdown("""
    <div class="premium-header fade-in-up">
        <h1 class="premium-title">💳 Withdraw Money</h1>
        <p class="premium-subtitle">Withdraw funds from your account</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        account_no = st.text_input("📋 Account Number", value=st.session_state.account_no, disabled=True)
        pin = st.text_input("🔑 PIN", type="password", placeholder="Enter your PIN", max_chars=4)
        
        current_balance = st.session_state.user_data.get("balance", 0)
        st.info(f"💰 Available Balance: ${current_balance:,.2f}")
        
        amount = st.number_input(
            "💳 Amount to Withdraw",
            min_value=1,
            max_value=current_balance if current_balance > 0 else 1,
            step=100,
            value=min(100, current_balance)
        )
        
        if st.button("💳 Withdraw Now", use_container_width=True):
            if pin and amount:
                try:
                    pin_int = int(pin)
                    success, message = bank.withdraw_money(account_no, pin_int, amount)
                    if success:
                        st.success(f"✅ {message}")
                        user_data, _ = bank.get_user_details(account_no, pin_int)
                        if user_data:
                            st.session_state.user_data = user_data
                    else:
                        st.error(f"❌ {message}")
                except ValueError:
                    st.error("❌ PIN must be a number!")
            else:
                st.warning("⚠️ Please enter your PIN!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card fade-in-up" style="background: linear-gradient(135deg, rgba(245, 87, 108, 0.2), rgba(255, 107, 107, 0.2));">
            <h4 style="color: white; margin-bottom: 0.5rem;">📌 Guidelines</h4>
            <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Minimum: $1
                </div>
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Maximum: Available Balance
                </div>
                <div style="padding: 0.3rem 0;">
                    ✅ Instant processing
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def my_details_page():
    user_data = st.session_state.user_data
    
    st.markdown("""
    <div class="premium-header fade-in-up">
        <h1 class="premium-title">👤 My Details</h1>
        <p class="premium-subtitle">View your account information</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"""
        <div class="account-premium fade-in-up" style="text-align: center;">
            <div style="font-size: 4rem; margin-bottom: 0.5rem;">👤</div>
            <h3 style="color: white; margin: 0;">{user_data.get('name', 'N/A')}</h3>
            <div class="account-number-display" style="margin-top: 0.3rem; font-size: 1rem;">
                {user_data.get('accountNo.', 'N/A')}
            </div>
            <div style="margin-top: 0.5rem;">
                <span class="status-badge active">● Active</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        details = {
            "📋 Account Number": user_data.get("accountNo.", "N/A"),
            "👤 Full Name": user_data.get("name", "N/A"),
            "🎂 Age": f"{user_data.get('age', 'N/A')} years",
            "📧 Email": user_data.get("email", "N/A"),
            "💰 Balance": f"${user_data.get('balance', 0):,.2f}",
            "🔑 PIN": "****"
        }
        
        for key, value in details.items():
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.03); padding: 0.6rem 1rem; border-radius: 10px; margin-bottom: 0.4rem; border: 1px solid rgba(255,255,255,0.05);">
                <div style="color: rgba(255,255,255,0.4); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px;">
                    {key}
                </div>
                <div style="color: white; font-size: 1.1rem; font-weight: 600; margin-top: 0.2rem;">
                    {value}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def update_details_page():
    user_data = st.session_state.user_data
    
    st.markdown("""
    <div class="premium-header fade-in-up">
        <h1 class="premium-title">✏️ Update Details</h1>
        <p class="premium-subtitle">Modify your account information</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        account_no = st.text_input("📋 Account Number", value=st.session_state.account_no, disabled=True)
        current_pin = st.text_input("🔑 Current PIN", type="password", placeholder="Enter your current PIN", max_chars=4)
        
        st.markdown('<div class="premium-divider"></div>', unsafe_allow_html=True)
        st.markdown("### 📝 Update Fields")
        
        name = st.text_input("👤 Full Name", value=user_data.get("name", ""))
        email = st.text_input("📧 Email", value=user_data.get("email", ""))
        new_pin = st.text_input("🔑 New PIN (4 digits)", type="password", placeholder="Leave blank to keep current", max_chars=4)
        confirm_new_pin = st.text_input("🔑 Confirm New PIN", type="password", placeholder="Re-enter new PIN", max_chars=4)
        
        if st.button("💾 Update Details", use_container_width=True):
            if current_pin:
                try:
                    pin_int = int(current_pin)
                    updates = {}
                    
                    if name and name != user_data.get("name"):
                        updates["name"] = name
                    if email and email != user_data.get("email"):
                        updates["email"] = email
                    if new_pin:
                        if new_pin == confirm_new_pin:
                            if len(new_pin) != 4:
                                st.error("❌ PIN must be exactly 4 digits!")
                            else:
                                updates["new_pin"] = int(new_pin)
                        else:
                            st.error("❌ New PINs do not match!")
                    
                    if updates:
                        success, message = bank.update_details(
                            account_no,
                            pin_int,
                            name=updates.get("name"),
                            email=updates.get("email"),
                            new_pin=updates.get("new_pin")
                        )
                        if success:
                            st.success(f"✅ {message}")
                            user_data, _ = bank.get_user_details(account_no, pin_int)
                            if user_data:
                                st.session_state.user_data = user_data
                            st.rerun()
                        else:
                            st.error(f"❌ {message}")
                    else:
                        st.warning("⚠️ No changes to update!")
                except ValueError:
                    st.error("❌ PIN must be a number!")
            else:
                st.warning("⚠️ Please enter your current PIN!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card fade-in-up" style="background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.2));">
            <h4 style="color: white; margin-bottom: 0.5rem;">📌 What You Can Update</h4>
            <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Name
                </div>
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    ✅ Email
                </div>
                <div style="padding: 0.3rem 0;">
                    ✅ PIN
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def delete_account_page():
    st.markdown("""
    <div class="premium-header fade-in-up" style="background: linear-gradient(135deg, #f5576c 0%, #ff6b6b 100%);">
        <h1 class="premium-title">🗑️ Delete Account</h1>
        <p class="premium-subtitle">Permanently delete your account</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="glass-card fade-in-up">', unsafe_allow_html=True)
        
        st.error("⚠️ This action cannot be undone!")
        
        account_no = st.text_input("📋 Account Number", value=st.session_state.account_no, disabled=True)
        pin = st.text_input("🔑 PIN", type="password", placeholder="Enter your PIN", max_chars=4)
        confirm = st.text_input("✍️ Type 'DELETE' to confirm", placeholder="Type DELETE to confirm")
        
        if st.button("🗑️ Delete Account", use_container_width=True):
            if pin and confirm == "DELETE":
                try:
                    pin_int = int(pin)
                    success, message = bank.delete_account(account_no, pin_int)
                    if success:
                        st.success(f"✅ {message}")
                        st.session_state.logged_in = False
                        st.session_state.account_no = None
                        st.session_state.pin = None
                        st.session_state.user_data = None
                        st.session_state.page = "Login"
                        st.info("You have been logged out.")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
                except ValueError:
                    st.error("❌ PIN must be a number!")
            elif confirm != "DELETE":
                st.warning("⚠️ Please type 'DELETE' to confirm!")
            else:
                st.warning("⚠️ Please enter your PIN!")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card fade-in-up" style="background: linear-gradient(135deg, rgba(245, 87, 108, 0.2), rgba(255, 107, 107, 0.2));">
            <h4 style="color: white; margin-bottom: 0.5rem;">⚠️ Important</h4>
            <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.05);">
                    🚫 Permanent deletion
                </div>
                <div style="padding: 0.3rem 0;">
                    🚫 Data cannot be recovered
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def logout():
    st.session_state.logged_in = False
    st.session_state.account_no = None
    st.session_state.pin = None
    st.session_state.user_data = None
    st.session_state.page = "Login"
    st.success("✅ Logged out successfully!")
    st.rerun()

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="premium-footer">
    🏦 World Bank Management System v2.0 | Developed with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()