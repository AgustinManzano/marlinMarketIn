from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx

# Inicializar FastAPI
app = FastAPI()

# Agregar middleware CORS para permitir todas las orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar variables de entorno
VAPI_API_KEY = os.getenv("VAPI_API_KEY", "TU_VAPI_KEY_AQUI")
VAPI_ASSISTANT_ID = os.getenv("VAPI_ASSISTANT_ID", "TU_VAPI_ASSISTANT_ID_AQUI")
VAPI_BASE_URL = "https://api.vapi.ai"


@app.post("/api/trigger-call")
async def trigger_call(request: Request):
    """
    Endpoint para disparar una llamada de VAPI a un número de teléfono.
    Espera un JSON con el campo 'phoneNumber'.
    """
    try:
        # Parsear el JSON del request
        data = await request.json()
        phone_number = data.get("phoneNumber", "").strip()

        # Validar el número de teléfono
        if not phone_number:
            return {
                "success": False,
                "message": "El número de teléfono es requerido.",
            }

        # Validar que sea un número (básica validación)
        if not phone_number.replace("+", "").replace(" ", "").replace("-", "").isdigit():
            return {
                "success": False,
                "message": "El número de teléfono no es válido.",
            }

        # Crear la llamada usando la API REST de VAPI
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{VAPI_BASE_URL}/call",
                headers={
                    "Authorization": f"Bearer {VAPI_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "phoneNumber": phone_number,
                    "assistantId": VAPI_ASSISTANT_ID,
                },
            )

            if response.status_code in [200, 201]:
                response_data = response.json()
                return {
                    "success": True,
                    "message": "Llamada iniciada exitosamente.",
                    "call_id": response_data.get("id"),
                }
            else:
                error_data = response.json()
                return {
                    "success": False,
                    "message": f"Error de VAPI: {error_data.get('message', 'Error desconocido')}",
                }

    except ValueError:
        return {
            "success": False,
            "message": "El cuerpo de la solicitud debe ser JSON válido.",
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al iniciar la llamada: {str(e)}",
        }


@app.get("/")
async def root():
    """
    Endpoint raíz que devuelve un mensaje simple.
    """
    return {"message": "Market In - API Backend"}
