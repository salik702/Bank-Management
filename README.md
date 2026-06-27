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
  <img src="https://img.shields.io/badge/Open%20Source-Free%20to%20Use-22c55e?style=for-the-badge" />
</p>

<p>
  <a href="https://bank-management-salik.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Click%20to%20Launch-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
</p>

</div>

<br/>

## 📌 Overview

**World Bank Management System** is a full-featured banking application combining secure authentication, real-time transactions, and a modern UI. Built with Python OOP and Streamlit, it delivers a polished banking experience with PIN-based security, live balance updates, and full account management — all backed by a lightweight JSON database.

> Designed as a practical demonstration of clean OOP architecture paired with a production-style Streamlit front end — no heavy framework, no external database, fully self-contained.

<br/>

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🔐 Security
- PIN-based authentication (4-digit)
- Session-based access control
- Input validation on every transaction
- Confirmed, irreversible account deletion

</td>
<td width="50%" valign="top">

### 💰 Transactions
- Deposit funds ($1 – $10,000 per transaction)
- Withdraw with live balance validation
- Instant balance updates on the dashboard
- Transaction limits to prevent abuse

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 👤 Account Management
- Unique account number on signup
- Create / view / update / delete account
- Editable name, email, and PIN
- Persistent JSON-backed storage

</td>
<td width="50%" valign="top">

### 📊 Dashboard & UI
- Real-time balance & account metrics
- Quick-action shortcuts
- Dark glassmorphism theme
- Fully responsive layout with animations

</td>
</tr>
</table>

<br/>

## 🧱 System Architecture

```mermaid
flowchart LR
    A["User"] --> B["Login / Create Account"]
    B --> C{"PIN Valid?"}
    C -- No --> B
    C -- Yes --> D["Dashboard"]
    D --> E["Deposit"]
    D --> F["Withdraw"]
    D --> G["Update Profile"]
    D --> H["Delete Account"]
    E --> I[("data.json")]
    F --> I
    G --> I
    H --> I
```

<br/>

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

<br/>

## 📁 Project Structure

```
Bank-Management-System/
├── app.py                  # Main Streamlit application
├── Bank Management.py      # Core OOP implementation
├── data.json                # JSON database (auto-generated)
├── requirements.txt
└── README.md
```

<br/>

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

<br/>

## 📖 Usage

| Action | Steps |
|---|---|
| **Create Account** | Sidebar → fill details → save your account number → log in |
| **Deposit** | Login → Deposit → enter PIN + amount → confirm |
| **Withdraw** | Login → Withdraw → enter PIN + amount → system validates balance |
| **Update Profile** | My Details → Update → change name, email, or PIN |
| **Delete Account** | Delete Account → enter PIN → type `DELETE` to confirm |

<br/>

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

<br/>

## 🗺️ Roadmap

- [x] Account creation & PIN auth
- [x] Deposit / withdraw
- [x] Profile management & dashboard
- [ ] Transaction history
- [ ] Email notifications & PDF statements
- [ ] Interest calculation & multiple account types
- [ ] PostgreSQL migration + Docker deployment
- [ ] Two-factor authentication

<br/>

## 🤝 Contributing

Contributions are welcome — especially transaction history, encryption, and unit tests.

```bash
git checkout -b feature/your-improvement
git commit -m "feat: describe your change"
git push origin feature/your-improvement
```
Then open a pull request.

<br/>

## 📄 License

This project is **free and open source** — no license restrictions.

- ✅ Free to use, modify, and distribute
- ✅ Free for personal, academic, and commercial use
- ✅ No attribution required
- ⚠️ Provided "as-is" without warranty

---

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

## 📧 Lets Connect

<div align="center">

<h3>Built with obsession by <b>Salik Ahmad</b> 🏦</h3>

<p>
  <a href="https://salikahmad.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/Website-salikahmad.vercel.app-818CF8?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="https://www.linkedin.com/in/salik-ahmad-programmer/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Salik%20Ahmad-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="https://www.kaggle.com/salikahmad702" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-salikahmad702-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="https://github.com/SalikAhmad702" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-SalikAhmad702-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0d0d0d" />
  </a>
</p>

<br/>

<a href="https://salikahmad.vercel.app/">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&size=14&duration=4000&pause=1000&color=818CF8&center=true&vCenter=true&width=700&lines=AI%2FML+Engineer;Copyright+©+2026+Salik+Ahmad.+All+rights+reserved." alt="Footer Typing" />
</a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=shark&color=0:0f0c29,50:302b63,100:24243e&height=140&section=footer" width="100%"/>

</div>
