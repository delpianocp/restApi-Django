# 🔌 REST API CRUD — Django

> API RESTful con operaciones CRUD completas construida con **Django REST Framework** · Deploy con Gunicorn/Uvicorn · Lista para producción

---

## 📌 Descripción

API backend desarrollada con Django y Django REST Framework que expone endpoints para realizar operaciones **Create, Read, Update y Delete (CRUD)**. Preparada para deployarse en plataformas como Railway o Render con soporte para PostgreSQL y archivos estáticos con WhiteNoise.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Django 5.1** | Framework web backend |
| **Django REST Framework 3.15** | Construcción de la API REST |
| **Gunicorn + Uvicorn** | Servidor ASGI/WSGI para producción |
| **WhiteNoise** | Servicio de archivos estáticos en producción |
| **PostgreSQL** | Base de datos para producción |
| **psycopg2-binary** | Conector Python para PostgreSQL |
| **dj-database-url** | Configuración de base de datos por URL |

---

## 📁 Estructura del proyecto

```
restApi-Django/
│
├── apirest/               # App principal con modelos, vistas y serializers
├── proyecto/              # Configuración de Django (settings, urls, wsgi/asgi)
│
├── manage.py              # Utilidad de línea de comandos de Django
├── build.sh               # Script de build para deploy automático
├── requirements.txt       # Dependencias del proyecto
└── .gitignore
```

---

## 🔗 Endpoints de la API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/` | Listar todos los registros |
| `POST` | `/api/` | Crear un nuevo registro |
| `GET` | `/api/<id>/` | Obtener un registro por ID |
| `PUT` | `/api/<id>/` | Actualizar un registro completo |
| `PATCH` | `/api/<id>/` | Actualizar campos parciales |
| `DELETE` | `/api/<id>/` | Eliminar un registro |

---

## 🚀 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/delpianocp/restApi-Django.git
cd restApi-Django
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### 4. Aplicar migraciones e iniciar

```bash
python manage.py migrate
python manage.py runserver
```

La API estará disponible en: `http://localhost:8000/api/`

---

## 🌐 Deploy en producción

El proyecto incluye un `build.sh` listo para plataformas como **Railway** o **Render**:

```bash
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### Variables de entorno requeridas en producción

```env
SECRET_KEY=tu_clave_secreta
DEBUG=False
DATABASE_URL=postgresql://usuario:password@host:5432/nombre_db
ALLOWED_HOSTS=tu-dominio.com
```

---

## 🧪 Probar la API

Podés probar los endpoints con **curl**, **Postman** o directamente desde el navegador usando el panel de Django REST Framework:

```bash
# Listar todos los registros
curl http://localhost:8000/api/

# Crear un nuevo registro
curl -X POST http://localhost:8000/api/ \
  -H "Content-Type: application/json" \
  -d '{"campo": "valor"}'

# Eliminar un registro
curl -X DELETE http://localhost:8000/api/1/
```

---

## 📄 Dependencias principales

```
Django==5.1.6
djangorestframework==3.15.2
gunicorn==23.0.0
uvicorn==0.34.0
whitenoise==6.9.0
psycopg2-binary==2.9.10
dj-database-url==2.3.0
```

---

## 👤 Autor

**delpianocp** — [github.com/delpianocp](https://github.com/delpianocp)
