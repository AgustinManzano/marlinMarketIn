# 🚀 GUÍA RÁPIDA - Web Call (Solución Simple)

## ✅ Qué hicimos:

Cambiamos de **llamadas telefónicas** a **llamadas web en el navegador**.

### Ventajas:
- ❌ **No necesitas backend** (FastAPI ya no es necesario)
- ❌ **No necesitas número de teléfono**
- ❌ **No pagas por llamadas internacionales**
- ✅ **Solo HTML + JavaScript**
- ✅ **El visitante habla directo desde su navegador**
- ✅ **Funciona en cualquier dispositivo con micrófono**

---

## 📋 Configuración en 3 Pasos:

### **Paso 1: Obtener PUBLIC API KEY**

1. Ve a: **https://dashboard.vapi.ai/org/api-keys**
2. Busca la sección **"Public API Key"** (NO private)
3. Cópiala (será un UUID como: `5ea63f19-d1c2-4b95-90d4-bb3802aef53b`)

### **Paso 2: Configurar la Key**

Abre el archivo: `public/config.js`

Reemplaza esta línea:
```javascript
const VAPI_PUBLIC_KEY = 'TU_PUBLIC_KEY_AQUI';
```

Por:
```javascript
const VAPI_PUBLIC_KEY = 'tu_public_key_que_copiaste';
```

### **Paso 3: Probar**

1. **Inicia el servidor** (si no está corriendo):
   ```bash
   cd /home/agustin/Trabajo/personal/marketin/public
   python -m http.server 8080
   ```

2. **Abre en el navegador**:
   - http://localhost:8080

3. **Haz clic en "Hablar Ahora"**
   - Permite el micrófono
   - ¡Habla con la IA!

---

## 🎯 Cómo Funciona:

```
Visitante escanea QR
        ↓
Abre la página web
        ↓
Hace clic en "Hablar Ahora"
        ↓
Permite acceso al micrófono
        ↓
Habla directamente con la IA
        ↓
Escucha el pitch de Market In
        ↓
Cuelga cuando termina
```

---

## 📱 Para el Stand:

1. **Despliega en Vercel** (instrucciones en README.md)
2. **Genera QR** con tu URL de Vercel
3. **Imprime el QR**
4. En el stand:
   - Visitante escanea QR
   - Entra a tu página
   - Hace clic en "Hablar Ahora"
   - ¡Conversa con la IA!

---

## 🔧 Archivos Importantes:

| Archivo | Qué Hace |
|---------|----------|
| `public/index.html` | Página principal con botón de llamada |
| `public/config.js` | ⚠️ **Configuración** (pone tu PUBLIC KEY aquí) |
| `public/webcall.html` | Copia de respaldo |

---

## ❌ Lo que YA NO necesitas:

- ~~`api/index.py`~~ (backend FastAPI)
- ~~`api/requirements.txt`~~ (dependencias Python)
- ~~`.env`~~ (variables de entorno)
- ~~FastAPI corriendo~~
- ~~Números de teléfono~~
- ~~Twilio~~

**Solo necesitas:**
- ✅ `public/index.html`
- ✅ `public/config.js` con tu PUBLIC KEY
- ✅ Servidor web simple (Python HTTP Server o Vercel)

---

## 🚀 Deploy en Vercel:

```bash
# 1. Crear repo en GitHub
git init
git add public/
git commit -m "Market In - Web Call"
git remote add origin https://github.com/TU_USERNAME/marketin.git
git push -u origin main

# 2. Desplegar en Vercel
vercel

# 3. NO necesitas configurar variables de entorno
# La PUBLIC KEY va directo en config.js
```

---

## ⚠️ IMPORTANTE:

**PUBLIC KEY vs PRIVATE KEY:**

- **PUBLIC KEY** → Va en el frontend (config.js) ✅
- **PRIVATE KEY** → Solo para backend (ya no la necesitas) ❌

La PUBLIC KEY es **segura** para usar en el navegador.

---

## 🆘 Troubleshooting:

### Error: "VAPI no está inicializado"
- Verifica que la PUBLIC KEY esté en `config.js`
- Recarga la página

### Error: "Micrófono no disponible"
- El navegador te pide permiso
- Permite el acceso al micrófono

### La IA no responde
- Verifica que el Assistant ID sea correcto en `config.js`
- Verifica en VAPI Dashboard que el asistente existe

---

**¡Listo! Ahora solo necesitas configurar la PUBLIC KEY y probar.** 🎉
