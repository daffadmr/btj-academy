# Daffa Damar Ardhika

### [Ansible Task 1](https://github.com/daffadmr/btj-academy/tree/main/ansible_task1)
### [Ansible Task 2](https://github.com/daffadmr/btj-academy/tree/main/ansible_task2)

## Simple Task - Development Environment - 27 November 2023

1. Buatlah image dari aplikasi sederhana yang sudah dibuat
2. Jalankan image tersebut sebagai container dan berjalan pada port 8081
3. Berapakah IP docker container **whoami**?
4. Apa isi dari file yang tersembunyi dari docker container **whoami**? Clue: Volume Mounting
5. Image apa yang digunakan pada docker container **whoami**?

## Jawaban Nomor 1
### Clone repository yang telah dikerjakan sebelumnya
```bash
git clone https://github.com/daffadmr/btj-academy.git
```
### Masuk ke direktori repo yang telah di-clone
```bash
cd btj-academy
```
### Buat Dockerfile dengan VIM pada VM
```bash
touch Dockerfile
vim Dockerfile
```
Lalu isi dengan:
```Dockerfile
FROM python:latest

WORKDIR /app

COPY . .

CMD ["python", "todo_list.py"]
```

### Build Dockerfile
```bash
docker build -t todo-list-app:v1.0 .
```

## Jawaban Nomor 2
### Jalankan images sebagai container pada port 8081
```bash
docker run -it -p 8081:8081 --name todo-list-daffa todo-list-app:v1.0
```    
### Cek apakah container sudah berjalan
```bash
docker ps
```
## Jawaban Nomor 3
### Melihat IP yang digunakan whoami
```bash
docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" whoami
```
### Output
```
172.17.0.2
```
## Jawaban Nomor 4
### Lakukan inspect pada whoami
```bash
docker inspect whoami
```
### Ditemukan pada mounts
```json
"Mounts": [
            {
                "Type": "bind",
                "Source": "/home/local/.docker",
                "Destination": "/tmp/system",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ]
```
### Lalu jalankan perintah
```bash
docker exec -it whoami bin/sh
```
### Lihat file apa yang ada di direktori dengan perintah
```bash
ls tmp/system
```

### Ditemukan file bernama whoami, lalu jalankan perintah
```bash
cat tmp/system/whoami
```

### File yang ada berisi
```
Oofooni1eeb9aengol3feekiph6fieve
```
## Jawaban Nomor 5
### Dengan menjalankan perintah
```
docker ps
```
### Dapat dilihat images yang ada pada whoami
```
secret:aequaix9De6dii1ay4HeeWai2obie6Ei
```