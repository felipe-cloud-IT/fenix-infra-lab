# Laboratorio 01 — Preparación del servidor Debian base

## Estado

🟡 **Documentado y pendiente de ejecución.**

Este estado solo cambiará a **verificado** después de ejecutar el procedimiento y registrar evidencias anonimizadas.

## Objetivo

Preparar una máquina virtual Debian 13 estable y segura que servirá como base para `DC01`, el futuro controlador de dominio Samba Active Directory del entorno ficticio Fénix Lab.

## Escenario empresarial

Fénix Servicios TI necesita un servidor base con nombre, red, hora y actualizaciones controladas antes de instalar servicios de identidad. La preparación se documenta por separado para facilitar el diagnóstico y evitar atribuir a Samba errores provenientes del sistema operativo o de la red.

## Alcance y límites

Este laboratorio:

- Se ejecuta en una **máquina virtual exclusiva de pruebas**.
- No instala todavía Samba AD.
- No modifica equipos ni servidores productivos.
- Utiliza únicamente el dominio reservado `fenixlab.test` y la red ficticia `10.20.0.0/24`.
- No publica contraseñas, direcciones MAC, IP públicas, nombres de redes Wi-Fi ni identificadores reales.

## Requisitos

| Recurso | Valor de laboratorio |
|---|---|
| Sistema | Debian 13 de 64 bits |
| CPU | 2 vCPU |
| Memoria | 2 GB mínimo; 4 GB recomendado |
| Disco | 25 GB mínimo |
| Hostname | `dc01` |
| FQDN previsto | `dc01.fenixlab.test` |
| IP estática prevista | `10.20.0.10/24` |
| Puerta de enlace | `10.20.0.1` |
| DNS temporal | DNS del laboratorio durante la preparación |
| Adaptador | Red interna o segmento virtual aislado |

> La IP y la puerta de enlace deben existir dentro de la red virtual del laboratorio. No las configures en la red doméstica o empresarial sin comprobar antes que no haya conflictos.

## Riesgos y precauciones

- Un cambio de red incorrecto puede cortar la conexión SSH.
- Renombrar un host que ya presta servicios puede afectar DNS y autenticación.
- Las actualizaciones pueden requerir reinicio.
- La salida de algunos comandos puede mostrar hostname, IP, MAC, usuario o repositorios configurados.

Antes de publicar evidencias, oculta:

- Direcciones MAC.
- IP públicas.
- Nombres de usuario personales.
- SSID y datos de redes reales.
- Tokens, claves, contraseñas y rutas privadas.

## Procedimiento

### 1. Confirmar que estamos en la VM correcta

```bash
hostnamectl
cat /etc/os-release
ip -brief address
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

**Verificación esperada:** Debian 13, discos de la VM y una interfaz perteneciente al segmento de laboratorio.

**Detención segura:** si aparecen discos, hostnames o redes de un entorno productivo, no continúes.

### 2. Actualizar el sistema

```bash
sudo apt update
apt list --upgradable
sudo apt full-upgrade
```

Revisa la lista antes de confirmar. Si se actualiza el kernel o componentes base:

```bash
sudo reboot
```

Después del reinicio:

```bash
uname -r
systemctl --failed
```

### 3. Instalar utilidades de diagnóstico

```bash
sudo apt install curl dnsutils jq lsof net-tools rsync sudo vim
```

Estas herramientas permitirán revisar DNS, puertos, registros y respaldos en laboratorios posteriores.

### 4. Configurar el nombre del servidor

```bash
sudo hostnamectl set-hostname dc01
hostnamectl
hostname --fqdn
```

Durante esta fase, `hostname --fqdn` podría no devolver todavía `dc01.fenixlab.test`; la resolución definitiva se validará cuando configuremos DNS y Samba AD.

### 5. Identificar el método de administración de red

```bash
systemctl is-active NetworkManager
systemctl is-active systemd-networkd
ip -brief link
ip route
```

No mezcles NetworkManager, `systemd-networkd` y `/etc/network/interfaces`. El procedimiento de IP estática se elegirá según el servicio activo y se documentará con el nombre real de la interfaz de la VM.

### 6. Verificar hora y zona horaria

```bash
timedatectl
systemctl status systemd-timesyncd --no-pager
```

La sincronización horaria es esencial para Kerberos. El resultado esperado es reloj sincronizado y servicio NTP activo.

### 7. Revisar el estado base

```bash
hostnamectl
ip -brief address
ip route
resolvectl status
timedatectl
df -h
free -h
systemctl --failed
ss -tulpn
```

## Criterios de aprobación

El laboratorio se considerará verificado cuando:

- Debian 13 esté actualizado.
- El hostname sea `dc01`.
- No existan unidades fallidas relevantes.
- La hora esté sincronizada.
- La interfaz y el plan de IP estén identificados.
- Exista conectividad dentro del segmento aislado.
- Las evidencias hayan sido revisadas y anonimizadas.

## Evidencias permitidas

Guardar solo evidencia técnica necesaria:

1. Versión de Debian.
2. Hostname ficticio `dc01`.
3. Estado de sincronización horaria.
4. IP privada ficticia del laboratorio.
5. Ausencia de servicios fallidos relevantes.

No subir archivos completos de `/etc`, historiales de shell ni capturas sin revisar.

## Resultado esperado

Una VM Debian preparada para el siguiente laboratorio: configuración definitiva de red, DNS y provisión de Samba Active Directory.

## Registro de ejecución

| Campo | Valor |
|---|---|
| Fecha de ejecución | Pendiente |
| Entorno | VM de laboratorio |
| Resultado | Pendiente |
| Incidentes encontrados | Pendiente |
| Evidencia anonimizada | Pendiente |
| Responsable | Felipe Ruiz |
