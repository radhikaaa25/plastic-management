# 🍃 Plastic Waste Exchanger

A Django-based web application that gamifies plastic recycling through QR code scanning and point-based rewards system.

## 🌟 Features

- **QR Code Scanning**: Scan QR codes on plastic bottles using your device's camera
- **Gamification**: Earn points for each bottle recycled (10 points per QR scan, 1 point per manual deposit)
- **User Dashboard**: Track your recycling progress, total bottles, and points earned
- **Auto-Registration**: Seamless user onboarding with automatic account creation
- **Manual Deposit**: Fallback option for bottles without QR codes
- **Real-time Updates**: Instant feedback and statistics updates
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6 (Python)
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **QR Scanning**: HTML5-QRCode library
- **Icons**: Font Awesome
- **Authentication**: Django's built-in auth system

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd plastic_project_django
   ```

2. **Install Django**
   ```bash
   pip install django
   ```

3. **Run migrations**
   ```bash
   python3 manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python3 manage.py runserver
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000/`

## 🎯 How It Works

### User Flow
1. **Login/Register**: Users can log in with existing credentials or automatically register
2. **Dashboard**: View current points, bottles recycled, and member since date
3. **QR Scanning**: Use the QR scanner to scan bottle QR codes
4. **Points Award**: Automatically earn 10 points per valid QR code scan
5. **Manual Deposit**: Alternative option for bottles without QR codes (1 point each)

### QR Code System
- Each QR code can only be used **once** (prevents fraud)
- QR codes are **UUID-based** for security
- **Audit trail** tracks who used which code and when
- Admin can generate new QR codes for testing

## 📊 Database Models

### UserProfile
- Extends Django's User model
- Tracks coins (points) and total bottles recycled
- Automatic creation when new user registers

### QRCode
- Unique QR code identifiers
- Single-use validation
- User association and timestamp tracking

## 🔌 API Endpoints

- `GET /` - Login page
- `GET /home/` - User dashboard
- `GET /qr-scanner/` - QR code scanner interface
- `POST /api/login/` - User authentication
- `POST /api/qr-scan/` - Process QR code scans
- `GET /api/deposit/` - Manual bottle deposit
- `GET /api/stats/` - Get user statistics
- `POST /api/generate-qr/` - Generate new QR codes (admin)

## 🎨 UI/UX Features

- **Modern Design**: Clean, intuitive interface
- **Animations**: Smooth transitions and loading states
- **Mobile Responsive**: Optimized for all screen sizes
- **Real-time Feedback**: Instant updates without page refresh
- **Error Handling**: User-friendly error messages

## 🔒 Security Features

- **Django Authentication**: Built-in security
- **CSRF Protection**: Cross-site request forgery prevention
- **Input Validation**: Server-side validation for all inputs
- **Single-use QR Codes**: Prevents replay attacks
- **Session Management**: Secure user sessions

## 🚀 Deployment

### Development
```bash
python3 manage.py runserver
```

### Production Considerations
- Use PostgreSQL instead of SQLite
- Set `DEBUG = False` in settings
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for secrets
- Set up static file serving with Nginx
- Use Gunicorn or uWSGI as WSGI server

## 📝 Environment Variables

Create a `.env` file for production:
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the excellent web framework
- HTML5-QRCode library for camera integration
- Font Awesome for beautiful icons
- All contributors and users of this project

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

**Made with ♻️ for a greener planet!**
