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
> git+ssh://git@github.com/rlopez-bigdecisions/send_email.git
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

### 🔐 Credentials file

The credentials to send the email are automatically loaded from a JSON file defined by the `PATH_EMAIL_CREDENTIALS` constant in the module. This file should have the following structure:

```json
{
  "email_from": "your_email@example.com",
  "password": "your_password_here"
}
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Rubén López Pérez**
- Data Scientist
- lopezrbn@gmail.com
