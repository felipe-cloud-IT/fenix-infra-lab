# Fénix Infra Lab

Laboratorio práctico y documentado de infraestructura para demostrar competencias en administración de sistemas, redes, soporte TI, seguridad y evolución hacia Microsoft Azure.

> Este repositorio utiliza una empresa, un dominio, usuarios y direcciones IP completamente ficticios. No contiene configuraciones ni información de entornos productivos.

## Objetivo

Construir un entorno reproducible que represente una pequeña organización con servicios de identidad, DNS, archivos, estaciones Windows, auditoría y respaldos. Cada laboratorio explicará el propósito, la implementación, las verificaciones y la resolución de incidentes.

## Escenario ficticio

**Fénix Servicios TI** dispone de aproximadamente 25 estaciones de trabajo y necesita centralizar:

- Identidades y autenticación.
- Resolución DNS interna.
- Usuarios, grupos y permisos por área.
- Carpetas compartidas.
- Auditoría y respaldos.
- Administración de estaciones Windows.
- Preparación para una futura arquitectura híbrida con Azure.

| Componente | Definición de laboratorio |
|---|---|
| Dominio | `fenixlab.test` |
| Red | `10.20.0.0/24` |
| Servidor principal | Debian Linux |
| Identidad local | Samba Active Directory |
| Clientes | Windows de laboratorio |
| Nube | Microsoft Azure, fase futura |

## Alcance

El proyecto se desarrollará por fases:

1. Diseño de arquitectura y convenciones seguras.
2. Implementación de Linux, Samba AD y DNS.
3. Usuarios, grupos, permisos y recursos compartidos.
4. Integración y administración de clientes Windows.
5. Auditoría, respaldos y recuperación.
6. Incidentes prácticos con diagnóstico y verificación.
7. Comparación con servicios equivalentes de Azure.
8. Diseño de una evolución hacia infraestructura híbrida.

## Estado actual

🟡 **En desarrollo — fase de diseño y documentación inicial.**

| Elemento | Estado |
|---|---|
| Repositorio y licencia | Completado |
| Escenario ficticio | Completado |
| Arquitectura inicial | En preparación |
| Laboratorios reproducibles | Pendiente |
| Evidencias y pruebas | Pendiente |
| Integración con Azure | Planificada |

Los elementos planificados no se presentan como implementados. Cada laboratorio cambiará de estado únicamente después de ejecutarlo y verificarlo.

## Estructura prevista

```text
docs/
  arquitectura/
  seguridad/
labs/
  01-linux-base/
  02-samba-ad-dns/
  03-usuarios-grupos/
  04-recursos-compartidos/
  05-clientes-windows/
  06-auditoria-respaldo/
incidentes/
scripts/
evidencias/
```

## Método de documentación

Cada práctica incluirá:

- Objetivo.
- Escenario empresarial.
- Requisitos y riesgos.
- Procedimiento explicado.
- Comandos reproducibles.
- Verificaciones.
- Problemas encontrados y solución.
- Medidas preventivas.
- Evidencia anonimizada.

## Seguridad y privacidad

- No se publican contraseñas, tokens, claves privadas ni archivos `.env`.
- No se reutilizan nombres, dominios, IP, usuarios o documentos de empresas reales.
- Las evidencias se revisan y anonimizan antes de publicarse.
- Los secretos se representarán solo mediante valores ficticios o variables de entorno.

## Tecnologías previstas

Debian Linux · Samba Active Directory · DNS · Windows · Bash · PowerShell · Git/GitHub · Microsoft Azure

## Autor

**Felipe Ruiz** — Soporte TI, redes e infraestructura, en formación continua hacia administración y arquitectura de soluciones Azure.

## Licencia

Distribuido bajo la [licencia MIT](LICENSE).
