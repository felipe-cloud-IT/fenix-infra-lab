# Fénix Transcriptor

Herramienta local para convertir archivos de audio o video en texto (`.txt`) y subtítulos (`.srt`) usando `faster-whisper`.

Fue creada como apoyo al estudio técnico: permite transformar videos y audios en material textual que luego puede revisarse, resumirse y contrastarse con documentación oficial.

## Requisitos

- Windows 10/11.
- Python 3.12.
- FFmpeg disponible en `PATH`.
- Entorno virtual de Python recomendado.

## Instalación

Desde PowerShell:

```powershell
mkdir C:\FenixTranscriptor
cd C:\FenixTranscriptor
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

FFmpeg puede instalarse con:

```powershell
winget install --id Gyan.FFmpeg -e
```

Verificación:

```powershell
python --version
pip --version
ffmpeg -version
```

## Uso

Con el entorno virtual activo:

```powershell
python .\transcribir.py ".\archivo.m4a"
```

También acepta archivos como `.mp4`, `.mp3`, `.wav` o `.mkv`, siempre que FFmpeg pueda leerlos.

El script usa actualmente el modelo `medium` de Whisper sobre CPU con `int8`, priorizando precisión técnica sobre velocidad.

## Salidas

Para un archivo llamado:

```text
clase-azure.m4a
```

genera:

```text
clase-azure_medium.txt
clase-azure_medium.srt
```

Los archivos se escriben en UTF-8.

Para leer correctamente el TXT desde Windows PowerShell 5.1:

```powershell
Get-Content .\clase-azure_medium.txt -Encoding UTF8
```

## Arquitectura

```text
Audio / Video
     |
     v
faster-whisper + FFmpeg
     |
     +--> TXT UTF-8
     |
     +--> SRT con marcas de tiempo
```

## Decisiones técnicas

- `faster-whisper`: motor de transcripción local.
- Modelo `medium`: mejor reconocimiento de términos técnicos que `small` en las pruebas iniciales.
- `device="cpu"`: no requiere GPU.
- `compute_type="int8"`: reduce consumo de recursos en CPU.
- `vad_filter=True`: ayuda a ignorar silencios prolongados.
- Entorno `.venv`: evita mezclar dependencias con otros proyectos Python.

## Privacidad

La transcripción se procesa localmente una vez que el modelo está disponible. No se deben subir al repositorio videos, audios, transcripciones con información sensible ni material protegido que no corresponda publicar.

El `.gitignore` excluye medios y transcripciones generadas para evitar publicarlos accidentalmente.

## Estado

Versión inicial funcional:

- [x] Audio y video como entrada.
- [x] Transcripción a TXT.
- [x] Generación de SRT.
- [x] UTF-8.
- [x] Modelo `medium` en CPU.
- [ ] Selector gráfico de archivos.
- [ ] Barra de progreso.
- [ ] Selección de modelo desde argumentos.
- [ ] Normalización opcional de terminología técnica.

## Propósito dentro de Fénix Infra Lab

Fénix Transcriptor es una herramienta auxiliar para documentación, aprendizaje y análisis de material técnico dentro del laboratorio Fénix.
