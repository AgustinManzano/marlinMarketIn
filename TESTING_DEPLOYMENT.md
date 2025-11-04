# 🚀 Guía de Testing y Despliegue - Market In

## ✅ Estado Actual

Tu proyecto está correctamente configurado y funcionando localmente:

- ✅ Backend FastAPI corriendo en `http://localhost:8000`
- ✅ Frontend HTML/JS corriendo en `http://localhost:8080`
- ✅ Variables de entorno configuradas en `.env`

---

## 🧪 Testing Local

### Backend

Tu API backend está disponible en:
- **URL Base:** `http://localhost:8000`
- **Endpoint:** `POST /api/trigger-call`
- **Health Check:** `GET http://localhost:8000/`

**Probar con curl:**
```bash
curl -X POST http://localhost:8000/api/trigger-call \
  -H "Content-Type: application/json" \
  -d '{"phoneNumber": "+549112345678"}'
```

**Respuesta esperada:**
```json
{
  "success": true,
  "message": "Llamada iniciada exitosamente.",
  "call_id": "call_123xyz"
}
```

### Frontend

Tu página web está disponible en:
- **URL:** `http://localhost:8080`

**Cómo probar manualmente:**
1. Abre `http://localhost:8080` en tu navegador
2. Ingresa un número de teléfono (+54 9 11 2345 6789)
3. Haz clic en "Recibir Llamada"
4. Verás el estado de la llamada

**Nota:** Para que funcione totalmente, necesitas:
- Variables `VAPI_API_KEY` y `VAPI_ASSISTANT_ID` correctas en `.env`
- Número de teléfono válido para probar
- Asistente de VAPI ya configurado

---

## 🌐 Desplegar en Vercel

### Paso 1: Preparar Git

```bash
cd /home/agustin/Trabajo/personal/marketin
git init
git add .
git commit -m "Initial commit: Market In project"
```

### Paso 2: Crear repositorio en GitHub

1. Ve a **https://github.com/new**
2. Crea un nuevo repositorio llamado `marketin`
3. **No inicialices** con README
4. Copia el comando de remote y ejecutalo:

```bash
git remote add origin https://github.com/TU_USERNAME/marketin.git
git branch -M main
git push -u origin main
```

### Paso 3: Instalar Vercel CLI

```bash
npm install -g vercel
```

### Paso 4: Login en Vercel

```bash
vercel login
```

### Paso 5: Desplegar

```bash
vercel
```

Durante el deploy:
- Selecciona "Confirm" para desplegar
- Selecciona tu proyecto o crea uno nuevo
- El resto de opciones por defecto está bien

### Paso 6: Configurar Variables de Entorno en Vercel

1. Ve al **Dashboard de Vercel** → Tu Proyecto
2. Ve a **Settings** → **Environment Variables**
3. Añade las dos variables:
   - `VAPI_API_KEY` = tu_api_key_aqui
   - `VAPI_ASSISTANT_ID` = tu_assistant_id_aqui
4. **Redeploy** el proyecto

---

## 📱 Estructura de URLs en Producción (Vercel)

Una vez desplegado en Vercel:

- **Frontend:** `https://tu-proyecto.vercel.app/`
- **Backend API:** `https://tu-proyecto.vercel.app/api/trigger-call`

El frontend automáticamente apuntará a estas URLs relativas.

---

## 🔍 Verificar que Todo Funciona

### Test 1: Verificar Backend API

```bash
curl -X POST https://tu-proyecto.vercel.app/api/trigger-call \
  -H "Content-Type: application/json" \
  -d '{"phoneNumber": "+549112345678"}'
```

### Test 2: Verificar Frontend

Abre en navegador: `https://tu-proyecto.vercel.app/`

### Test 3: Probar Llamada Real

1. En la web, ingresa tu número telefónico
2. Haz clic en "Recibir Llamada"
3. El agente de VAPI debería llamarte en segundos

---

## 🎯 QR Code

Para generar el código QR que llevarás al stand:

1. Ve a **https://www.qr-code-generator.com/**
2. Ingresa: `https://tu-proyecto.vercel.app/`
3. Descarga el QR
4. Imprime en tamaño grande para el stand

---

## 📊 Monitoreo

### Ver Logs en Vercel

```bash
vercel logs
```

### Ver Llamadas en VAPI Dashboard

1. Ve a **https://dashboard.vapi.ai**
2. Ve a **Calls** o **Analytics**
3. Verás todas las llamadas realizadas con números, duración, etc.

---

## 🆘 Troubleshooting

### Problema: "Error al iniciar la llamada"

**Causas posibles:**
- Variables de entorno incorrectas en Vercel
- Asistente de VAPI no existe o está mal configurado
- Número de teléfono inválido

**Solución:**
1. Verifica en Vercel → Settings → Environment Variables
2. Verifica en VAPI Dashboard que el asistente existe
3. Prueba con un número válido (con código de país)

### Problema: "CORS error"

Esto ya está solucionado en el backend, pero si aparece:
1. Verifica que CORSMiddleware esté en `api/index.py`
2. Redeploya en Vercel

### Problema: Número no recibe llamada

1. Verifica que es un número real y puede recibir llamadas
2. Verifica en VAPI Dashboard → Calls que la llamada fue creada
3. Comprueba que el asistente está bien configurado

---

## 💡 Próximos Pasos Opcionales

- Agregar analytics/tracking de llamadas
- Agregar validación de formato de teléfono por país
- Crear dashboard de estadísticas
- Integrar con CRM para guardar datos de visitantes
- A/B testing de diferentes mensajes

---

**¿Alguna pregunta? Estoy aquí para ayudarte.** 🚀
