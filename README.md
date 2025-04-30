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

### 🔐 Credentials file

The email credentials are loaded from a JSON file whose path is defined by the environment variable `PATH_EMAIL_CREDENTIALS`. This file should have the following structure:

```json
{
  "email_from": "your_email@example.com",
  "password": "your_password_here"
}
```

### ⚙️ Setting the environment variable

You must define the `PATH_EMAIL_CREDENTIALS` variable in your system to point to your credentials file.

#### On Linux/macOS (bash/zsh)

In your terminal:

```bash
export PATH_EMAIL_CREDENTIALS="/home/youruser/credentials/email_credentials.json"
```

To make it persistent, add that line to your `~/.bashrc` or `~/.zshrc` file and run:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

#### On Windows (PowerShell)

```powershell
$env:PATH_EMAIL_CREDENTIALS="C:\Users\youruser\credentials\email_credentials.json"
```

To make it permanent, go to:
`Control Panel → System → Advanced system settings → Environment Variables`

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👤 Author

- **Rubén López Pérez**
- Data Scientist
- lopezrbn@gmail.com
