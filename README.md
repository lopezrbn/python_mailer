# 📧 python_mailer

A simple Python module to send emails easily.

## 🚀 Installation

You can install this package directly from GitHub using `pip`:

```bash
pip install git+https://github.com/lopezrbn/python_mailer.git
```

Alternatively, if you want to include it in your `requirements.txt` file, add the following line:

```
git+https://github.com/lopezrbn/python_mailer.git
```

> 💡 Note: If you prefer using SSH instead of HTTPS, you can use:
>
> ```
> git+ssh://git@github.com/rlopez-bigdecisions/python_mailer.git
> ```

Make sure your system has access to Git and that any authentication requirements (e.g., SSH keys) are configured appropriately.

## 📜 Usage

After installation, you can import and use the `send_email` function:

```python
from python_mailer import send_email

send_email(
    email_to="example@example.com",
    subject="Test Email",
    message="Hello, this is a test email!",
)
```

### 🔐 Providing Credentials

The function `send_email()` supports multiple methods to provide email credentials:

#### ✅ Option 1: Via environment variable (`PATH_EMAIL_CREDENTIALS`)

Define an environment variable with the path to your credentials JSON file:

```bash
export PATH_EMAIL_CREDENTIALS="/path/to/email_credentials.json"
```

Your JSON file must have the following structure:

```json
{
  "email_from": "your_email@example.com",
  "password": "your_password_here"
}
```

You can also optionally include a default recipient:

```json
{
  "email_from": "your_email@example.com",
  "password": "your_password_here",
  "email_to": "recipient@example.com"
}
```

If no `credentials` argument is passed to the function, it will automatically attempt to load the path from this variable.

#### ✅ Option 2: Pass the file path directly

```python
send_email(
    credentials="/path/to/email_credentials.json",
    subject="Hello",
    message="This is a test"
)
```

#### ✅ Option 3: Pass a dictionary

```python
send_email(
    credentials={
        "email_from": "your_email@example.com",
        "password": "your_password_here",
        "email_to": "recipient@example.com"  # Optional
    },
    subject="Hello",
    message="This is a test"
)
```

---

### 📥 Handling `email_to`

- The `email_to` parameter can be passed directly to the function.
- If it is **not provided**, and the loaded credentials dictionary includes an `"email_to"` field, that value will be used as the recipient address.
- If neither is present, the function will raise a `ValueError`.

---

## ⚠️ Security Note

Do **not** commit any credentials file to your public repositories.  
Make sure to include your credentials file (e.g. `.env`, `.json`) in `.gitignore`:

```gitignore
*.json
.env
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Rubén López Pérez**
- Data Scientist
- lopezrbn@gmail.com
