# Market In - AI Call Stand

Aplicación web para stand de feria que integra un formulario de teléfono con llamadas de IA usando VAPI.

## 🚀 Descripción del Proyecto

Un visitante escanea un QR que lo lleva a esta página web. Ingresa su número de teléfono y automáticamente recibe una llamada de un agente de IA que:

1. Lo saluda y explica qué es Market In en 30 segundos
2. Le invita a hablar con un fundador en el stand
3. Proporciona contexto sobre "aprender haciendo"

## 📁 Estructura del Proyecto

```
marketin/
├── api/
│   ├── index.py              # Backend FastAPI
│   └── requirements.txt       # Dependencias Python
├── public/
│   ├── index.html            # Frontend HTML
│   └── app.js                # Lógica del cliente
├── vercel.json               # Configuración de Vercel
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Este archivo
```

## 🛠️ Stack Tecnológico

- **Hosting**: Vercel
- **Backend**: FastAPI (Python Serverless)
- **Frontend**: HTML5, CSS3, JavaScript Vainilla
- **AI**: VAPI

## 🔧 Instalación Local

### Requisitos

- Python 3.8+
- pip
- Node.js (para Vercel CLI, opcional)

### Pasos

1. **Clonar/Descargar el proyecto**
   ```bash
   cd marketin
   ```

2. **Instalar dependencias de Python**
   ```bash
   pip install -r api/requirements.txt
   ```

3. **Configurar variables de entorno**
   
   Crea un archivo `.env` en la raíz del proyecto:
   ```
   VAPI_API_KEY=tu_clave_api_aqui
   VAPI_ASSISTANT_ID=tu_asistente_id_aqui
   ```

4. **Ejecutar localmente con FastAPI**
   ```bash
   pip install uvicorn
   uvicorn api.index:app --reload --port 8000
   ```

5. **Servir el frontend**
   
   Abre `public/index.html` en tu navegador o usa un servidor local:
   ```bash
   python -m http.server 8080 --directory public
   ```

   Luego accede a `http://localhost:8080`

## 🚀 Desplegar en Vercel

### Pasos

1. **Instalar Vercel CLI** (si no lo tienes)
   ```bash
   npm install -g vercel
   ```

2. **Desplegar**
   ```bash
   vercel
   ```

3. **Configurar variables de entorno en Vercel Dashboard**
   - `VAPI_API_KEY`: Tu clave API de VAPI
   - `VAPI_ASSISTANT_ID`: ID de tu asistente en VAPI

4. **El proyecto estará disponible en** `https://tu-proyecto.vercel.app`

## 📱 Cómo Funciona

1. **Usuario escanea QR** → lleva a `https://tu-proyecto.vercel.app`
2. **Usuario ingresa teléfono** → envía a `/api/trigger-call`
3. **Backend valida y crea llamada** → VAPI inicia llamada automática
4. **Agente de IA ejecuta pitch** → 30 segundos de propuesta de valor
5. **Usuario invitado a hablar con fundador** → en el stand

## 🎯 Configuración de VAPI (Dashboard)

En el dashboard de VAPI, configura el asistente con:

**First Message:**
```
Hola, ¿acabás de escanear nuestro QR? Soy la IA de Market In. Te llamo porque el marketing se volvió frío y teórico... y nosotros venimos a cambiar eso.
```

**System Prompt:**
```
Eres la IA de Market In, un proyecto que transforma el aprendizaje del marketing en una experiencia viva, sensorial y social. Tu misión es hablar con alguien que escaneó un QR en nuestro stand. El problema que resolvemos es que el marketing se volvió teórico y desconectado. Nuestra solución es hacer que el marketing 'se sienta', combinando cursos con eventos sociales y networking. Tu Tono: Entusiasta y creativo. Tu Objetivo (CTA): Tienes 30 segundos. Tu objetivo principal es que la persona hable con un fundador que está físicamente en el stand. Diles: 'De hecho, la persona que ideó esto está justo frente a vos. Buscalo/a. Decile que te conté sobre "aprender haciendo". ¡Que disfrutes la experiencia!' Luego despídete y corta.
```

## 🔒 Seguridad

- Las variables de entorno se almacenan de forma segura en Vercel
- CORS está habilitado para permitir solicitudes desde el frontend
- El input de teléfono se valida en cliente y servidor
- No se almacenan datos de usuarios

## 📝 Notas de Desarrollo

- El backend está optimizado para Vercel Serverless Functions
- El archivo `api/index.py` se expone automáticamente como endpoint
- Las rutas del API se sirven bajo `/api/`
- El frontend se sirve desde `public/` como contenido estático

## 🤝 Contribuir

Para mejoras o reportes de bugs, contacta al equipo de Market In.

## 📄 Licencia

Proyecto privado de Market In.
