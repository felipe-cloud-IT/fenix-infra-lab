from faster_whisper import WhisperModel
from pathlib import Path
import sys


def segundos_a_srt(segundos: float) -> str:
    milisegundos = int((segundos % 1) * 1000)
    total_segundos = int(segundos)

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos_restantes = total_segundos % 60

    return f"{horas:02}:{minutos:02}:{segundos_restantes:02},{milisegundos:03}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso:")
        print('python transcribir.py "C:\\ruta\\video_o_audio.mp4"')
        return 1

    archivo = Path(sys.argv[1])

    if not archivo.exists():
        print(f"ERROR: No existe el archivo: {archivo}")
        return 1

    print(f"Archivo: {archivo.name}")
    print("Cargando modelo Whisper medium...")

    model = WhisperModel(
        "medium",
        device="cpu",
        compute_type="int8",
    )

    print("Transcribiendo...")

    segments, info = model.transcribe(
        str(archivo),
        language="es",
        vad_filter=True,
    )

    salida_txt = archivo.with_name(archivo.stem + "_medium.txt")
    salida_srt = archivo.with_name(archivo.stem + "_medium.srt")

    with open(salida_txt, "w", encoding="utf-8") as txt, open(
        salida_srt, "w", encoding="utf-8"
    ) as srt:
        for numero, segment in enumerate(segments, start=1):
            texto = segment.text.strip()

            print(f"[{segment.start:8.2f}s -> {segment.end:8.2f}s] {texto}")

            txt.write(texto + "\n")

            srt.write(f"{numero}\n")
            srt.write(
                f"{segundos_a_srt(segment.start)} --> "
                f"{segundos_a_srt(segment.end)}\n"
            )
            srt.write(texto + "\n\n")

    print()
    print("Proceso terminado.")
    print(f"Idioma detectado/configurado: {info.language}")
    print(f"TXT: {salida_txt}")
    print(f"SRT: {salida_srt}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
