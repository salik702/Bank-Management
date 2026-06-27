<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=220&section=header&text=WORLD%20BANK&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Banking%20Management%20System%20%E2%80%A2%20Python%20OOP%20%2B%20Streamlit&descAlignY=55&descSize=18&descColor=93c5fd" width="100%"/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&duration=2600&pause=700&color=818CF8&center=true&vCenter=true&repeat=true&width=750&height=50&lines=Secure+Banking+Management+System;PIN-based+Authentication;Real-time+Transactions;Interactive+Streamlit+Dashboard" alt="Typing SVG" />
</a>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-22c55e?style=for-the-badge" />
</p>

<p>
  <a href="https://bank-management-system-salik.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Click%20to%20Launch-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
</p>

</div>

---

## 📌 Overview

**World Bank Management System** is a full-featured banking application combining secure authentication, real-time transactions, and a modern UI. Built with Python OOP and Streamlit, it delivers a polished banking experience with PIN-based security, live balance updates, and full account management — all backed by a lightweight JSON database.

---

## ✨ Features

| Category | Highlights |
|---|---|
| 🔐 **Security** | PIN-based authentication · session handling · input validation |
| 💰 **Transactions** | Deposit & withdraw ($1–$10,000) · real-time balance updates |
| 👤 **Account Management** | Create · view · update · delete account |
| 📊 **Dashboard** | Live metrics · account overview · quick actions |
| 🎨 **UI/UX** | Dark glassmorphism theme · responsive layout · smooth animations |

---

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
</p>

**OOP principles applied:** Encapsulation · Inheritance · Polymorphism · Abstraction

---

## 📁 Project Structure

```
Bank-Management-System/
├── app.py                          # Main Streamlit application
├── Bank Management.py # Core OOP implementation
├── data.json                       # JSON database (auto-generated)
└── README.md
```

---

## 🔧 Installation

```bash
git clone https://github.com/SalikAhmad702/Bank-Management-System.git
cd Bank-Management-System

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

**requirements.txt**
```
streamlit==1.28.0
plotly==5.17.0
pandas==2.0.3
streamlit-option-menu==0.3.6
Pillow==10.1.0
```

---

## 📖 Usage

**Create Account** → Sidebar → fill details → save your account number → log in
**Deposit** → Login → Deposit → enter PIN + amount → confirm
**Withdraw** → Login → Withdraw → enter PIN + amount → system validates balance
**Update Profile** → My Details → Update → change name, email, or PIN
**Delete Account** → Delete Account → enter PIN → type `DELETE` to confirm

---

## 📊 API Reference

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `create_account` | name, age, email, pin | `(bool, str)` | Creates a new account |
| `deposit_money` | account_no, pin, amount | `(bool, str)` | Deposits funds |
| `withdraw_money` | account_no, pin, amount | `(bool, str)` | Withdraws funds |
| `get_user_details` | account_no, pin | `(dict, str)` | Retrieves user info |
| `update_details` | account_no, pin, name, email, new_pin | `(bool, str)` | Updates profile |
| `delete_account` | account_no, pin | `(bool, str)` | Deletes account |

**Sample record (`data.json`)**
```json
{
  "name": "John Doe",
  "age": 25,
  "email": "john@example.com",
  "pin": 1234,
  "accountNo": "AbC12!3",
  "balance": 5000
}
```

---

## 🗺️ Roadmap

- [x] Account creation & PIN auth
- [x] Deposit / withdraw
- [x] Profile management & dashboard
- [ ] Transaction history
- [ ] Email notifications & PDF statements
- [ ] Interest calculation & multiple account types
- [ ] PostgreSQL migration + Docker deployment

---

## 🤝 Contributing

```bash
git checkout -b feature/your-improvement
git commit -m "feat: describe your change"
git push origin feature/your-improvement
```
Open a pull request — contributions like transaction history, encryption, and unit tests are especially welcome.

---

## 👨‍💻 Author

<div align="center">

**Salik Ahmad** — Python Developer | OOP & Streamlit Builder

<p>
  <a href="https://salikahmad.vercel.app/"><img src="https://img.shields.io/badge/Website-818CF8?style=for-the-badge&logo=vercel&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/salik-ahmad-programmer/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/SalikAhmad702"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.kaggle.com/salikahmad702"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" /></a>
</p>

</div>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=120&section=footer&text=Thank%20You&fontSize=36&fontColor=ffffff&animation=twinkling&fontAlignY=65" width="100%"/>
</div>
