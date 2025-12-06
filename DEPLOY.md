# 🚀 Codenthia Blog - Deployment Rehberi


---

##  Ön Gereksinimler

- GitHub hesabı
- Render.com hesabı (ücretsiz)
- Proje GitHub'a push edilmiş olmalı

---

## 🔧 Adım 1: GitHub'a Push

```bash
git add .
git commit -m "Production ready - PostgreSQL"
git push origin main
```

---

##  Adım 2: Render.com'a Kayıt

1. https://render.com adresine git
2. **GitHub ile kayıt ol** veya giriş yap

---

##  Adım 3: PostgreSQL Veritabanı Oluştur

1. Dashboard'da **New +** → **PostgreSQL** tıkla
2. Ayarları doldur:

| Ayar | Değer |
|------|-------|
| **Name** | `codenthia-db` |
| **Database** | `codenthia` |
| **User** | (otomatik) |
| **Region** | Frankfurt (EU) |
| **Plan** | **Free** |

3. **Create Database** butonuna tıkla
4.  1-2 dakika bekle (veritabanı oluşturulacak)

### Veritabanı URL'ini Kopyala

Veritabanı oluştuktan sonra:
1. Veritabanına tıkla
2. **Connections** bölümüne git
3. **Internal Database URL** değerini kopyala

Bu URL şuna benzer:
```
postgres://codenthia_user:abc123xyz@dpg-xxx.frankfurt-postgres.render.com/codenthia
```

>  Bu URL'i bir yere kaydet, Adım 5'te lazım olacak

---

##  Adım 4: Web Service Oluştur

1. Dashboard'da **New +** → **Web Service** tıkla
2. **Build and deploy from a Git repository** seç
3. GitHub repo'nu bağla: `codenthia_blog`
4. Ayarları doldur:

| Ayar | Değer |
|------|-------|
| **Name** | `codenthia-blog` |
| **Region** | Frankfurt (EU) |
| **Branch** | `main` |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| **Start Command** | `gunicorn DjangoBlog.wsgi:application` |
| **Plan** | Free |

---

##  Adım 5: Environment Variables

**"Environment"** sekmesinde şu değişkenleri ekle:

### Zorunlu Değişkenler

| Key | Value | Açıklama |
|-----|-------|----------|
| `SECRET_KEY` | `django-secret-key-buraya-cok-uzun-ve-random-bir-deger-yaz-12345!@#$%` | Güvenli, uzun, rastgele |
| `DEBUG` | `False` | Production'da her zaman False |
| `DATABASE_URL` | `postgres://...` (Adım 3'te kopyaladığın) | PostgreSQL bağlantısı |
| `ALLOWED_HOSTS` | `.onrender.com` | İzin verilen domain'ler |
| `CSRF_TRUSTED_ORIGINS` | `https://codenthia-blog.onrender.com` | CSRF güvenliği |
| `PYTHON_VERSION` | `3.12.0` | Python versiyonu |

### Opsiyonel Değişkenler (Email)

| Key | Value |
|-----|-------|
| `EMAIL_HOST` | `smtp.gmail.com` |
| `EMAIL_PORT` | `587` |
| `EMAIL_HOST_USER` | `your-email@gmail.com` |
| `EMAIL_HOST_PASSWORD` | `your-gmail-app-password` |

>  Gmail App Password almak için: Google Hesabı → Güvenlik → 2 Adımlı Doğrulama → Uygulama Şifreleri

### Opsiyonel Değişkenler (Chatbot)

| Key | Value |
|-----|-------|
| `TOGETHER_API_KEY` | `your-together-api-key` |

---

##  Adım 6: Deploy

1. Tüm ayarları kontrol et
2. **Create Web Service** butonuna tıkla
3. ⏳ 5-10 dakika bekle (ilk deploy uzun sürer)
4. Logları takip et - "Your service is live" mesajını bekle

---

##  Adım 7: Veritabanı Migration

Deploy tamamlandıktan sonra:

1. Render Dashboard'da Web Service'e git
2. **Shell** sekmesine tıkla
3. Şu komutları çalıştır:

```bash
# Tabloları oluştur
python manage.py migrate

# Admin kullanıcısı oluştur
python manage.py createsuperuser
```

Superuser bilgilerini gir:
- Username: `admin`
- Email: `your-email@example.com`
- Password: (güçlü bir şifre)

---

##  Adım 8: Test Et

### Site URL'leri

| Sayfa | URL |
|-------|-----|
| **Ana Sayfa** | https://codenthia-blog.onrender.com |
| **Admin Panel** | https://codenthia-blog.onrender.com/admin |

### Kontrol Listesi

- [ ] Ana sayfa açılıyor mu?
- [ ] Admin paneline giriş yapılabiliyor mu?
- [ ] Makale eklenebiliyor mu?
- [ ] Resim yüklenebiliyor mu?
- [ ] Kayıt/Giriş çalışıyor mu?

---

## 🔧 Sorun Giderme

### Hata: "Application Error"

1. Render Dashboard → Logs sekmesini kontrol et
2. Hata mesajını oku
3. Environment variables'ı kontrol et

### Hata: "Database connection failed"

1. `DATABASE_URL` değerini kontrol et
2. PostgreSQL veritabanının çalıştığından emin ol
3. Internal URL kullandığından emin ol

### Hata: "Static files not found"

```bash
# Shell'de çalıştır
python manage.py collectstatic --noinput
```

### Hata: "CSRF verification failed"

1. `CSRF_TRUSTED_ORIGINS` değerini kontrol et
2. URL'in `https://` ile başladığından emin ol

---

##  Ücretsiz Plan Limitleri

Render.com Free Plan:
- **Web Service:** Aylık 750 saat (yeterli)
- **PostgreSQL:** 90 gün sonra silinir (yeniden oluşturulabilir)
- **Bandwidth:** 100 GB/ay
- **Sleep:** 15 dakika inaktiviteden sonra uyku moduna geçer

>  İpucu: Uyku modundan çıkış ilk istekte 30-60 saniye sürebilir.

---

##  Güncelleme Yapma

Kod değişikliklerini yayınlamak için:

```bash
git add .
git commit -m "Update description"
git push origin main
```

Render otomatik olarak yeni deploy başlatacak.

---

##  Önemli Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `requirements.txt` | Python bağımlılıkları |
| `Procfile` | Gunicorn başlatma komutu |
| `runtime.txt` | Python versiyonu |
| `render.yaml` | Render Blueprint (opsiyonel) |

---

##  Faydalı Linkler

- [Render.com Docs](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [PostgreSQL on Render](https://render.com/docs/databases)

---


*Son güncelleme: Aralık 2025*

