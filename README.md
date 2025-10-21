# Website Catalog WetechX

Đây là dự án website catalog sản phẩm cho công ty WetechX, được xây dựng bằng HTML/CSS/JS và tích hợp với Django framework.

## Cấu trúc thư mục

Dưới đây là cấu trúc cây thư mục của dự án:

```
.
├── catalog_app/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── catalog_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── templates/
│   ├── 404.html
│   ├── about.html
│   ├── contact.html
│   ├── index.html
│   ├── product-detail.html
│   └── products.html
├── .gitignore
└── manage.py
```

## Hướng dẫn cài đặt và chạy dự án

1.  **Clone repository:**

    ```bash
    git clone https://github.com/wetech-thevan/Catalog_wetech.git
    cd Catalog_wetech
    ```

2.  **Tạo và kích hoạt môi trường ảo:**

    ```bash
    python -m venv venv
    # Trên Windows
    .\venv\Scripts\activate
    # Trên macOS/Linux
    source venv/bin/activate
    ```

3.  **Cài đặt các thư viện cần thiết:**

    ```bash
    pip install django
    ```

4.  **Chạy server:**

    ```bash
    python manage.py runserver
    ```

5.  Mở trình duyệt và truy cập `http://127.0.0.1:8000/`.
