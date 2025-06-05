# DjangoBlog

Modern ve özelleştirilebilir bir blog platformu. Django framework'ü kullanılarak geliştirilmiş, kullanıcı dostu arayüzü ve zengin özellikleriyle öne çıkan bir web uygulaması.

## 🚀 Özellikler

- 📝 Zengin metin editörü (CKEditor) ile blog yazıları
- 👤 Kullanıcı yönetimi ve profil sistemi
- 🤖 AI destekli chatbot entegrasyonu
- 🔍 Gelişmiş arama ve öneri sistemi
- 📧 E-posta doğrulama sistemi
- 📱 Responsive tasarım
- 🔒 Güvenli oturum yönetimi
- 📸 Medya dosyası yönetimi
- 🌐 Çoklu dil desteği (Türkçe)
- 📊 Admin paneli

## 🛠️ Teknik Altyapı

### Kullanılan Teknolojiler

- **Backend Framework:** Django 5.2.1
- **Database:** SQLite3 (Geliştirme) / PostgreSQL (Üretim)
- **Frontend:** HTML5, CSS3, JavaScript
- **Rich Text Editor:** CKEditor
- **AI Integration:** Together AI API
- **Static File Serving:** WhiteNoise
- **Email Service:** SMTP (Gmail)

### Proje Yapısı

```
DjangoBlog/
├── Django/
│   ├── DjangoBlog/          # Ana proje dizini
│   │   ├── settings.py      # Proje ayarları
│   │   ├── urls.py         # Ana URL yapılandırması
│   │   └── wsgi.py         # WSGI yapılandırması
│   ├── article/            # Blog yazıları uygulaması
│   ├── user/              # Kullanıcı yönetimi uygulaması
│   ├── chatbot/           # AI chatbot uygulaması
│   ├── templates/         # HTML şablonları
│   ├── static/           # Statik dosyalar (CSS, JS, images)
│   └── media/            # Kullanıcı yüklemeleri
```

## 🚀 Kurulum

1. **Gereksinimler**
   - Python 3.8 veya üzeri
   - pip (Python paket yöneticisi)
   - Git

2. **Projeyi Klonlama**
   ```bash
   git clone [proje-url]
   cd DjangoBlog
   ```

3. **Sanal Ortam Oluşturma ve Aktifleştirme**
   ```bash
   python -m venv venv
   # Windows için:
   venv\Scripts\activate
   # Linux/Mac için:
   source venv/bin/activate
   ```

4. **Bağımlılıkları Yükleme**
   ```bash
   pip install -r requirements.txt
   ```

5. **Çevre Değişkenlerini Ayarlama**
   `.env` dosyası oluşturun ve aşağıdaki değişkenleri ekleyin:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   TOGETHER_API_KEY=your-together-api-key
   ```

6. **Veritabanı Migrasyonları**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Süper Kullanıcı Oluşturma**
   ```bash
   python manage.py createsuperuser
   ```

8. **Statik Dosyaları Toplama**
   ```bash
   python manage.py collectstatic
   ```

9. **Sunucuyu Başlatma**
   ```bash
   python manage.py runserver
   ```

## 🔧 Geliştirme Ortamı Kurulumu

1. **IDE Önerileri**
   - Visual Studio Code
   - PyCharm
   - Sublime Text

2. **Önerilen VS Code Eklentileri**
   - Python
   - Django
   - Python Docstring Generator
   - Python Test Explorer
   - GitLens

3. **Geliştirme Araçları**
   - Git
   - Postman (API testleri için)
   - SQLite Browser (veritabanı yönetimi için)

## 📦 Ek Geliştirmeler İçin Gerekli Paketler

```bash
# Form işlemleri için
pip install django-widget-tweaks

# Zengin metin editörü için
pip install django-ckeditor

# Dosya temizleme için
pip install django-cleanup

# Statik dosya sunumu için
pip install whitenoise

# Çevre değişkenleri için
pip install python-dotenv

# AI entegrasyonu için
pip install together
```

## 🔐 Güvenlik Notları

1. **Üretim Ortamı Ayarları**
   - `DEBUG = False` yapın
   - Güvenli bir `SECRET_KEY` kullanın
   - `ALLOWED_HOSTS` listesini güncelleyin
   - SSL sertifikası kullanın
   - `CSRF_COOKIE_SECURE` ve `SESSION_COOKIE_SECURE` True yapın

2. **E-posta Güvenliği**
   - Gmail için "App Password" kullanın
   - SMTP ayarlarını güvenli bir şekilde yapılandırın

## 🤝 Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Proje Sahibi - [https://www.linkedin.com/in/erkanturgut1205](https://www.linkedin.com/in/erkanturgut1205)

Proje Linki: [https://github.com/Erkan3034/DjangoBlog](https://github.com/Erkan3034/DjangoBlog) 